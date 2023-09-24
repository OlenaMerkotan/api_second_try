import requests
from requests import Response

class Assertion:

    def assert_status_code(self, response: Response, expected_status_code: int):
        actual_status_code = response.status_code
        assert actual_status_code == expected_status_code, \
            f"Unexpected status code. Expected: {expected_status_code}, Actual: {actual_status_code}"

    def assert_body_text(self, response: Response, expected_text: str):
        actual_text = response.json()
        assert actual_text["first_name"] == expected_text

