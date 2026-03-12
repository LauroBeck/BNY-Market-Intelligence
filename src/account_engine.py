import requests

class GlobalAccountEngine:
    def __init__(self, endpoint="http://127.0.0.1:8000"):
        self.endpoint = endpoint

    def get_balance(self, bank_id):
        """Standard AISP balance request using Open Banking v3.1 headers"""
        url = f"{self.endpoint}/open-banking/v3.1/aisp/accounts/ACT-GLOBAL/balances"
        headers = {"x-fapi-financial-id": bank_id}
        
        try:
            response = requests.get(url, headers=headers)
            data = response.json()
            balance = float(data['Data']['Balance'][0]['Amount']['Amount'])
            bank_name = data['Meta']['Bank']
            return {"status": "success", "balance": balance, "bank": bank_name}
        except Exception as e:
            return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    engine = GlobalAccountEngine()
    for bank in ["BNY", "JPM", "WFB"]:
        res = engine.get_balance(bank)
        print(f"[{bank}] {res.get('bank')}: ${res.get('balance'):,.2f}")
