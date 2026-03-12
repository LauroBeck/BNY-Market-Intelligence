from fastapi import FastAPI, Header
import uuid
import random
from datetime import datetime

app = FastAPI(title="BNY Mellon Mock Gateway - Volatility Mode")

# Persistence for "Account State" during a session
BASE_BALANCE = 5000000.00

@app.get("/open-banking/v3.1/aisp/accounts/{account_id}/balances")
async def get_balances(account_id: str):
    # Simulate a 0.5% market swing for every API call
    swing = BASE_BALANCE * random.uniform(-0.005, 0.005)
    current_val = round(BASE_BALANCE + swing, 2)
    
    return {
        "Data": {
            "Balance": [{
                "AccountId": account_id,
                "Amount": {"Amount": str(current_val), "Currency": "USD"},
                "CreditDebitIndicator": "Credit",
                "Type": "ClosingAvailable",
                "DateTime": datetime.utcnow().isoformat() + "Z"
            }]
        }
    }

@app.post("/open-banking/v3.1/aisp/account-access-consents")
async def create_consent():
    return {"Data": {"ConsentId": f"CSNT-{uuid.uuid4().hex[:8]}", "Status": "Authorised"}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)
