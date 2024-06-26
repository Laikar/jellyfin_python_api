from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.session_info import SessionInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    controllable_by_user_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    active_within_seconds: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["controllableByUserId"] = controllable_by_user_id

    params["deviceId"] = device_id

    params["activeWithinSeconds"] = active_within_seconds

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Sessions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | list["SessionInfo"] | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = SessionInfo.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | list["SessionInfo"]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    active_within_seconds: Unset | int = UNSET,
) -> Response[Any | list["SessionInfo"]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SessionInfo']]]
    """

    kwargs = _get_kwargs(
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    active_within_seconds: Unset | int = UNSET,
) -> Any | list["SessionInfo"] | None:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SessionInfo']]
    """

    return sync_detailed(
        client=client,
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    active_within_seconds: Unset | int = UNSET,
) -> Response[Any | list["SessionInfo"]]:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, List['SessionInfo']]]
    """

    kwargs = _get_kwargs(
        controllable_by_user_id=controllable_by_user_id,
        device_id=device_id,
        active_within_seconds=active_within_seconds,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    controllable_by_user_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    active_within_seconds: Unset | int = UNSET,
) -> Any | list["SessionInfo"] | None:
    """Gets a list of sessions.

    Args:
        controllable_by_user_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        active_within_seconds (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, List['SessionInfo']]
    """

    return (
        await asyncio_detailed(
            client=client,
            controllable_by_user_id=controllable_by_user_id,
            device_id=device_id,
            active_within_seconds=active_within_seconds,
        )
    ).parsed
