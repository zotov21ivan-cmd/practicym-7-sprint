import pytest
import sys
import os
import allure

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api_client.scooters_api import ScootersApiClient
from data_pak import *

class TestOrderAPI:
    @allure.feature("Создание заказа")
    @allure.story("Успешное создание заказа с валидными данными")
    @pytest.mark.parametrize("test_data", [
        VALID_ORDER_DATA_SET_1,
        VALID_ORDER_DATA_SET_2,
        VALID_ORDER_DATA_SET_3,
        VALID_ORDER_DATA_SET_4,
    ])
    @allure.title("Тест успешного создания заказа (набор данных: {test_data})")
    def test_create_order_success(self, api_client, test_data):
        with allure.step("Отправка запроса на создание заказа с валидными данными"):
            response = api_client.create_order(test_data)

        with allure.step("Проверка статуса ответа — ожидается 201 (Created)"):
            assert response.status_code == 201

        with allure.step("Парсинг JSON-ответа"):
            response_data = response.json()
            track = response.json()["track"]

        with allure.step("Проверка наличия поля 'track' в ответе"):
            assert "track" in response_data

        with allure.step("Проверка типа поля 'track' — ожидается целое число"):
            assert isinstance(response_data["track"], int)

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=str(test_data),
                name="Отправленные данные заказа",
                attachment_type=allure.attachment_type.JSON
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API",
                attachment_type=allure.attachment_type.JSON
            )