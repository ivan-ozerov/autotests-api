import httpx

host = "http://localhost:8000/"

auth_payload = {"email": "ivanozer@yandex.ru", "password": "patrick_star"}


auth_response = httpx.post(host + "api/v1/authentication/login", json=auth_payload)

auth_response_json = auth_response.json()

print("\nauth response body: ", auth_response_json, end="\n\n")
print("auth status code: ", auth_response.status_code, end="\n\n\n")

me_headers = {"Authorization": f"Bearer {auth_response.json()['token']['accessToken']}"}

me_response = httpx.get(host + "api/v1/users/me", headers=me_headers)

me_response_json = me_response.json()

print("me response body: ", me_response_json, end='\n\n')
print("me status code: ", me_response.status_code, end="\n\n")
