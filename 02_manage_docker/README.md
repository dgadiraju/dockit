## Manage Docker
As part of this module we will explore some of the important APIs to manage Docker containers.
### Setting up Docker Server
Here are the details to ensure you have Docker running on a server.
* Provision VM from GCP using Ubuntu 18.04.
* Setup Docker following instructions using digital ocean article from Google Search results.
* Make sure the user used for login into VM on Ubuntu is added to group docker.
```
sudo usermod -aG docker `whoami`
```
* Pull images and start containers.
```
docker pull hello-world
docker run hello-world
docker pull mysql
docker run --name mysql_container -p 5000:5000 -e MYSQL_ROOT_PASSWORD=itversity -d mysql
docker exec -it mysql_container bash
docker exec -it mysql_container mysql -u root -p
```
* Understand important commands related to managing images and containers.
  * Managing images - `docker image`

|Command           |Description |
|------------------|------------|
|docker image pull |Pull image  |
|docker image rm   |Remove image|
|docker image build|Build image |
  * Managing containers - `docker container`

|Command                |Description                       |
|-----------------------|----------------------------------|
|docker container create|Create Container                  |
|docker container start |Start Container                   |
|docker container run   |Build, Create and Start Container |
|docker logs            |Check logs of docker container    |
|docker container rm    |Remove Container                  |
|docker container ls    |List Container                    |

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
docker build -t 02_manage_docker .
```
* Start the Container
```
docker run --name 02_manage_docker_1 -v `pwd`:/app -it 02_manage_docker bash
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
