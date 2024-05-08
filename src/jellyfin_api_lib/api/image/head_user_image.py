from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_format import ImageFormat
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    image_type: ImageType,
    *,
    tag: Unset | str = UNSET,
    format_: Unset | ImageFormat = UNSET,
    max_width: Unset | int = UNSET,
    max_height: Unset | int = UNSET,
    percent_played: Unset | float = UNSET,
    unplayed_count: Unset | int = UNSET,
    width: Unset | int = UNSET,
    height: Unset | int = UNSET,
    quality: Unset | int = UNSET,
    fill_width: Unset | int = UNSET,
    fill_height: Unset | int = UNSET,
    crop_whitespace: Unset | bool = UNSET,
    add_played_indicator: Unset | bool = UNSET,
    blur: Unset | int = UNSET,
    background_color: Unset | str = UNSET,
    foreground_layer: Unset | str = UNSET,
    image_index: Unset | int = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tag"] = tag

    json_format_: Unset | str = UNSET
    if not isinstance(format_, Unset):
        json_format_ = format_.value

    params["format"] = json_format_

    params["maxWidth"] = max_width

    params["maxHeight"] = max_height

    params["percentPlayed"] = percent_played

    params["unplayedCount"] = unplayed_count

    params["width"] = width

    params["height"] = height

    params["quality"] = quality

    params["fillWidth"] = fill_width

    params["fillHeight"] = fill_height

    params["cropWhitespace"] = crop_whitespace

    params["addPlayedIndicator"] = add_played_indicator

    params["blur"] = blur

    params["backgroundColor"] = background_color

    params["foregroundLayer"] = foreground_layer

    params["imageIndex"] = image_index

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "head",
        "url": f"/Users/{user_id}/Images/{image_type}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | None:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient | Client,
    tag: Unset | str = UNSET,
    format_: Unset | ImageFormat = UNSET,
    max_width: Unset | int = UNSET,
    max_height: Unset | int = UNSET,
    percent_played: Unset | float = UNSET,
    unplayed_count: Unset | int = UNSET,
    width: Unset | int = UNSET,
    height: Unset | int = UNSET,
    quality: Unset | int = UNSET,
    fill_width: Unset | int = UNSET,
    fill_height: Unset | int = UNSET,
    crop_whitespace: Unset | bool = UNSET,
    add_played_indicator: Unset | bool = UNSET,
    blur: Unset | int = UNSET,
    background_color: Unset | str = UNSET,
    foreground_layer: Unset | str = UNSET,
    image_index: Unset | int = UNSET,
) -> Response[ProblemDetails]:
    """Get user profile image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        crop_whitespace (Union[Unset, bool]):
        add_played_indicator (Union[Unset, bool]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        image_type=image_type,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        crop_whitespace=crop_whitespace,
        add_played_indicator=add_played_indicator,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        image_index=image_index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient | Client,
    tag: Unset | str = UNSET,
    format_: Unset | ImageFormat = UNSET,
    max_width: Unset | int = UNSET,
    max_height: Unset | int = UNSET,
    percent_played: Unset | float = UNSET,
    unplayed_count: Unset | int = UNSET,
    width: Unset | int = UNSET,
    height: Unset | int = UNSET,
    quality: Unset | int = UNSET,
    fill_width: Unset | int = UNSET,
    fill_height: Unset | int = UNSET,
    crop_whitespace: Unset | bool = UNSET,
    add_played_indicator: Unset | bool = UNSET,
    blur: Unset | int = UNSET,
    background_color: Unset | str = UNSET,
    foreground_layer: Unset | str = UNSET,
    image_index: Unset | int = UNSET,
) -> ProblemDetails | None:
    """Get user profile image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        crop_whitespace (Union[Unset, bool]):
        add_played_indicator (Union[Unset, bool]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return sync_detailed(
        user_id=user_id,
        image_type=image_type,
        client=client,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        crop_whitespace=crop_whitespace,
        add_played_indicator=add_played_indicator,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        image_index=image_index,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient | Client,
    tag: Unset | str = UNSET,
    format_: Unset | ImageFormat = UNSET,
    max_width: Unset | int = UNSET,
    max_height: Unset | int = UNSET,
    percent_played: Unset | float = UNSET,
    unplayed_count: Unset | int = UNSET,
    width: Unset | int = UNSET,
    height: Unset | int = UNSET,
    quality: Unset | int = UNSET,
    fill_width: Unset | int = UNSET,
    fill_height: Unset | int = UNSET,
    crop_whitespace: Unset | bool = UNSET,
    add_played_indicator: Unset | bool = UNSET,
    blur: Unset | int = UNSET,
    background_color: Unset | str = UNSET,
    foreground_layer: Unset | str = UNSET,
    image_index: Unset | int = UNSET,
) -> Response[ProblemDetails]:
    """Get user profile image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        crop_whitespace (Union[Unset, bool]):
        add_played_indicator (Union[Unset, bool]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        image_type=image_type,
        tag=tag,
        format_=format_,
        max_width=max_width,
        max_height=max_height,
        percent_played=percent_played,
        unplayed_count=unplayed_count,
        width=width,
        height=height,
        quality=quality,
        fill_width=fill_width,
        fill_height=fill_height,
        crop_whitespace=crop_whitespace,
        add_played_indicator=add_played_indicator,
        blur=blur,
        background_color=background_color,
        foreground_layer=foreground_layer,
        image_index=image_index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    image_type: ImageType,
    *,
    client: AuthenticatedClient | Client,
    tag: Unset | str = UNSET,
    format_: Unset | ImageFormat = UNSET,
    max_width: Unset | int = UNSET,
    max_height: Unset | int = UNSET,
    percent_played: Unset | float = UNSET,
    unplayed_count: Unset | int = UNSET,
    width: Unset | int = UNSET,
    height: Unset | int = UNSET,
    quality: Unset | int = UNSET,
    fill_width: Unset | int = UNSET,
    fill_height: Unset | int = UNSET,
    crop_whitespace: Unset | bool = UNSET,
    add_played_indicator: Unset | bool = UNSET,
    blur: Unset | int = UNSET,
    background_color: Unset | str = UNSET,
    foreground_layer: Unset | str = UNSET,
    image_index: Unset | int = UNSET,
) -> ProblemDetails | None:
    """Get user profile image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        tag (Union[Unset, str]):
        format_ (Union[Unset, ImageFormat]): Enum ImageOutputFormat.
        max_width (Union[Unset, int]):
        max_height (Union[Unset, int]):
        percent_played (Union[Unset, float]):
        unplayed_count (Union[Unset, int]):
        width (Union[Unset, int]):
        height (Union[Unset, int]):
        quality (Union[Unset, int]):
        fill_width (Union[Unset, int]):
        fill_height (Union[Unset, int]):
        crop_whitespace (Union[Unset, bool]):
        add_played_indicator (Union[Unset, bool]):
        blur (Union[Unset, int]):
        background_color (Union[Unset, str]):
        foreground_layer (Union[Unset, str]):
        image_index (Union[Unset, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            image_type=image_type,
            client=client,
            tag=tag,
            format_=format_,
            max_width=max_width,
            max_height=max_height,
            percent_played=percent_played,
            unplayed_count=unplayed_count,
            width=width,
            height=height,
            quality=quality,
            fill_width=fill_width,
            fill_height=fill_height,
            crop_whitespace=crop_whitespace,
            add_played_indicator=add_played_indicator,
            blur=blur,
            background_color=background_color,
            foreground_layer=foreground_layer,
            image_index=image_index,
        )
    ).parsed
