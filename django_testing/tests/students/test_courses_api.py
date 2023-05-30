from model_bakery import baker
from rest_framework.test import APIClient
import pytest

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory

@pytest.fixture
def student():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory

def test_get_courses(client, course):
    courses = course(_quantity=10)

    response = client.get('/courses/')
    assert response.status_code == 200


# def test_example():
#
#     assert False, "Just test example"
