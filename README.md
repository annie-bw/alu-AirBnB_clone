#  AirBnB Clone – The Console

## 📌 Project Description

This project is the first step in building a full web application: the AirBnB clone.  
In this stage, we develop a command-line interface (CLI) that allows users to create, manage, store, and retrieve objects related to an AirBnB-like application.

The console is responsible for:

- Creating new objects (e.g., users)
- Retrieving objects from storage
- Updating object attributes
- Destroying objects
- Persisting data using JSON serialization

This console will serve as the foundation for future stages of the project, including database storage, web frameworks, and front-end integration.

---

## 🚀 How to Start the Console

1. **Clone the repository:**

```bash
git clone https://github.com/<your-username>/alu-AirBnB_clone.git
Navigate into the project directory:

bash
Copy code
cd alu-AirBnB_clone
Run the console:

bash
Copy code
./console.py
You should see the prompt:

scss
Copy code
(hbnb)
🛠 How to Use the Console
The console works in interactive mode and non-interactive mode.

Interactive Mode
bash
Copy code
./console.py
(hbnb) help
(hbnb) quit
Non-Interactive Mode
bash
Copy code
echo "help" | ./console.py
📖 Available Commands
Command	Description
help	Displays available commands
quit	Exits the console
EOF	Exits the console (Ctrl+D)
create <class>	Creates a new instance of a class
show <class> <id>	Shows an instance
destroy <class> <id>	Deletes an instance
all [class]	Displays all instances
update <class> <id> <attr> <value>	Updates an instance

🧪 Command Examples
bash
Copy code
(hbnb) create BaseModel
(hbnb) show BaseModel 1234-5678
(hbnb) all
(hbnb) update BaseModel 1234-5678 name "MyModel"
(hbnb) destroy BaseModel 1234-5678
(hbnb) quit
🗂 Project Structure (Overview)
javascript
Copy code
.
├── console.py
├── models/
│   ├── base_model.py
│   ├── user.py
│   └── engine/
│       └── file_storage.py
├── tests/
│   └── test_models/
└── README.md
