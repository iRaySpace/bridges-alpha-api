from fastapi import HTTPException
from fastapi.routing import APIRouter
from bridges.domain.dto import TransactionCreate, AccountCreate
from bridges.domain.entity import Account, Transaction
from bridges.data import account_repository
from bridges.domain import usecase


api_router = APIRouter()


@api_router.post('/transactions')
async def process_transaction(transaction: TransactionCreate) -> Transaction:
    try:
        return usecase.create_transaction(transaction)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@api_router.post('/accounts')
async def process_account(account: AccountCreate) -> Account:
    try:
        return usecase.create_account(account)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))


@api_router.get('/transactions')
async def send_transactions():
    return usecase.get_transactions()
