import json
import os
from datetime import datetime

def save_bny_report(data, report_type="AISP"):
    # Ensure the reports directory exists
    os.makedirs('reports', exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"reports/BNY_{report_type}_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    
    print(f"Report saved to: {filename}")

if __name__ == "__main__":
    # Test saving a dummy interaction
    sample_data = {"account_id": "ACT-778899", "balance": 2488700.00, "status": "verified"}
    save_bny_report(sample_data)
