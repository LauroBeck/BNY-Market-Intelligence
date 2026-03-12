import http.client
import json

class BNYAccountEngine:
    def __init__(self, cert_path=None, key_path=None, simulate=True):
        # Pointing to your verified working Mock Gateway
        self.host = "127.0.0.1"
        self.port = 8080
        self.base_path = "/open-banking/v3.1/aisp"
        self.simulate = simulate

    def _request(self, method, path, payload=None, token="MOCK_TOKEN"):
        if self.simulate:
            return {"status": 200, "data": {"MockData": "Success"}, "path": path}
            
        try:
            conn = http.client.HTTPConnection(self.host, self.port, timeout=5)
            conn.request(method, path, body=json.dumps(payload) if payload else None)
            res = conn.getresponse()
            raw_data = res.read().decode()
            return {
                "status": res.status, 
                "data": json.loads(raw_data) if raw_data else {}
            }
        except Exception as e:
            # This will now show up in your Dashboard as the error message
            return {"status": 500, "error_msg": str(e)}

    def get_balances(self, account_id, token):
        path = f"{self.base_path}/accounts/{account_id}/balances"
        return self._request("GET", path, token=token)

    def get_account_by_id(self, account_id, token):
        path = f"{self.base_path}/accounts/{account_id}"
        return self._request("GET", path, token=token)

if __name__ == "__main__":
    engine = BNYAccountEngine(simulate=False)
    print(engine.get_balances("ACT-778899", "TEST"))
