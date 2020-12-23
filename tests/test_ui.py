from todo_app import create_app
BASE_URL = "http://localhost:5000"


# Using Pyleniumio
def test_homepage_title(py):
    py.visit(BASE_URL)
    assert py.title() == 'Todo App'


# Using Pyleniumio
def test_homepage_has_text_field_and_add_button(py):
    py.visit(BASE_URL)
    text_field = py.get('input')
    add_button = py.get('button')
    assert text_field.is_displayed()
    assert add_button.is_displayed()


def test_home_page_todo_has_title(py):
    py.visit(BASE_URL)
    assert py.contains('Clean room')


def test_home_page_title_with_test_client():
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


def test_home_page_title_with_test_client_fixture(test_client):
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



