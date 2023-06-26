from typing import Optional
from pydantic import BaseModel, Field
from datetime import datetime


class Transaction(BaseModel):
    id: str
    created_at: datetime = Field(alias='createdAt')
    sender_no: str = Field(alias='senderNo')
    receiver_no: str = Field(alias='receiverNo')
    notes: str


class Account(BaseModel):
    phone_no: str = Field(alias='phoneNo')
    created_at: datetime = Field(alias='createdAt')
