import requests , time

base_url = "https://httpbin.org/get"

for user_id in range(1,6):
    try:
        response = requests.get(base_url,params = {"user_id": user_id},timeout=4)
        if response.status_code == 200:
            print(f"[VULN CHECK] Probed ID {user_id} -> STATUS:200 OK | Endpoint accessible")
            time.sleep(0.5)
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Request failed for ID {user_id}")


