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
    return 'Hello World, Getting Started'
```
* Run the application from terminal
```
export FLASK_APP=app.py
flask run
```
* We can also export **FLASK_ENV** to **development** so that the application is restarted automatically in case of changes.
```
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```
