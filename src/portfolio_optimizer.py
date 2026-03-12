from bny_test_project.src.investment_engine import InvestmentEngine

class PortfolioOptimizer:
    def __init__(self, liquidity_target=0.70):
        self.target_liquidity_ratio = liquidity_target
        self.engine = InvestmentEngine()

    def optimize_allocation(self, total_capital):
        print("\n" + "="*60)
        print("      2026 STRATEGIC ASSET ALLOCATION (70/20/10)      ")
        print("="*60)
        
        allocation_plan = {
            "Operational Liquidity (Cash)": 0.70,
            "Growth (S&P 500 InfoTech)": 0.20,
            "Risk-Free Hedge (10Y Bonds)": 0.10
        }

        print(f"{'ALLOCATION TYPE':<30} | {'RATIO':<6} | {'AMOUNT':>18}")
        print("-" * 60)

        for asset, ratio in allocation_plan.items():
            amount = total_capital * ratio
            print(f"{asset:<30} | {ratio:>5.0%} | ${amount:>17,.2f}")

        print("-" * 60)
        print(f"TOTAL CAPITAL TO DEPLOY: ${total_capital:,.2f}")
        print("="*60 + "\n")
        
        cash_amount = total_capital * 0.70
        sweep_amount = total_capital * 0.30
        
        print(">>> ARCHITECT'S RECOMMENDATION:")
        print(f" [!] Sweep ${sweep_amount:,.2f} from JPM to Investment Sub-Ledger.")
        print(f" [!] Maintain ${cash_amount:,.2f} for Nasdaq Signal Execution.\n")

if __name__ == "__main__":
    optimizer = PortfolioOptimizer()
    optimizer.optimize_allocation(8548607.93)
