from unittest.mock import Mock
from fastapi import Depends
from lab.domain.api_models.song import CreateSong
from lab.repository import SongRepository, ISongRepository, ExternalApi, IExternalApi
from lab.use_cases.songs.create_song import CreateSongUseCase, ICreateSongUseCase
import pytest


@pytest.fixture
def create_song_use_case(
    repository: ISongRepository = SongRepository(),
    external_api: IExternalApi = Mock(spec=IExternalApi),
):
    # external_api.integrate.return_value = True
    # external_api.integrate.side_effect = Exception("Integration failed")
    return CreateSongUseCase(repository=repository, external_api=external_api)


def test_create_song(create_song_use_case: ICreateSongUseCase):

    create_song = CreateSong(
        title="Why'd You Only Call Me When You're High",
        artist_id=1,
        album="AM",
        year=2013,
    )

    result = create_song_use_case.execute(create_song)
    assert result.title == create_song.title
    assert result.album == create_song.album
    assert result.year == create_song.year
    assert result.artist_id == create_song.artist_id
    assert result.id is not None
    assert result.created_at is not None
