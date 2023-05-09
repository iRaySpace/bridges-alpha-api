from typing import Optional
from pydantic import BaseModel, Field

class Transaction(BaseModel):
    amount: int
    source_no: str = Field(alias='sourceNo')
    destination_no: str = Field(alias='destinationNo')


class Account(BaseModel):
    email: str
    password: str
    account_no: str = Field(alias='accountNo')


class AccountCreate(BaseModel):
    email: str
    password: str
