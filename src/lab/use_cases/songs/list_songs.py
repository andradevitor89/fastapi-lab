from abc import ABC, abstractmethod
from fastapi import Depends
from lab.domain.models import Song
from lab.repository import SongRepository, ISongRepository


class IListSongsUseCase(ABC):
    @abstractmethod
    def execute(self, name_filter: str = "") -> list[Song]:
        """Create a song."""


class ListSongsUseCase(IListSongsUseCase):
    def __init__(self, repository: ISongRepository = Depends(SongRepository)):
        self.repository = repository

    def execute(self, name_filter: str = "") -> list[Song]:
        entities = self.repository.query(name_filter)
        songs = [Song.model_validate(entity) for entity in entities]
        return songs
