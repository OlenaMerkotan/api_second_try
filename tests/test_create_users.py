from src.my_requests import MyRequests
from generator.generator import generated_person
from src.assertions import Assertion
from data.status_code import StatusCode
from src.base_page import BasePage

class TestCreateUsers(BasePage):
    assertion = Assertion
    status_code = StatusCode

    def test_create_user(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post("/users/", self.get_body(first_name, last_name, company_id))
        body = response.json()
        self.assertion.assert_body_text(response, first_name)
        assert body["last_name"] == last_name, "Last name was not created"

    def test_get_status_code_201(self):
        person_info = next(generated_person())
        first_name = person_info.first_name
        last_name = person_info.last_name
        company_id = person_info.company_id
        response = MyRequests.post("/users/", self.get_body(first_name, last_name, company_id))
        self.assertion.assert_status_code(response, self.status_code.CREATE)
