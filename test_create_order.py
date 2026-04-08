import pytest
import allure
from api_client import ScooterApi

class TestCreateOrder:
    api = ScooterApi()

    @allure.title("Создание заказа с выбором цвета")
    @pytest.mark.parametrize("color", [
        (["BLACK"]), 
        (["GREY"]), 
        (["BLACK", "GREY"]), 
        ([])
    ])
    def test_create_order_colors(self, color):
        payload = {
            "firstName": "Naruto",
            "lastName": "Uchiha",
            "address": "Konoha, 142 apt.",
            "metroStation": 4,
            "phone": "+7 800 355 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-06",
            "comment": "Saske, come back!",
            "color": color
        }
        response = self.api.create_order(payload)
        assert response.status_code == 201
        assert "track" in response.json()
