from typing import TypedDict

from httpx import QueryParams, Response
from clients.api_client import APIClient

class GetExercisesQueryDict(TypedDict):
    """
    Описание структуры параметров запроса на получение списка упражнений
    """
    courseId: str

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

class UpdateExerciseRequestDIct(TypedDict):
    """
    Описание структуры запроса на обновление упражнения
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


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

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для получения упражнения по exercise_id
        
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.get(url=f"/api/v1/exercises/{exercise_id}")

    def create_exercise_api(self, request: CreateExerciseRequestDict) -> Response:
        """
        Метод для создания упражнения
        
        :param request: словарь с параметрами для создания упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.post(url="/api/v1/exercises", json=request)
    
    def update_exercise_api(self, request: UpdateExerciseRequestDIct, exercise_id: str) -> Response:
        """
        Метод для обновления упражнения
        
        :param request: словарь с параметрами для обновления упражнения
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(url=f"/api/v1/exercises/{exercise_id}", json=request)
    
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод для удаления упражнения
        
        :param exercise_id: идентификатор упражнения
        :return: ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(url=f"/api/v1/exercises/{exercise_id}")
