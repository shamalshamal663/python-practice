import requests
import sys


for word in sys.stdin:
    res =  requests.get(url=f'https://jsonplaceholder.typicode.com/{word}')
    print(res)
    data = res.json()
    print(data)