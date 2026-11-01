from booking_api import BookingApi


def test_create_booking(booking_data):
    api = BookingApi()

    response = api.create_booking(booking_data)

    assert response.status_code == 200

    response_data = response.json()

    assert "bookingid" in response_data
    assert response_data["booking"]["firstname"] == "John"
    assert response_data["booking"]["lastname"] == "Doe"


def test_get_booking(booking_data):
    api = BookingApi()

    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]

    response = api.get_booking(booking_id)

    assert response.status_code == 200

    response_data = response.json()

    assert response_data["firstname"] == "John"
    assert response_data["lastname"] == "Doe"
    assert response_data["totalprice"] == 100


def test_update_booking(booking_data):
    api = BookingApi()

    # Получаем токен
    token_response = api.get_token()
    token = token_response.json()["token"]

    # Создаём бронирование
    create_response = api.create_booking(booking_data)
    booking_id = create_response.json()["bookingid"]

    # Изменяем только имя
    update_data = {
        "firstname": "Alex"
    }

    response = api.update_booking(booking_id, update_data, token)

    assert response.status_code == 200

    # Проверяем результат изменения
    get_response = api.get_booking(booking_id)
    response_data = get_response.json()

    assert response_data["firstname"] == "Alex"
    assert response_data["lastname"] == "Doe"


def test_get_booking_not_found():
    api = BookingApi()

    response = api.get_booking(999999999)

    assert response.status_code == 404