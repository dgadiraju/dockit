from flask import Flask
import manage

app = Flask(__name__)


@app.route('/')
def index():
    return list_containers()


@app.route('/containers')
def list_containers():
    containers = manage.list_containers()
    return {'containers': containers}


@app.route('/images')
def list_images():
    images = manage.list_images()
    return {'images': images}
