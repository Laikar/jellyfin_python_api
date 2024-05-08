from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.listings_provider_info import ListingsProviderInfo
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: ListingsProviderInfo | ListingsProviderInfo,
    pw: Unset | str = UNSET,
    validate_listings: Unset | bool = False,
    validate_login: Unset | bool = False,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    params: dict[str, Any] = {}

    params["pw"] = pw

    params["validateListings"] = validate_listings

    params["validateLogin"] = validate_login

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/LiveTv/ListingProviders",
        "params": params,
    }

    if isinstance(body, ListingsProviderInfo):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/json"
    if isinstance(body, ListingsProviderInfo):
        _json_body = body.to_dict()

        _kwargs["json"] = _json_body
        headers["Content-Type"] = "application/*+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ListingsProviderInfo | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = ListingsProviderInfo.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ListingsProviderInfo]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: ListingsProviderInfo | ListingsProviderInfo,
    pw: Unset | str = UNSET,
    validate_listings: Unset | bool = False,
    validate_login: Unset | bool = False,
) -> Response[Any | ListingsProviderInfo]:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, str]):
        validate_listings (Union[Unset, bool]):  Default: False.
        validate_login (Union[Unset, bool]):  Default: False.
        body (ListingsProviderInfo):
        body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingsProviderInfo]]
    """

    kwargs = _get_kwargs(
        body=body,
        pw=pw,
        validate_listings=validate_listings,
        validate_login=validate_login,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: ListingsProviderInfo | ListingsProviderInfo,
    pw: Unset | str = UNSET,
    validate_listings: Unset | bool = False,
    validate_login: Unset | bool = False,
) -> Any | ListingsProviderInfo | None:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, str]):
        validate_listings (Union[Unset, bool]):  Default: False.
        validate_login (Union[Unset, bool]):  Default: False.
        body (ListingsProviderInfo):
        body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingsProviderInfo]
    """

    return sync_detailed(
        client=client,
        body=body,
        pw=pw,
        validate_listings=validate_listings,
        validate_login=validate_login,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: ListingsProviderInfo | ListingsProviderInfo,
    pw: Unset | str = UNSET,
    validate_listings: Unset | bool = False,
    validate_login: Unset | bool = False,
) -> Response[Any | ListingsProviderInfo]:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, str]):
        validate_listings (Union[Unset, bool]):  Default: False.
        validate_login (Union[Unset, bool]):  Default: False.
        body (ListingsProviderInfo):
        body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ListingsProviderInfo]]
    """

    kwargs = _get_kwargs(
        body=body,
        pw=pw,
        validate_listings=validate_listings,
        validate_login=validate_login,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: ListingsProviderInfo | ListingsProviderInfo,
    pw: Unset | str = UNSET,
    validate_listings: Unset | bool = False,
    validate_login: Unset | bool = False,
) -> Any | ListingsProviderInfo | None:
    """Adds a listings provider.

    Args:
        pw (Union[Unset, str]):
        validate_listings (Union[Unset, bool]):  Default: False.
        validate_login (Union[Unset, bool]):  Default: False.
        body (ListingsProviderInfo):
        body (ListingsProviderInfo):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ListingsProviderInfo]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            pw=pw,
            validate_listings=validate_listings,
            validate_login=validate_login,
        )
    ).parsed
