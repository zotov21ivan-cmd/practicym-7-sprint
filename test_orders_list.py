import allure
from api_client import ScooterApi

@allure.title("Проверка получения списка заказов")
def test_get_orders_list():
    api = ScooterApi()
    response = api.get_orders_list()
    assert response.status_code == 200
    assert isinstance(response.json().get("orders"), list)
