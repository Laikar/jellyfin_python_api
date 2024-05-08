from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.user_item_data_dto import UserItemDataDto
from ...types import Response


def _get_kwargs(
    user_id: str,
    item_id: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/Users/{user_id}/FavoriteItems/{item_id}",
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
) -> Response[Any | UserItemDataDto]:
    """Unmarks item as a favorite.

    Args:
        user_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
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
) -> Any | UserItemDataDto | None:
    """Unmarks item as a favorite.

    Args:
        user_id (str):
        item_id (str):

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
    ).parsed


async def asyncio_detailed(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> Response[Any | UserItemDataDto]:
    """Unmarks item as a favorite.

    Args:
        user_id (str):
        item_id (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, UserItemDataDto]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
) -> Any | UserItemDataDto | None:
    """Unmarks item as a favorite.

    Args:
        user_id (str):
        item_id (str):

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
        )
    ).parsed