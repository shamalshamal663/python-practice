import requests

url = "https://www.google.com"

custom_headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64)"
}

try:
 response = requests.get(url, headers=custom_headers, timeout=5)
 if "Content-Type" in response.headers:
    print(f"Server Content-Type: {response.headers['Content-Type']}")
 else:
    print("Header not Found!")    
except requests.exceptions.RequestException as e:
  print(f"Connection failed : {e}")    