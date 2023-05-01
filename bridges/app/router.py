from fastapi.routing import APIRouter
from bridges.app.schema import Message, Transaction, Signup
from bridges.data.transaction_repository import create
from bridges.data.auth_repository import signup_with_email

api_router = APIRouter()


@api_router.post('/', response_model=Message)
async def send_echo_message(incoming_message: Message) -> Message:
    return incoming_message


@api_router.post('/transaction')
async def process_transaction(transaction: Transaction) -> None:
    create(transaction)
    return None


@api_router.post('/signup')
async def process_signup(signup: Signup):
    return signup_with_email(signup)