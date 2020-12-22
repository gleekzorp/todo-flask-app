# Todo Application

This is a todo app using a tdd/bdd approach built with flask.

> Main purpose is for teaching.

## Helpful Links
- Patrick Kennedy
  - https://testdriven.io/blog/flask-pytest/
  - https://gitlab.com/patkennedy79/flask_user_management_example
- Todd Birchard
  - https://github.com/toddbirchard
  - https://hackersandslackers.com/flask-application-factory
  - https://hackersandslackers.com/configure-flask-applications
- Corey Schafer
  - https://www.youtube.com/c/Coreyms
  - https://www.youtube.com/playlist?list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
- Miguel Grinberg
  - Flask Mega Tutorial
    - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
      - Try and research further into the db migration section
        - https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
        - https://flask-migrate.readthedocs.io/en/latest/
 - Some various things I came across from reading
   - pytest-flask
     - https://pytest-flask.readthedocs.io/en/latest/
   - Common flask patterns via flask docs
     - https://flask.palletsprojects.com/en/1.1.x/patterns/
   - Great repo for all the awesomeness of flask
     - https://github.com/mjhea0/awesome-flask

### Current Way To Setup DB
> This is my current way to setup the app db.  Testing has it's own functionality with fixtures
- Hop into a `python` repl and run these commands
```
>>> from todo_app import db, create_app
>>> db.create_all(app=create_app('flask.cfg'))
```
- More information from the flask docs
  - https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
- I still need to decide on `.db` and `.sqlite` file type in the `flask.cfg` and `flask_test.cfg`