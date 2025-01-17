from abc import ABC, abstractmethod
from lab.repository import models


class IExternalApi(ABC):
    @abstractmethod
    def integrate(self, song: models.SongEntity) -> None:
        """Integrate new song"""


class ExternalApi(IExternalApi):
    def integrate(self, song: models.SongEntity) -> None:
        """Integrate new song"""
        print(f"Integrating song: {song.title}")
        return True
