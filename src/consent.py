import json
import uuid
from datetime import datetime, timedelta

def create_account_consent_payload():
    """Builds a BNY v3.1 Account Access Consent request."""
    return {
        "Data": {
            "Permissions": [
                "ReadAccountsDetail",
                "ReadBalances",
                "ReadTransactionsDetail",
                "ReadStatementsDetail"
            ],
            "ExpirationDateTime": (datetime.utcnow() + timedelta(days=90)).isoformat() + "Z",
            "TransactionFromDateTime": (datetime.utcnow() - timedelta(days=365)).isoformat() + "Z",
            "TransactionToDateTime": datetime.utcnow().isoformat() + "Z"
        },
        "Risk": {}
    }

def get_fapi_headers(token):
    return {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'x-fapi-financial-id': 'bny-mellon-id-123',
        'x-fapi-interaction-id': str(uuid.uuid4()),
        'Accept': 'application/json'
    }
