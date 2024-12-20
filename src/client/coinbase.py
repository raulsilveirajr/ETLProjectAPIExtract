import requests

from tools.logger import logger


def extract_bitcoin_price() -> dict:
    # url = "https://api.coinbase.com/v2/prices/spot"
    url = "https://api.coinbase.com/v2/exchange-rates"
    params = {"currency": "BTC"}
    headers = {
        "Accept": "application/json",
        "User-Agent": "MinhaAplicacao/1.0",
    }

    logger.info(f"Requesting {url} with params {params} and headers {headers}")
    try:
        response = requests.get(url, headers=headers, params=params)
        logger.debug(f"Response: {response.json()}")
        rates = response.json()["data"]["rates"]
    except Exception as e:
        logger.error(f"Error requesting {url}: {e}")
        raise e

    if response.status_code != requests.codes.ok:
        logger.error(f"Error requesting {url}: {response.status_code}")
        raise Exception(f"Error requesting {url}: {response.status_code}")

    logger.info(response.status_code)

    currencies = ["USD", "BRL"]
    filtered_rates = {
        currency: rate for currency, rate in rates.items() if currency in currencies
    }

    logger.info(f"Filtered rates: {filtered_rates}")

    return filtered_rates
