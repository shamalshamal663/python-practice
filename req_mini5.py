import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    response = requests.get(url,timeout=5)
    data = response.json()
    print(f"Post Title : {data['title']}")
    print(f"ID:{data['id']}")
except requests.exceptions.RequestException as e:
    print(f"[ERROR]:{e}")    