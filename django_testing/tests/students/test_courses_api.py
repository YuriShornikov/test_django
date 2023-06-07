import pytest

#все фикстуры находятся в файле conftest

@pytest.mark.django_db # создание курса через фабрику, проверка гет запроса, и соответствие имени
def test_get_course(client, url, create_course, student):

    response = client.get(f'{url}{create_course[0].id}/')

    assert response.status_code == 200 #проверка статуса

    data = response.json()
    print(data)
    assert data['name'] == create_course[0].name


@pytest.mark.django_db #проверка длины списка курсов
def test_get_list_courses(client, url, course):
    courses = course(_quantity=5)

    response = client.get(url)
    data = response.json()
    assert len(data) == len(courses)

@pytest.mark.django_db #поиск курса по айди
def test_get_course_id(client, url, course):
    courses = course(_quantity=5)

    response = client.get(f'{url}?id={courses[0].id}')

    assert response.status_code == 200

    data = response.json()

    assert data[0]['id'] == courses[0].id

@pytest.mark.django_db #поиск курса по имени
def test_get_course_name(client, url, course):
    courses = course(_quantity=5)

    response = client.get(f'{url}?name={courses[0].name}')
    data = response.json()

    assert data[0]['name'] == courses[0].name


@pytest.mark.django_db #создание курса
def test_create_course(client, url):

    response = client.post(f'{url}', data={'id': 30, 'name': 'python', 'students': []}, format='json')
    assert response.status_code == 201


@pytest.mark.django_db #изменение курса
def test_patch_course(client, url, create_course):

    response = client.patch(f'{url}{create_course[0].id}', data={'name': 'java'}, format='json')
    assert response.status_code == 301

@pytest.mark.django_db #удаление курса
def test_delete_course(client, url, create_course):

    response = client.delete(f'{url}{create_course[0].id}')
    assert response.status_code == 301

