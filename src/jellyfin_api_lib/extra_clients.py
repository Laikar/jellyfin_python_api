from .api.system import get_public_system_info
from .api.user import authenticate_user_by_name
from .client import AuthenticatedClient, Client
from .models.authenticate_user_by_name import AuthenticateUserByName


def HeaderClient(
    base_url: str, client_name: str = "API Client", device_name: str = "Controller", device_id: str = "api_lib_device", version: str = None, token: str = None
):
    with Client(base_url=base_url) as client:
        public_info_response = get_public_system_info.sync(client=client)
        if version is None:
            version = public_info_response.version
        common_headers = {
            "MediaBrowser Client": f"{client_name}",
            "Device": f"{device_name}",
            "DeviceId": f"{device_id}",
            "Version": f"{version}",
        }
        if token is not None:
            common_headers["Token"] = token
        headers = {"X-Emby-Authorization": ", ".join(f'{key}="{value}"' for key, value in common_headers.items())}
        return client.with_headers(headers=headers)


def UserPassClient(
    base_url: str,
    username: str,
    password: str,
    client_name: str = "API Client",
    device_name: str = "Controller",
    device_id: str = "api_lib_device",
    version: str = None,
):
    with HeaderClient(base_url=base_url, client_name=client_name, device_name=device_name, device_id=device_id, version=version) as base_client:
        public_info_response = get_public_system_info.sync(client=base_client)
        if version is None:
            version = public_info_response.version
        auth_result = authenticate_user_by_name.sync_detailed(client=base_client, body=AuthenticateUserByName(username=username, pw=password))
        match auth_result.status_code:
            case 200:
                token = auth_result.parsed.access_token
                return HeaderClient(base_url=base_url, client_name=client_name, device_name=device_name, device_id=device_id, version=version, token=token)
            case _:
                raise ValueError("Unknown Error")


def KeyClient(
    base_url: str, key: str, client_name: str = "API Client", device_name: str = "Controller", device_id: str = "api_lib_device", version: str = None
):
    with Client(base_url=base_url) as client:
        public_info_response = get_public_system_info.sync(client=client)
        if version is None:
            version = public_info_response.version
    common_headers = {
        "MediaBrowser Client": f"{client_name}",
        "Device": f"{device_name}",
        "DeviceId": f"{device_id}",
        "Version": f"{version}",
    }
    headers = {"X-Emby-Authorization": ", ".join(f'{key}="{value}"' for key, value in common_headers.items())}
    return AuthenticatedClient(base_url=base_url, token=key).with_headers(headers=headers)
