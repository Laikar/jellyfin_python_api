from http import HTTPStatus
from io import BytesIO
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_format: str,
    *,
    item_id: Unset | str = UNSET,
    media_source_id: Unset | str = UNSET,
    index: Unset | int = UNSET,
    format_: Unset | str = UNSET,
    end_position_ticks: Unset | int = UNSET,
    copy_timestamps: Unset | bool = False,
    add_vtt_time_map: Unset | bool = False,
    start_position_ticks: Unset | int = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["itemId"] = item_id

    params["mediaSourceId"] = media_source_id

    params["index"] = index

    params["format"] = format_

    params["endPositionTicks"] = end_position_ticks

    params["copyTimestamps"] = copy_timestamps

    params["addVttTimeMap"] = add_vtt_time_map

    params["startPositionTicks"] = start_position_ticks

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Videos/{route_item_id}/{route_media_source_id}/Subtitles/{route_index}/Stream.{route_format}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> File | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.text))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[File]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: Unset | str = UNSET,
    media_source_id: Unset | str = UNSET,
    index: Unset | int = UNSET,
    format_: Unset | str = UNSET,
    end_position_ticks: Unset | int = UNSET,
    copy_timestamps: Unset | bool = False,
    add_vtt_time_map: Unset | bool = False,
    start_position_ticks: Unset | int = 0,
) -> Response[File]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (str):
        route_media_source_id (str):
        route_index (int):
        route_format (str):
        item_id (Union[Unset, str]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.
        start_position_ticks (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
        start_position_ticks=start_position_ticks,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: Unset | str = UNSET,
    media_source_id: Unset | str = UNSET,
    index: Unset | int = UNSET,
    format_: Unset | str = UNSET,
    end_position_ticks: Unset | int = UNSET,
    copy_timestamps: Unset | bool = False,
    add_vtt_time_map: Unset | bool = False,
    start_position_ticks: Unset | int = 0,
) -> File | None:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (str):
        route_media_source_id (str):
        route_index (int):
        route_format (str):
        item_id (Union[Unset, str]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.
        start_position_ticks (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return sync_detailed(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_format=route_format,
        client=client,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
        start_position_ticks=start_position_ticks,
    ).parsed


async def asyncio_detailed(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: Unset | str = UNSET,
    media_source_id: Unset | str = UNSET,
    index: Unset | int = UNSET,
    format_: Unset | str = UNSET,
    end_position_ticks: Unset | int = UNSET,
    copy_timestamps: Unset | bool = False,
    add_vtt_time_map: Unset | bool = False,
    start_position_ticks: Unset | int = 0,
) -> Response[File]:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (str):
        route_media_source_id (str):
        route_index (int):
        route_format (str):
        item_id (Union[Unset, str]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.
        start_position_ticks (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[File]
    """

    kwargs = _get_kwargs(
        route_item_id=route_item_id,
        route_media_source_id=route_media_source_id,
        route_index=route_index,
        route_format=route_format,
        item_id=item_id,
        media_source_id=media_source_id,
        index=index,
        format_=format_,
        end_position_ticks=end_position_ticks,
        copy_timestamps=copy_timestamps,
        add_vtt_time_map=add_vtt_time_map,
        start_position_ticks=start_position_ticks,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    route_item_id: str,
    route_media_source_id: str,
    route_index: int,
    route_format: str,
    *,
    client: AuthenticatedClient | Client,
    item_id: Unset | str = UNSET,
    media_source_id: Unset | str = UNSET,
    index: Unset | int = UNSET,
    format_: Unset | str = UNSET,
    end_position_ticks: Unset | int = UNSET,
    copy_timestamps: Unset | bool = False,
    add_vtt_time_map: Unset | bool = False,
    start_position_ticks: Unset | int = 0,
) -> File | None:
    """Gets subtitles in a specified format.

    Args:
        route_item_id (str):
        route_media_source_id (str):
        route_index (int):
        route_format (str):
        item_id (Union[Unset, str]):
        media_source_id (Union[Unset, str]):
        index (Union[Unset, int]):
        format_ (Union[Unset, str]):
        end_position_ticks (Union[Unset, int]):
        copy_timestamps (Union[Unset, bool]):  Default: False.
        add_vtt_time_map (Union[Unset, bool]):  Default: False.
        start_position_ticks (Union[Unset, int]):  Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        File
    """

    return (
        await asyncio_detailed(
            route_item_id=route_item_id,
            route_media_source_id=route_media_source_id,
            route_index=route_index,
            route_format=route_format,
            client=client,
            item_id=item_id,
            media_source_id=media_source_id,
            index=index,
            format_=format_,
            end_position_ticks=end_position_ticks,
            copy_timestamps=copy_timestamps,
            add_vtt_time_map=add_vtt_time_map,
            start_position_ticks=start_position_ticks,
        )
    ).parsed
