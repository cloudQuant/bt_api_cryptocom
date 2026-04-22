# CRYPTOCOM Documentation

## English

Welcome to the CRYPTOCOM documentation for bt_api.

### Quick Start

```bash
pip install bt_api_cryptocom
```

```python
from bt_api import BtApi

api = BtApi(exchange_kwargs={
    "CRYPTOCOM___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("CRYPTOCOM___SPOT", "BTCUSDT")
print(ticker)
```

### Supported Operations

| Operation | Exchange Code | Description |
|-----------|---------------|-------------|
| Ticker | `CRYPTOCOM___SPOT` | Get ticker data |
| OrderBook | `CRYPTOCOM___SPOT` | Get order book depth |
| Klines | `CRYPTOCOM___SPOT` | Get candlestick data |
| Trade History | `CRYPTOCOM___SPOT` | Get recent trades |
| Order | `CRYPTOCOM___SPOT` | Place/cancel orders |
| Account | `CRYPTOCOM___SPOT` | Get account info |
| Balance | `CRYPTOCOM___SPOT` | Get balance info |

## 中文

欢迎使用 bt_api 的 CRYPTOCOM 文档。

### 快速开始

```bash
pip install bt_api_cryptocom
```

```python
from bt_api import BtApi

api = BtApi(exchange_kwargs={
    "CRYPTOCOM___SPOT": {
        "api_key": "your_api_key",
        "secret": "your_secret",
    }
})

ticker = api.get_tick("CRYPTOCOM___SPOT", "BTCUSDT")
print(ticker)
```

### 支持的操作

| 操作 | 交易所代码 | 说明 |
|------|------------|------|
| Ticker | `CRYPTOCOM___SPOT` | 获取行情数据 |
| OrderBook | `CRYPTOCOM___SPOT` | 获取订单簿深度 |
| Klines | `CRYPTOCOM___SPOT` | 获取K线数据 |
| Trade History | `CRYPTOCOM___SPOT` | 获取成交历史 |
| Order | `CRYPTOCOM___SPOT` | 下单/撤单 |
| Account | `CRYPTOCOM___SPOT` | 获取账户信息 |
| Balance | `CRYPTOCOM___SPOT` | 获取余额信息 |

## API Reference

See source code in `src/bt_api_cryptocom/` for detailed API documentation.
