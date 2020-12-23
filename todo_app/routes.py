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
    todos = Todo.query.all()
    return redirect(url_for("routes.home", todos=todos))

