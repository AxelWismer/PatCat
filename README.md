# PatCat
### PatCat (Pattern Catalog) is a web catalog of business patterns applied in real cases of e-government.

Project beta [here](https://houv30niob.execute-api.us-east-2.amazonaws.com/dev)

# Sections
## Admin section
This section that allows an administrator to register all the data of the pattern catalog
![alt text](/docs/admin_dashboard.png)


## Researcher section
This section allows a researcher to search for business patterns that fit the problem they are dealing with.
![alt text](/docs/researcher_section.png)

# Modules
## Pattern
Manages the application models and their modification by an administrator.
### Data models
![alt text](/docs/patterns_models.png)

## MemoryDB
### Data models
This module allows the application to manage a database in memory, making a single query to the real database, which is a file stored in an AWS S3
![alt text](/docs/memoryDB.png)

# Installation
### Install python 3.9 (for linux)
    sudo apt update
    sudo add-apt-repository ppa:deadsnakes/ppa
    sudo apt install python3.9
    sudo apt install python3.9-venv

### Create virtual environment
    python3.9 -m venv venv

### Install libraries:
    pip install -r requirements.txt

# Generating the docs
    python manage.py graph_models -o docs/patterns_models.png

# Development
## To test the application run the init.sh script
    source init.sh

## Deploy Django as lambda
### Collect the static files and place them in the S3.
    python manage.py collectstatic

### Deploy commands
    zappa init
    zappa deploy
    zappa update
