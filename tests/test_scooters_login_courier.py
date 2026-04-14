import pytest
import sys
import os
import allure

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from api_client.scooters_api import ScootersApiClient

from data_pak import *

class TestCourierAuth:
    @allure.feature("Авторизация курьера")
    @allure.story("Успешная авторизация")
    @allure.title("Тест успешной авторизации курьера с валидными данными (статус 200)")
    def test_login_success(self, api_client):
        with allure.step(f"Отправка запроса на авторизацию курьера (логин: {VALID_LOGIN_DATA['login']})"):
            response = api_client.login_courier(
                VALID_LOGIN_DATA["login"],
                VALID_LOGIN_DATA["password"]
            )

        with allure.step("Проверка статуса ответа — ожидается 200 (OK)"):
            assert response.status_code == 200

        with allure.step("Парсинг JSON-ответа"):
            response_data = response.json()
            courier_id = response_data["id"]

        with allure.step("Проверка наличия ID курьера в ответе"):
            assert "id" in response_data

        with allure.step("Проверка типа ID курьера — ожидается целое число"):
            assert isinstance(response_data["id"], int)

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=f"Логин: {VALID_LOGIN_DATA['login']}\nПароль: {VALID_LOGIN_DATA['password']}",
                name="Данные для авторизации",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API (успешная авторизация)",
                attachment_type=allure.attachment_type.JSON
            )

    @allure.feature("Авторизация курьера")
    @allure.story("Обработка ошибки авторизации")
    @allure.title("Тест авторизации с несуществующей учётной записью (ошибка 404)")
    def test_login_account_not_found_error(self, api_client):
        with allure.step(f"Попытка авторизации с несуществующими данными (логин: {INVALID_LOGIN_DATA_1['login']})"):
            response = api_client.login_courier(
                INVALID_LOGIN_DATA_1["login"],
                INVALID_LOGIN_DATA_1["password"]
            )

        with allure.step("Проверка статуса ответа — ожидается 404 (Not Found)"):
            assert response.status_code == 404

        with allure.step("Парсинг JSON-ответа с ошибкой"):
            response_data = response.json()

        with allure.step("Проверка наличия поля 'message' в ответе с ошибкой"):
            assert "message" in response_data

        with allure.step("Проверка текста сообщения об ошибке"):
            assert response_data["message"] == "Учетная запись не найдена"

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=f"Логин: {INVALID_LOGIN_DATA_1['login']}\nПароль: {INVALID_LOGIN_DATA_1['password']}",
                name="Неверные данные для авторизации",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API (ошибка 404)",
                attachment_type=allure.attachment_type.JSON
            )

    @allure.feature("Авторизация курьера")
    @allure.story("Обработка ошибок валидации")
    @allure.title("Тест авторизации без пароля (ошибка 400)")
    def test_login_missing_password_error(self, api_client):
        with allure.step(f"Попытка авторизации без пароля (логин: {INVALID_LOGIN_DATA_2['login']})"):
            response = api_client.login_courier(
                INVALID_LOGIN_DATA_2["login"],
                INVALID_LOGIN_DATA_2["password"]
            )

        with allure.step("Проверка статуса ответа — ожидается 400 (Bad Request)"):
            assert response.status_code == 400

        with allure.step("Парсинг JSON-ответа с ошибкой"):
            response_data = response.json()

        with allure.step("Проверка наличия поля 'message' в ответе с ошибкой"):
            assert "message" in response_data

        with allure.step("Проверка текста сообщения об ошибке"):
            assert response_data["message"] == "Недостаточно данных для входа"

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=f"Логин: {INVALID_LOGIN_DATA_2['login']}\nПароль: {INVALID_LOGIN_DATA_2['password']}",
                name="Неполные данные для авторизации (отсутствует пароль)",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API (ошибка 400 — отсутствует пароль)",
                attachment_type=allure.attachment_type.JSON
            )

    @allure.feature("Авторизация курьера")
    @allure.story("Обработка ошибок валидации")
    @allure.title("Тест авторизации без логина (ошибка 400)")
    def test_login_missing_login_error(self, api_client):
        with allure.step("Попытка авторизации без логина"):
            response = api_client.login_courier(
                INVALID_LOGIN_DATA_3["login"],
                INVALID_LOGIN_DATA_3["password"]
            )

        with allure.step("Проверка статуса ответа — ожидается 400 (Bad Request)"):
            assert response.status_code == 400

        with allure.step("Парсинг JSON-ответа с ошибкой"):
            response_data = response.json()

        with allure.step("Проверка наличия поля 'message' в ответе с ошибкой"):
            assert "message" in response_data

        with allure.step("Проверка текста сообщения об ошибке"):
            assert response_data["message"] == "Недостаточно данных для входа"

        with allure.step("Дополнительная информация в отчёте"):
            allure.attach(
                body=f"Логин: {INVALID_LOGIN_DATA_3['login']}\nПароль: {INVALID_LOGIN_DATA_3['password']}",
                name="Неполные данные для авторизации (отсутствует логин)",
                attachment_type=allure.attachment_type.TEXT
            )
            allure.attach(
                body=response.text,
                name="Полный ответ API (ошибка 400 — отсутствует логин)",
                attachment_type=allure.attachment_type.JSON
            )