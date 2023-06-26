from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    amount: int
    sender_no: str = Field(alias='senderNo')
    receiver_no: str = Field(alias='receiverNo')
    notes: str


class AccountCreate(BaseModel):
    phone_no: str = Field(alias='phoneNo')


class AccountLogin(BaseModel):
    phone_no: str = Field(alias='phoneNo')
    pin_no: str = Field(alias='pinNo')


class AccountToken(BaseModel):
    access_token: str
