import pytest
import allure
from api_client import ScooterApi

class TestCreateCourier:
    api = ScooterApi()

    @allure.title("Проверка создания курьера и ответа {ok: True}")
    def test_create_courier_success(self):
        payload = {"login": "test_alex_001", "password": "password123", "firstName": "Alex"}
        response = self.api.create_courier(payload)
        assert response.status_code == 201
        assert response.json() == {"ok": True}

    @allure.title("Нельзя создать двух одинаковых курьеров")
    def test_create_duplicate_courier_error(self):
        payload = {"login": "unique_user", "password": "123", "firstName": "Ivan"}
        self.api.create_courier(payload)
        response = self.api.create_courier(payload)
        assert response.status_code == 409
        assert "Этот логин уже используется" in response.json()['message']

    @allure.title("Ошибка при отсутствии обязательного поля (логин)")
    def test_create_courier_without_login_error(self):
        payload = {"password": "123", "firstName": "Ivan"}
        response = self.api.create_courier(payload)
        assert response.status_code == 400
        assert response.json()['message'] == "Недостаточно данных для создания учетной записи"
