from fastapi.routing import APIRouter
from bridges.app.schema import Message, Transaction

api_router = APIRouter()


@api_router.post('/', response_model=Message)
async def send_echo_message(incoming_message: Message) -> Message:
    return incoming_message


@api_router.post('/transaction')
async def process_transaction(transaction: Transaction) -> None:
    return None