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
* Create Dockerfile
```
FROM python:3.7

RUN useradd -m itversity
RUN mkdir /app
RUN chown itversity:itversity /app
USER itversity

WORKDIR /app
COPY . /app
RUN python -m venv env
ENV PATH=/app/env/bin:$PATH
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP app.py
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]

```