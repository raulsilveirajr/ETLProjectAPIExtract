import time
from datetime import datetime

import logfire

from client.coinbase import extract_bitcoin_price
from repository.postgresql.bitcoin_price import (
    insert_bitcoin_price as insert_bitcoin_price_postgresql,
)
from repository.postgresql.db import create_table
from repository.tinydb.bitcoin_price import (
    insert_bitcoin_price as insert_bitcoin_price_tinydb,
)
from tools.logger import logger


def transform_bitcoin_price(rates: dict) -> list:
    return [
        {
            "crypto_currency": "BTC",
            "fiat_currency": "USD",
            "timestamp": timestamp,
            "price": float(rates["USD"]),
        },
        {
            "crypto_currency": "BTC",
            "fiat_currency": "BRL",
            "timestamp": timestamp,
            "price": float(rates["BRL"]),
        },
    ]


if __name__ == "__main__":
    logger.info("Starting pipeline_extract.py")
    logger.info("Creating table")
    create_table()
    logger.info("Table created")
    while True:
        with logfire.span("Executando pipeline ETL Bitcoin"):
            timestamp = datetime.now().isoformat()
            with logfire.span("Getting bitcoin price"):
                logger.info("Extracting bitcoin price")
                rates = extract_bitcoin_price()
                logger.info("Bitcoin price extracted")
            with logfire.span("Transforming bitcoin price"):
                data = transform_bitcoin_price(rates)
            with logfire.span("Inserting bitcoin price"):
                for item in data:
                    insert_bitcoin_price_postgresql(item)
                    insert_bitcoin_price_tinydb(item)
        time.sleep(3)
        break
