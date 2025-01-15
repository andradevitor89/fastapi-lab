from http import HTTPStatus

from fastapi.testclient import TestClient

from main import app


ROUTER_PATH = "/song"


def test_create_and_get_song_should_succeed():
    client = TestClient(app)

    artists_count_old = len(client.get("/artist").json())

    create_artist_response = client.post(
        "/artist", json={"country": "UK", "name": "Arctic Monkeys"}
    )
    assert create_artist_response.status_code == HTTPStatus.CREATED
    artists_count_new = len(client.get("/artist").json())
    assert artists_count_new == artists_count_old + 1

    artist_id = create_artist_response.json()["id"]

    songs_count_old = len(client.get(ROUTER_PATH).json())
    create_song_response = client.post(
        ROUTER_PATH,
        json={
            "album": "The Car",
            "artist_id": artist_id,
            "title": "There'd Better Be A Mirroball",
            "year": 2022,
        },
    )
    assert create_song_response.status_code == HTTPStatus.CREATED
    songs_count_new = len(client.get(ROUTER_PATH).json())
    assert songs_count_new == songs_count_old + 1
