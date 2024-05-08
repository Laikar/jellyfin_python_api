import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_item_data_dto import UserItemDataDto
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    item_id: str,
    *,
    date_played: Unset | datetime.datetime = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_date_played: Unset | str = UNSET
    if not isinstance(date_played, Unset):
        json_date_played = date_played.isoformat()
    params["datePlayed"] = json_date_played

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/Users/{user_id}/PlayedItems/{item_id}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | UserItemDataDto | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = UserItemDataDto.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | UserItemDataDto]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    date_played: Unset | datetime.datetime = UNSET,
) -> Response[Any | UserItemDataDto]:
    """Marks an item as played for user.

    Args:
        user_id (str):
        item_id (str):
        date_played (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        date_played=date_played,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    date_played: Unset | datetime.datetime = UNSET,
) -> Any | UserItemDataDto | None:
    """Marks an item as played for user.

    Args:
        user_id (str):
        item_id (str):
        date_played (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserItemDataDto]
    """

    return sync_detailed(
        user_id=user_id,
        item_id=item_id,
        client=client,
        date_played=date_played,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    date_played: Unset | datetime.datetime = UNSET,
) -> Response[Any | UserItemDataDto]:
    """Marks an item as played for user.

    Args:
        user_id (str):
        item_id (str):
        date_played (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        date_played=date_played,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    date_played: Unset | datetime.datetime = UNSET,
) -> Any | UserItemDataDto | None:
    """Marks an item as played for user.

    Args:
        user_id (str):
        item_id (str):
        date_played (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, UserItemDataDto]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            item_id=item_id,
            client=client,
            date_played=date_played,
        )
    ).parsed
