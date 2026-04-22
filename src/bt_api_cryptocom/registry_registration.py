from __future__ import annotations

from typing import Any

from bt_api_base.balance_utils import (
    nested_balance_handler as _cryptocom_balance_handler,
)
from bt_api_base.registry import ExchangeRegistry

from bt_api_cryptocom.exchange_data import CryptoComExchangeDataSpot
from bt_api_cryptocom.feeds.live_cryptocom.spot import CryptoComRequestDataSpot


def _cryptocom_spot_subscribe_handler(
    data_queue: Any, exchange_params: Any, topics: Any, bt_api: Any
) -> None:
    topic_list = [i["topic"] for i in topics]
    bt_api.log(f"Crypto.com Spot topics requested: {topic_list}")


def register_cryptocom(registry: type[ExchangeRegistry]) -> None:
    registry.register_feed("CRYPTOCOM___SPOT", CryptoComRequestDataSpot)
    registry.register_exchange_data("CRYPTOCOM___SPOT", CryptoComExchangeDataSpot)
    registry.register_balance_handler("CRYPTOCOM___SPOT", _cryptocom_balance_handler)
    registry.register_stream("CRYPTOCOM___SPOT", "subscribe", _cryptocom_spot_subscribe_handler)
