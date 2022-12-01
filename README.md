# PatCat
PatCat (Pattern Catalog) is a web catalog of business patterns applied in real cases of e-government.

#### Check the [project beta](https://houv30niob.execute-api.us-east-2.amazonaws.com/dev)

# Architecture
![alt text](/docs/architecture.png)

The system is a Django web application that is deployed in AWS lambdas using Zappa. The application contains an SQLite in-memory database that obtains its data from a JSON file. The file is stored in an S3 bucket, and through the use of signals, it updates the file when a change in the database state occurs.

This architecture was chosen in the context of an application that will be used mostly for queries and will have a single administrator at any one time. This application requires a small database with public data.

### Advantages of the architecture:
- Cost: Based on the expected usage, the application can run indefinitely on AWS's free layer.
- Modularity: The data persistence mechanism can be modified at any time by removing the memoryDB application and configuring the new database from the settings file.
- Scalability: Because the application is deployed in AWS lambdas, it can scale automatically to provide services to an unlimited number of users.

### Disadvantages of the architecture:
- Performance: Loading data into the memory database adds processing overhead that can decrease application response time.
- Data scalability: The persistence mechanism is not suitable for large amounts of data.

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

# Deploy Django App as AWS Lambda
### Collect the static files and place them in the S3.
    python manage.py collectstatic

### Deploy lambda with Zappa
    zappa init
    zappa deploy
    zappa update

