import pytest
import requests
from data import BASE_URL, COURIERS_URL, LOGIN_URL
import allure


class TestCourier:
    @allure.step('Создаем курьера')
    def test_create_success(self, new_courier):
        assert new_courier['response'].status_code == 201
        assert new_courier['response'].json() == {"ok": True}

    @allure.step('Проверка дублирования курьера')
    def test_duplicate_courier(self, new_courier):
        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json={
                "login": new_courier['login'],
                "password": new_courier['password'],
                "firstName": new_courier['first_name']
            }
        )
        assert response.status_code == 409

    @allure.step('Проверка обязательных полей')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_missing_field(self, field):
        payload = {
            "login": "test",
            "password": "test",
            "firstName": "test"
        }
        del payload[field]

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)
        assert response.status_code == 400

    @allure.step('Проверка успешной авторизации')
    def test_login_success(self, new_courier):
        response = requests.post(f"{BASE_URL}{LOGIN_URL}", json={
                "login": new_courier['login'],
                "password": new_courier['password']}
        )
        assert response.status_code == 200
        assert 'id' in response.json()

    @allure.step('Проверка неверных учетных данных')
    def test_login_wrong_credentials(self, new_courier):
        response = requests.post(f"{BASE_URL}{LOGIN_URL}", json={
                "login": new_courier['login'],
                "password": "wrong_password"}
        )
        assert response.status_code == 404

    @allure.step('Проверка отсутствия поля при авторизации')
    def test_login_missing_field(self):
        response = requests.post(f"{BASE_URL}{LOGIN_URL}", json={"login": "only_login"})
        assert response.status_code in [400, 404, 504]

    @allure.step('Проверка несуществующего пользователя')
    def test_login_nonexistent_user(self):
        response = requests.post(f"{BASE_URL}{LOGIN_URL}", json={
                "login": "nonexistent_user_123",
                "password": "any_password"}
        )
        assert response.status_code == 404
