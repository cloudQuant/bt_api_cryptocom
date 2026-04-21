from __future__ import annotations

from bt_api_base.containers.exchanges.exchange_data import ExchangeData


class CryptoComExchangeData(ExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.exchange_name = "CRYPTOCOM"
        self.rest_url = "https://api.crypto.com/exchange/v1"
        self.wss_url = "wss://stream.crypto.com/exchange/v1/market"
        self.acct_wss_url = "wss://stream.crypto.com/exchange/v1/user"
        self.rest_paths = {}
        self.wss_paths = {}
        self.kline_periods = {
            "1m": "1m",
            "3m": "3m",
            "5m": "5m",
            "15m": "15m",
            "30m": "30m",
            "1h": "1h",
            "2h": "2h",
            "4h": "4h",
            "6h": "6h",
            "12h": "12h",
            "1d": "1D",
            "7d": "7D",
            "14d": "14D",
            "1M": "1M",
        }
        self.legal_currency = ["USDT", "USD", "BTC", "ETH", "CRO"]

    def get_symbol(self, symbol: str) -> str:
        return symbol.replace("/", "_").replace("-", "_")

    def get_period(self, key: str) -> str:
        return key

    def get_rest_path(self, key: str, **kwargs) -> str:
        if key not in self.rest_paths or self.rest_paths[key] == "":
            raise ValueError(f"Unknown REST path key: {key}")
        return self.rest_paths[key]


class CryptoComExchangeDataSpot(CryptoComExchangeData):
    def __init__(self) -> None:
        super().__init__()
        self.asset_type = "SPOT"
        self.exchange_name = "CRYPTOCOM___SPOT"
        self.rest_paths = {
            "get_server_time": "GET /public/get-ticker",
            "get_exchange_info": "GET /public/get-instruments",
            "get_tick": "GET /public/get-tickers",
            "get_ticker": "GET /public/get-tickers",
            "get_depth": "GET /public/get-book",
            "get_kline": "GET /public/get-candlestick",
            "get_trade_history": "GET /public/get-trades",
            "get_account": "POST /private/get-account-summary",
            "get_balance": "POST /private/get-account-summary",
            "make_order": "POST /private/create-order",
            "cancel_order": "POST /private/cancel-order",
            "query_order": "POST /private/get-order-detail",
            "get_order": "POST /private/get-order-detail",
            "get_open_orders": "POST /private/get-open-orders",
        }
        self.status_dict = {
            "active": "ACTIVE",
            "suspended": "SUSPENDED",
            "delisted": "DELISTED",
        }
        self.rate_limit_type = "REQUEST_WEIGHT"
        self.interval = "SECOND"
        self.interval_num = 1
        self.limit = 100
        self.rate_limits = [
            {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "SECOND",
                "intervalNum": 1,
                "limit": 100,
            },
            {"rateLimitType": "ORDERS", "interval": "SECOND", "intervalNum": 1, "limit": 15},
            {
                "rateLimitType": "REQUEST_WEIGHT",
                "interval": "MINUTE",
                "intervalNum": 1,
                "limit": 6000,
            },
        ]
        self.server_time = 0.0
        self.local_update_time = 0.0
        self.timezone = "UTC"

    def get_symbol_path(self, symbol: str) -> str:
        return symbol.replace("/", "_")

    def get_instrument_name(self, symbol: str) -> str:
        return symbol.replace("/", "_")

    def get_symbol_from_instrument(self, instrument_name: str) -> str:
        return instrument_name.replace("_", "/")

    def validate_symbol(self, symbol: str) -> bool:
        if not symbol:
            return False
        if "/" in symbol:
            base, quote = symbol.split("/")
            if len(base) < 1 or len(quote) < 1:
                return False
        else:
            if "_" in symbol:
                base, quote = symbol.split("_")
                if len(base) < 1 or len(quote) < 1:
                    return False
        return True

    def get_depth_levels(self, depth: int = 50) -> int:
        return min(max(1, depth), 50)

    def get_kline_period(self, period: str) -> str:
        return self.kline_periods.get(period, period)

    def get_period_from_kline(self, kline_period: str) -> str:
        reverse_map = {v: k for k, v in self.kline_periods.items()}
        return reverse_map.get(kline_period, kline_period)
