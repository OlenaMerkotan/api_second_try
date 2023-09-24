# import json
# import os
# import pytest
# import requests
# from data.urls import Urls
# from generator.generator import generated_person
#
# @pytest.fixture(scope="function")
# def prepare_user_in_active_company():
#     person_info = next(generated_person())
#     first_name = person_info.first_name
#     last_name = person_info.last_name
#     company_id = person_info.company_id
#     body = {
#         "firts_name": first_name,
#         "last_name": last_name,
#         "company_id": company_id
#     }
#
#     print(body)
#     return body

