from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.authentication_result import AuthenticationResult
from ...models.problem_details import ProblemDetails
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    pw: str,
    password: Unset | str = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["pw"] = pw

    params["password"] = password

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/Users/{user_id}/Authenticate",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> AuthenticationResult | ProblemDetails | None:
    if response.status_code == HTTPStatus.OK:
        response_200 = AuthenticationResult.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = ProblemDetails.from_dict(response.json())

        return response_403
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = ProblemDetails.from_dict(response.json())

        return response_404
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[AuthenticationResult | ProblemDetails]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    pw: str,
    password: Unset | str = UNSET,
) -> Response[AuthenticationResult | ProblemDetails]:
    """Authenticates a user.

    Args:
        user_id (str):
        pw (str):
        password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        pw=pw,
        password=password,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    pw: str,
    password: Unset | str = UNSET,
) -> AuthenticationResult | ProblemDetails | None:
    """Authenticates a user.

    Args:
        user_id (str):
        pw (str):
        password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthenticationResult, ProblemDetails]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        pw=pw,
        password=password,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    pw: str,
    password: Unset | str = UNSET,
) -> Response[AuthenticationResult | ProblemDetails]:
    """Authenticates a user.

    Args:
        user_id (str):
        pw (str):
        password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[AuthenticationResult, ProblemDetails]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        pw=pw,
        password=password,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    user_id: str,
    *,
    client: AuthenticatedClient | Client,
    pw: str,
    password: Unset | str = UNSET,
) -> AuthenticationResult | ProblemDetails | None:
    """Authenticates a user.

    Args:
        user_id (str):
        pw (str):
        password (Union[Unset, str]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[AuthenticationResult, ProblemDetails]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            pw=pw,
            password=password,
        )
    ).parsed
