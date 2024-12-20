from sqlalchemy import Column, DateTime, Float, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BitcoinPrice(Base):
    __tablename__ = "bitcoin_price"
    id = Column(Integer, primary_key=True, autoincrement=True)
    price = Column(Float)
    crypto_currency = Column(String)
    fiat_currency = Column(String)
    timestamp = Column(DateTime)

    def __str__(self) -> str:
        return (
            f"BitcoinPrice("
            f"id={self.id}, "
            f"price={self.price}, "
            f"crypto_currency={self.crypto_currency}, "
            f"fiat_currency={self.fiat_currency}, "
            f"timestamp={self.timestamp}"
            f")"
        )
