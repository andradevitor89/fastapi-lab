from abc import ABC, abstractmethod
from fastapi import Depends
from lab.repository import ArtistRepository, IArtistRepository
from lab.domain import api_models
from lab.repository.models import ArtistEntity
from lab.domain.models import Artist


class ICreateArtistUseCase(ABC):
    @abstractmethod
    def execute(self, create_artist: api_models.CreateArtist) -> Artist:
        """Create an artist."""


class CreateArtistUseCase(ICreateArtistUseCase):
    def __init__(self, repository: IArtistRepository = Depends(ArtistRepository)):
        self.repository = repository

    def execute(self, create_artist: api_models.CreateArtist) -> Artist:
        entity = ArtistEntity(name=create_artist.name, country=create_artist.country)
        entity = self.repository.create(entity)
        artist = Artist.model_validate(entity)
        return artist
