import pytest
from pprint import pprint
from data.data_files import StatusCompanies
from src.my_requests import MyRequests

class TestStatusCompanies:
    status_list = StatusCompanies.status_list
    request = MyRequests()

    @pytest.mark.parametrize("status", status_list)
    def test_get_status_companies(self, status):
        response = self.request.get(f"/companies/?status={status}&limit=3&offset=0")
        assert response.status_code == 200, f"Status code in not 200, it is {response.status_code}"
        # response1 = requests.get(f"""{base_url}/?status=ACTIVE&limit=3&offset=1""")
        pprint(response.headers)
        # pprint(response.json())

    @pytest.mark.parametrize("status", status_list)
    def test_get_closed_companies(self, status):
        response = self.request.get(f"/?status={status}&limit=3&offset=0")
        items_list = response.json()["data"]
        # print(items_list)
        # print(len(items_list))
        for item in items_list:
            assert item["company_status"] == status
        # print(response.json()["data"][0]["company_status"])


