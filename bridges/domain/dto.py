from pydantic import BaseModel, Field


class TransactionCreate(BaseModel):
    amount: int
    source_no: str = Field(alias='sourceNo')
    destination_no: str = Field(alias='destinationNo')


class AccountCreate(BaseModel):
    email: str
    password: str
