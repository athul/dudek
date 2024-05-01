import typer
from dudek.docker import get_exposed_image_ports
from dudek.portainer import create_container, start_container, get_container_ports
from dudek.domain import add_domain

cli = typer.Typer()


@cli.command("deploy")
def main(image_name: str):
    try:
        port_str: list[str] | str = get_exposed_image_ports(image_name=image_name)
        exposed_port: int | None = int(port_str[0].split("/")[0])
    except Exception:
        port_str = ""
    domain: str = typer.prompt("Please specify the Domain name for the container")
    print(f"The domain name will be {domain}.aj.athulcyriac.in")
    if port_str:
        print(f"The Exposed port of the image config seems to be {str(exposed_port)}")
    else:
        print("Could not find the image locally for checking port")
    container_name = typer.prompt("What should the container be named?")
    container = create_container(container_name, image_name)
    cid = start_container(container)
    hostport = get_container_ports(cid, port_str[0])
    add_domain(f"{domain}.aj.athulcyriac.in", hostport)
