import manage


import sys
command = sys.argv[1]


if command == 'list_containers':
    containers = manage.list_containers()
    for container in containers:
        print(container)
elif command == 'list_images':
    images = manage.list_images()
    for image in images:
        print(image)
elif command == 'stop_container':
    container_id = sys.argv[2]
    manage.stop_container(container_id)
elif command == 'start_container':
    container_id = sys.argv[2]
    manage.start_container(container_id)
elif command == 'delete_container':
    container_id = sys.argv[2]
    manage.delete_container(container_id)
else:
    print('{} not valid is a not valid command'.format(command))
