from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.remote_search_result import RemoteSearchResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    body: RemoteSearchResult | RemoteSearchResult,
    replace_all_images: Unset | bool = True,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["replaceAllImages"] = replace_all_images

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/Items/RemoteSearch/Apply/{item_id}",
        "params": params,
    }

    if isinstance(body, RemoteSearchResult):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, RemoteSearchResult):
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
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: RemoteSearchResult | RemoteSearchResult,
    replace_all_images: Unset | bool = True,
) -> Response[Any]:
    """Applies search criteria to an item and refreshes metadata.

    Args:
        item_id (str):
        replace_all_images (Union[Unset, bool]):  Default: True.
        body (RemoteSearchResult):
        body (RemoteSearchResult):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        replace_all_images=replace_all_images,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    body: RemoteSearchResult | RemoteSearchResult,
    replace_all_images: Unset | bool = True,
) -> Response[Any]:
    """Applies search criteria to an item and refreshes metadata.

    Args:
        item_id (str):
        replace_all_images (Union[Unset, bool]):  Default: True.
        body (RemoteSearchResult):
        body (RemoteSearchResult):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        body=body,
        replace_all_images=replace_all_images,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
