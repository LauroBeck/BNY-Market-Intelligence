from .account_engine import BNYAccountEngine

def validate_trade_liquidity(required_amount, account_id="ACT-778899"):
    # Initialize engine in non-simulation mode to hit your Mock Gateway
    engine = BNYAccountEngine(simulate=False)
    
    # Define a Safety Buffer (e.g., always keep M in the account)
    SAFETY_BUFFER = 100000.00
    
    print(f"\n[VALIDATOR] Checking liquidity for trade amount: ${required_amount:,.2f}")
    
    response = engine.get_balances(account_id, "VALIDATOR_TOKEN")
    
    if response.get("status") == 200:
        try:
            raw_balance = float(response['data']['Data']['Balance'][0]['Amount']['Amount'])
            available_capital = raw_balance - SAFETY_BUFFER
            
            print(f"[VALIDATOR] Current Balance: ${raw_balance:,.2f}")
            print(f"[VALIDATOR] Available (Minus Buffer): ${available_capital:,.2f}")
            
            if available_capital >= required_amount:
                return True, "LIQUIDITY_CONFIRMED"
            else:
                return False, "INSUFFICIENT_FUNDS_AFTER_BUFFER"
        except Exception as e:
            return False, f"PARSING_ERROR: {str(e)}"
    else:
        return False, "GATEWAY_UNREACHABLE"

if __name__ == "__main__":
    # Test a typical trade for your Nasdaq monitoring
    is_valid, reason = validate_trade_liquidity(50000.00)
    print(f"RESULT: {'✅ APPROVED' if is_valid else '❌ REJECTED'} | Reason: {reason}")
