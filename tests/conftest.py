import pytest

from todo_app import create_app, db
from todo_app.models import Todo


@pytest.fixture(scope='module')
def new_todo():
    todo = Todo(title="Clean room", done=False)
    return todo


@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):
    # Create the database and the database table
    # Don't need anymore with new factory setup
    # db.create_all()

    # Insert user data
    todo_one = Todo(title="Clean room", done=False)
    todo_two = Todo(title="Wash Car", done=False)
    todo_three = Todo(title="Cut Hair", done=True)
    todo_four = Todo(title="Code", done=True)
    db.session.add(todo_one)
    db.session.add(todo_two)
    db.session.add(todo_three)
    db.session.add(todo_four)

    # Commit the changes for the users
    db.session.commit()

    yield  # this is where the testing happens!

    db.drop_all()
