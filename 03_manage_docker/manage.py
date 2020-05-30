import docker


def get_client():
    return docker.from_env(environment={'DOCKER_HOST': 'tcp://35.193.6.228:2375'})


def list_containers():
    client = get_client()
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
    client = get_client()
    images_list = client.images.list(all=True)
    images = map(lambda image:
                 {
                     'image_id': image.short_id,
                     'image_tag': 'No Tag' if len(image.tags) == 0 else image.tags[0]
                 }, images_list
                 )
    return list(images)


def stop_container(container_id):
    client = get_client()
    container = client.containers.get(container_id)
    container.stop()


def start_container(container_id):
    client = get_client()
    container = client.containers.get(container_id)
    container.start()


def delete_container(container_id):
    client = get_client()
    container = client.containers.get(container_id)
    container.remove()
