import datetime
from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.activity_log_entry_query_result import ActivityLogEntryQueryResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    min_date: Unset | datetime.datetime = UNSET,
    has_user_id: Unset | bool = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["startIndex"] = start_index

    params["limit"] = limit

    json_min_date: Unset | str = UNSET
    if not isinstance(min_date, Unset):
        json_min_date = min_date.isoformat()
    params["minDate"] = json_min_date

    params["hasUserId"] = has_user_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/System/ActivityLog/Entries",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ActivityLogEntryQueryResult | Any | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = ActivityLogEntryQueryResult.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ActivityLogEntryQueryResult | Any]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    min_date: Unset | datetime.datetime = UNSET,
    has_user_id: Unset | bool = UNSET,
) -> Response[ActivityLogEntryQueryResult | Any]:
    """Gets activity log entries.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        min_date (Union[Unset, datetime.datetime]):
        has_user_id (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityLogEntryQueryResult, Any]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        min_date=min_date,
        has_user_id=has_user_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    min_date: Unset | datetime.datetime = UNSET,
    has_user_id: Unset | bool = UNSET,
) -> ActivityLogEntryQueryResult | Any | None:
    """Gets activity log entries.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        min_date (Union[Unset, datetime.datetime]):
        has_user_id (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityLogEntryQueryResult, Any]
    """

    return sync_detailed(
        client=client,
        start_index=start_index,
        limit=limit,
        min_date=min_date,
        has_user_id=has_user_id,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    min_date: Unset | datetime.datetime = UNSET,
    has_user_id: Unset | bool = UNSET,
) -> Response[ActivityLogEntryQueryResult | Any]:
    """Gets activity log entries.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        min_date (Union[Unset, datetime.datetime]):
        has_user_id (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ActivityLogEntryQueryResult, Any]]
    """

    kwargs = _get_kwargs(
        start_index=start_index,
        limit=limit,
        min_date=min_date,
        has_user_id=has_user_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    min_date: Unset | datetime.datetime = UNSET,
    has_user_id: Unset | bool = UNSET,
) -> ActivityLogEntryQueryResult | Any | None:
    """Gets activity log entries.

    Args:
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        min_date (Union[Unset, datetime.datetime]):
        has_user_id (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ActivityLogEntryQueryResult, Any]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_index=start_index,
            limit=limit,
            min_date=min_date,
            has_user_id=has_user_id,
        )
    ).parsed
