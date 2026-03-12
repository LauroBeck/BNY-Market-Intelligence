from fastapi import FastAPI, Header
import random
from datetime import datetime

app = FastAPI()

# 2026 Asset Class Projections
ASSET_PROJECTIONS = {
    "SP500_IT": {"growth": 0.125, "volatility": "High", "desc": "S&P 500 InfoTech ETF"},
    "BOND_10Y": {"growth": 0.042, "volatility": "Low", "desc": "10Y Treasury Bond"},
    "TECH_BOND": {"growth": 0.068, "volatility": "Med", "desc": "Corporate Tech Bond"}
}

BANK_DATA = {
    "BNY": {"balance": 2500000.00, "name": "BNY Mellon Main"},
    "JPM": {"balance": 4850000.00, "name": "JPM Chase Corporate"},
    "WFB": {"balance": 1200000.00, "name": "Wells Fargo Treasury"}
}

@app.get("/open-banking/v3.1/aisp/accounts/{account_id}/balances")
async def get_multi_bank_balance(account_id: str, x_fapi_financial_id: str = Header(None)):
    bank_key = x_fapi_financial_id if x_fapi_financial_id in BANK_DATA else "BNY"
    current_bal = BANK_DATA[bank_key]["balance"] + random.uniform(-1000, 1000)
    return {
        "Data": {"Balance": [{"Amount": {"Amount": f"{current_bal:.2f}", "Currency": "USD"}}]},
        "Meta": {"Bank": BANK_DATA[bank_key]["name"]}
    }

@app.get("/enterprise/v1/projections")
async def get_market_projections():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "assets": {k: {**v, "expected_yield": v["growth"] + random.uniform(-0.01, 0.01)} 
                   for k, v in ASSET_PROJECTIONS.items()}
    }

if __name__ == "__main__":
    import uvicorn
    # Using uvicorn.run directly inside the script
    uvicorn.run(app, host="0.0.0.0", port=8000)
