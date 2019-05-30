from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-agent')
    return '<h1>Hello world!</h1><p>You are using {}</p>'.format(user_agent)

@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)
