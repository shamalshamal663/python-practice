import requests

target_url = "https://httpbin.org/post"


login_payload = {
    "username": "cypher_admin",
    "password": "SuperSecret2026!",
    "csrf_token": "token_xyz_98765"
}


def submit(url,payload):
    try:
        response = requests.post(url, data=payload, timeout=5)
        if response.status_code == 200:
            data = response.json()
            echoed_form = data.get("form" ,{})
            if "username" in echoed_form:
                print(f"[LOGIN SENT] Authenticating user:{echoed_form.get('username')}")
                print(f"[TOKEN VERIFIED] CSRF Token matched:{echoed_form.get('csrf_token')}")
    except requests.exceptions.RequestException:
        print(f"[ERROR] POST request failed to {url}")


submit(target_url,login_payload)

