import os
from bridges.app.schema import Transaction, BalanceRequest, Balance
from supabase import create_client, Client


def create(transaction: Transaction) -> None:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
    data = (
        supabase.table('transaction')
        .insert(
            {
                'amount': transaction.amount,
                'sourceName': transaction.source_name,
                'destinationName': transaction.destination_name,
            }
        )
        .execute()
    )


def get_balance(balance_request: BalanceRequest) -> Balance:
    url: str = os.environ.get('SUPABASE_URL')
    key: str = os.environ.get('SUPABASE_KEY')
    supabase: Client = create_client(url, key)
    query = (
        supabase.table('transaction')
        .select('*')
        .execute()
    )
    total_amount = sum([x.get('amount') for x  in query.data])
    return Balance(name=balance_request.name, amount=total_amount)
