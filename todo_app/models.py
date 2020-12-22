from todo_app import db


class Todo(db.Model):
    """
    Class that represents a user of the application

    The following attributes of a todo are stored in this table:
        * id - Primary_key
        * title - String
        * done - Boolean
    """

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    done = db.Column(db.Boolean, nullable=False)
