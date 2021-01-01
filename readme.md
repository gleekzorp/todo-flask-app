# Todo Application

This is a todo app using a tdd/bdd approach built with flask.
> My main purpose for this was to help me learn and possibly use it to teach others.

## Setup
> After downloading or cloning, run the following commands in your terminal while in the `todo-flask-app` directory.
> Once the flask server is running open a browser to http://localhost:5000
- Pycharm
```commandline
(venv)$ pipenv install
(venv)$ python run.py
```
- vscode
```commandline
$ pipenv install
$ pipenv shell
(venv)$ python run.py
```

## Tests
> Tests are done via `pytest` and `pyleniumio`.
> Some tests are still in the works, and these are noted with a comment.
> I'm still working out my fixtures, and a better way to test with `pyleniumio` via a test database.

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

### Old manual way to set up DB
> I originally had to set up the db in this way.
> I'm keeping the notes of it for now until I find out if my new way is correct.
- Hop into a `python` repl and run these commands
```
>>> from todo_app import db, create_app
>>> db.create_all(app=create_app('flask.cfg'))
```
- More information from the flask docs
  - https://flask-sqlalchemy.palletsprojects.com/en/2.x/contexts/
- I still need to decide on `.db` and `.sqlite` file type in the `flask.cfg` and `flask_test.cfg`