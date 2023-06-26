from fastapi.routing import APIRouter
from bridges.domain.dto import TransactionCreate, AccountCreate
from bridges.domain.entity import Account, Transaction
from bridges.data import account_repository
from bridges.domain import usecase


api_router = APIRouter()


@api_router.post('/transactions')
async def process_transaction(transaction: TransactionCreate) -> Transaction:
    return usecase.create_transaction(transaction)


@api_router.post('/account')
async def process_account(account: AccountCreate) -> Account:
    return account_repository.create(account)
 

@api_router.get('/transactions')
async def send_transactions():
    return usecase.read_transactions()
