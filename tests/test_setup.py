from jellyfin_api_lib.operations.setup import setup, setup_completed


def test_check_result(start_container, client):
    setup_not_completed_result = setup_completed(client=client)
    assert setup_not_completed_result.is_ok()
    assert setup_not_completed_result.unwrap() is False


def test_perform_setup(start_container, client):
    setup_not_completed_result = setup_completed(client=client)
    assert setup_not_completed_result.is_ok()
    assert setup_not_completed_result.unwrap() is False
    result = setup(
        client=client,
        admin_user="admin",
        admin_password="admin123",
        automatic_port_mapping=False,
        remote_access=True,
        metadata_country_code="EN",
        metadata_language="en",
        ui_culture="en-US",
    )
    assert result.is_ok()
    setup_completed_result = setup_completed(client=client)
    assert setup_completed_result.is_ok()
    assert setup_completed_result.unwrap() is True
