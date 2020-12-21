
def test_homepage_title(py):
    py.visit('http://localhost:5000')
    assert py.title() == 'Todo App'
