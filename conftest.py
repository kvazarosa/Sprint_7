import pytest
from methods.courier_methods import CourierMethods


@pytest.fixture
def new_courier():
    courier_api = CourierMethods()
    courier_data = courier_api.register_new_courier()

    if not courier_data:
        pytest.fail("Не удалось создать тестового курьера")

    yield courier_data

    login_response = courier_api.login_courier(
        courier_data['login'],
        courier_data['password']
    )
    if login_response.status_code == 200:
        courier_id = login_response.json().get('id')
        if courier_id:
            courier_api.delete_courier(courier_id)
