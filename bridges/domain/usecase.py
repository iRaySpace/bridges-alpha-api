from bridges.domain.dto import TransactionCreate
from bridges.data import transaction_repository


def create_transaction(transaction: TransactionCreate):
    return transaction_repository.create(transaction)


def read_transactions():
    return transaction_repository.get()
