import pytest
import allure
from api_client import ScooterApi

class TestDeleteCourier:
    api = ScooterApi()

    @allure.title("Успешное удаление курьера")
    def test_delete_courier_success(self):
        # 1. Создаем курьера, чтобы было кого удалять
        payload = {"login": "to_be_deleted", "password": "123", "firstName": "Ivan"}
        self.api.create_courier(payload)
        
        login_response = self.api.login_courier({"login": "to_be_deleted", "password": "123"})
        courier_id = login_response.json()["id"]

        response = self.api.delete_courier(courier_id)
        
        assert response.status_code == 200
        assert response.json() == {"ok": True}

    @allure.title("Ошибка при удалении без id")
    def test_delete_courier_without_id_error(self):
        response = self.api.delete_courier(None)
        
        assert response.status_code == 400 or response.status_code == 404
        assert response.json()["message"] == "Недостаточно данных для удаления курьера"

    @allure.title("Ошибка при удалении несуществующего курьера")
    def test_delete_non_existent_courier_error(self):
        non_existent_id = 999999
        response = self.api.delete_courier(non_existent_id)
        
        assert response.status_code == 404
        assert response.json()["message"] == "Курьера с таким id нет"

    @allure.title("Неуспешный запрос возвращает ошибку (неверный формат id)")
    def test_delete_courier_invalid_id_type_error(self):
        invalid_id = "abc" 
        response = self.api.delete_courier(invalid_id)

        assert response.status_code != 200
        assert "message" in response.json()
