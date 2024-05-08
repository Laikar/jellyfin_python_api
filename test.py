import pprint
import time

import requests
from testcontainers.core.container import DockerContainer

with DockerContainer(image="lscr.io/linuxserver/jellyfin").with_exposed_ports(8096) as container:
    print(container.get_container_host_ip())
    exposed_port = container.get_exposed_port(8096)
    print(exposed_port)
    while True:
        try:
            response = requests.get(f"http://localhost:{exposed_port}/System/Info")
            pprint.pprint(response)
            if response.status_code == 200:
                break
        except requests.RequestException:
            pass  # Ignore connection errors
        print("waiting")
        time.sleep(4)
