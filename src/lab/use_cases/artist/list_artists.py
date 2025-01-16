from abc import abstractmethod
from fastapi import Depends
from lab.repository import ArtistRepository, IArtistRepository
from lab.domain.models import Artist


class IListArtistsUseCase:
    @abstractmethod
    def execute(self, name_filter: str = "") -> list[Artist]:
        """List artists."""


class ListArtistsUseCase(IListArtistsUseCase):
    def __init__(self, repository: IArtistRepository = Depends(ArtistRepository)):
        self.repository = repository

    def execute(self, name_filter: str = "") -> list[Artist]:
        entities = self.repository.query(name_filter)
        artists = [Artist.model_validate(entity) for entity in entities]
        return artists
