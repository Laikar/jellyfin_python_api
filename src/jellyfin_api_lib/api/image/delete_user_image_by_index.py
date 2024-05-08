from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.image_type import ImageType
from ...models.problem_details import ProblemDetails
from ...types import Response


def _get_kwargs(
    user_id: str,
    image_type: ImageType,
    index: int,
) -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "delete",
        "url": f"/Users/{user_id}/Images/{image_type}/{index}",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | ProblemDetails | None:
    if response.status_code == HTTPStatus.NO_CONTENT:
        response_204 = cast(Any, None)
        return response_204
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = cast(Any, None)
        return response_401
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
    user_id: str,
    image_type: ImageType,
    index: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails]:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        image_type=image_type,
        index=index,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    image_type: ImageType,
    index: int,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | None:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return sync_detailed(
        user_id=user_id,
        image_type=image_type,
        index=index,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    image_type: ImageType,
    index: int,
    *,
    client: AuthenticatedClient,
) -> Response[Any | ProblemDetails]:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        image_type=image_type,
        index=index,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    image_type: ImageType,
    index: int,
    *,
    client: AuthenticatedClient,
) -> Any | ProblemDetails | None:
    """Delete the user's image.

    Args:
        user_id (str):
        image_type (ImageType): Enum ImageType.
        index (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            image_type=image_type,
            index=index,
            client=client,
        )
    ).parsed
