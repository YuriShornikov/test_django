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
def test_get_course(client, course, student):
    courses = course(_quantity=1)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200 #проверка статуса

    data = response.json()
    print(data)
    print(courses)
    assert len(data) == len(courses)    #проверка длины словаря
    for i, m in enumerate(data):
        assert m['name'] == courses[i].name  #проверка имени курса в базе данных с созданным

@pytest.mark.django_db
def test_get_list_courses(client, course):
    courses = course(_quantity=5)

    response = client.get('/api/v1/courses/')
    data = response.json()
    assert len(data) == len(courses)

@pytest.mark.django_db
def test_get_course_id(client, course):
    courses = course(_quantity=5)
    url = '/api/v1/courses/'

    response = client.get(f'{url}?id={courses[0].id}')

    assert response.status_code == 200

    data = response.json()

    assert data[0]['id'] == courses[0].id

@pytest.mark.django_db
def test_get_course_name(client, course):
    courses = course(_quantity=5)
    url = '/api/v1/courses/'

    response = client.get(f'{url}?name={courses[0].name}')
    data = response.json()

    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db
def test_create_course(client):
    url = '/api/v1/courses/'
    response = client.post(f'{url}', data={'id': 30, 'name': 'python', 'students': []}, format='json')
    assert response.status_code == 201


@pytest.mark.django_db
def test_patch_course(client, course):
    url = '/api/v1/courses/'
    courses = course(_quantity=1)
    response = client.patch(f'{url}?id={courses[0].id}', data={'id': courses[0].id, 'name': 'java', 'students': []}, format='json')
    assert response.status_code == 201







# def test_example():
#
#     assert False, "Just test example"
