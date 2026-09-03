import requests

test_cookie_url = "https://httpbin.org/cookies/set/session_token/SEC-9988-ACTIVE"

view_cookie_url = "https://httpbin.org/cookies"


def audit_session(set_url, check_url):
    try:
        session = requests.session()
        session.get(set_url,timeout=5)
        response = session.get(check_url,timeout=5)
        data = response.json()
        cookies = data.get("cookies",{})
        if "session_token" in cookies:
            print(f"[SESSION ACTIVE] Stored Cookies : {cookies.get('session_token')}")
            print(f"[PERSISTANCE CONFIRMED] Session state maintained across requests."
                  )
        else:
            print(f"[FAILED] Cookies not found in session : {cookies}")
    
    except requests.exceptions.RequestException as e :
        print(f"[ERROR] Session requests failed: {e}")



audit_session(test_cookie_url,view_cookie_url)