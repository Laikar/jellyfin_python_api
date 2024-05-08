from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    playlist_id: str,
    *,
    entry_ids: Unset | list[str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_entry_ids: Unset | list[str] = UNSET
    if not isinstance(entry_ids, Unset):
        json_entry_ids = entry_ids

    params["entryIds"] = json_entry_ids

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/Playlists/{playlist_id}/Items",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == HTTPStatus.NO_CONTENT:
        return None
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        return None
    if response.status_code == HTTPStatus.FORBIDDEN:
        return None
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    entry_ids: Unset | list[str] = UNSET,
) -> Response[Any]:
    """Removes items from a playlist.

    Args:
        playlist_id (str):
        entry_ids (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        entry_ids=entry_ids,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    playlist_id: str,
    *,
    client: AuthenticatedClient,
    entry_ids: Unset | list[str] = UNSET,
) -> Response[Any]:
    """Removes items from a playlist.

    Args:
        playlist_id (str):
        entry_ids (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        playlist_id=playlist_id,
        entry_ids=entry_ids,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
