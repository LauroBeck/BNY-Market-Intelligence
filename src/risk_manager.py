from bny_test_project.src.account_engine import GlobalAccountEngine

class RiskManager:
    def __init__(self, concentration_limit=0.60):
        self.engine = GlobalAccountEngine()
        self.banks = ["BNY", "JPM", "WFB"]
        self.limit = concentration_limit

    def check_concentration_risk(self):
        print("\n" + "="*50)
        print("      2026 TREASURY RISK & REBALANCING REPORT      ")
        print("="*50)
        
        results = []
        total_global = 0.0
        
        # Gather all data
        for bank_id in self.banks:
            res = self.engine.get_balance(bank_id)
            if res['status'] == 'success':
                results.append(res)
                total_global += res['balance']

        # Analyze distribution
        alerts = []
        for res in results:
            share = res['balance'] / total_global
            status = "OK"
            if share > self.limit:
                status = "⚠️ OVER-CONCENTRATED"
                alerts.append(f"REBALANCE SUGGESTED: Move funds FROM {res['bank']}")
            
            print(f"{res['bank']:<25} | {share:>6.1%} | {status}")

        print("-" * 50)
        print(f"TOTAL GLOBAL CAPITAL: ${total_global:>19,.2f}")
        
        if alerts:
            print("\n>>> RISK ALERTS DETECTED:")
            for a in alerts:
                print(f" [!] {a}")
        else:
            print("\n✅ Risk profile is within enterprise limits.")
        print("="*50 + "\n")

if __name__ == "__main__":
    rm = RiskManager()
    rm.check_concentration_risk()
