import requests

try:
     response = requests.get(
          "https://this-domain-does-not-exist-12345.org",
          timeout=3)
     print(response.status_code)
except requests.exceptions.RequestException:
     print("[ALERT] Host down or Unreachable")



