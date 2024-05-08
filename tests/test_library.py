from jellyfin_api_lib.operations.library import get_libraries


def test_get_libraries(setup_instance, userpass_client):
    libraries_result = get_libraries(client=userpass_client)
    assert libraries_result.is_ok()
    assert len(libraries_result.unwrap()) == 0
