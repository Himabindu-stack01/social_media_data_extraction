import requests

API_URL = "http://127.0.0.1:8000/save_youtube/"

with open("youtube_data.txt", "r", encoding="utf-8") as file:
    for line in file:
        if "|" in line:
            title, date = line.strip().split("|")
            data = {"title": title.strip(), "upload_date": date.strip()}
            res = requests.post(API_URL, params=data)
            print(res.json())
