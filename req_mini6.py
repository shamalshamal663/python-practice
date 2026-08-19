#goal send an HTTP GET req using the params=arguments
#in request to filter api records dynamically and then 
#iterate through the resulting JSON list

import requests

url = "https://jsonplaceholder.typicode.com/posts"

user_payload = {"userId":1}

try:
 response = requests.get(url,user_payload,timeout=5)
 posts = response.json()

 for post in posts:
  print(f"[ID:{post['id']}] Title:{post['title']} ")

except requests.exceptions.RequestException as e:
 print(f"[ERROR]:{e}")