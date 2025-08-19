from sqlalchemy import Column, Integer, String, Text
from database import Base

class YouTubeVideo(Base):
    __tablename__ = "youtube_videos"

    id = Column(Integer, primary_key=True, index=True)
    video_id = Column(String, unique=True, index=True)
    title = Column(String)
    description = Column(Text)
    channel = Column(String)
    url = Column(String)
    upload_date = Column(String)      
    view_count = Column(Integer)      
    like_count = Column(Integer)      


class TextData(Base):
    __tablename__ = "text_data"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(Text)
