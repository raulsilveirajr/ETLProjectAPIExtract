from tinydb import TinyDB

file_name: str = "bitcoin_price_db.json"


def insert_bitcoin_price(data: dict) -> None:
    db = TinyDB(file_name)
    db.insert(data)


def load_bitcoin_price(data: dict) -> dict:
    db = TinyDB(file_name)
    return db.all()
