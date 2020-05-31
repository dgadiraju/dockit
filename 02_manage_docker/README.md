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
* We can open terminal and run `pip install -r requirements.txt`.
* Docker library can be imported using `import docker`
* We can configure client to connect to remote Docker Server.
```
client = docker.from_env(environment={'DOCKER_HOST': 'tcp://35.193.6.228:2375'})
```
* Listing Containers - `containers_list = client.containers.list(all=True)`
* `containers_list` contains list of container objects with ids.
* We can create a container object by saying `container = containers_list[0]`
* Here are some of the functions or attributes available for container object that can be leveraged to get information or to manage containers.
  * `container.short_id` gives us id of the container.
  * `container.name` gives us name of the container.
  * `container.status` gives us the status of the container.
  * We can use `container.stop()` to stop the container.
  * `container.start()` to start the container and `container.remove()` to remove the container.
  * For almost all the commands we have seen using `docker container ps`, we have corresponding APIs.
* Listing Images - `images_list = client.images.list(all=True)`
* APIs related to images are also similar to containers.

### Develop Python Programs
Let us develop Python Program to integrate with Flask REST APIs later.
* We will have 2 files **dock.py** and **manage.py**
* **manage.py** will have some functions to manage docker containers.
  * Listing Containers
```python
def list_containers():
    containers_list = client.containers.list(all=True)
    containers = map(lambda container:
                     {
                         'container_id': container.short_id,
                         'container_name': container.name,
                         'container_status': container.status
                     }, containers_list
                    )
    return list(containers)
```
  * Listing Images
```python
def list_images():
    images_list = client.images.list(all=True)
    images = map(lambda image:
                 {
                     'image_id': image.short_id,
                     'image_tag': 'No Tag' if len(image.tags) == 0 else image.tags[0]
                 }, images_list
                 )
    return list(images)
```
  * Managing Containers
```python
def manage_container(container_id, action):
    container = client.containers.get(container_id)
    if action == 'stop':
        container.stop()
    elif action == 'start':
        container.start()
    else:
        container.remove()
```
* We will use the same program as part of Flask based web application to manage Docker containers later.
* Here are the steps to use functions from library  `docker` to manage containers.
  * Once docker library is installed we need to `import docker`.
  * Create client object using `docker.from_env`.
  * We can pass `DOCKER_HOST` to `docker.from_env` to connect to docker server running remotely.
  
### Dockerize Application
Let us also dockerize our application so that we can streamline our development process.
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
