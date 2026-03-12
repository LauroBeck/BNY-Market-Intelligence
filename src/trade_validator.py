from bny_test_project.src.account_engine import GlobalAccountEngine

class TradeValidator:
    def __init__(self):
        self.min_liquidity_buffer = 0.10  # 10% Enterprise Safety Buffer

    def validate_trade(self, trade_amount, available_balance):
        """Standard architectural check for trade viability."""
        required_minimum = trade_amount * (1 + self.min_liquidity_buffer)
        
        if available_balance >= required_minimum:
            return True, "VALIDATED: Sufficient Liquidity"
        else:
            return False, f"DENIED: Insufficient Buffer (Needs ${required_minimum:,.2f})"

if __name__ == "__main__":
    # Unit test for the validator
    v = TradeValidator()
    print(v.validate_trade(1000000, 1500000))
