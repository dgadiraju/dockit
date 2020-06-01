import docker
import os


docker_host = os.environ.get('DOCKER_HOST')
client = docker.from_env(environment={'DOCKER_HOST': docker_host})


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


def list_images():
    images_list = client.images.list(all=True)
    images = map(lambda image:
                     {
                         'image_id': image.short_id,
                         'image_tag': 'No Tag' if len(image.tags) == 0 else image.tags[0]
                     }, images_list
                    )
    return list(images)


def manage_container(container_id, action):
    container = client.containers.get(container_id)
    if action == 'stop':
        container.stop()
    elif action == 'start':
        container.start()
    else:
        container.remove()