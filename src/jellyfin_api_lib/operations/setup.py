from result import Err, Ok, Result

from ..api.startup import complete_wizard, get_first_user, set_remote_access, update_initial_configuration, update_startup_user
from ..api.system import get_public_system_info
from ..models.startup_configuration_dto import StartupConfigurationDto
from ..models.startup_remote_access_dto import StartupRemoteAccessDto
from ..models.startup_user_dto import StartupUserDto


def setup_completed(client) -> Result[bool, str]:
    system_info_response = get_public_system_info.sync_detailed(client=client)
    if system_info_response.status_code != 200:
        return Err("Unexpected response when obtainning system info")
    return Ok(system_info_response.parsed.startup_wizard_completed)


def setup(client, admin_user, admin_password, automatic_port_mapping, remote_access, metadata_country_code, metadata_language, ui_culture) -> Result[None, str]:
    # This needs to be done or jellyfin throws server error on updating startup user
    default_user_response = get_first_user.sync_detailed(client=client)
    if default_user_response.status_code != 200:
        return Err("Unexpected response when obtaining default user")

    update_user_response = update_startup_user.sync_detailed(client=client, body=StartupUserDto(name=admin_user, password=admin_password))
    if update_user_response.status_code != 204:
        return Err("Unexpected response when updating default user")
    remote_asccess_response = set_remote_access.sync_detailed(
        client=client, body=StartupRemoteAccessDto(enable_automatic_port_mapping=automatic_port_mapping, enable_remote_access=remote_access)
    )
    if remote_asccess_response.status_code != 204:
        return Err("Unexpected response when updating remote acess settings")
    initial_config_response = update_initial_configuration.sync_detailed(
        client=client,
        body=StartupConfigurationDto(metadata_country_code=metadata_country_code, preferred_metadata_language=metadata_language, ui_culture=ui_culture),
    )
    if initial_config_response.status_code != 204:
        return Err("Unexpected response when updating initial configuration")
    complete_wizrd_request = complete_wizard.sync_detailed(client=client)
    if complete_wizrd_request.status_code != 204:
        return Err("Unexpected response when finishing the setup wizard")
    return Ok(None)
