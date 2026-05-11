import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")
print(response.status_code)
print(response.json())


data = {
    "title": "Новая задача 1",
    "completed": False,
    "userID": 1
}

response = httpx.post("https://jsonplaceholder.typicode.com/todos", json=data)

print(response.status_code)
# print(response.request.headers)
print(response.json())

data = {"username": "new_user", "password": "123456"}
response = httpx.post("https://httpbin.org/post", data=data)

print(response.status_code)
# print(response.request.headers)
print(response.json())

headers = {"Authorization": "Bearer my_secret_token"}
response = httpx.get("https://httpbin.org/get", headers=headers)
print(response.status_code)
print(response.request.headers)

params = {"userID": 1}
response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
print(response.url)
print(response.json())

file = {"file": ("example.txt", open("example.txt", "rb"))}
response = httpx.post("https://httpbin.org/post", files=file)
print(response.json())
print(response.status_code)


with httpx.Client() as client:
    response_client_1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
    response_client_2 = client.get("https://jsonplaceholder.typicode.com/todos/2")

print(response_client_1.json())
print(response_client_2.json())