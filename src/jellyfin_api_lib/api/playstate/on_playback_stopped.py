from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    item_id: str,
    *,
    media_source_id: Unset | str = UNSET,
    next_media_type: Unset | str = UNSET,
    position_ticks: Unset | int = UNSET,
    live_stream_id: Unset | str = UNSET,
    play_session_id: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["mediaSourceId"] = media_source_id

    params["nextMediaType"] = next_media_type

    params["positionTicks"] = position_ticks

    params["liveStreamId"] = live_stream_id

    params["playSessionId"] = play_session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/Users/{user_id}/PlayingItems/{item_id}",
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
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    media_source_id: Unset | str = UNSET,
    next_media_type: Unset | str = UNSET,
    position_ticks: Unset | int = UNSET,
    live_stream_id: Unset | str = UNSET,
    play_session_id: Unset | str = UNSET,
) -> Response[Any]:
    """Reports that a user has stopped playing an item.

    Args:
        user_id (str):
        item_id (str):
        media_source_id (Union[Unset, str]):
        next_media_type (Union[Unset, str]):
        position_ticks (Union[Unset, int]):
        live_stream_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        media_source_id=media_source_id,
        next_media_type=next_media_type,
        position_ticks=position_ticks,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    user_id: str,
    item_id: str,
    *,
    client: AuthenticatedClient,
    media_source_id: Unset | str = UNSET,
    next_media_type: Unset | str = UNSET,
    position_ticks: Unset | int = UNSET,
    live_stream_id: Unset | str = UNSET,
    play_session_id: Unset | str = UNSET,
) -> Response[Any]:
    """Reports that a user has stopped playing an item.

    Args:
        user_id (str):
        item_id (str):
        media_source_id (Union[Unset, str]):
        next_media_type (Union[Unset, str]):
        position_ticks (Union[Unset, int]):
        live_stream_id (Union[Unset, str]):
        play_session_id (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        item_id=item_id,
        media_source_id=media_source_id,
        next_media_type=next_media_type,
        position_ticks=position_ticks,
        live_stream_id=live_stream_id,
        play_session_id=play_session_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
