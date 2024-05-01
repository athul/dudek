import requests
import os


url = os.getenv("PROXY_URL")


def add_domain(domain_name: str, port: int):
    payload = {
        "domain_names": [domain_name],
        "forward_scheme": "http",
        "forward_host": "172.17.0.1",
        "forward_port": port,
        "caching_enabled": True,
        "block_exploits": True,
        "allow_websocket_upgrade": True,
        "access_list_id": "0",
        "certificate_id": 8,
        "ssl_forced": True,
        "meta": {"letsencrypt_agree": False, "dns_challenge": False},
        "advanced_config": "",
        "locations": [],
        "http2_support": False,
        "hsts_enabled": False,
        "hsts_subdomains": False,
    }
    headers = {
        "Authorization": f"Bearer {os.getenv('PROXY_KEY')}",
        "content-type": "application/json",
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.ok:
        print(f"Domain created!. Access the service at {domain_name}")
