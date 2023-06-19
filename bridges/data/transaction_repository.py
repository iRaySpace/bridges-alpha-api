import uuid
from fastapi.encoders import jsonable_encoder
from datetime import datetime
from bridges.domain.dto import TransactionCreate
from bridges.domain.entity import Transaction

data = []


def create(transaction: TransactionCreate):
    new_transaction = {
        **transaction.dict(by_alias=True),
        'id': str(uuid.uuid4()),
        'createdAt': datetime.today(),
    }
    data.append(jsonable_encoder(new_transaction))
    return new_transaction


def get():
    return data
