import pytest
from jellyfin_api_lib.operations.api_keys import create_api_keys, delete_api_keys, get_api_keys


def test_get_api_keys(setup_instance, userpass_client):
    keys_result = get_api_keys(client=userpass_client)
    assert keys_result.is_ok()
    assert len(keys_result.unwrap()) == 0


createkeys = [
    (["Key1", "Key1"], False, ["Key1"]),
    (["Key1", "Key2"], False, ["Key1", "Key2"]),
    (["Key1", "Key1"], True, ["Key1", "Key1"]),
]


@pytest.mark.parametrize("key_list,duplicates,expected", createkeys)
def test_create_keys(setup_instance, userpass_client, key_list, duplicates, expected):
    create_keys_result = create_api_keys(userpass_client, key_names=key_list, create_duplciates=duplicates)
    assert create_keys_result.is_ok()
    # TODO Test that create_api_keys returns the list of created keys
    keys = get_api_keys(client=userpass_client).unwrap()
    assert len(keys) == len(expected)
    for key in keys.values():
        assert key in expected
        expected.remove(key)
    assert len(expected) == 0


deletekeys = [
    (["Key1", "Key2", "Key3"], ["Key1", "Key2"], False, ["Key3"]),
    (["Key1", "Key1", "Key3"], ["Key1"], True, ["Key1", "Key3"]),
    (["Key1", "Key1", "Key3"], ["Key1"], False, ["Key3"]),
]


@pytest.mark.parametrize("existing_keys, key_list, duplicates, expected", deletekeys)
def test_delete_keys(setup_instance, userpass_client, existing_keys, key_list, duplicates, expected):
    create_api_keys(userpass_client, existing_keys, True).unwrap()
    keys = get_api_keys(client=userpass_client).unwrap()

    delete_keys_result = delete_api_keys(userpass_client, key_list, duplicates)
    assert delete_keys_result.is_ok()
    keys = get_api_keys(client=userpass_client).unwrap()
    assert len(keys) == len(expected)
    for key in keys.values():
        assert key in expected
        expected.remove(key)
    assert len(expected) == 0
