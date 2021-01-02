from todo_app.models import Todo


def test_new_todo():
    """
    GIVEN a Todo model
    WHEN a new Todo is created
    THEN check the title, and done fields are defined correctly
    """
    todo = Todo(title="Clean room", done=False)
    assert todo.title == 'Clean room'
    assert todo.done is False


def test_new_todo_with_fixture(new_todo):
    """
    GIVEN a Todo model
    WHEN a new Todo is created
    THEN check the title, and done fields are defined correctly
    """
    assert new_todo.title == 'Clean room'
    assert new_todo.done is False


def test_init_database(init_database):
    todos = Todo.query.all()
    assert len(todos) == 4


def test_clear_data(clear_data):
    todos = Todo.query.all()
    assert len(todos) == 0
