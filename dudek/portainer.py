from typing import Any
import requests
import os

URL: str | None = os.getenv("PORTAINER_URL")

HEADERS = {
    "Authorization": f"Bearer {os.getenv("PORTAINER_KEY")}",
    "content-type": "application/json",
}


def create_container(cname: str, image: str) -> dict:
    querystring = {"name": cname}
    payload: dict[Any, Any] = {
        "Image": image,
        "Env": [],
        "MacAddress": "",
        "ExposedPorts": {},
        "Entrypoint": None,
        "HostConfig": {
            "RestartPolicy": {"Name": "no"},
            "PortBindings": {},
            "PublishAllPorts": True,
            "Binds": [],
            "AutoRemove": False,
            "NetworkMode": "bridge",
            "Privileged": False,
            "Init": False,
            "Runtime": None,
            "ExtraHosts": [],
            "Devices": [],
            "DeviceRequests": [],
            "Sysctls": {},
            "Dns": [],
            "ShmSize": 67108864,
            "Memory": 0,
            "MemoryReservation": 0,
            "NanoCpus": 0,
        },
        "NetworkingConfig": {
            "EndpointsConfig": {
                "bridge": {"IPAMConfig": {"IPv4Address": "", "IPv6Address": ""}}
            }
        },
        "Labels": {},
        "name": cname,
        "OpenStdin": False,
        "Tty": False,
        "Volumes": {},
    }

    response = requests.post(
        URL + "create", json=payload, headers=HEADERS, params=querystring
    )
    return response.json()


def start_container(cresp: requests.Response) -> str:
    cid: str | None = cresp.get("Id")
    req: requests.Response = requests.post(URL + f"{cid}/start", headers=HEADERS)
    if req.status_code == 204:
        print("Container has started")
    return cid


def get_container_ports(id, eport) -> str:
    req: requests.Response = requests.get(URL + f"{id}/json", headers=HEADERS)
    res: dict = req.json()
    if eport:
        hostport: str = res["NetworkSettings"]["Ports"][eport][0]["HostPort"]
    else:
        ports: dict = res["NetworkSettings"]["Ports"]
        all_ports: dict = list(ports.values())[0][0]
        hostport: str = all_ports["HostPort"]
    return hostport
