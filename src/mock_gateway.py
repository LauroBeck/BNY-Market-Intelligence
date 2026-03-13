from fastapi import FastAPI, Header, HTTPException
import random

app = FastAPI(title="Open Banking AISP v3.1 Multi-Bank Gateway")

BANKS = {
    "JPM": {"Name": "JPMorgan Chase Corporate", "BIC": "CHASUS33"},
    "BNY": {"Name": "BNY Mellon Main", "BIC": "BONYUS33"},
    "WFB": {"Name": "Wells Fargo Treasury", "BIC": "WELSUS66"}
}

ACCOUNTS = {
    "ACC-JPM-001": {"Nickname": "Main Operating", "Balance": 4850000.00, "Bank": "JPM"},
    "ACC-BNY-002": {"Nickname": "Alpha Treasury", "Balance": 2500000.00, "Bank": "BNY"},
    "ACC-WFB-003": {"Nickname": "Beta Liquidity", "Balance": 1200000.00, "Bank": "WFB"}
}

@app.get("/open-banking/v3.1/aisp/accounts")
async def get_accounts(x_fapi_financial_id: str = Header(None)):
    bank_id = x_fapi_financial_id
    filtered = []
    
    for acc_id, data in ACCOUNTS.items():
        if not bank_id or data["Bank"] == bank_id:
            bank_info = BANKS[data["Bank"]]
            filtered.append({
                "AccountId": acc_id,
                "Nickname": data["Nickname"],
                "Servicer": {
                    "SchemeName": "UK.OBIE.BICFI",
                    "Identification": bank_info["BIC"]
                }
            })
    return {"Data": {"Account": filtered}}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
