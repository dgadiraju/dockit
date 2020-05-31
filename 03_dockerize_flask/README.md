## Dockerize Flask Application

Here are the instructions to dockerize Flask Application.
* Make sure Hello World Flask application is validated.
* Update return statement in index function to `return 'Hello World, from docker'`
```python
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World, from docker'
```
* Create Dockerfile using Dockerfile of this repository
```dockerfile
FROM python:3.7

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP app.py
ENV FLASK_ENV development

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
```
* Build the image
```
docker build -t 03_dockerize_flask .
```
* Start the Container by mounting our project directory
```
docker run --name 03_dockerize_flask_1 -p 5000:5000 -v `pwd`:/app 03_dockerize_flask
```
