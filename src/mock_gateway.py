from fastapi import FastAPI, Header
import random
from datetime import datetime

app = FastAPI()

# Enterprise Liquidity Pools - 2026 Simulation
BANK_DATA = {
    "BNY": {"balance": 2500000.00, "name": "BNY Mellon Main"},
    "JPM": {"balance": 4850000.00, "name": "JPM Chase Corporate"},
    "WFB": {"balance": 1200000.00, "name": "Wells Fargo Treasury"}
}

@app.get("/open-banking/v3.1/aisp/accounts/{account_id}/balances")
async def get_multi_bank_balance(account_id: str, x_fapi_financial_id: str = Header(None)):
    # Header routing: defaults to BNY if missing
    bank_key = x_fapi_financial_id if x_fapi_financial_id in BANK_DATA else "BNY"
    
    # Simulate high-frequency market movement
    current_bal = BANK_DATA[bank_key]["balance"] + random.uniform(-1000, 1000)
    
    return {
        "Data": {
            "Balance": [{
                "Amount": {"Amount": f"{current_bal:.2f}", "Currency": "USD"},
                "CreditDebitIndicator": "Credit",
                "Type": "ClosingAvailable",
                "DateTime": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
            }]
        },
        "Meta": {
            "Bank": BANK_DATA[bank_key]["name"],
            "FinancialId": bank_key
        }
    }

if __name__ == "__main__":
    import uvicorn
    print(f"🚀 Multi-Bank Gateway Active: BNY | JPM | WFB")
    uvicorn.run(app, host="0.0.0.0", port=8000)
