import requests

BASE_URL = 'https://reqres.in/'

# проверка успешного подключения к BASE_URL
def test_get_base_url():
    responce = requests.get(BASE_URL)
    assert responce.status_code == 200

# проверка списка пользователей на 2-й странице
def test_get_list_users():
    responce = requests.get(BASE_URL + 'api/users?page=2')
    data = responce.json()

    assert responce.status_code == 200
    assert data['page'] == 2

# проверка наличия пользователя id 2
def test_get_single_user():
    responce = requests.get(BASE_URL + 'api/users/2')
    data = responce.json()

    assert responce.status_code == 200
    assert data['data']['id'] == 2

# проверка отсутствия пользователя id 23
def test_get_single_user_not_found():
    responce = requests.get(BASE_URL + 'api/users/23')

    assert responce.status_code == 404

def test_get_list():
    responce = requests.get(BASE_URL + 'api/unknown')
    data = responce.json()

    assert responce.status_code == 200
    assert len(data['data']) == 6

# проверка добавления пользователя
def test_post_create():
    # данные пользователя
    new_user = {
        'name': 'morpheus',
        'job': 'leader'
    }
    # передаваемый запрос с данными нового пользователя
    responce = requests.post(BASE_URL + 'api/users', json=new_user)
    data = responce.json()

    assert responce.status_code == 201
    assert data['name'] == 'morpheus'
    assert data['job'] == 'leader'

# проверка обновлений данных пользователя
def test_put_update():
    # обновленные данные пользователя
    update_user = {
    'name': 'morpheus',
    'job': 'zion resident'
    }

    # передаваемый запрос с обновленными данными пользователя
    responce= requests.put(BASE_URL + 'api/users/2', json=update_user)
    data = responce.json()

    assert responce.status_code == 200
    assert data['name'] == 'morpheus'
    assert data['job'] == 'zion resident'

# проверка удаления пользователя
def test_delete_user():
    responce = requests.delete(BASE_URL + 'api/users/2')

    assert responce.status_code == 204

# проверка регистрации с корректными данными
def test_post_register_successful():
    new_user = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'
    }

    responce = requests.post(BASE_URL + 'api/register', json=new_user)
    data = responce.json()

    assert responce.status_code == 200
    assert data['id'] == 4
    assert data['token'] == 'QpwL5tke4Pnpja7X4'

# проверка регистрации с некорректными данными
def test_post_register_successful():
    new_user = {
        'email': 'sydney@file',
    }

    responce = requests.post(BASE_URL + 'api/register', json=new_user)
    data = responce.json()

    assert responce.status_code == 400
    assert data['error'] == 'Missing password'

# проверка получения токена при корректном логине
def test_post_login_successful():
    new_user = {
        'email': 'eve.holt@reqres.in',
        'password': 'cityslicka'
    }

    responce = requests.post(BASE_URL + 'api/login', json=new_user)
    data = responce.json()

    assert responce.status_code == 200
    assert data['token'] == 'QpwL5tke4Pnpja7X4'

# проверка получения токена при некорректном логине
def test_post_login_unsuccessful():
    new_user = {
        'email': 'peter@klaven'
    }

    responce = requests.post(BASE_URL + 'api/login', json=new_user)
    data = responce.json()

    assert responce.status_code == 400
    assert data['error'] == 'Missing password'