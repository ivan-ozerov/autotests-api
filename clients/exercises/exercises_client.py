from typing import TypedDict

from httpx import QueryParams, Response
from clients.api_client import APIClient
from clients.private_http_builder import AuthenticationUserDict, get_private_http_client

class Exercise(TypedDict):
  id: str
  title: str
  courseId: str
  maxScore: int
  minScore: int
  orderIndex: int
  description: str
  estimatedTime: str


class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры параметров запроса на получение списка упражнений
    """
    courseId: str

class GetExercisesResponseDict(TypedDict):
    """
    Описание структуры ответа на получение списка упражнений
    """
    exercises: list[Exercise]

class GetExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на получение упражнения
    """
    exercise: Exercise

class CreateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на создание упражнения
    """
    title: str
    courseId: str
    maxScore: int | None
    minScore: int | None
    orderIndex: int
    description: str 
    estimatedTime: str | None

class CreateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на создание упражнения
    """
    exercise: Exercise

class UpdateExerciseRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None

class UpdateExerciseResponseDict(TypedDict):
    """
    Описание структуры ответа на обновление упражнения
    """
    exericse: Exercise


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self, query: GetExercisesQueryDict) -> Response:
        """
        Метод для получения списка упражнений
        
        :param query: словарь с course_id
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url="/api/v1/exercises", params=QueryParams(**query))
    
    def get_exercises(self, query: GetExercisesQueryDict) -> GetExercisesResponseDict:
        """
        Метод для получения тела ответа из get_exercises_api
        
        :param query: словарь с courseId
        :return: тело ответа в виде GetExerciseResponseDict
        """
        return self.get_exercises_api(query).json()

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения упражнения по exercise_id
        
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")
    
    def get_exercise(self, exercise_id: str) -> GetExerciseResponseDict:
        """
        Метод для получения тела ответа из get_exercise_api
        
        :param exercise_id: идентификатор упражнения
        :return: тело ответа вида GetExerciseResponseDict
        """
        return self.get_exercise_api(exercise_id).json()

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения
        
        :param request: словарь с параметрами для создания упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)
    
    def create_exercise(self, request: CreateExerciseRequestDict) -> CreateExerciseResponseDict:
        """
        Метод для получения тела ответа из create_exercise_api
        
        :param request: словарь с параметрами для создания упражнения
        :return: тело ответа вида CreateExerciseResponseDict
        """
        return self.create_exercise_api(request=request).json()
        
    
    def update_exercise_api(self, request: UpdateExerciseRequestDict, exercise_id: str) -> Response:
        """
        Метод для обновления упражнения
        
        :param request: словарь с параметрами для обновления упражнения
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)
    
    def update_exercise(self, request: UpdateExerciseRequestDict, exercise_id: str) -> UpdateExerciseResponseDict:
        """
        Метод для получения тела ответа на обновление упражнения

        :param request: словарь с параметрами для обновления упражнения
        :param exercise_id: идентификатор упражнения
        :return: тело ответ в виде объекта UpdateExerciseResponseDict
        """
        return self.update_exercise_api(request=request, exercise_id=exercise_id).json()
    
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения
        
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")


def get_exercises_client(user: AuthenticationUserDict) -> ExercisesClient:
    return ExercisesClient(client=get_private_http_client(user))
