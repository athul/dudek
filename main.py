import typer
from docker_image_deployer.docker import get_exposed_image_ports

cli = typer.Typer()

@cli.command()
def main(image_name:str):
    print(get_exposed_image_ports(image_name=image_name))

if __name__ == "__main__":
    cli()
