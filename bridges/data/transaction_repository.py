from bridges.domain.entity import Transaction

data = []


def create(transaction: Transaction):
    data.append(transaction)
    return transaction
