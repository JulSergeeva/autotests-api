import httpx
from tools.fakers import get_random_email

create_user_payload = {
  "email": get_random_email(),
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}

response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)

print(response.json())
print(response.status_code)