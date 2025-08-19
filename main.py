from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import engine, SessionLocal, Base
from models import YouTubeVideo, TextData
import yt_dlp
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class YouTubeRequest(BaseModel):
    url: str

class TextRequest(BaseModel):
    content: str


@app.post("/save_youtube")
def save_youtube(request: YouTubeRequest, db: Session = Depends(get_db)):
    try:
        ydl_opts = {"quiet": True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.url, download=False)

        video = YouTubeVideo(
            video_id=info.get("id"),
            title=info.get("title"),
            description=info.get("description"),
            channel=info.get("uploader"),
            url=request.url,
            upload_date=info.get("upload_date"),
            view_count=info.get("view_count"),
            like_count=info.get("like_count")
        )
        db.add(video)

     
        if info.get("description"):
            text_entry = TextData(content=info.get("description"))
            db.add(text_entry)

        db.commit()
        db.refresh(video)
        return {
            "message": "Video and text saved successfully",
            "video": video.title,
            "views": video.view_count,
            "likes": video.like_count,
            "upload_date": video.upload_date
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/videos")
def get_videos(db: Session = Depends(get_db)):
    videos = db.query(YouTubeVideo).all()
    return videos


@app.get("/texts")
def get_texts(db: Session = Depends(get_db)):
    texts = db.query(TextData).all()
    return texts
