import pytz
from random import randint
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from bridges.domain.entity import Account
from bridges.domain.dto import AccountCreate

data = []


def create(account: AccountCreate) -> Account:
    new_account = Account(**{
        **account.dict(by_alias=True),
        'createdAt': datetime.today().astimezone(pytz.UTC),
    })
    data.append(jsonable_encoder(new_account))
    return new_account


def get(phone_no: str) -> Account:
    existing_account = [x for x in data if x.get('phoneNo') == phone_no]
    return existing_account[0] if existing_account else None
