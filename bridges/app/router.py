from fastapi.routing import APIRouter
from bridges.app.schema import Message

api_router = APIRouter()


@api_router.post('/', response_model=Message)
async def send_echo_message(incoming_message: Message) -> Message:
    return incoming_message
