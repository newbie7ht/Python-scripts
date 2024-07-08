#Managing Docker Containers
#This script lists all running Docker containers.

import docker

def list_running_containers():
    client = docker.from_env()
    containers = client.containers.list()
    for container in containers:
        print(container.name)

list_running_containers()
