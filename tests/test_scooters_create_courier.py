import pytest
import allure
import string
import random
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

class TestCreateCourierAPI:

    def generate_random_string(self, length: int, charset: str = string.ascii_letters) -> str:
        return ''.join(random.choices(charset, k=length))

    @allure.feature("Создание курьера")
    @allure.story("Успешное создание курьера")
    @allure.title("Тест успешного создания курьера с валидными данными")
    def test_create_courier_success(self, api_client):
        # Генерация данных
        courier_data = {
            "login": self.generate_random_string(random.randint(2, 10), string.ascii_letters),
            "password": self.generate_random_string(4, string.digits),
            "firstName": self.generate_random_string(random.randint(2, 10), string.ascii_letters)
        }

        # Регистрация курьера
        with allure.step("Регистрация нового курьера"):
            create_response = api_client.create_courier(courier_data)
            assert create_response.status_code == 201
            assert create_response.json() == {"ok": True}

        # Авторизация и получение ID
        with allure.step("Авторизация курьера и получение ID"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            courier_id = login_response.json()["id"]

        # Сохраняем все данные для теста
        courier_info = {
            **courier_data,
            "id": courier_id
        }

        # Проверка данных 
        with allure.step("Проверка наличия ID курьера"):
            assert courier_info["id"] is not None
            assert isinstance(courier_info["id"], int)

        with allure.step("Проверка валидности созданных данных"):
            assert len(courier_info["login"]) >= 2 and len(courier_info["login"]) <= 10
            assert courier_info["login"].isalpha()
            assert len(courier_info["password"]) == 4
            assert courier_info["password"].isdigit()
            assert len(courier_info["firstName"]) >= 2 and len(courier_info["firstName"]) <= 10

        # Очистка после теста
        with allure.step("Очистка: удаление курьера после теста"):
            api_client.delete_courier(courier_id)

    @allure.feature("Создание курьера")
    @allure.story("Обработка дубликатов")
    @allure.title("Тест создания курьера с уже существующим логином (ошибка 409)")
    def test_create_duplicate_courier_error(self, api_client):
        # Генерация данных
        courier_data = {
            "login": self.generate_random_string(random.randint(2, 10), string.ascii_letters),
            "password": self.generate_random_string(4, string.digits),
            "firstName": self.generate_random_string(random.randint(2, 10), string.ascii_letters)
        }

        with allure.step("Первое создание курьера (успешно)"):
            response1 = api_client.create_courier(courier_data)
            assert response1.status_code == 201
            assert response1.json() == {"ok": True}
    
        # Авторизация и получение ID
        with allure.step("Авторизация курьера и получение ID"):
            login_response = api_client.login_courier(
                courier_data["login"],
                courier_data["password"]
            )
            courier_id = login_response.json()["id"]

        # Сохраняем все данные для теста
        courier_info = {
            **courier_data,
            "id": courier_id
        }

        # Проверка данных 
        with allure.step("Проверка наличия ID курьера"):
            assert courier_info["id"] is not None
            assert isinstance(courier_info["id"], int)

        with allure.step("Второе создание курьера с тем же логином (ожидается ошибка 409)"):
            response2 = api_client.create_courier(courier_data)
            assert response2.status_code == 409
            assert response2.json() == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}            

         # Очистка после теста
        with allure.step("Очистка: удаление курьера после теста"):
            api_client.delete_courier(courier_id)

    @allure.feature("Создание курьера")
    @allure.story("Валидация входных данных")
    @allure.title("Тест создания курьера без логина (ошибка 400)")
    def test_create_missing_login_error(self, api_client):
        invalid_courier_data = {
            "login": "",
            "password": "1234",
            "firstName": "Test"
        }

        with allure.step("Попытка создания курьера с пустым логином"):
            response = api_client.create_courier(invalid_courier_data)
            assert response.status_code == 400
            assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}

    @allure.feature("Создание курьера")
    @allure.story("Валидация входных данных")
    @allure.title("Тест создания курьера без пароля (ошибка 400)")
    def test_create_missing_password_error(self, api_client):
        invalid_courier_data = {
            "login": self.generate_random_string(random.randint(2, 10), string.ascii_letters),
            "password": "",
            "firstName": "Test"
        }

        with allure.step("Попытка создания курьера с пустым паролем"):
            response = api_client.create_courier(invalid_courier_data)
            assert response.status_code == 400
            assert response.json() == {"code": 400, "message": "Недостаточно данных для создания учетной записи"}