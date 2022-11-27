### Airbnb Clone

#### Description
> Phase 1: Airbnb Clone -> the console
> The repo contains a command interpreter and classes
> 

#### How to Use Command Interpreter
---
| Commands | How to use          | Function
|--------- |---------------------|------------------------------
|`help`    |  `help`             | shows all commands available                  
| `show`   |  `User.show('1278')`| retrieve an object from file

#### Usage
```
Interactive mode
```
$./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb) quit
$
```
Non-Interactive Mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
---
### The Environment
* Language: Python3 (v3.8.5)
* OS: Ubuntu 20.04 LTS
* Style guidelines: pycodestyle v2.8; PEP

### Authors
* Ngoni19 <<ngoni19@live.com>>
* Asmamaw Baye <<asmamaw.lejalem7@gmail.com>>

