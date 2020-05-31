from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Another Hello World, from docker'
