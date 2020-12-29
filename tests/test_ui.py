from todo_app import create_app
BASE_URL = "http://localhost:5000"


# Using Pyleniumio
def test_homepage_title(py):
    py.visit(BASE_URL)
    assert py.title() == 'Todo App'


# Using Pyleniumio
def test_homepage_has_text_field_and_add_button(py):
    py.visit(BASE_URL)
    text_field = py.get('#add-todo-input')
    add_button = py.get('#add-todo-btn')
    assert text_field.is_displayed()
    assert add_button.is_displayed()


# Using Pyleniumio
# Currently fails since todo doesn't exist.  Should we remove test since we have test_add_todo_with_ui now?
def test_home_page_todo_has_title(py):
    py.visit(BASE_URL)
    assert py.contains('Clean room')


# Using Pyleniumio
def test_add_todo_with_ui(py):
    py.visit(BASE_URL)
    text_field = py.get('#add-todo-input')
    add_button = py.get('#add-todo-btn')
    text_field.type('Buy Milk')
    add_button.click()
    assert py.contains('Buy Milk')


# Using Pyleniumio
# Might need to look into some fixtures.
# This will only work if the database has zero todos
def test_mark_complete(py):
    py.visit(BASE_URL)
    py.get('#add-todo-input').type('Buy Milk')
    py.get('#add-todo-btn').click()
    py.get('.checkbox').click()
    title = py.get('.title')
    assert py.get('.checkbox').is_checked()
    assert title.should().have_class('title done')
    assert title.css_value("text-decoration")


# Currently passes as long as database is empty to start with
def test_delete_all_complete(py):
    todos = [
        {
            "title": 'Clean room',
            "done": False
        },
        {
            "title": 'Wash Car',
            "done": False
        },
        {
            "title": 'Cut Hair',
            "done": True
        },
        {
            "title": 'Code',
            "done": True
        },
    ]
    py.visit(BASE_URL)
    for i in range(len(todos)):
        py.get('#add-todo-input').type(todos[i]['title'])
        py.get('#add-todo-btn').click()
        if todos[i]['done']:
            py.get(f'#checkbox-{i+1}').click()
    py.get('.delete-all-btn').click()
    assert py.should().not_contain('Code')
    assert py.should().not_contain('Cut Hair')


def test_home_page_title_with_test_client(init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    flask_app = create_app('flask_test.cfg')

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200
        assert b"Todo App" in response.data


def test_home_page_title_with_test_client_fixture(test_client, init_database):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Todo App" in response.data


def test_home_page_todo_has_title_with_test_client_fixture(init_database, test_client):
    response = test_client.get('/')
    assert b'Clean room' in response.data
