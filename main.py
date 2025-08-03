from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import YouTubeVideo

app = FastAPI()

@app.post("/save_youtube/")
def save_youtube_video(title: str, upload_date: str, db: Session = Depends(get_db)):
    video = YouTubeVideo(title=title, upload_date=upload_date)
    db.add(video)
    db.commit()
    db.refresh(video)
    return {"message": "Video saved", "id": video.id}

@app.post("/save_text/")
def save_text_to_file(content: str):
    file_path = "youtube_data.txt"
    with open(file_path, "a", encoding="utf-8") as f:
        f.write(content + "\n")
    return {"message": f"Content saved to {file_path}"}
@app.get("/videos/")
def get_youtube_videos(db: Session = Depends(get_db)):
    videos = db.query(YouTubeVideo).all()
    return videos

