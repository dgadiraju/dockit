## Integrate Docker and Flask

Let us understand how we can integrate Docker and Flask using REST APIs.
* Make sure **requirements.txt** have the required dependencies for Flask and Docker.
* Develop functions in **app.py**
  * End point - `containers`
    * Request Type - `GET`
    * Function - `list_containers`
  * End point - `images`
    * Request Type - `GET`
    * Function - `list_images`
* Let us also start exploring docker compose which can streamline the process of integrating and managing multiple containers.
  * Create Dockerfile using Dockerfile of this repository
  * Create **docker-compose.yml** file for the following
    * Build the image
    * Create the container
    * Start the container by mounting the source code
  * Run `docker-compose up` command to launch the Flask Web Application
