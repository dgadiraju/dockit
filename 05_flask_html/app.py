from flask import Flask, render_template
import manage

app = Flask(__name__)


@app.route('/')
def index():
    return list_containers()


@app.route('/containers')
def list_containers():
    containers = manage.list_containers()
    columns = containers[0].keys()
    return render_template('containers.html', data=containers, columns=columns)


@app.route('/images')
def list_images():
    images = manage.list_images()
    columns = images[0].keys()
    return render_template('images.html', data=images, columns=columns)
