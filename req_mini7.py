import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "Ethical Hacking Notes",
    "body": "Testing HTTP POST methods in Python.",
    "userId": 101
}



try:

 response = requests.post(url,json=payload,timeout=5)

 if response.status_code == 201:
    create_post = response.json()
    print(f"SUCCESS : Resource created! status:{response.status_code}")
    print(f"Server Assigned ID : {create_post['id']}")
    print(f"Title: {create_post['title']}")
 else:
    print(f"[FAILED]:Server Returned status:{response.status_code}")
except requests.exceptions.RequestException as e:
  print(f"[ERROR] : with exception {e}")
