import requests

API_URL = "http://127.0.0.1:8000/save_youtube"


with open("youtube_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        url = line.strip()
        if url:
            data = {"url": url}
            try:
                res = requests.post(API_URL, json=data)
                print(f"URL: {url}")
                print("Response:", res.json())
                print("-" * 50)
            except Exception as e:
                print(f"Error for {url}: {e}")
