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

@pytest.mark.django_db
def test_get_courses(client, course, student):
    courses = course(_quantity=1)
    students = student(_quantity=5)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200

    data = response.json()
    assert len(data) == len(courses)#проверка длины словаря
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name#проверка имени курса в базе данных с созданным

    # assert data[0] == 1




# def test_example():
#
#     assert False, "Just test example"
