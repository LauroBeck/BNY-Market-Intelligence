from bny_test_project.src.account_engine import GlobalAccountEngine

class SmartOrderRouter:
    def __init__(self):
        self.engine = GlobalAccountEngine()
        self.banks = ["BNY", "JPM", "WFB"]

    def select_best_provider(self, trade_amount):
        """Finds the optimal bank to fund a specific trade amount."""
        print(f"\n[SOR] Analyzing liquidity for trade: ${trade_amount:,.2f}...")
        
        candidates = []
        for bank_id in self.banks:
            res = self.engine.get_balance(bank_id)
            if res['status'] == 'success':
                # Check if bank can cover the trade + a 10% safety buffer
                if res['balance'] >= (trade_amount * 1.1):
                    candidates.append(res)
        
        if not candidates:
            return None
            
        # Strategy: Pick the bank with the HIGHEST remaining balance to preserve liquidity ratios
        best_pick = max(candidates, key=lambda x: x['balance'])
        return best_pick

if __name__ == "__main__":
    router = SmartOrderRouter()
    # Test a M trade
    pick = router.select_best_provider(2000000.00)
    
    if pick:
        print(f"✅ ROUTING SUCCESS: Use {pick['bank']} (Available: ${pick['balance']:,.2f})")
    else:
        print("❌ ROUTING FAILED: Insufficient global liquidity for this trade.")
