from bny_test_project.src.account_engine import GlobalAccountEngine
import os

def render_global_view():
    engine = GlobalAccountEngine()
    banks = ["BNY", "JPM", "WFB"]
    
    os.system('clear')
    print("="*60)
    print("      LAURO BECK - MULTI-BANK LIQUIDITY TERMINAL (2026)      ")
    print("="*60)
    print(f"{'INSTITUTION':<25} | {'STATUS':<10} | {'BALANCE':>15}")
    print("-" * 60)
    
    total = 0.0
    for bank in banks:
        data = engine.get_balance(bank)
        if data['status'] == 'success':
            total += data['balance']
            print(f"{data['bank']:<25} | ACTIVE     | ${data['balance']:>14,.2f}")
        else:
            print(f"{bank:<25} | OFFLINE    | {'--':>15}")

    print("-" * 60)
    print(f"{'CONSOLIDATED LIQUIDITY':<25} |            | ${total:>14,.2f}")
    print("="*60)

if __name__ == "__main__":
    render_global_view()
