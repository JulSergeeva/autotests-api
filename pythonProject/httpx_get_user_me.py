import httpx

login_payload = {
  "email": "user@example.com",
  "password": "string"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
json_login_response = login_response.json()

print(f"Login_json{json_login_response}")
print(login_response.status_code)


get_headers = {"Authorization": f"Bearer {json_login_response["token"]["refreshToken"]}"}
get_me_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=get_headers)
json_get_me_response = get_me_response.json()

print(json_get_me_response)
print(get_me_response.status_code)