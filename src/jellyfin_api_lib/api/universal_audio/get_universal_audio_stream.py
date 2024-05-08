from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    container: Unset | list[str] = UNSET,
    media_source_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    audio_codec: Unset | str = UNSET,
    max_audio_channels: Unset | int = UNSET,
    transcoding_audio_channels: Unset | int = UNSET,
    max_streaming_bitrate: Unset | int = UNSET,
    audio_bit_rate: Unset | int = UNSET,
    start_time_ticks: Unset | int = UNSET,
    transcoding_container: Unset | str = UNSET,
    transcoding_protocol: Unset | str = UNSET,
    max_audio_sample_rate: Unset | int = UNSET,
    max_audio_bit_depth: Unset | int = UNSET,
    enable_remote_media: Unset | bool = UNSET,
    break_on_non_key_frames: Unset | bool = False,
    enable_redirection: Unset | bool = True,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_container: Unset | list[str] = UNSET
    if not isinstance(container, Unset):
        json_container = container

    params["container"] = json_container

    params["mediaSourceId"] = media_source_id

    params["deviceId"] = device_id

    params["userId"] = user_id

    params["audioCodec"] = audio_codec

    params["maxAudioChannels"] = max_audio_channels

    params["transcodingAudioChannels"] = transcoding_audio_channels

    params["maxStreamingBitrate"] = max_streaming_bitrate

    params["audioBitRate"] = audio_bit_rate

    params["startTimeTicks"] = start_time_ticks

    params["transcodingContainer"] = transcoding_container

    params["transcodingProtocol"] = transcoding_protocol

    params["maxAudioSampleRate"] = max_audio_sample_rate

    params["maxAudioBitDepth"] = max_audio_bit_depth

    params["enableRemoteMedia"] = enable_remote_media

    params["breakOnNonKeyFrames"] = break_on_non_key_frames

    params["enableRedirection"] = enable_redirection

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Audio/{item_id}/universal",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == HTTPStatus.FOUND:
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
    item_id: str,
    *,
    client: AuthenticatedClient,
    container: Unset | list[str] = UNSET,
    media_source_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    audio_codec: Unset | str = UNSET,
    max_audio_channels: Unset | int = UNSET,
    transcoding_audio_channels: Unset | int = UNSET,
    max_streaming_bitrate: Unset | int = UNSET,
    audio_bit_rate: Unset | int = UNSET,
    start_time_ticks: Unset | int = UNSET,
    transcoding_container: Unset | str = UNSET,
    transcoding_protocol: Unset | str = UNSET,
    max_audio_sample_rate: Unset | int = UNSET,
    max_audio_bit_depth: Unset | int = UNSET,
    enable_remote_media: Unset | bool = UNSET,
    break_on_non_key_frames: Unset | bool = False,
    enable_redirection: Unset | bool = True,
) -> Response[Any]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, List[str]]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        max_audio_channels (Union[Unset, int]):
        transcoding_audio_channels (Union[Unset, int]):
        max_streaming_bitrate (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        transcoding_container (Union[Unset, str]):
        transcoding_protocol (Union[Unset, str]):
        max_audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        enable_remote_media (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):  Default: False.
        enable_redirection (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    container: Unset | list[str] = UNSET,
    media_source_id: Unset | str = UNSET,
    device_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    audio_codec: Unset | str = UNSET,
    max_audio_channels: Unset | int = UNSET,
    transcoding_audio_channels: Unset | int = UNSET,
    max_streaming_bitrate: Unset | int = UNSET,
    audio_bit_rate: Unset | int = UNSET,
    start_time_ticks: Unset | int = UNSET,
    transcoding_container: Unset | str = UNSET,
    transcoding_protocol: Unset | str = UNSET,
    max_audio_sample_rate: Unset | int = UNSET,
    max_audio_bit_depth: Unset | int = UNSET,
    enable_remote_media: Unset | bool = UNSET,
    break_on_non_key_frames: Unset | bool = False,
    enable_redirection: Unset | bool = True,
) -> Response[Any]:
    """Gets an audio stream.

    Args:
        item_id (str):
        container (Union[Unset, List[str]]):
        media_source_id (Union[Unset, str]):
        device_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        audio_codec (Union[Unset, str]):
        max_audio_channels (Union[Unset, int]):
        transcoding_audio_channels (Union[Unset, int]):
        max_streaming_bitrate (Union[Unset, int]):
        audio_bit_rate (Union[Unset, int]):
        start_time_ticks (Union[Unset, int]):
        transcoding_container (Union[Unset, str]):
        transcoding_protocol (Union[Unset, str]):
        max_audio_sample_rate (Union[Unset, int]):
        max_audio_bit_depth (Union[Unset, int]):
        enable_remote_media (Union[Unset, bool]):
        break_on_non_key_frames (Union[Unset, bool]):  Default: False.
        enable_redirection (Union[Unset, bool]):  Default: True.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        container=container,
        media_source_id=media_source_id,
        device_id=device_id,
        user_id=user_id,
        audio_codec=audio_codec,
        max_audio_channels=max_audio_channels,
        transcoding_audio_channels=transcoding_audio_channels,
        max_streaming_bitrate=max_streaming_bitrate,
        audio_bit_rate=audio_bit_rate,
        start_time_ticks=start_time_ticks,
        transcoding_container=transcoding_container,
        transcoding_protocol=transcoding_protocol,
        max_audio_sample_rate=max_audio_sample_rate,
        max_audio_bit_depth=max_audio_bit_depth,
        enable_remote_media=enable_remote_media,
        break_on_non_key_frames=break_on_non_key_frames,
        enable_redirection=enable_redirection,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
