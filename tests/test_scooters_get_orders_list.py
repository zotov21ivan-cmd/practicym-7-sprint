import pytest
import sys
import os
import allure

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api_client.scooters_api import ScootersApiClient

from data_pak import *

class TestOrdersListAPI:
    @allure.feature("Получение списка заказов")
    @allure.story("Успешное получение общего списка заказов")
    @allure.title("Тест успешного получения общего списка заказов (статус 200)")
    def test_get_orders_list_success(self, api_client):
        with allure.step("Отправка запроса на получение общего списка заказов"):
            response = api_client.get_orders_list()

        with allure.step("Проверка статуса ответа — ожидается 200 (OK)"):
            assert response.status_code == 200

        with allure.step("Парсинг JSON-ответа"):
            response_data = response.json()

        with allure.step("Проверка типа ответа — ожидается словарь (dict)"):
            assert isinstance(response_data, dict)

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=response.text,
                name="Полный ответ API (список заказов)",
                attachment_type=allure.attachment_type.JSON
            )

    @allure.feature("Получение списка заказов")
    @allure.story("Успешное получение списка заказов курьера")
    @allure.title("Тест успешного получения списка заказов конкретного курьера (статус 200)")
    def test_get_orders_list_courier_success(self, api_client):
        with allure.step(f"Отправка запроса на получение списка заказов для курьера ID: {VALID_LOGIN_DATA['id']}"):
            response = api_client.get_orders_list_courier(VALID_LOGIN_DATA["id"])

        with allure.step("Проверка статуса ответа — ожидается 200 (OK)"):
            assert response.status_code == 200

        with allure.step("Парсинг JSON-ответа"):
            response_data = response.json()

        with allure.step("Проверка типа ответа — ожидается словарь (dict)"):
            assert isinstance(response_data, dict)

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=f"ID курьера: {VALID_LOGIN_DATA['id']}",
                name="Параметры запроса",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API (список заказов курьера)",
                attachment_type=allure.attachment_type.JSON
            )

    @allure.feature("Получение списка заказов")
    @allure.story("Обработка ошибки при получении списка заказов несуществующего курьера")
    @allure.title("Тест получения списка заказов для несуществующего курьера (ошибка 404)")
    def test_get_orders_list_courier_not_found_error(self, api_client):
        message_invalid = f"Курьер с идентификатором {str(INVALID_LOGIN_DATA_4['id'])} не найден"

        with allure.step(f"Попытка получить список заказов для несуществующего курьера ID: {INVALID_LOGIN_DATA_4['id']}"):
            response = api_client.get_orders_list_courier(INVALID_LOGIN_DATA_4["id"])

        with allure.step("Проверка статуса ответа — ожидается 404 (Not Found)"):
            assert response.status_code == 404

        with allure.step("Парсинг JSON-ответа с ошибкой"):
            response_data = response.json()

        with allure.step("Проверка наличия поля 'message' в ответе с ошибкой"):
            assert "message" in response_data

        with allure.step("Проверка текста сообщения об ошибке"):
            assert response_data["message"] == message_invalid

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=f"ID несуществующего курьера: {INVALID_LOGIN_DATA_4['id']}",
                name="Параметры ошибочного запроса",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API (ошибка 404)",
                attachment_type=allure.attachment_type.JSON
            )