import csv
import os
from datetime import datetime

def log_trade_decision(symbol, amount, balance, status, reason):
    os.makedirs('reports', exist_ok=True)
    file_path = 'reports/trade_journal_2026.csv'
    
    file_exists = os.path.isfile(file_path)
    
    with open(file_path, mode='a', newline='') as f:
        writer = csv.writer(f)
        # Header for the Data Analyst workflow
        if not file_exists:
            writer.writerow(['Timestamp', 'Symbol', 'Requested_Amount', 'BNY_Balance', 'Status', 'Reason'])
        
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            symbol,
            f"{amount:.2f}",
            f"{balance:.2f}",
            status,
            reason
        ])

if __name__ == "__main__":
    print("Audit Logger initialized. Ready for record keeping.")
