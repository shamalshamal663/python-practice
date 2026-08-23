import requests

base_url = "https://jsonplaceholder.typicode.com"

endpoints = ["users", "admin", "posts", "secret_tokens", "comments"]

for endpoint in endpoints:
 target_url = f"{base_url}/{endpoint}"

 try:

    response = requests.get(target_url,timeout =5 )

    if response.status_code == 200:
        print(f"[DISCOVERED]:valid route /{endpoint} (status:{response.status_code})")
    elif response.status_code == 404 :
        print(f"[NOT FOUND]/{endpoint}")
    else:
        print(f"[OTHERS]/{endpoint} (status:{response.status_code})")

 except requests.exceptions.RequestException as e:
    print(f"[ERROR] :return {e}")                

