# PatCat
PatCat (Pattern Catalog) is a web catalog of business patterns applied in real cases of e-government.

# Modules
## Pattern
Manages the application models and their modification by an administrator.
### Data models
![alt text](/docs/patterns_models.png)

## MemoryDB
### Data models
This module allows the application to manage a database in memory, making a single query to the real database, which is a file stored in an AWS S3
![alt text](/docs/memoryDB.png)

# Installation and execution
### Create a virtual env for python3
    python venv venv

### Install libraries:
    pip install -r requirements.txt

# Generating the docs
    python manage.py graph_models -o docs/patterns_models.png

# Development
To test the application run the init.sh script
    source init.sh