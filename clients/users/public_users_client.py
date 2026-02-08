from typing import TypedDict
from httpx import Response
from clients.api_client import APIClient
from clients.public_http_builder import get_public_http_client

class User(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str

class CreateUserResponseDict(TypedDict):
    user: User

class CreateUserRequestDict(TypedDict):
    """
    Описание структуры запроса для создания пользователя
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str

class PublicUsersClient(APIClient):
    """
    Клиент для публичных запросов к /api/v1/users
    """
    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        """
        Метод создает пользователя
        
        :param request: Словарь с email, password, lastName, firstName, middleName
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/users", json=request)
    
    def create_user(self, request: CreateUserRequestDict) -> CreateUserResponseDict:
        response = self.create_user_api(request=request)
        return response.json()

def get_public_users_client() -> PublicUsersClient:
    return PublicUsersClient(client=get_public_http_client())

