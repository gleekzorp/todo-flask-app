from flask import render_template, Blueprint, request, redirect, url_for

from todo_app import db
from todo_app.models import Todo

routes = Blueprint('routes', __name__)


@routes.route('/')
def home():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)


@routes.route('/add-todo', methods=["POST"])
def add_todo():
    title = request.form['title']
    todo = Todo(title=title, done=False)
    db.session.add(todo)
    db.session.commit()
    return redirect(url_for("routes.home"))


@routes.route('/delete-todo/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("routes.home"))


@routes.route('/mark-complete/<int:todo_id>', methods=['POST'])
def mark_complete(todo_id):
    todo = Todo.query.get(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("routes.home"))


@routes.route('/delete-all-complete', methods=['POST'])
def delete_all_complete():
    completed_todos = Todo.query.filter_by(done=True).all()
    for todo in completed_todos:
        db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("routes.home"))
