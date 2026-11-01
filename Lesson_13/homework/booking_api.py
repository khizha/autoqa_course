import requests


class BookingApi:

    def __init__(self):
        self.url = "https://restful-booker.herokuapp.com"

    def create_booking(self, booking_data):
        return requests.post(
            f"{self.url}/booking",
            json=booking_data
        )

    def get_booking(self, booking_id):
        return requests.get(
            f"{self.url}/booking/{booking_id}"
        )

    def update_booking(self, booking_id, booking_data, token):
        headers = {
            "Cookie": f"token={token}"
        }

        return requests.patch(
            f"{self.url}/booking/{booking_id}",
            json=booking_data,
            headers=headers
        )

    def get_token(self):
        auth_data = {
            "username": "admin",
            "password": "password123"
        }

        return requests.post(
            f"{self.url}/auth",
            json=auth_data
        )