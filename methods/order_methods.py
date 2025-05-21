import requests
from data import BASE_URL, ORDERS_URL
import allure


class OrderMethods:
    @allure.step("Создание заказа")
    def create_order(self, color=None):
        order_data = {
            "firstName": "Тест",
            "lastName": "Тестов",
            "address": "Москва",
            "metroStation": 4,
            "phone": "+79991112233",
            "rentTime": 1,
            "deliveryDate": "2023-12-31"
        }
        if color:
            order_data["color"] = color
        return requests.post(f"{BASE_URL}{ORDERS_URL}", json=order_data)

    @allure.step("Получение заказа")
    def get_orders(self):
        return requests.get(f"{BASE_URL}{ORDERS_URL}")
