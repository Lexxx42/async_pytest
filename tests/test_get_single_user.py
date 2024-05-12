from fastapi.testclient import TestClient

from application.endpoints import app
from dto.error_dto import ErrorDto
from dto.get_single_user_dto import GetSingleUserDto

client = TestClient(app)


def test_single_user_valid_user():
    response = client.get(url="/api/users/1", headers={"X-Token": "sun_of_the_beach"})
    assert response.status_code == 200
    model = GetSingleUserDto.model_validate(response.json())
    assert model.data.id == 1


def test_single_user_no_such_user():
    response = client.get(url="/api/users/-150", headers={"X-Token": "sun_of_the_beach"})
    assert response.status_code == 404
    ErrorDto.model_validate(response.json())


def test_single_user_invalid_token():
    response = client.get(url="/api/users/1", headers={"X-Token": "hello world!"})
    assert response.status_code == 400
    ErrorDto.model_validate(response.json())
