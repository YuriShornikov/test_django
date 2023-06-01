import pytest
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student


@pytest.fixture #создание клиента
def client():
    return APIClient()

@pytest.fixture #урл для запроса
def url():
    return '/api/v1/courses/'

@pytest.fixture #создание рандома курсов
def course():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture #создание рандома студентов
def student():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

@pytest.fixture #создание 1 курса
def create_course(course):
    return course(_quantity=1)