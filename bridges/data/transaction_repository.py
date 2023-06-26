import uuid
import pytz
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from bridges.domain.dto import TransactionCreate
from bridges.domain.entity import Transaction

data = []


def create(transaction: TransactionCreate):
    new_transaction = {
        **transaction.dict(by_alias=True),
        'id': str(uuid.uuid4()),
        'createdAt': datetime.today().astimezone(pytz.UTC),
    }
    data.append(jsonable_encoder(new_transaction))
    return new_transaction


def get(sender_no: str = None):
    if sender_no:
        return [x for x in data if x.get('senderNo') == sender_no]
    return data
