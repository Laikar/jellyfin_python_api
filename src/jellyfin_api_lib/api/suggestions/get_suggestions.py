from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.base_item_kind import BaseItemKind
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    media_type: Unset | list[str] = UNSET,
    type: Unset | list[BaseItemKind] = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    enable_total_record_count: Unset | bool = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_media_type: Unset | list[str] = UNSET
    if not isinstance(media_type, Unset):
        json_media_type = media_type

    params["mediaType"] = json_media_type

    json_type: Unset | list[str] = UNSET
    if not isinstance(type, Unset):
        json_type = []
        for type_item_data in type:
            type_item = type_item_data.value
            json_type.append(type_item)

    params["type"] = json_type

    params["startIndex"] = start_index

    params["limit"] = limit

    params["enableTotalRecordCount"] = enable_total_record_count

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Users/{user_id}/Suggestions",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | BaseItemDtoQueryResult | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = BaseItemDtoQueryResult.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | BaseItemDtoQueryResult]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Unset | list[str] = UNSET,
    type: Unset | list[BaseItemKind] = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    enable_total_record_count: Unset | bool = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, List[str]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Unset | list[str] = UNSET,
    type: Unset | list[BaseItemKind] = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    enable_total_record_count: Unset | bool = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, List[str]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Unset | list[str] = UNSET,
    type: Unset | list[BaseItemKind] = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    enable_total_record_count: Unset | bool = False,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, List[str]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        media_type=media_type,
        type=type,
        start_index=start_index,
        limit=limit,
        enable_total_record_count=enable_total_record_count,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient,
    media_type: Unset | list[str] = UNSET,
    type: Unset | list[BaseItemKind] = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    enable_total_record_count: Unset | bool = False,
) -> Any | BaseItemDtoQueryResult | None:
    """Gets suggestions.

    Args:
        user_id (str):
        media_type (Union[Unset, List[str]]):
        type (Union[Unset, List[BaseItemKind]]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        enable_total_record_count (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            media_type=media_type,
            type=type,
            start_index=start_index,
            limit=limit,
            enable_total_record_count=enable_total_record_count,
        )
    ).parsed
