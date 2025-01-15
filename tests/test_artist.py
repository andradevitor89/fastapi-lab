# from http import HTTPStatus

# from fastapi.testclient import TestClient

# from main import app


# ROUTER_PATH = "/artist"


# def test_create_and_get_artist_should_succeed():
#     client = TestClient(app)

#     old_get_artists_response = client.get(ROUTER_PATH)
#     assert old_get_artists_response.status_code == HTTPStatus.OK
#     old_artists_count = len(old_get_artists_response.json())

#     create_artist_response = client.post(
#         ROUTER_PATH, json={"country": "UK", "name": "Arctic Monkeys"}
#     )
#     assert create_artist_response.status_code == HTTPStatus.CREATED

#     new_get_artists_response = client.get(ROUTER_PATH)
#     assert new_get_artists_response.status_code == HTTPStatus.OK
#     new_artists_count = len(new_get_artists_response.json())

#     assert new_artists_count == old_artists_count + 1
