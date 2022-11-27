#!/usr/bin/python3
"""CMD console-> entry point"""
import re
import cmd
from shlex import split

import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# A global constants.
CLASSES = [
    "BaseModel",
    "User",
    "State",
    "City",
    "Amenity",
    "Place"
    "Review"
]


def parse(arg):
    _curlyBrac = re.search(r"\{(.*?)\}", arg)
    _sbrackets = re.search(r"\[(.*?)\]", arg)
    if _curlyBrac is None:
        if _sbrackets is None:
            return [v.strip(",") for v in split(arg)]
        else:
            arg_lex = split(arg[:_sbrackets.span()[0]])
            arg_rl = [v.strip(",") for v in arg_lex]
            arg_rl.append(_sbrackets.group())
            return arg_rl
    else:
        arg_lex = split(arg[:_curlyBrac.span()[0]])
        arg_rl = [i.strip(",") for i in arg_lex]
        arg_rl.append(_curlyBrac.group())
        return arg_rl


def check_args(args):
    """checks args validity

    Args:
        args (str): string contains arguments passed to a command

    Returns:
        Error msg if args is None or not a valid class, else args
    """
    arg_L = parse(args)

    if len(arg_L) == 0:
        print("** class name missing **")
    elif arg_L[0] not in CLASSES:
        print("** class doesn't exist **")
    else:
        return arg_L


class HBNBCommand(cmd.Cmd):
    """The class-> implements AirBnB clone web application console
    """
    prompt = "(hbnb) "
    storage = models.storage

    def emptyline(self):
        """executed for empty line + <ENTER> key"""
        pass

    def do_EOF(self, argv):
        """EOF signal -> exit the program"""
        print("")
        return True

    def do_quit(self, argv):
        """Quit command -> exits the console."""
        return True

    def do_create(self, argv):
        """Creates a new instance of BaseModel, saves it (to a JSON file)
        and prints the id"""
        args = check_args(argv)
        if args:
            print(eval(args[0])().id)
            self.storage.save()

    def do_show(self, argv):
        """Prints the string repr of an instance based
        on the class name and id"""
        args = check_args(argv)
        if args:
            if len(args) != 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(args[0], args[1])
                if key not in self.storage.all():
                    print("** no instance found **")
                else:
                    print(self.storage.all()[key])

    def do_all(self, argv):
        """Prints all string repre of all instances based or not
        based on the class name"""
        arg_L = split(argv)
        objects = self.storage.all().values()
        if not arg_L:
            print([str(obj) for obj in objects])
        else:
            if arg_L[0] not in CLASSES:
                print("** class doesn't exist **")
            else:
                print([str(obj) for obj in objects
                       if arg_L[0] in str(obj)])

    def do_destroy(self, argv):
        """Delete a class instance based on the name and given id."""
        arg_L = check_args(argv)
        if arg_L:
            if len(arg_L) == 1:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(*arg_L)
                if key in self.storage.all():
                    del self.storage.all()[key]
                    self.storage.save()
                else:
                    print("** no instance found **")

    def do_update(self, argv):
        """Updates an instance and save it to the JSON file."""
        arg_L = check_args(argv)
        if arg_L:
            if len(arg_L) == 1:
                print("** instance id missing **")
            else:
                inst_id = "{}.{}".format(arg_L[0], arg_L[1])
                if inst_id in self.storage.all():
                    if len(arg_L) == 2:
                        print("** attribute name missing **")
                    elif len(arg_L) == 3:
                        print("** value missing **")
                    else:
                        obj = self.storage.all()[inst_id]
                        if arg_L[2] in type(obj).__dict__:
                            v_type = type(obj.__class__.__dict__[arg_L[2]])
                            setattr(obj, arg_L[2], v_type(arg_L[3]))
                        else:
                            setattr(obj, arg_L[2], arg_L[3])
                else:
                    print("** no instance found **")

            self.storage.save()

    def do_count(self, arg):
        """Retrieve number of instances of a class"""
        arg01 = parse(arg)
        count = 0
        for obj in models.storage.all().values():
            if arg01[0] == type(obj).__name__:
                count += 1
        print(count)

    def default(self, arg):
        """Default behaviour-> when input is invalid"""
        cmd_map = {
            "create": self.do_create,
            "update": self.do_update,
            "all": self.do_all,
            "show": self.do_show,
            "count": self.do_count,
            "destroy": self.do_destroy
            }

        match = re.search(r"\.", arg)
        if match:
            arg01 = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg01[1])
            if match:
                command = [arg01[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in cmd_map:
                    call = "{} {}".format(arg01[0], command[1])
                    return cmd_map[command[0]](call)

        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
