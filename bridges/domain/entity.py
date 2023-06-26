from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Transaction(BaseModel):
    id: str
    created_at: datetime = Field(alias='createdAt')
    source_no: str = Field(alias='sourceNo')
    destination_no: str = Field(alias='destinationNo')
    amount: int


class Account(BaseModel):
    email: str
    password: str
    account_no: str = Field(alias='accountNo')
