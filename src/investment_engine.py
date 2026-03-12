import requests
import pandas as pd

class InvestmentEngine:
    def __init__(self, endpoint="http://127.0.0.1:8000"):
        self.endpoint = endpoint

    def get_projections(self):
        try:
            r = requests.get(f"{self.endpoint}/enterprise/v1/projections")
            return r.json()['assets']
        except:
            return None

    def simulate_portfolio_growth(self, total_liquidity):
        assets = self.get_projections()
        if not assets: return
        
        print("\n" + "="*60)
        print("     2026 ASSET PROJECTION REPORT: INFO-TECH & BONDS      ")
        print("="*60)
        print(f"{'ASSET CLASS':<20} | {'YIELD':<8} | {'12M PROJECTION':>18}")
        print("-" * 60)
        
        for key, data in assets.items():
            projected_value = total_liquidity * (1 + data['expected_yield'])
            print(f"{data['desc']:<20} | {data['expected_yield']:>7.2%} | ${projected_value:>17,.2f}")
        
        print("-" * 60)
        print(f"BASE LIQUIDITY: ${total_liquidity:,.2f}")
        print("="*60 + "\n")

if __name__ == "__main__":
    # Simulate based on your current ~.5M liquidity
    engine = InvestmentEngine()
    engine.simulate_portfolio_growth(8548607.93)
