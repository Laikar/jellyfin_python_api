from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.image_type import ImageType
from ...models.item_fields import ItemFields
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    series_id: str,
    *,
    user_id: Unset | str = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
    is_special_season: Unset | bool = UNSET,
    is_missing: Unset | bool = UNSET,
    adjacent_to: Unset | str = UNSET,
    enable_images: Unset | bool = UNSET,
    image_type_limit: Unset | int = UNSET,
    enable_image_types: Unset | list[ImageType] = UNSET,
    enable_user_data: Unset | bool = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userId"] = user_id

    json_fields: Unset | list[str] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params["isSpecialSeason"] = is_special_season

    params["isMissing"] = is_missing

    params["adjacentTo"] = adjacent_to

    params["enableImages"] = enable_images

    params["imageTypeLimit"] = image_type_limit

    json_enable_image_types: Unset | list[str] = UNSET
    if not isinstance(enable_image_types, Unset):
        json_enable_image_types = []
        for enable_image_types_item_data in enable_image_types:
            enable_image_types_item = enable_image_types_item_data.value
            json_enable_image_types.append(enable_image_types_item)

    params["enableImageTypes"] = json_enable_image_types

    params["enableUserData"] = enable_user_data

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Shows/{series_id}/Seasons",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | BaseItemDtoQueryResult | ProblemDetails | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | BaseItemDtoQueryResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
    is_special_season: Unset | bool = UNSET,
    is_missing: Unset | bool = UNSET,
    adjacent_to: Unset | str = UNSET,
    enable_images: Unset | bool = UNSET,
    image_type_limit: Unset | int = UNSET,
    enable_image_types: Unset | list[ImageType] = UNSET,
    enable_user_data: Unset | bool = UNSET,
) -> Response[Any | BaseItemDtoQueryResult | ProblemDetails]:
    """Gets seasons for a tv series.

    Args:
        series_id (str):
        user_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        is_special_season (Union[Unset, bool]):
        is_missing (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        user_id=user_id,
        fields=fields,
        is_special_season=is_special_season,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
    is_special_season: Unset | bool = UNSET,
    is_missing: Unset | bool = UNSET,
    adjacent_to: Unset | str = UNSET,
    enable_images: Unset | bool = UNSET,
    image_type_limit: Unset | int = UNSET,
    enable_image_types: Unset | list[ImageType] = UNSET,
    enable_user_data: Unset | bool = UNSET,
) -> Any | BaseItemDtoQueryResult | ProblemDetails | None:
    """Gets seasons for a tv series.

    Args:
        series_id (str):
        user_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        is_special_season (Union[Unset, bool]):
        is_missing (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult, ProblemDetails]
    """

    return sync_detailed(
        series_id=series_id,
        client=client,
        user_id=user_id,
        fields=fields,
        is_special_season=is_special_season,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
    ).parsed


async def asyncio_detailed(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
    is_special_season: Unset | bool = UNSET,
    is_missing: Unset | bool = UNSET,
    adjacent_to: Unset | str = UNSET,
    enable_images: Unset | bool = UNSET,
    image_type_limit: Unset | int = UNSET,
    enable_image_types: Unset | list[ImageType] = UNSET,
    enable_user_data: Unset | bool = UNSET,
) -> Response[Any | BaseItemDtoQueryResult | ProblemDetails]:
    """Gets seasons for a tv series.

    Args:
        series_id (str):
        user_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        is_special_season (Union[Unset, bool]):
        is_missing (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        series_id=series_id,
        user_id=user_id,
        fields=fields,
        is_special_season=is_special_season,
        is_missing=is_missing,
        adjacent_to=adjacent_to,
        enable_images=enable_images,
        image_type_limit=image_type_limit,
        enable_image_types=enable_image_types,
        enable_user_data=enable_user_data,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    series_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
    is_special_season: Unset | bool = UNSET,
    is_missing: Unset | bool = UNSET,
    adjacent_to: Unset | str = UNSET,
    enable_images: Unset | bool = UNSET,
    image_type_limit: Unset | int = UNSET,
    enable_image_types: Unset | list[ImageType] = UNSET,
    enable_user_data: Unset | bool = UNSET,
) -> Any | BaseItemDtoQueryResult | ProblemDetails | None:
    """Gets seasons for a tv series.

    Args:
        series_id (str):
        user_id (Union[Unset, str]):
        fields (Union[Unset, List[ItemFields]]):
        is_special_season (Union[Unset, bool]):
        is_missing (Union[Unset, bool]):
        adjacent_to (Union[Unset, str]):
        enable_images (Union[Unset, bool]):
        image_type_limit (Union[Unset, int]):
        enable_image_types (Union[Unset, List[ImageType]]):
        enable_user_data (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            series_id=series_id,
            client=client,
            user_id=user_id,
            fields=fields,
            is_special_season=is_special_season,
            is_missing=is_missing,
            adjacent_to=adjacent_to,
            enable_images=enable_images,
            image_type_limit=image_type_limit,
            enable_image_types=enable_image_types,
            enable_user_data=enable_user_data,
        )
    ).parsed
