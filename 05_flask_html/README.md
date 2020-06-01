## Flask HTML (Templating) 

We can use Flask Templating for the UI of web application based up on Flask Framework.
* Create folder for html pages by name **templates**
* Create HTML Pages for the following:
  * Base template for the website `base.html`
```html
<!DOCTYPE html>
<title>{% block title %}{% endblock %} - Flask HTML</title>

<section class="header">
    {% block header %}
    {% endblock %}
</section>

<section class="content">
    {% block content %}
    {% endblock %}
</section>
```
  * To display containers in tabular format for containers end point `containers.html`. In this case the table will be rendered dynamically using column names and data returned by `list_containers` function.
```html
{% extends 'base.html' %}

{% block header %}
    <h1>{% block title %}Containers{% endblock %}</h1>
{% endblock %}

{% block content %}
    <table>
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
{% endblock %}
```
  * To display images in tabular format for images end point `images.html`
```html
{% extends 'base.html' %}

{% block header %}
    <h1>{% block title %}Images{% endblock %}</h1>
{% endblock %}

{% block content %}
    <table>
        <thead>
            <tr>
                {% for column in columns %}
                    <th>{{ column }}</th>
                {% endfor %}
            </tr>
        </thead>
        <tbody>
            {% for image in data %}
                <tr>
                    {% for column in columns %}
                        <td>{{ image[column] }}</td>
                    {% endfor %}
                </tr>
            {% endfor %}
        </tbody>
    </table>
{% endblock %}
```
* We need to refactor the return statement for our functions (**list_containers** and **list_images**) 
  * Add `render_template` to the import statement - `from flask import Flask, render_template`
  * Refactor `list_containers`
```python
@app.route('/containers')
def list_containers():
    containers = manage.list_containers()
    columns = containers[0].keys()
    return render_template('containers.html', data=containers, columns=columns)
```
  * Refactor `list_images`
```python
@app.route('/images')
def list_images():
    images = manage.list_images()
    columns = images[0].keys()
    return render_template('images.html', data=images, columns=columns)
```
* Make sure both **Dockerfile** and **docker-compose.yml** are in Project Base Directory.
* Run `docker-compose up` to start the application.
* Go to following pages and see if the output is rendered in HTML or not.
  * For list of containers - [http://localhost:5000](http://localhost:5000)
  * For list of containers - [http://localhost:5000/containers](http://localhost:5000/containers)
  * For list of images - [http://localhost:5000/images](http://localhost:5000/image)
