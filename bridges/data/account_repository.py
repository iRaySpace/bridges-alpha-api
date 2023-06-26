import jwt
import pytz
import time
from random import randint
from datetime import datetime
from fastapi.encoders import jsonable_encoder
from bridges.app.settings import get_settings
from bridges.domain.entity import Account
from bridges.domain.dto import AccountCreate, AccountLogin, AccountToken

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
    return Account(**existing_account[0]) if existing_account else None


# TODO: not the right place
def login(data: AccountLogin, expires_in=300):
    epoch = int(time.time())
    payload = {
        'sub': data.phone_no,
        'iat': epoch,
        'exp': epoch + expires_in,
    }
    return AccountToken(
        access_token=jwt.encode(
            payload,
            get_settings().secret_key,
            get_settings().algorithm,
        ),
    )


def verify_token(token: str) -> str:
    try:
        decoded_token = jwt.decode(
            token,
            get_settings().secret_key,
            get_settings().algorithm,
        )
        return decoded_token if decoded_token.get('exp') >= int(time.time()) else None
    except:
        return None
