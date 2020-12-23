import pytest


def test_get_all_todos(init_database, test_client):
    response = test_client.get('/')
    assert b'Clean room' in response.data
    assert b'Wash Car' in response.data
    assert b'Cut Hair' in response.data
    assert b'Code' in response.data


def test_add_todo(init_database, test_client):
    response = test_client.post('/add-todo', data=dict(title='Buy Milk'), follow_redirects=True)
    assert response.status_code == 200
    assert b'Buy Milk' in response.data


def test_mark_complete():
    pytest.xfail()


def test_delete_todo():
    pytest.xfail()


def test_delete_todos_marked_complete():
    pytest.xfail()
