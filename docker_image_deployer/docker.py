import docker
from docker.models.images import Image

client = docker.DockerClient(base_url="unix:///run/user/1000/podman/podman.sock")

def get_exposed_image_ports(image_name:str) -> list[str] :
    image:Image = client.images.get(image_name)
    breakpoint()
    ports = image.attrs.get("Config").get("ExposedPorts")
    return list(ports.keys())


