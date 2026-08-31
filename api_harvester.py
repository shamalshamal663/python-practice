import time, requests

target_url = "https://httpbin.org/json"

def extract_api_data(url,timeout=5):
    try:
        response = requests.get( url,timeout=timeout)
        data =response.json()

        title  = data["slideshow"]["title"]
        author  = data["slideshow"]["author"]
        slide_count = len(data["slideshow"]["slides"])

        print(f"[API EXTRACT] Title:{title}")
        print(f"[API EXTRACT] Author:{author}")
        print(f"[API EXTRACT] Total Slides Found :{slide_count}")

    except requests.exceptions.RequestException:
        print(f"[ERROR] Connection Failed to {url}")

extract_api_data(target_url)        
