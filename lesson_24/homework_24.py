import requests
from lesson_24.data_logger import log


class TestRequests:
    def __init__(self):
        self.auth_url = 'http://127.0.0.1:8080/auth'
        self.cars_url = 'http://127.0.0.1:8080/cars'
        self.username = 'test_user'
        self.password = 'test_pass'
        self.token = None
        self.log = log

    def test_auth(self, username=None, password=None):
        self.log.info(f'\n___________________start test_auth___________________\n')
        if username is None:
            username = self.username
        if password is None:
            password = self.password
        try:
            auth_response = requests.post(self.auth_url, auth=(username, password))
            self.log.info(
                f"Send request to {self.auth_url} with username: {self.username} and password: {self.password}."
                f"Response status code: {auth_response.status_code}. Response body: {auth_response.text}")
            if auth_response.status_code == 200:
                if 'access_token' in auth_response.json().keys():
                    self.token = auth_response.json()['access_token']
                    self.log.info(f"Access token: {self.token}. Return: True")
                    return True
                self.log.info(f"Access token not found. Return: False")
                return False
            else:
                self.log.info(f"Return: False")
                return False
        except Exception as e:
            self.log.error(f"Request error: {e}")

    def test_cars(self, **kwargs):
        self.log.info(f'\n___________________start test_cars___________________\n')
        headers = {
            'Authorization': f'Bearer {self.token}'
        }
        try:
            cars_response = requests.get(self.cars_url, headers=headers, params=kwargs)
            self.log.info(f"Send request to {self.cars_url} with params: {kwargs}. Response status code: {cars_response.status_code}. Response body: {cars_response.text}")
            if cars_response.status_code == 200:
                cars_data = cars_response.json()
                self.log.info(f"Return: {cars_data}, 'Status code': {cars_response.status_code}")
                return {'cars': cars_data, 'status_code': cars_response.status_code}
            else:
                self.log.info(f"Return: status code: {cars_response.status_code}")
                return {'status_code': cars_response.status_code}
        except Exception as e:
            self.log.error(f"Request error: {e}")