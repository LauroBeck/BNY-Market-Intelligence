import requests
import time

BANKS = ["BNY", "JPM", "WFB"]
ENDPOINT = "http://127.0.0.1:8000/open-banking/v3.1/aisp/accounts/ACT-778899/balances"

def fetch_global_liquidity():
    print(f"\n{'='*45}")
    print(f"{'INSTITUTION':<20} | {'AVAILABLE BALANCE':>20}")
    print(f"{'-'*45}")
    
    total_liquidity = 0.0
    
    for bank_id in BANKS:
        headers = {"x-fapi-financial-id": bank_id}
        try:
            response = requests.get(ENDPOINT, headers=headers)
            data = response.json()
            balance = float(data['Data']['Balance'][0]['Amount']['Amount'])
            bank_name = data['Meta']['Bank']
            
            print(f"{bank_name:<20} | ${balance:>19,.2f}")
            total_liquidity += balance
        except Exception as e:
            print(f"{bank_id:<20} | ERROR: {str(e)}")

    print(f"{'-'*45}")
    print(f"{'TOTAL GLOBAL LIQUIDITY':<20} | ${total_liquidity:>19,.2f}")
    print(f"{'='*45}\n")

if __name__ == "__main__":
    fetch_global_liquidity()
