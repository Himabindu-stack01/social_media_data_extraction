from sqlalchemy import Column, Integer, String
from database import Base

class YouTubeVideo(Base):
    __tablename__ = "youtube_videos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    upload_date = Column(String)
