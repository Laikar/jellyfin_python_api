import time

import docker
import pytest
import requests
from jellyfin_api_lib import Client, HeaderClient, KeyClient, UserPassClient
from jellyfin_api_lib.operations.setup import setup
from podman import PodmanClient
from testcontainers.core.container import DockerContainer


def start_container_docker():
    docker_client = docker.from_env()
    container = docker_client.containers.run(image="lscr.io/linuxserver/jellyfin", name="jellyfin", detach=True, ports={"8096": "8096"})

    while True:
        try:
            response = requests.get("http://localhost:8096/System/Info")
            if response.status_code == 200:
                break
        except requests.RequestException:
            pass  # Ignore connection errors
        time.sleep(0.5)
    yield container
    container.stop()
    container.remove(v=True)
    docker_client.close()


@pytest.fixture
def start_container_podman():
    with PodmanClient.from_env() as client:
        container = client.containers.run(image="lscr.io/linuxserver/jellyfin", name="jellyfin", detach=True, ports={"8096": "8096"})
        while True:
            try:
                response = requests.get("http://localhost:8096/System/Info")
                if response.status_code == 200:
                    break
            except requests.RequestException:
                pass  # Ignore connection errors
            time.sleep(0.5)
        yield container
        container.stop()
        container.remove(v=True)


def wait_for_jellyfin(port):
    while True:
        try:
            response = requests.get(f"http://localhost:{port}/System/Info")
            if response.status_code == 200:
                break
        except requests.RequestException:
            pass  # Ignore connection errors
        time.sleep(0.5)


@pytest.fixture
def start_container():
    with DockerContainer(image="lscr.io/linuxserver/jellyfin").with_exposed_ports(8096) as container:
        wait_for_jellyfin(container.get_exposed_port(8096))
        yield container


@pytest.fixture
def setup_instance(start_container):
    with HeaderClient(base_url=f"http://localhost:{start_container.get_exposed_port(8096)}") as client:
        setup(
            client=client,
            admin_user="admin",
            admin_password="admin123",
            automatic_port_mapping=False,
            remote_access=True,
            metadata_country_code="EN",
            metadata_language="en",
            ui_culture="en-US",
        ).expect("Somethign went wrong, jellyfin is not reachable")


@pytest.fixture
def client(start_container):
    with Client(base_url=f"http://localhost:{start_container.get_exposed_port(8096)}") as client:
        yield client


@pytest.fixture
def header_client(start_container):
    with HeaderClient(base_url=f"http://localhost:{start_container.get_exposed_port(8096)}") as client:
        yield client


@pytest.fixture
def userpass_client(start_container, user="admin", password="admin123"):
    with UserPassClient(base_url=f"http://localhost:{start_container.get_exposed_port(8096)}", username=user, password=password) as client:
        yield client


@pytest.fixture
def key_client(start_container, key):
    with KeyClient(base_url=f"http://localhost:{start_container.get_exposed_port(8096)}", key=key) as client:
        yield client
