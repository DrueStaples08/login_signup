# login_signup
Login / Signup Page for the movie app

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
