"""Module-level docstring."""
from __future__ import annotations

import json
import time
from typing import Any

from bt_api_base.containers.orders.order import OrderData


class CryptoComOrder(OrderData):
    """Class CryptoComOrder"""
    def __init__(
        self,
        order_info: Any,
        symbol_name: str,
        asset_type: str = "SPOT",
        has_been_json_encoded: bool = False,
    ):
        """__init__ method"""
        super().__init__(order_info, has_been_json_encoded)
        self.exchange_name = "CRYPTOCOM"
        self.local_update_time = time.time()
        self.symbol_name = symbol_name
        self.asset_type = asset_type
        self.order_data: dict[str, Any] | None = (
            order_info if has_been_json_encoded else None
        )
        self.order_id: str | None = None
        self.client_oid: str | None = None
        self.side: str | None = None
        self.type: str | None = None
        self.quantity: float | None = None
        self.price: float | None = None
        self.status: str | None = None
        self.filled_quantity: float | None = None
        self.remaining_quantity: float | None = None
        self.all_data: dict[str, Any] | None = None
        self.has_been_init_data = False

    def init_data(self) -> CryptoComOrder:
        """init_data method"""
        if not self.has_been_json_encoded:
            self.order_data = (
                json.loads(self.order_info)
                if isinstance(self.order_info, str)
                else self.order_info
            )
            self.has_been_json_encoded = True
        if self.has_been_init_data:
            return self

        assert self.order_data is not None
        self.order_id = self.order_data.get("order_id")
        self.client_oid = self.order_data.get("client_oid")
        self.side = self.order_data.get("side")
        self.type = self.order_data.get("type")
        self.quantity = float(self.order_data.get("quantity", 0))
        self.price = float(self.order_data.get("price", 0))
        self.status = self.order_data.get("status")
        self.filled_quantity = float(self.order_data.get("filled_quantity", 0))
        self.remaining_quantity = float(self.order_data.get("remaining_quantity", 0))
        self.has_been_init_data = True
        return self

    def get_all_data(self) -> dict[str, Any]:
        """get_all_data method"""
        if self.all_data is None:
            self.all_data = {
                "exchange_name": self.exchange_name,
                "symbol_name": self.symbol_name,
                "asset_type": self.asset_type,
                "local_update_time": self.local_update_time,
                "order_id": self.order_id,
                "client_oid": self.client_oid,
                "side": self.side,
                "type": self.type,
                "quantity": self.quantity,
                "price": self.price,
                "status": self.status,
                "filled_quantity": self.filled_quantity,
                "remaining_quantity": self.remaining_quantity,
            }
        return self.all_data

    def __str__(self) -> str:
        return json.dumps(self.get_all_data())

    def __repr__(self) -> str:
        return self.__str__()

    def get_event(self) -> str:
        """get_event method"""
        return "OrderEvent"

    def get_exchange_name(self) -> str:
        """get_exchange_name method"""
        return self.exchange_name

    def get_local_update_time(self) -> float:
        """get_local_update_time method"""
        return self.local_update_time

    def get_symbol_name(self) -> str:
        """get_symbol_name method"""
        return self.symbol_name

    def get_asset_type(self) -> str:
        """get_asset_type method"""
        return self.asset_type

    def get_server_time(self) -> None:
        """get_server_time method"""
        return None

    def get_order_id(self) -> str | None:
        """get_order_id method"""
        return self.order_id

    def get_client_order_id(self) -> str | None:
        """get_client_order_id method"""
        return self.client_oid

    def get_cum_quote(self) -> None:
        """get_cum_quote method"""
        return None

    def get_executed_qty(self) -> float | None:
        """get_executed_qty method"""
        return self.filled_quantity

    def get_order_size(self) -> float | None:
        """get_order_size method"""
        return self.quantity

    def get_order_price(self) -> float | None:
        """get_order_price method"""
        return self.price

    def get_reduce_only(self) -> None:
        """get_reduce_only method"""
        return None

    def get_order_side(self) -> str | None:
        """get_order_side method"""
        return self.side

    def get_order_status(self) -> str | None:
        """get_order_status method"""
        return self.status

    def get_order_symbol_name(self) -> str:
        """get_order_symbol_name method"""
        return self.symbol_name

    def get_order_time_in_force(self) -> None:
        """get_order_time_in_force method"""
        return None

    def get_order_type(self) -> str | None:
        """get_order_type method"""
        return self.type

    def get_order_avg_price(self) -> float | None:
        """get_order_avg_price method"""
        if self.filled_quantity and self.filled_quantity > 0:
            return self.price
        return None

    def get_origin_order_type(self) -> str | None:
        """get_origin_order_type method"""
        return self.type

    def get_position_side(self) -> None:
        """get_position_side method"""
        return None

    def get_trailing_stop_price(self) -> None:
        """get_trailing_stop_price method"""
        return None

    def get_trailing_stop_trigger_price(self) -> None:
        """get_trailing_stop_trigger_price method"""
        return None

    def get_trailing_stop_callback_rate(self) -> None:
        """get_trailing_stop_callback_rate method"""
        return None

    def get_trailing_stop_trigger_price_type(self) -> None:
        """get_trailing_stop_trigger_price_type method"""
        return None

    def get_stop_loss_price(self) -> None:
        """get_stop_loss_price method"""
        return None

    def get_stop_loss_trigger_price(self) -> None:
        """get_stop_loss_trigger_price method"""
        return None

    def get_stop_loss_trigger_price_type(self) -> None:
        """get_stop_loss_trigger_price_type method"""
        return None

    def get_take_profit_price(self) -> None:
        """get_take_profit_price method"""
        return None

    def get_take_profit_trigger_price(self) -> None:
        """get_take_profit_trigger_price method"""
        return None

    def get_take_profit_trigger_price_type(self) -> None:
        """get_take_profit_trigger_price_type method"""
        return None

    def get_close_position(self) -> None:
        """get_close_position method"""
        return None

    def get_order_offset(self) -> None:
        """get_order_offset method"""
        return None

    def get_order_exchange_id(self) -> None:
        """get_order_exchange_id method"""
        return None

    def to_dict(self) -> dict[str, Any]:
        """to_dict method"""
        self.init_data()
        return self.get_all_data()
