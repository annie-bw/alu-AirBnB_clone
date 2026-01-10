# AirBnB Clone - The Console

## Description
This project is the first step towards building a full web application: an AirBnB clone. 
The console is a command interpreter to manage objects for the AirBnB website.

This command interpreter allows us to:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## Command Interpreter

### How to Start
To start the console, run:
```bash
./console.py
```

### How to Use
The console works in both interactive and non-interactive mode.

**Interactive mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) quit
$
```

**Non-interactive mode:**
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

### Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| create | Creates a new instance | `create <class_name>` |
| show | Displays an instance | `show <class_name> <id>` |
| destroy | Deletes an instance | `destroy <class_name> <id>` |
| all | Displays all instances | `all` or `all <class_name>` |
| update | Updates an instance | `update <class_name> <id> <attribute> <value>` |
| quit | Exits the console | `quit` |
| EOF | Exits the console | `EOF` (Ctrl+D) |

### Examples

**Creating a new object:**
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
```

**Showing an object:**
```bash
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
```

**Updating an object:**
```bash
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 3, 49401), 'first_name': 'Betty'}
```

**Destroying an object:**
```bash
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
** no instance found **
```

**Showing all objects:**
```bash
(hbnb) all
["[BaseModel] (2dd6ef5c-467c-4f82-9521-a772ea7d84e9) {'id': '2dd6ef5c-467c-4f82-9521-a772ea7d84e9', 'created_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639717), 'updated_at': datetime.datetime(2017, 10, 2, 3, 11, 23, 639724)}"]
```

## Project Structure
```
alu-AirBnB_clone/
│
├── AUTHORS
├── README.md
├── console.py
│
├── models/
│   ├── __init__.py
│   ├── base_model.py
│   ├── user.py
│   ├── state.py
│   ├── city.py
│   ├── amenity.py
│   ├── place.py
│   ├── review.py
│   │
│   └── engine/
│       ├── __init__.py
│       └── file_storage.py
│
└── tests/
    ├── __init__.py
    │
    ├── test_models/
    │   ├── __init__.py
    │   ├── test_base_model.py
    │   ├── test_user.py
    │   ├── test_state.py
    │   ├── test_city.py
    │   ├── test_amenity.py
    │   ├── test_place.py
    │   └── test_review.py
    │
    └── test_engine/
        ├── __init__.py
        └── test_file_storage.py
```

## Authors
See [AUTHORS](AUTHORS) file for a list of contributors.
