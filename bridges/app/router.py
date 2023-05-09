from fastapi.routing import APIRouter
from bridges.domain.entity import AccountCreate, Account, Transaction
from bridges.data import account_repository, transaction_repository

api_router = APIRouter()


@api_router.post('/transaction')
async def process_transaction(transaction: Transaction) -> Transaction:
    return transaction_repository.create(transaction)


@api_router.post('/account')
async def process_account(account: AccountCreate) -> Account:
    return account_repository.create(account)
 
