from .account_engine import BNYAccountEngine

def generate_intel_report(account_id, token):
    engine = BNYAccountEngine(simulate=False) 
    balance_resp = engine.get_balances(account_id, token)
    
    if "data" in balance_resp and "Data" in balance_resp["data"]:
        try:
            raw_amount = balance_resp['data']['Data']['Balance'][0]['Amount']['Amount']
            balance_formatted = f"${float(raw_amount):,.2f}"
            status_text = str(balance_resp['status'])
        except:
            balance_formatted = "PARSE_ERROR"
            status_text = "INVALID_JSON"
    else:
        # Show the actual error message from the engine
        error_info = balance_resp.get("error_msg", "Unknown Engine Error")
        balance_formatted = f"ERROR: {error_info}"
        status_text = str(balance_resp.get("status", 500))

    print("="*45)
    print(f" BNY MELLON INTELLIGENCE REPORT | 2026")
    print("="*45)
    print(f"Account ID: {account_id}")
    print(f"API Status: {status_text}")
    print("-" * 45)
    print(f"CURRENT BALANCE: {balance_formatted}")
    print("-" * 45)
    print("="*45)

if __name__ == "__main__":
    generate_intel_report("ACT-778899", "DEV_TOKEN_AISP")
