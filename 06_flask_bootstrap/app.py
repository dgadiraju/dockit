from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

import manage

app = Flask(__name__)
Bootstrap(app)


@app.route('/')
def index():
    return list_containers()


@app.route('/containers', methods=['GET', 'POST'])
def list_containers():
    if request.method == 'POST':
        container_id = request.form.get('container_id')
        action = request.form.get('action')
        manage.manage_container(container_id, action)
    containers = manage.list_containers()
    columns = containers[0].keys()
    return render_template('containers.html', data=containers, columns=columns)


@app.route('/images')
def list_images():
    images = manage.list_images()
    columns = images[0].keys()
    return render_template('images.html', data=images, columns=columns)
