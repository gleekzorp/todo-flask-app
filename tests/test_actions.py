
from todo_app.models import Todo


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


def test_delete_todo(init_database, test_client):
    todo = Todo.query.filter_by(title="Clean room").first()
    todo_id = todo.id
    response = test_client.post(f'/delete-todo/{todo_id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Clean room' not in response.data


# Currently passes when running on its own.  If you run test_actions file it fails
def test_mark_complete(init_database, test_client):
    todo = Todo.query.filter_by(title="Clean room").first()
    todo_id = todo.id
    response = test_client.post(f'/mark-complete/{todo_id}', follow_redirects=True)
    updated_todo = Todo.query.get(todo_id)
    assert response.status_code == 200
    assert updated_todo.done is True


# Failing but yet it is deleting the todos
def test_delete_all_complete(init_database, test_client):
    response = test_client.post('/delete-all-complete', follow_redirects=True)
    print(response.data)
    assert response.status_code == 200
    assert b'Clean room' not in response.data
    assert b'Code' not in response.data
