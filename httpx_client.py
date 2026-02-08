import httpx
from tools.fakers import get_random_email

client = httpx.Client(
    timeout=100,
    base_url='http://localhost:8000',
)

# create user
create_user_payload = {
    "email": get_random_email(),   
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = client.post("/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)


login_payload = {
    "email": create_user_payload["email"],
    "password": "string"
}

login_response = client.post("/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()
print('Login data:', login_response_data)

auth_header = {'Authorization' : f'Bearer {login_response_data['token']['accessToken']}'}

headers=auth_header
client.headers.update(auth_header)

get_user_me_response = client.get('/api/v1/users/me')
get_user_me_response_data = get_user_me_response.json()
print('Get user me data:', get_user_me_response_data)
