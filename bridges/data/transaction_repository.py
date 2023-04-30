import os
from bridges.app.schema import Transaction
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
    print(data)
