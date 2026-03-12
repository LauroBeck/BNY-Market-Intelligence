import http.client
import ssl
import json
import os
from .consent import create_consent_payload, get_fapi_headers

def run_bny_check(debtor_iban, token="MOCK_TOKEN_2026", simulate=True):
    # The real 2026 BNY Gateway
    host = "apigatewayb2b.bny.com"
    path = "/tpp/v1/funds-confirmation-consents"
    
    if simulate:
        return {
            "status": 201,
            "interaction_id": "SIM-" + os.urandom(4).hex(),
            "consent_id": "bny-consent-2026-x99",
            "note": "SIMULATED RESPONSE: Handshake bypassed for development."
        }

    context = ssl.create_default_context()
    try:
        context.load_cert_chain(
            certfile="bny_test_project/certs/bny_client_cert.pem",
            keyfile="bny_test_project/certs/bny_private_key.key"
        )
    except Exception as e:
        return {"error": f"Local SSL Load Fail: {e}"}

    payload = json.dumps(create_consent_payload(debtor_iban))
    headers = get_fapi_headers(token)

    try:
        conn = http.client.HTTPSConnection(host, context=context, timeout=5)
        conn.request("POST", path, body=payload, headers=headers)
        res = conn.getresponse()
        return {"status": res.status, "response": res.read().decode()}
    except Exception as e:
        return {"error": str(e), "type": "Handshake_Rejected_By_BNY"}

if __name__ == "__main__":
    # Toggle simulate=False only when you have real BNY certificates
    result = run_bny_check("BR1234567890", simulate=True)
    print(json.dumps(result, indent=2))
