import requests

target_url = "https://httpbin.org/headers"

custom_headers = {
"User-Agent": "Cypher-Security-Auditor/1.0",
"Authorization" : "Bearer SEC_TOKEN_9981_ADMIN",
"X-Request-ID": "REQ-0042"

}


def audit_custom_headers(url, header_dict):
    try:
        response = requests.get(url,headers= header_dict, timeout=5)
        data = response.json()
        echoed_header = data.get("headers",{})
        if "Authorization" in echoed_header:
            print(f"[AUTH SUCCESS] Token accepted:{echoed_header['Authorization']}")
            print(f"[AGENT VERIFIED] Echoed User-Agent:{echoed_header.get('User-Agent')}")  
    except requests.exceptions.RequestException:
            print(f"[ERROR] Connection failed to {url}")


audit_custom_headers(target_url,custom_headers)
            