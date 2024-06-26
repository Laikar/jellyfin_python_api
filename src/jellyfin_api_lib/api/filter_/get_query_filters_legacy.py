from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.base_item_kind import BaseItemKind
from ...models.query_filters_legacy import QueryFiltersLegacy
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    user_id: Unset | str = UNSET,
    parent_id: Unset | str = UNSET,
    include_item_types: Unset | list[BaseItemKind] = UNSET,
    media_types: Unset | list[str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userId"] = user_id

    params["parentId"] = parent_id

    json_include_item_types: Unset | list[str] = UNSET
    if not isinstance(include_item_types, Unset):
        json_include_item_types = []
        for include_item_types_item_data in include_item_types:
            include_item_types_item = include_item_types_item_data.value
            json_include_item_types.append(include_item_types_item)

    params["includeItemTypes"] = json_include_item_types

    json_media_types: Unset | list[str] = UNSET
    if not isinstance(media_types, Unset):
        json_media_types = media_types

    params["mediaTypes"] = json_media_types

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/Items/Filters",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | QueryFiltersLegacy | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = QueryFiltersLegacy.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | QueryFiltersLegacy]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    parent_id: Unset | str = UNSET,
    include_item_types: Unset | list[BaseItemKind] = UNSET,
    media_types: Unset | list[str] = UNSET,
) -> Response[Any | QueryFiltersLegacy]:
    """Gets legacy query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        media_types (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueryFiltersLegacy]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        media_types=media_types,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    parent_id: Unset | str = UNSET,
    include_item_types: Unset | list[BaseItemKind] = UNSET,
    media_types: Unset | list[str] = UNSET,
) -> Any | QueryFiltersLegacy | None:
    """Gets legacy query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        media_types (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueryFiltersLegacy]
    """

    return sync_detailed(
        client=client,
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        media_types=media_types,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    parent_id: Unset | str = UNSET,
    include_item_types: Unset | list[BaseItemKind] = UNSET,
    media_types: Unset | list[str] = UNSET,
) -> Response[Any | QueryFiltersLegacy]:
    """Gets legacy query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        media_types (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, QueryFiltersLegacy]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        parent_id=parent_id,
        include_item_types=include_item_types,
        media_types=media_types,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    parent_id: Unset | str = UNSET,
    include_item_types: Unset | list[BaseItemKind] = UNSET,
    media_types: Unset | list[str] = UNSET,
) -> Any | QueryFiltersLegacy | None:
    """Gets legacy query filters.

    Args:
        user_id (Union[Unset, str]):
        parent_id (Union[Unset, str]):
        include_item_types (Union[Unset, List[BaseItemKind]]):
        media_types (Union[Unset, List[str]]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, QueryFiltersLegacy]
    """

    return (
        await asyncio_detailed(
            client=client,
            user_id=user_id,
            parent_id=parent_id,
            include_item_types=include_item_types,
            media_types=media_types,
        )
    ).parsed
