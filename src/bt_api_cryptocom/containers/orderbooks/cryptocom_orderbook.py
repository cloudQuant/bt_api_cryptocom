from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orderbooks.orderbook import OrderBookData


class CryptoComOrderBook(OrderBookData):
    def __init__(
        self,
        order_book_info: Any,
        symbol_name: str,
        asset_type: str = "SPOT",
        has_been_json_encoded: bool = False,
    ) -> None:
        super().__init__(order_book_info, has_been_json_encoded)
        self.exchange_name = "CRYPTOCOM"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.order_book_data: Any = order_book_info if has_been_json_encoded else None
        self.order_book_symbol_name: str | None = None
        self.server_time: float | None = None
        self.bid_price_list: list[float] | None = None
        self.ask_price_list: list[float] | None = None
        self.bid_volume_list: list[float] | None = None
        self.ask_volume_list: list[float] | None = None
        self.bids: list[list[float | int]] = []
        self.asks: list[list[float | int]] = []
        self.all_data: dict[str, Any] | None = None
        self.has_been_init_data = False

    def init_data(self) -> "CryptoComOrderBook":
        if not self.has_been_json_encoded:
            self.order_book_data = (
                json.loads(self.order_book_info)
                if isinstance(self.order_book_info, str)
                else self.order_book_info
            )
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        data = self.order_book_data or {}
        self.order_book_symbol_name = self.symbol_name
        t_val = data.get("t")
        self.server_time = float(t_val) / 1000 if t_val else None

        if "data" in data and data["data"]:
            book_data = data["data"][0]
            self.asks = []
            for ask in book_data.get("asks", []):
                self.asks.append([float(ask[0]), float(ask[1]), int(ask[2])])
            self.bids = []
            for bid in book_data.get("bids", []):
                self.bids.append([float(bid[0]), float(bid[1]), int(bid[2])])
            self.bid_price_list = [b[0] for b in self.bids]
            self.ask_price_list = [a[0] for a in self.asks]
            self.bid_volume_list = [b[1] for b in self.bids]
            self.ask_volume_list = [a[1] for a in self.asks]

        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        if self.all_data is None:
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "asset_type": self.asset_type,
                "local_update_time": self.local_update_time,
                "order_book_symbol_name": self.order_book_symbol_name,
                "server_time": self.server_time,
                "bid_price_list": self.bid_price_list,
                "ask_price_list": self.ask_price_list,
                "bid_volume_list": self.bid_volume_list,
                "ask_volume_list": self.ask_volume_list,
                "bids": self.bids,
                "asks": self.asks,
            }
        return self.all_data

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_exchange_name(self) -> str:
        return self.exchange_name

    def get_local_update_time(self) -> float:
        return self.local_update_time

    def get_symbol_name(self) -> str:
        return self.symbol_name

    def get_order_book_symbol_name(self) -> str | None:
        return self.order_book_symbol_name

    def get_asset_type(self) -> str:
        return self.asset_type

    def get_server_time(self) -> float | None:
        return self.server_time

    def get_bid_price_list(self) -> list[float] | None:
        return self.bid_price_list

    def get_ask_price_list(self) -> list[float] | None:
        return self.ask_price_list

    def get_bid_volume_list(self) -> list[float] | None:
        return self.bid_volume_list

    def get_ask_volume_list(self) -> list[float] | None:
        return self.ask_volume_list

    def get_bid_trade_nums(self) -> list[int]:
        return [int(b[2]) if len(b) > 2 else 0 for b in self.bids]

    def get_ask_trade_nums(self) -> list[int]:
        return [int(a[2]) if len(a) > 2 else 0 for a in self.asks]

    def get_price_levels(self, side: str, levels: int = 10) -> list[list[float | int]]:
        if side.upper() == "ASK":
            return self.asks[:levels]
        elif side.upper() == "BID":
            return self.bids[:levels]
        return []
