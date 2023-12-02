# :octocat: AirBnB Clone Console Project

![plot](https://repository-images.githubusercontent.com/520549705/a67ad5ce-2374-4762-a985-4967eafb5912)

## ⌨️ Overview 

The AirBnB Clone project replicates Airbnb's functionality, starting with a command-line interface (CLI) for managing AirBnB objects in Python.<br>
Our mission: crafting an Airbnb replica—a property rental platform. Guided by a robust development tool (CLI), our website merges fixed and dynamic features. With a robust database, we store property and user data. The API ensures seamless front-to-back communication, aspiring to mirror Airbnb's user-friendly excellence.

## 🗃️ Project Structure 

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
## 📁 Files and Directories 
| Files               | Description                               |
|---------------------|-------------------------------------------|
| models              | Directory for classes used in the project |
| tests               | Directory for unit tests                   |
| console.py          | Entry point for the command interpreter   |
| models/base_model.py| Base class for all models                  |
| models/engine       | Directory for storage classes              |

## 📝 Phase One 

- Create a parent class (BaseModel) for instance initialization, serialization, and deserialization.
- Establish a serialization/deserialization flow: Instance <-> Dictionary <-> JSON string <-> File
- Create AirBnB classes (User, State, City, Place) inheriting from BaseModel
- Implement the first storage engine: File storage
- Develop unittests for all classes and the storage engine
- Create a data model
- Manage objects via a console/command interpreter
- Store and persist objects to files (JSON files)

## 🔎 What’s a command interpreter?
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object

## ⌨️ Description of the Command Interpreter 

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
<class>.show(<ID>) | Same as show <class> <ID>
<class>.destroy(<ID>) | Same as destroy <class> <ID>
<class>.update(<ID>, <attribute name>, <attribute value>) | Same as update <class> <ID> <attribute name> <attribute value>
<class>.update(<ID>, <dictionary representation>) | Updates an object based on a dictionary representation

## 🛠️ General Execution 

Interactive mode:

``` 
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$

```

Non-interactive mode:

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
```

## ➡️ Next Steps 
The next steps involve developing a front-end for user interaction, starting with HTML prototyping.

## 🚀 Phases of the Project 

1 - Console Phase:

Implemented a command-line interface for managing AirBnB objects.
Covered various Python concepts to ensure a robust foundation.

2 - HTML Prototyping:

Created simple HTML static pages.
Developed a style guide for consistent design.
Added fake content for visual representation.
No JavaScript involved in this phase.
Data is not loaded from any external source.

## :toolbox: Languages and Tools

<p align="center">
  <a href="https://www.python.org/" target="_blank" rel="noreferrer">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" alt="c" width="40" height="40"/> 
  </a>
</p>

## 👥 Author
🚀 Marwen Rebah<br>
📧 Email: 6863@holbertonstudents.com<br>
👻 Github: https://github.com/marwenrebah