from unittest.mock import AsyncMock, MagicMock
import pytest
from bt_api_base.containers.requestdatas.request_data import RequestData
from bt_api_cryptocom.feeds.live_cryptocom.request_base import CryptoComRequestData


def test_cryptocom_request_allows_missing_extra_data(monkeypatch) -> None:
    request_data = CryptoComRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="CRYPTOCOM___SPOT",
    )

    monkeypatch.setattr(
        request_data,
        "http_request",
        lambda method, url, headers, body, timeout: {"code": 0, "result": {}},
    )

    result = request_data.request("GET /public/get-time", is_sign=False)

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == {"code": 0, "result": {}}


def test_cryptocom_disconnect_closes_http_client() -> None:
    request_data = CryptoComRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="CRYPTOCOM___SPOT",
    )
    request_data._http_client.close = MagicMock()

    request_data.disconnect()

    request_data._http_client.close.assert_called_once_with()


async def test_cryptocom_async_request_uses_initialized_http_client(monkeypatch) -> None:
    request_data = CryptoComRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="CRYPTOCOM___SPOT",
    )

    async_request_mock = AsyncMock(return_value={"code": 0, "result": {"server_time": 1}})
    monkeypatch.setattr(request_data._http_client, "async_request", async_request_mock)

    result = await request_data.async_request("GET /public/get-time", is_sign=False)

    assert isinstance(result, RequestData)
    assert result.get_extra_data() == {}
    assert result.get_input_data() == {"code": 0, "result": {"server_time": 1}}
    async_request_mock.assert_awaited_once_with(
        method="GET",
        url=f"{request_data._params.rest_url}/public/get-time",
        headers={"Content-Type": "application/json"},
        json_data=None,
        timeout=10,
    )


async def test_cryptocom_async_request_passes_signed_payload_via_json_data(monkeypatch) -> None:
    request_data = CryptoComRequestData(
        public_key="public-key",
        private_key="secret-key",
        exchange_name="CRYPTOCOM___SPOT",
    )

    monkeypatch.setattr(request_data, "sign", lambda api_method, params, req_id, nonce: "signed")
    async_request_mock = AsyncMock(return_value={"code": 0, "result": {}})
    monkeypatch.setattr(request_data._http_client, "async_request", async_request_mock)

    await request_data.async_request(
        "GET /private/get-account-summary",
        params={"instrument_name": "BTC_USDT"},
        timeout=7,
        is_sign=True,
    )

    awaited_kwargs = async_request_mock.await_args.kwargs
    assert awaited_kwargs["method"] == "POST"
    assert awaited_kwargs["url"] == f"{request_data._params.rest_url}/private/get-account-summary"
    assert awaited_kwargs["headers"] == {"Content-Type": "application/json"}
    assert awaited_kwargs["timeout"] == 7
    assert awaited_kwargs["json_data"]["method"] == "private/get-account-summary"
    assert awaited_kwargs["json_data"]["api_key"] == "public-key"
    assert awaited_kwargs["json_data"]["params"] == {"instrument_name": "BTC_USDT"}
    assert awaited_kwargs["json_data"]["sig"] == "signed"
