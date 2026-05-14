# import httpx
# from tools.fakers import get_random_email
#
# create_user_payload = {
#   "email": get_random_email(),
#   "password": "string",
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }
#
# create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
# create_user_response_data = create_user_response.json()
#
# print(f"Create user data: {create_user_response_data}")
# print(create_user_response.status_code)
#
# #############
#
# login_payload = {
#     "email": create_user_payload["email"],
#     "password": create_user_payload["password"]
# }
#
# login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
# login_response_data = login_response.json()
# print(f"Login data: {login_response_data}")
#
# ###########
# update_user_headers = {
#     "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
# }
#
# update_user_payload = {
#   "email": get_random_email(),
#   "lastName": "string",
#   "firstName": "string",
#   "middleName": "string"
# }
#
# update_response = httpx.patch(
#     f"http://localhost:8000/api/v1/users/{create_user_response_data["user"]["id"]}",
#     json=update_user_payload,
#     headers=update_user_headers
# )
# update_response_data = update_response.json()
# print(update_response.status_code)

# import json
#
# my_json = """
# [
#   {
#     "manager": {"first_name": "Dasi", "last_name": "Ungerer"},
#     "cars": [
#       {"maker": "Audi", "model": "100", "year": 1993, "price": 3504},
#       {"maker": "Ford", "model": "F-Series", "year": 1997, "price": 14382}
#     ]
#   },
#   {
#     "manager": {"first_name": "Wendell", "last_name": "Fortescue"},
#     "cars": [
#       {"maker": "BMW", "model": "5 Series", "year": 1999, "price": 11585},
#       {"maker": "Honda", "model": "CR-V", "year": 2004, "price": 13680}
#     ]
#   }
# ]
# """
#
# best_manager = {}
#
# sellers_data = json.loads(my_json)
# for manager in sellers_data:
#     print(manager[])


# напишите декторатор, который увеличивает аргумент с на 1

from typing import Callable
import time

def param_timer_deco(func: Callable):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        stop = time.time()
        print(stop - start)
        return res
    return wrapper

@param_timer_deco
def my_func(sleep_time: int):
    time.sleep(sleep_time)
    return(123)

print(my_func(5))