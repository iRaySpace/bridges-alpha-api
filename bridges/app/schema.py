from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str


# TODO: add date
class Transaction(BaseModel):
    amount: int
    source_name: str = Field(alias='sourceName')
    destination_name: str = Field(alias='destinationName')


class Signup(BaseModel):
    email: str
    password: str
