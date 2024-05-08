from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_dto_query_result import BaseItemDtoQueryResult
from ...models.item_fields import ItemFields
from ...models.item_filter import ItemFilter
from ...models.sort_order import SortOrder
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    folder_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    sort_order: Unset | list[SortOrder] = UNSET,
    filters: Unset | list[ItemFilter] = UNSET,
    sort_by: Unset | list[str] = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["folderId"] = folder_id

    params["userId"] = user_id

    params["startIndex"] = start_index

    params["limit"] = limit

    json_sort_order: Unset | list[str] = UNSET
    if not isinstance(sort_order, Unset):
        json_sort_order = []
        for sort_order_item_data in sort_order:
            sort_order_item = sort_order_item_data.value
            json_sort_order.append(sort_order_item)

    params["sortOrder"] = json_sort_order

    json_filters: Unset | list[str] = UNSET
    if not isinstance(filters, Unset):
        json_filters = []
        for filters_item_data in filters:
            filters_item = filters_item_data.value
            json_filters.append(filters_item)

    params["filters"] = json_filters

    json_sort_by: Unset | list[str] = UNSET
    if not isinstance(sort_by, Unset):
        json_sort_by = sort_by

    params["sortBy"] = json_sort_by

    json_fields: Unset | list[str] = UNSET
    if not isinstance(fields, Unset):
        json_fields = []
        for fields_item_data in fields:
            fields_item = fields_item_data.value
            json_fields.append(fields_item)

    params["fields"] = json_fields

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Channels/{channel_id}/Items",
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
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    sort_order: Unset | list[SortOrder] = UNSET,
    filters: Unset | list[ItemFilter] = UNSET,
    sort_by: Unset | list[str] = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, List[SortOrder]]):
        filters (Union[Unset, List[ItemFilter]]):
        sort_by (Union[Unset, List[str]]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    sort_order: Unset | list[SortOrder] = UNSET,
    filters: Unset | list[ItemFilter] = UNSET,
    sort_by: Unset | list[str] = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, List[SortOrder]]):
        filters (Union[Unset, List[ItemFilter]]):
        sort_by (Union[Unset, List[str]]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    sort_order: Unset | list[SortOrder] = UNSET,
    filters: Unset | list[ItemFilter] = UNSET,
    sort_by: Unset | list[str] = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
) -> Response[Any | BaseItemDtoQueryResult]:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, List[SortOrder]]):
        filters (Union[Unset, List[ItemFilter]]):
        sort_by (Union[Unset, List[str]]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, BaseItemDtoQueryResult]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        folder_id=folder_id,
        user_id=user_id,
        start_index=start_index,
        limit=limit,
        sort_order=sort_order,
        filters=filters,
        sort_by=sort_by,
        fields=fields,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: str,
    *,
    client: AuthenticatedClient,
    folder_id: Unset | str = UNSET,
    user_id: Unset | str = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    sort_order: Unset | list[SortOrder] = UNSET,
    filters: Unset | list[ItemFilter] = UNSET,
    sort_by: Unset | list[str] = UNSET,
    fields: Unset | list[ItemFields] = UNSET,
) -> Any | BaseItemDtoQueryResult | None:
    """Get channel items.

    Args:
        channel_id (str):
        folder_id (Union[Unset, str]):
        user_id (Union[Unset, str]):
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        sort_order (Union[Unset, List[SortOrder]]):
        filters (Union[Unset, List[ItemFilter]]):
        sort_by (Union[Unset, List[str]]):
        fields (Union[Unset, List[ItemFields]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, BaseItemDtoQueryResult]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            folder_id=folder_id,
            user_id=user_id,
            start_index=start_index,
            limit=limit,
            sort_order=sort_order,
            filters=filters,
            sort_by=sort_by,
            fields=fields,
        )
    ).parsed
