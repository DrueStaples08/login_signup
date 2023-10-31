# login_signup
Login / Signup Page for the movie app

## What this API does?
- Verifies if user is in database or not otherwise they will need to signup. 
- Once account is created, that user account is saved in database (Big Query)


## Create/Activate Virtual Environment 

A1. Install a Specific Python Version

A1A. Check available Python versions using the following command:

pyenv install --list

A1B. Install a specific Python version using pyenv install followed by the version number. For example, to install Python 3.8.12:

pyenv install 3.8.12

A2. Create a Virtual Environment

Create a new virtual environment using the pyenv virtualenv command and specify the Python version you want to use. For example, to create an environment named "myenv" using Python 3.8.12:

pyenv virtualenv 3.8.12 myenv

A3. Activate the Virtual Environment

Activate the virtual environment using the pyenv activate command:

pyenv activate myenv



## Architecture

- backend/ 
    - flask app
- lib/
    - GCP interaction
- scripts/
    - UX
- static/
    - Front-end asthetics
- templates
    - UI

Todo:
create user table in bq

create gcp script to update to users table 

create the front end

create the flask app 

add stylizing

add js for login/signup button to showcase either windown on screen


### Authenticate with GCP
```gcloud auth application-default login```

### Resources

https://flask-restx.readthedocs.io/en/latest/example.html

https://flask-restx.readthedocs.io/en/latest/quickstart.html




### Run Flask App
```
FLASK_ENV=development
FLASK_APP=app.py
flask run
```