import requests

url = "https://httpbin.org/status/404"

try :
    response = requests.get(url,timeout=5)
    status = response.status_code
    if status == 200 :
        print(f"[SUCCESS] Target found:{status}")
    elif status == 404:
        print(f"[NOT FOUND] resource missing :{status}")
    elif status == 403:
        print(f"[FORBIDDEN] Access blocked:{status}")
    else:
        print(f"[OTHER] server returned status;{status}")
except requests.exceptions.RequestException as e:
    print(f"[OTHER] connection failed {e} ")                    
