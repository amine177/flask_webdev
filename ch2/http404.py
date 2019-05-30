from flask import Flask
from flask import abort

app = Flask(__name__)

@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)

def load_user(id):
    if int(id) > 5:
        return User("Success")
    else: return None

class User:
    def __init__(self, name):
        self.name = name;

