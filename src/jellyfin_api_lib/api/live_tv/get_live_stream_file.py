from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    stream_id: str,
    container: str,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/LiveTv/LiveStreamFiles/{stream_id}/stream.{container}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ProblemDetails | None:
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    stream_id: str,
    container: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails]:
    """Gets a live tv channel stream.

    Args:
        stream_id (str):
        container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        stream_id=stream_id,
        container=container,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    stream_id: str,
    container: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | None:
    """Gets a live tv channel stream.

    Args:
        stream_id (str):
        container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return sync_detailed(
        stream_id=stream_id,
        container=container,
        client=client,
    ).parsed


async def asyncio_detailed(
    stream_id: str,
    container: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ProblemDetails]:
    """Gets a live tv channel stream.

    Args:
        stream_id (str):
        container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ProblemDetails]
    """

    kwargs = _get_kwargs(
        stream_id=stream_id,
        container=container,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    stream_id: str,
    container: str,
    *,
    client: AuthenticatedClient | Client,
) -> ProblemDetails | None:
    """Gets a live tv channel stream.

    Args:
        stream_id (str):
        container (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ProblemDetails
    """

    return (
        await asyncio_detailed(
            stream_id=stream_id,
            container=container,
            client=client,
        )
    ).parsed
