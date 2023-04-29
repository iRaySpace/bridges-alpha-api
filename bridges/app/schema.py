from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str


# TODO: add date
class Transaction(BaseModel):
    amount: int
    source_uuid: str = Field(alias='sourceUuid')
    destination_uuid: str = Field(alias='destinationUuid')
