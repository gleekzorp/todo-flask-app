
BASE_URL = "http://localhost:5000"


def test_homepage_title(py):
    py.visit(BASE_URL)
    assert py.title() == 'Todo App'


def test_homepage_has_text_field_and_add_button(py):
    py.visit(BASE_URL)
    text_field = py.get('input')
    add_button = py.get('button')
    assert text_field.is_displayed()
    assert add_button.is_displayed()
