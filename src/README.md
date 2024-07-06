## Development

Pages are added to the application using Jinja2 template engine and adding a path to the `app.py` file for the page.

----

### Starting the application in dev:
Firstly create your python environment, cd into `/src` and run the command:

`python3 -m venv .venv`

Start the environment using:

`. ./.venv/bin/activate`

Install all the dependencies of the code using:

`pip install -r requirements.txt`

Start the Gunicorn server to see the web pages served locally with the following command:

`
gunicorn app:app --reload --reload-engine auto 
`

This command is also run by Render to host the application.

To view your local environment go to this address in your browser:

`http://127.0.0.1:8000`


To deactivate the virtual environment simple type `deactivate` into the terminal and hit ENTER. 