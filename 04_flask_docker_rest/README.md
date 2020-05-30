## Getting Started

Here are the instructions to setup environment for flask project.
* Create Project using pycharm or any other IDE
* Create **requirements.txt** and add the dependencies.
```
flask==1.1.2

```
* Create a file in the project with name of your choice **app.py**
  * Import Flask
  * Define function for base endpoint
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World, from docker'
```
* Run the application from terminal
```
export FLASK_APP=app.py
flask run
```
* Create Dockerfile using Dockerfile of this repository
* Create **docker-compose.yml** file for the following
  * Build the image
  * Create the container
  * Start the container by mounting the source code
* Run `docker-compose up` command to launch the Flask Web Application
