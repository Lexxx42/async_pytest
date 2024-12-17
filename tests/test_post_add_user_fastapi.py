from fastapi.testclient import TestClient

from application import FAKE_SECRET_TOKEN, app
from dto import UserCreation
from dto.error_dto import ErrorDto
from dto.get_single_user_dto import GetSingleUserDto

client = TestClient(app)


def test_post_users_fastapi():
    response = client.post(
        url="/routers/users",
        headers={"X-Token": FAKE_SECRET_TOKEN},
        json=UserCreation(
            email="kevin@gmail.com",
            first_name="Kevin",
            last_name="Kim",
            avatar="https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        ).model_dump(mode="json"),
    )
    assert response.status_code == 201
    GetSingleUserDto.model_validate(response.json())


def test_post_users_fastapi_negative():
    response = client.post(
        url="/routers/users",
        headers={"X-Token": FAKE_SECRET_TOKEN},
        json={
            "email": "kevin@gmail.com",
            "first_name": "AVas",
            "avatar": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        },
    )
    assert response.status_code == 422
    ErrorDto.model_validate(response.json())
