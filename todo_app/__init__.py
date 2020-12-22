from flask import Flask

app = Flask(__name__)

# In order to fix this warning you would want to use a create_app() function
from todo_app import routes
