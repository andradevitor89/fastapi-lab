from sqlalchemy.orm import declarative_base

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timezone

Base = declarative_base()


class SongEntity(Base):
    __tablename__ = "songs"

    id = Column(Integer(), primary_key=True)
    title = Column(String(100), nullable=False)
    album = Column(String(100), nullable=False)
    year = Column(Integer(), nullable=False)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(tz=timezone.utc)
    )
    artist_id = Column(Integer, ForeignKey("artists.id"), nullable=False)
    artist = relationship("ArtistEntity", back_populates="songs")


class ArtistEntity(Base):
    __tablename__ = "artists"

    id = Column(Integer(), primary_key=True)
    name = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(tz=timezone.utc)
    )
    songs = relationship("SongEntity", back_populates="artist")
