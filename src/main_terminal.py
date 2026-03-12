from .trade_validator import validate_trade_liquidity
from .audit_logger import log_trade_decision
from .account_engine import BNYAccountEngine

def process_market_signal(symbol, signal_type, trade_amount):
    print(f"\n>>> MARKET SIGNAL DETECTED: [{symbol}] - {signal_type}")
    
    # Quick balance fetch for logging purposes
    engine = BNYAccountEngine(simulate=False)
    bal_resp = engine.get_balances("ACT-778899", "LOG_TOKEN")
    current_bal = float(bal_resp['data']['Data']['Balance'][0]['Amount']['Amount'])

    if "STRONG_BULL" in signal_type:
        is_approved, reason = validate_trade_liquidity(trade_amount)
        status = "AUTHORIZED" if is_approved else "ABORTED"
        
        # Log the decision
        log_trade_decision(symbol, trade_amount, current_bal, status, reason)
        
        if is_approved:
            print(f"🚀 EXECUTION AUTHORIZED: Placing trade for {symbol}.")
        else:
            print(f"🛑 TRADE ABORTED: {reason}")
    else:
        print(f"Holding position for {symbol}.")

if __name__ == "__main__":
    process_market_signal("ORCL", "STRONG_BULL", 50000.00)
    process_market_signal("IBM", "STRONG_BULL", 2000000.00)
    print("\n[SYSTEM] Decisions archived to reports/trade_journal_2026.csv")
