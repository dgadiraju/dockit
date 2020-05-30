## Manage Docker
As part of this project we will explore some of the important APIs to manage Docker containers.
### Setting up Docker Server
Here are the details to ensure you have Docker running on a server.
* Provision VM from GCP using Ubuntu 18.04.
* Setup Docker following instructions
* Make sure the user used for login into VM on Ubuntu is added to group docker.
* Pull images and start containers.
* Understand important commands related to managing images and containers.
### Docker APIs
Here are the instructions to explore APIs or functions to manage docker containers using Python based libraries.
* Create Project using pycharm or any other IDE
* Create **requirements.txt** and add the dependencies.
```
docker==4.2.0
```
* We will have 2 files **dock.py** and **manage.py**
* **manage.py** will have some functions to manage docker containers.
* We will use the same program as part of Flask based web application to manage Docker containers later.
* Here are the steps to use functions from library  `docker` to manage containers.
  * Once docker library is installed we need to `import docker`.
  * Create client object using `docker.from_env`.
  * We can pass `DOCKER_HOST` to `docker.from_env` to connect to docker server running remotely.
* We will continue using Docker based approach to build run time environment to run the APIs.
* Create Dockerfile using Dockerfile of this repository
* Build the image
```
docker build -t dockit .
```
* Start the Container
```
docker run --name 03_manage_docker_1 -it dockit bash
```
* Here are some of the commands which can be used to validate.
```
python dock.py list_containers
python dock.py list_images
python dock.py stop_container 92565afacf
python dock.py list_containers
python dock.py start_container 92565afacf
python dock.py list_containers
```
