import pytest
import allure
from api_client import ScooterApi

class TestCourierLogin:
    api = ScooterApi()

    @allure.title("Успешная авторизация курьера")
    @allure.description("Проверка, что курьер может авторизоваться и получает id")
    def test_login_success(self):
        # Данные существующего курьера (предположим, он создан заранее)
        payload = {"login": "test_alex_001", "password": "password123"}
        response = self.api.login_courier(payload)
        
        assert response.status_code == 200
        assert "id" in response.json()
        assert isinstance(response.json()["id"], int)

    @allure.title("Ошибка при отсутствии обязательного поля")
    @pytest.mark.parametrize("payload, missing_field", [
        ({"password": "password123"}, "login"),
        ({"login": "test_alex_001"}, "password")
    ])
    def test_login_missing_field_error(self, payload, missing_field):
        response = self.api.login_courier(payload)
        
        assert response.status_code == 400
        assert response.json()["message"] == "Недостаточно данных для входа"

    @allure.title("Ошибка при вводе неверного логина или пароля")
    @pytest.mark.parametrize("wrong_payload", [
        {"login": "test_alex_001", "password": "wrong_password"}, # неверный пароль
        {"login": "wrong_login_999", "password": "password123"}   
    ])
    def test_login_invalid_credentials_error(self, wrong_payload):
        response = self.api.login_courier(wrong_payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"

    @allure.title("Авторизация под несуществующим пользователем")
    def test_login_non_existent_user_error(self):
        payload = {"login": "non_existent_user_000000", "password": "some_password"}
        response = self.api.login_courier(payload)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Учетная запись не найдена"