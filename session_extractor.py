import requests


set_cookies_url = "https://httpbin.org/cookies/set?auth_token=CYPHER_9981&role=admin"
check_cookies_url = "https://httpbin.org/cookies"


def extract_session_data(set_url, check_url):
    try :
        session = requests.session()
        session.get(set_url, timeout=5)
        response = session.get(check_url,timeout=5)

        data = response.json()
        cookies = data.get("cookies",{})

        if "auth_token" in cookies:
            print(f"[TOKEN EXTRACTED] Auth Token : {cookies.get('auth_token')} ")
        if "role" in cookies:
            print(f"[PRIVILAGE VERIFIED] Assigned Role : {cookies.get('role')}") 
        if "auth_token" in cookies and "role" in cookies:
            print(f"[SESSION VALIDATED] Multi-cookies persistance comfirmed")
        else:
            print(f"[ERROR]:Session Terminated:Missing required cookies.")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed : {e}")


extract_session_data(set_cookies_url, check_cookies_url)