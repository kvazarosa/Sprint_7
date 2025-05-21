import pytest
from methods.order_methods import OrderMethods
import allure


@allure.title("Тесты заказов")
class TestOrder:
    @pytest.mark.parametrize('color', [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        None
    ])

    @allure.title("Проверка создания заказа с разными цветами")
    @allure.description("Проверка создания заказа с разными цветами")
    def test_create_order(self, color):
        order_api = OrderMethods()
        response = order_api.create_order(color)
        assert response.status_code == 201
        assert 'track' in response.json()

    @allure.title("Проверка получения списка заказов")
    @allure.description("Проверка получения списка заказов")
    def test_get_orders(self):
        order_api = OrderMethods()
        response = order_api.get_orders()
        assert response.status_code == 200
        assert 'orders' in response.json()
