## Responsive using Flask and Bootstrap

Let us understand how we can make our pages responsive using Bootstrap

## Features
Let us go through the features which we will be developing as part of this module.
* Enable Bootstrap
* Have a simple Nav Bar linking to our end points (`/containers` and `/images`)
* Make table responsive using Bootstrap
* Add buttons to stop, start and delete
* Develop functionality for Post request to stop, start or delete

## Enabling Bootstrap
Let us understand how to enable Bootstrap.
* Update **requirements.txt** with `Flask-Boostrap`
```
Flask==1.1.2
Flask-Bootstrap==3.3.7.1
docker==4.2.0
```
* Register the app with Bootstrap (updata `app.py`)
```python
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)
```
* Update `base.html`
```html
{% extends "bootstrap/base.html" %}

<title>{% block title %}{% endblock %} - Dockit Bootstrap</title>
```
* As **requirements.txt** is updated we need to delete the Docker container and image and then run `docker-compose up` again.
* Validate the pages

## Adding Nav bar
Let us understand how to add Nav Bar to our simple web application.

* As Nav Bar has to reflect in all html pages, we will add it to `base.html`
```html
{% block navbar %}
<div class="navbar navbar-default navbar-static-top">
    <ul class="nav navbar-nav">
        <li><a href="containers">Containers</a></li>
        <li><a href="images">Images</a></li>
    </ul>
</div>
{% endblock %}
```
* We can refresh the page, and we should be able to see the Nav Bar.

## Making tables responsive
Let us make our tables also responsive using Bootstrap.

* We need to enclose the entire table tag as part of Bootstrap div container.
* We also need to define our table as Bootstrap table using `class` attribute - `table class="table"`
* Here is the updated **table** as part of `containers.html`
```html
{% block content %}
<div class="container">
    <table class="table">
        <thead>
        <tr>
            {% for column in columns %}
            <th>{{ column }}</th>
            {% endfor %}
        </tr>
        </thead>
        <tbody>
        {% for container in data %}
        <tr>
            {% for column in columns %}
            <td>{{ container[column] }}</td>
            {% endfor %}
        </tr>
        {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
```
* We can use the similar approach to display images in responsive table.

## Adding Buttons
Let us go ahead and add buttons to the table which lists the containers.
* We would like to have **Stop** button if container is up and running.
* In case container is stopped, we would like to have **Start** as well as **Delete** buttons.
* Here is how the loop which renders rows in the table look like.
```html
{% for container in data %}
<tr>
    {% for column in columns %}
    <td>{{ container[column] }}</td>
    {% endfor %}
    <td>
        {% if container['container_status'] == 'running' %}
        <button class="btn btn-primary" name="action" type="submit" value="stop">Stop</button>
        {% else %}
        <button class="btn btn-primary" name="action" type="submit" value="start">Start</button>
        <button class="btn btn-primary" name="action" type="submit" value="delete">Delete</button>
        {% endif %}
    </td>
</tr>
{% endfor %}
```
* Let us validate by refreshing the page, we should see the buttons. However, POST request is not implemented yet.

## Implement POST request

Let us take care of implementing POST request for the buttons in the table.
* We need to update the `list_containers` function, so that it is invoked on POST requests from `containers.html`.
```python
@app.route('/containers', methods=['GET', 'POST'])
def list_containers():
    if request.method == 'POST':
        container_id = request.form.get('container_id')
        action = request.form.get('action')
        manage.manage_container(container_id, action)
    containers = manage.list_containers()
    columns = containers[0].keys()
    return render_template('containers.html', data=containers, columns=columns)
```
* We also need to submit as a form along with container id when the button is clicked.
```html
{% for container in data %}
<tr>
    {% for column in columns %}
    <td>{{ container[column] }}</td>
    {% endfor %}
    <td>
        <form action="/containers" method="POST" role="form">
            <input type="hidden" name="container_id" id="container_id" value="{{ container.container_id }}"/>
            {% if container['container_status'] == 'running' %}
            <button class="btn btn-primary" name="action" type="submit" value="stop">Stop</button>
            {% else %}
            <button class="btn btn-primary" name="action" type="submit" value="start">Start</button>
            <button class="btn btn-primary" name="action" type="submit" value="delete">Delete</button>
            {% endif %}
        </form>
    </td>
</tr>
{% endfor %}
```
