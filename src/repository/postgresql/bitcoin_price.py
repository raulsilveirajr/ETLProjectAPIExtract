from repository.postgresql.bitcoin_price_struct import BitcoinPrice
from repository.postgresql.db import Session
from tools.logger import logger


def insert_bitcoin_price(data: dict) -> BitcoinPrice:
    newRecord = BitcoinPrice(**data)
    logger.info(f"BitcoinPrice inserted data: {str(newRecord)}")
    session = Session()
    session.add(newRecord)
    session.commit()
    session.refresh(newRecord)
    session.close()
    return newRecord


def load_bitcoin_price(data: dict) -> list[BitcoinPrice]:
    session = Session()
    return session.query(BitcoinPrice).all()
