from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    name: str,
    *,
    assembly_guid: Unset | str = UNSET,
    version: Unset | str = UNSET,
    repository_url: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["assemblyGuid"] = assembly_guid

    params["version"] = version

    params["repositoryUrl"] = repository_url

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/Packages/Installed/{name}",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | None:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Unset | str = UNSET,
    version: Unset | str = UNSET,
    repository_url: Unset | str = UNSET,
) -> Response[Any | ProblemDetails]:
    """Installs a package.

    Args:
        name (str):
        assembly_guid (Union[Unset, str]):
        version (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        name=name,
        assembly_guid=assembly_guid,
        version=version,
        repository_url=repository_url,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Unset | str = UNSET,
    version: Unset | str = UNSET,
    repository_url: Unset | str = UNSET,
) -> Any | ProblemDetails | None:
    """Installs a package.

    Args:
        name (str):
        assembly_guid (Union[Unset, str]):
        version (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        name=name,
        client=client,
        assembly_guid=assembly_guid,
        version=version,
        repository_url=repository_url,
    ).parsed


async def asyncio_detailed(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Unset | str = UNSET,
    version: Unset | str = UNSET,
    repository_url: Unset | str = UNSET,
) -> Response[Any | ProblemDetails]:
    """Installs a package.

    Args:
        name (str):
        assembly_guid (Union[Unset, str]):
        version (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        name=name,
        assembly_guid=assembly_guid,
        version=version,
        repository_url=repository_url,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    name: str,
    *,
    client: AuthenticatedClient,
    assembly_guid: Unset | str = UNSET,
    version: Unset | str = UNSET,
    repository_url: Unset | str = UNSET,
) -> Any | ProblemDetails | None:
    """Installs a package.

    Args:
        name (str):
        assembly_guid (Union[Unset, str]):
        version (Union[Unset, str]):
        repository_url (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            name=name,
            client=client,
            assembly_guid=assembly_guid,
            version=version,
            repository_url=repository_url,
        )
    ).parsed
