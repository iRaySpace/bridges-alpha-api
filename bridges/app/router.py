from typing import List
from fastapi import HTTPException, Depends, status
from fastapi.routing import APIRouter
from fastapi.security import HTTPBearer
from bridges.domain.dto import TransactionCreate, AccountCreate, AccountLogin, AccountToken
from bridges.domain.entity import Account, Transaction
from bridges.data import account_repository
from bridges.domain import usecase


api_router = APIRouter()
http_bearer = HTTPBearer()


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


async def _token_auth(bearer: HTTPBearer = Depends(http_bearer)) -> Account:
    try:
        return usecase.process_token(bearer.credentials)
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )


@api_router.get('/transactions')
async def send_transactions(account: Account = Depends(_token_auth)) -> List[Transaction]:
    return usecase.get_transactions(account.phone_no)


@api_router.post('/login')
async def process_token(data: AccountLogin) -> AccountToken:
    try:
        return usecase.login(data)
    except Exception as err:
        raise HTTPException(status_code=400, detail=str(err))
