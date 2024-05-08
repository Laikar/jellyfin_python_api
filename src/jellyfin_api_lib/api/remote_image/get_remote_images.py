from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...models.remote_image_result import RemoteImageResult
from ...types import UNSET, Response, Unset


def _get_kwargs(
    item_id: str,
    *,
    type: Unset | ImageType = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    provider_name: Unset | str = UNSET,
    include_all_languages: Unset | bool = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_type: Unset | str = UNSET
    if not isinstance(type, Unset):
        json_type = type.value

    params["type"] = json_type

    params["startIndex"] = start_index

    params["limit"] = limit

    params["providerName"] = provider_name

    params["includeAllLanguages"] = include_all_languages

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/Items/{item_id}/RemoteImages",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | RemoteImageResult | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = RemoteImageResult.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProblemDetails | RemoteImageResult]:
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
    type: Unset | ImageType = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    provider_name: Unset | str = UNSET,
    include_all_languages: Unset | bool = False,
) -> Response[Any | ProblemDetails | RemoteImageResult]:
    """Gets available remote images for an item.

    Args:
        item_id (str):
        type (Union[Unset, ImageType]): Enum ImageType.
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        provider_name (Union[Unset, str]):
        include_all_languages (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, RemoteImageResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        type=type,
        start_index=start_index,
        limit=limit,
        provider_name=provider_name,
        include_all_languages=include_all_languages,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    item_id: str,
    *,
    client: AuthenticatedClient,
    type: Unset | ImageType = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    provider_name: Unset | str = UNSET,
    include_all_languages: Unset | bool = False,
) -> Any | ProblemDetails | RemoteImageResult | None:
    """Gets available remote images for an item.

    Args:
        item_id (str):
        type (Union[Unset, ImageType]): Enum ImageType.
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        provider_name (Union[Unset, str]):
        include_all_languages (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, RemoteImageResult]
    """

    return sync_detailed(
        item_id=item_id,
        client=client,
        type=type,
        start_index=start_index,
        limit=limit,
        provider_name=provider_name,
        include_all_languages=include_all_languages,
    ).parsed


async def asyncio_detailed(
    item_id: str,
    *,
    client: AuthenticatedClient,
    type: Unset | ImageType = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    provider_name: Unset | str = UNSET,
    include_all_languages: Unset | bool = False,
) -> Response[Any | ProblemDetails | RemoteImageResult]:
    """Gets available remote images for an item.

    Args:
        item_id (str):
        type (Union[Unset, ImageType]): Enum ImageType.
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        provider_name (Union[Unset, str]):
        include_all_languages (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails, RemoteImageResult]]
    """

    kwargs = _get_kwargs(
        item_id=item_id,
        type=type,
        start_index=start_index,
        limit=limit,
        provider_name=provider_name,
        include_all_languages=include_all_languages,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    item_id: str,
    *,
    client: AuthenticatedClient,
    type: Unset | ImageType = UNSET,
    start_index: Unset | int = UNSET,
    limit: Unset | int = UNSET,
    provider_name: Unset | str = UNSET,
    include_all_languages: Unset | bool = False,
) -> Any | ProblemDetails | RemoteImageResult | None:
    """Gets available remote images for an item.

    Args:
        item_id (str):
        type (Union[Unset, ImageType]): Enum ImageType.
        start_index (Union[Unset, int]):
        limit (Union[Unset, int]):
        provider_name (Union[Unset, str]):
        include_all_languages (Union[Unset, bool]):  Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails, RemoteImageResult]
    """

    return (
        await asyncio_detailed(
            item_id=item_id,
            client=client,
            type=type,
            start_index=start_index,
            limit=limit,
            provider_name=provider_name,
            include_all_languages=include_all_languages,
        )
    ).parsed
