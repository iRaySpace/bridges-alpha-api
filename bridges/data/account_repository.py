from random import randint
from bridges.domain.entity import Account
from bridges.domain.dto import AccountCreate

data = []


def create(account: AccountCreate) -> Account:
    account_no = randint(1000_0000_0000, 9999_9999_9999)
    new_account = {**account.dict(), 'accountNo': account_no}
    parsed_account = Account(**new_account)
    data.append(parsed_account)
    return parsed_account
