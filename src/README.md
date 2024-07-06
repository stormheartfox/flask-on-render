## Development

Pages are added to the application using Jinja2 template engine and adding a path to the `app.py` file for the page.

----

### Starting the application in dev:
To test your changes run the following command in the terminal
```
gunicorn app:app --reload --reload-engine auto 
```

This command is also run by Render to host the application.