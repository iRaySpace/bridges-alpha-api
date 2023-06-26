from bridges.domain.dto import TransactionCreate, AccountCreate
from bridges.data import transaction_repository, account_repository


def create_transaction(transaction: TransactionCreate):
    sender_account = account_repository.get(transaction.sender_no)
    if not sender_account:
        raise Exception('Sender account does not exist.')

    receiver_account = account_repository.get(transaction.receiver_no)
    if not receiver_account:
        raise Exception('Receiver account does not exist.')

    if transaction.sender_no == transaction.receiver_no:
        raise Exception('Sender account cannot be receiver account.')

    if transaction.amount <= 0:
        raise Exception('Amount cannot be less than or equal to 0')

    return transaction_repository.create(transaction)


def get_transactions():
    return transaction_repository.get()


def create_account(account: AccountCreate):
    existing_account = account_repository.get(account.phone_no)
    if existing_account:
        raise Exception('Account already exist.')
    return account_repository.create(account)
