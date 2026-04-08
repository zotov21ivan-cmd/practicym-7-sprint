import requests
import allure
from BASE_URL import BASE_URL
class ScooterApi:
    @allure.step("Создание курьера")
    def create_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/api/v1/courier", json=payload)

    @allure.step("Логин курьера")
    def login_courier(self, payload):
        return requests.post(f"{self.BASE_URL}/api/v1/courier/login", json=payload)

    @allure.step("Создание заказа")
    def create_order(self, payload):
        return requests.post(f"{self.BASE_URL}/api/v1/orders", json=payload)

    @allure.step("Получение списка заказов")
    def get_orders_list(self):
        return requests.get(f"{self.BASE_URL}/api/v1/orders")
