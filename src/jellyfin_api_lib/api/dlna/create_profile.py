from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.device_profile import DeviceProfile
from ...types import Response


def _get_kwargs(
    *,
    body: DeviceProfile | DeviceProfile,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/Dlna/Profiles",
    }

    if isinstance(body, DeviceProfile):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, DeviceProfile):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
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
    *,
    client: AuthenticatedClient,
    body: DeviceProfile | DeviceProfile,
) -> Response[Any]:
    """Creates a profile.

    Args:
        body (DeviceProfile): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata
            which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video
            and/or audio, including codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        body (DeviceProfile): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata
            which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video
            and/or audio, including codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: DeviceProfile | DeviceProfile,
) -> Response[Any]:
    """Creates a profile.

    Args:
        body (DeviceProfile): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata
            which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video
            and/or audio, including codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.
        body (DeviceProfile): A MediaBrowser.Model.Dlna.DeviceProfile represents a set of metadata
            which determines which content a certain device is able to play.
            <br />
            Specifically, it defines the supported <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.ContainerProfiles">containers</see> and
            <see cref="P:MediaBrowser.Model.Dlna.DeviceProfile.CodecProfiles">codecs</see> (video
            and/or audio, including codec profiles and levels)
            the device is able to direct play (without transcoding or remuxing),
            as well as which <see
            cref="P:MediaBrowser.Model.Dlna.DeviceProfile.TranscodingProfiles">containers/codecs to
            transcode to</see> in case it isn't.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
