# PatCat
PatCat (Pattern Catalogue) is a web catalog of business patterns applied in real cases of e-government.

# Modules
## Pattern
Manages the application models and their modification by an administrator.
![alt text](/docs/patterns_models.png)

# Instalation and execution
- Create a virtual env for python3
    python venv venv
- Intstall libraries:
    pip install -r requirements.txt

# Generating the docs
    python manage.py graph_models -o docs/patterns_models.png