# AirBnB Clone Console Project 💻

![plot](./web_static/images/logo.png)

## Overview ⌨️

The AirBnB Clone project replicates Airbnb's functionality, starting with a command-line interface (CLI) for managing AirBnB objects in Python.

## Project Structure 🗃️

```python
# Core Python Concepts
- Import
- Exceptions
- Class
- Private attribute
- Getter / Setter
- Class method
- Static method
- Inheritance
- Unittest
- Read / Write file
- args and kwargs
- Serialization / Deserialization
- JSON
```
## Files and Directories 📁
| Files               | Description                               |
|---------------------|-------------------------------------------|
| models              | Directory for classes used in the project |
| tests               | Directory for unit tests                   |
| console.py          | Entry point for the command interpreter   |
| models/base_model.py| Base class for all models                  |
| models/engine       | Directory for storage classes              |

## Phase One 📝

- Create a parent class (BaseModel) for instance initialization, serialization, and deserialization.
- Establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
- Create AirBnB classes (User, State, City, Place) inheriting from BaseModel
- Implement the first storage engine: File storage
- Develop unittests for all classes and the storage engine
- Create a data model
- Manage objects via a console/command interpreter
- Store and persist objects to files (JSON files)

## Description of the Command Interpreter ⌨️

Commands | Description
---------|-------------
quit, Ctrl+D | Quits the console
help <command> | Displays all commands or instructions for a specific command
create <class> | Creates an object, saves it to a JSON file, and prints the object's ID
show <class> <ID> | Shows the string representation of an object
destroy <class> <ID> | Deletes an object
all <class> | Prints string representations of all objects or of a specific class
update <class> <id> <attribute name> "<attribute value>" | Updates an object with a certain attribute
<class>.all() | Same as all <class>
<class>.count() | Retrieves the number of objects of a certain class
<class>.show(<ID>) | Same as show <class> <ID>
<class>.destroy(<ID>) | Same as destroy <class> <ID>
<class>.update(<ID>, <attribute name>, <attribute value>) | Same as update <class> <ID> <attribute name> <attribute value>
<class>.update(<ID>, <dictionary representation>) | Updates an object based on a dictionary representation

## General Execution 🛠️

Interactive mode:

``` 
bash
$ ./console.py
(hbnb) help
```
Non-interactive mode:
```
$ echo "help" | ./console.py
```

## Next Steps ➡️
The next steps involve developing a front-end for user interaction, starting with HTML prototyping.

## Phases of the Project 🚀

1 - Console Phase:

Implemented a command-line interface for managing AirBnB objects.
Covered various Python concepts to ensure a robust foundation.

2 - HTML Prototyping:

Created simple HTML static pages.
Developed a style guide for consistent design.
Added fake content for visual representation.
No JavaScript involved in this phase.
Data is not loaded from any external source.

## Author
🚀 Marwen Rebah<br>
📧 Email: 6863@holbertonstudents.com<br>
👻 Github: https://github.com/marwenrebah