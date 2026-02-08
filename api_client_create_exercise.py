from clients.courses.courses_client import CreateCourseRequestDict, get_courses_client
from clients.exercises.exercises_client import CreateExerciseRequestDict, get_exercises_client
from clients.files.files_client import CreateFileRequestDict, get_files_client
from clients.private_http_builder import AuthenticationUserDict
from clients.users.public_users_client import CreateUserRequestDict, get_public_users_client
from tools.fakers import get_random_email


public_users_client = get_public_users_client()

# Создание пользователя
create_user_request = CreateUserRequestDict(
    email=get_random_email(),
    password="string",
    lastName="string",
    firstName="string",
    middleName="string"
)

create_user_response = public_users_client.create_user(create_user_request)

authentication_user = AuthenticationUserDict(
    email = create_user_request["email"],
    password = create_user_request["password"]
)

files_client = get_files_client(authentication_user)
courses_client = get_courses_client(authentication_user)
exercises_client = get_exercises_client(authentication_user)

# Создание файла
create_file_request = CreateFileRequestDict(
    filename="image.png",
    directory="courses",
    upload_file="./test_data/files/image.png"
)

create_file_response = files_client.create_file(create_file_request)

# Создание курса
create_course_request = CreateCourseRequestDict(
    title="Python",
    maxScore=100,
    minScore=10,
    description="Python API course",
    estimatedTime="2 weeks",
    previewFileId=create_file_response['file']['id'],
    createdByUserId=create_user_response['user']['id']
)

create_course_response = courses_client.create_course(create_course_request)

# Создание упражнения
create_exercise_request = CreateExerciseRequestDict(
    title = "Create list",
    courseId = create_course_response['course']['id'],
    maxScore = 10,
    minScore = 2,
    orderIndex = 4,
    description = "exercise to create list",
    estimatedTime = "5 min",
)

create_exercise_response = exercises_client.create_exercise(create_exercise_request)

output_data = f"""
Create file data: {create_file_response}
Create course data: {create_course_response}
Create exercise data: {create_exercise_response}
"""

print(output_data)


