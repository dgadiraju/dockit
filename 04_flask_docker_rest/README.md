## Integrate Docker and Flask

Let us understand how we can integrate Docker and Flask using REST APIs.
* Make sure **requirements.txt** have the required dependencies for Flask and Docker.
* Develop functions in **app.py**
  * End point - `/containers`
    * Request Type - `GET`
    * Function - `list_containers`
```python
@app.route('/containers')
def list_containers():
    containers = manage.list_containers()
    return {'containers': containers}
```
  * End point - `/images`
    * Request Type - `GET`
    * Function - `list_images`
```python
@app.route('/images')
def list_images():
    images = manage.list_images()
    return {'images': images}
```
  * End point - `/`
    * Request Type - `GET`
    * Redirect to `list_containers`
```python
@app.route('/')
def index():
    return list_containers()
```
* Let us also start exploring docker compose which can streamline the process of integrating and managing multiple containers.
  * Create Dockerfile using Dockerfile of this repository
```dockerfile
FROM python:3.7

WORKDIR /app
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP app.py

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
```
  * Create **docker-compose.yml** file for the following
    * Build the image
    * Create the container
    * Start the container by mounting the source code
```dockerfile
version: '3'
services:
  web:
    build: .
    ports:
      - 5000:5000
    volumes:
      - .:/app
    environment:
      FLASK_ENV: development  
```
  * Run `docker-compose up` command to launch the Flask Web Application
