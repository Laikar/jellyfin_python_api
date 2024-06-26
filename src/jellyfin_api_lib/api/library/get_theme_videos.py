from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...models.theme_media_result import ThemeMediaResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    user_id: Unset | str = UNSET,
    inherit_from_parent: Unset | bool = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["userId"] = user_id

    params["inheritFromParent"] = inherit_from_parent

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Items/{item_id}/ThemeVideos",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | ThemeMediaResult | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = ThemeMediaResult.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProblemDetails | ThemeMediaResult]:
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
    user_id: Unset | str = UNSET,
    inherit_from_parent: Unset | bool = False,
) -> Response[Any | ProblemDetails | ThemeMediaResult]:
    """Get theme videos for an item.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        inherit_from_parent (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, ThemeMediaResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        user_id=user_id,
        inherit_from_parent=inherit_from_parent,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    inherit_from_parent: Unset | bool = False,
) -> Any | ProblemDetails | ThemeMediaResult | None:
    """Get theme videos for an item.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        inherit_from_parent (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, ThemeMediaResult]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        user_id=user_id,
        inherit_from_parent=inherit_from_parent,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    inherit_from_parent: Unset | bool = False,
) -> Response[Any | ProblemDetails | ThemeMediaResult]:
    """Get theme videos for an item.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        inherit_from_parent (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, ThemeMediaResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        user_id=user_id,
        inherit_from_parent=inherit_from_parent,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    user_id: Unset | str = UNSET,
    inherit_from_parent: Unset | bool = False,
) -> Any | ProblemDetails | ThemeMediaResult | None:
    """Get theme videos for an item.

    Args:
        item_id (str):
        user_id (Union[Unset, str]):
        inherit_from_parent (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, ThemeMediaResult]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            user_id=user_id,
            inherit_from_parent=inherit_from_parent,
        )
    ).parsed
