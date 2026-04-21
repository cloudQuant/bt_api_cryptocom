# bt_api_cryptocom

Crypto.com exchange plugin for `bt_api`, supporting Spot trading.

## Installation

```bash
pip install bt_api_cryptocom
```

## Usage

```python
from bt_api_cryptocom import CryptoComRequestDataSpot

feed = CryptoComRequestDataSpot(public_key="your_key", private_key="your_secret")
ticker = feed.get_ticker("BTCUSDT")
```

## Architecture

```
bt_api_cryptocom/
├── exchange_data/         # Exchange configuration and REST/WSS paths
├── errors/               # Error translator
├── tickers/              # Ticker data container
├── feeds/live_cryptocom/ # REST API implementation
├── containers/orders/    # Order data container
└── containers/orderbooks/ # OrderBook data container
```
