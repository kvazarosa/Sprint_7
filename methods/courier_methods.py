import requests
import random
import string
from data import BASE_URL, COURIERS_URL, LOGIN_URL
import allure


class CourierMethods:
    @staticmethod
    @allure.step("Генерация случайной строки")
    def generate_random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @allure.step("Регистрация нового курьера")
    def register_new_courier(self):
        login = self.generate_random_string()
        password = self.generate_random_string()
        first_name = self.generate_random_string()

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(f"{BASE_URL}{COURIERS_URL}", json=payload)

        if response.status_code == 201:
            return {
                'login': login,
                'password': password,
                'first_name': first_name,
                'response': response
            }
        return None

    @allure.step("Авторизация курьера")
    def login_courier(self, login, password):
        return requests.post(f"{BASE_URL}{LOGIN_URL}", json={"login": login, "password": password})

    @allure.step("Удаление курьера")
    def delete_courier(self, courier_id):
        return requests.delete(f"{BASE_URL}{COURIERS_URL}/{courier_id}")
