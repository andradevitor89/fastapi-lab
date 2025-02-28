from abc import ABC, abstractmethod
from fastapi import Depends
from lab.domain import api_models
from lab.repository.models import SongEntity
from lab.domain.models import Song
from lab.repository import SongRepository, ISongRepository, ExternalApi, IExternalApi


class ICreateSongUseCase(ABC):
    @abstractmethod
    def execute(self, create_song: api_models.CreateSong) -> Song:
        """Create a song."""


class CreateSongUseCase(ICreateSongUseCase):

    def __init__(
        self,
        repository: ISongRepository = Depends(SongRepository),
        external_api: IExternalApi = Depends(ExternalApi),
    ):
        self.repository = repository
        self.external_api = external_api

    def execute(self, create_song: api_models.CreateSong) -> Song:
        entity = SongEntity(
            title=create_song.title,
            artist_id=create_song.artist_id,
            album=create_song.album,
            year=create_song.year,
        )
        self.external_api.integrate(entity)
        entity = self.repository.create(entity)
        song = Song.model_validate(entity)
        return song
