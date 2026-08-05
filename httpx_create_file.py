import httpx
from tools.fakers import fake

create_user_payload = {
  "email": fake.email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

#########
login_payload = {
    "email": create_user_payload["email"],
    "password": create_user_payload["password"]
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print(login_response_data)

#########
create_file_headers = {
    "Authorization": f"Bearer {login_response_data["token"]["accessToken"]}"
}

file_path = "./testdata/files/image.png"
with open(file_path, "rb") as file:
    create_file_response = httpx.post(
        "http://localhost:8000/api/v1/files",
        data = {"filename": "image.png", "directory": "courses"},
        files = {"upload_file": file},
        headers = create_file_headers
    )

create_file_response_data = create_file_response.json()
print(f"create_file_response_data: {create_file_response_data}")
