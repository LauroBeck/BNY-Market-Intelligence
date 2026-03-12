from bny_test_project.src.smart_router import SmartOrderRouter
from bny_test_project.src.trade_validator import TradeValidator
import time

def execute_market_intelligence_loop():
    router = SmartOrderRouter()
    validator = TradeValidator()
    
    # Simulated Nasdaq Signal (e.g., ORCL Breakout)
    signals = [
        {"ticker": "ORCL", "action": "BUY", "amount": 1500000.00},
        {"ticker": "IBM", "action": "BUY", "amount": 3000000.00}
    ]

    for signal in signals:
        print(f"\n>>> SIGNAL DETECTED: {signal['action']} {signal['ticker']} for ${signal['amount']:,.2f}")
        
        # 1. Ask Router for the best bank
        provider = router.select_best_provider(signal['amount'])
        
        if provider:
            print(f"[SOR] Selected Provider: {provider['bank']}")
            
            # 2. Pass to Validator (using the selected bank's balance)
            is_valid, msg = validator.validate_trade(signal['amount'], provider['balance'])
            
            if is_valid:
                print(f"🚀 EXECUTION AUTHORIZED: Funding via {provider['bank']}")
            else:
                print(f"⚠️ EXECUTION DENIED: {msg}")
        else:
            print(f"🛑 CRITICAL: No single bank can safely fund ${signal['amount']:,.2f}")
        
        time.sleep(1)

if __name__ == "__main__":
    execute_market_intelligence_loop()
