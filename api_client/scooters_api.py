import requests
import allure

from curl import BASE_URL

class ScootersApiClient:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json"
        })

    @allure.step("Создание курьера через API")
    def create_courier(self, payload: dict) -> requests.Response:
        response = self.session.post(
            url=f"{BASE_URL}/api/v1/courier",
            json=payload
        )
        return response

    @allure.step("Авторизация курьера и получение его ID")
    def login_courier(self, login: str, password: str) -> requests.Response:
        response = self.session.post(
            url=f"{BASE_URL}/api/v1/courier/login",
            json={
                "login": login,
                "password": password
            }
        )
        return response

    @allure.step("Удаление курьера через API")
    def delete_courier(self, courier_id: int) -> requests.Response:
        response = self.session.delete(
            url=f"{BASE_URL}/api/v1/courier/{courier_id}"
        )
        response.raise_for_status()
        return response

    @allure.step("Создание заказа через API")
    def create_order(self, payload: dict) -> requests.Response:
        response = self.session.post(
            url=f"{BASE_URL}/api/v1/orders",
            json=payload
        )
        return response
    
    @allure.step("Получение заказа по трек-номеру")
    def get_order_by_track(self, track_number: int) -> requests.Response:
        response = self.session.get(
            url=f"{BASE_URL}/api/v1/orders/track?t={track_number}"
        )
        response.raise_for_status()
        return response

    @allure.step("Получение списка заказов курьера")   
    def get_orders_list_courier(self, courier_id: int) -> requests.Response:
        response = self.session.get(
            url=f"{BASE_URL}/api/v1/orders?courierId={courier_id}"
        )
        return response

    @allure.step("Получение списка заказов")    
    def get_orders_list(self) -> requests.Response:
        response = self.session.get(
            url=f"{BASE_URL}/api/v1/orders"
        )
        return response