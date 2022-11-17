import requests
from pytest_voluptuous import S
from schemas import schemas
from utils.base_session import reqres_session

#1 POST CREATE: создать пользователя
'''
Request
/api/users

{
    "name": "morpheus",
    "job": "leader"
}
 
Response
201

{
    "name": "morpheus",
    "job": "leader",
    "id": "463",
    "createdAt": "2022-11-17T10:30:36.261Z"
}
'''
def test_create_user():
    name = 'Olga'
    job = 'Qa'

    response = reqres_session().post(
        url='/api/users',
        json=
        {
            "name": name,
            "job": job
        }
    )
    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job
    assert response.json() == S(schemas.create_user_schema)

#2 PUT UPDATE: перезаписать пользователя
'''
Request
/api/users/2

{
    "name": "morpheus",
    "job": "zion resident"
}
 
Response
200

{
    "name": "morpheus",
    "job": "zion resident",
    "updatedAt": "2022-11-17T10:31:15.089Z"
}
'''
def test_update_user_schema():
    name = 'Vasia'
    job = 'Dev'

    response = reqres_session().put(
        url='/api/users/2',
        json={
            "name": name,
            "job": job
        }
    )
    assert response.status_code == 200
    assert response.json()["name"] == name
    assert response.json()["job"] == job
    assert response.json() == S(schemas.update_user_schema)


#3 DELETE: удалить пользователя
'''
Request
/api/users/2

Response
204
'''
def test_delete_user():
    response = reqres_session().delete(url='/api/users/2')
    assert response.status_code == 204

#4 GET SINGLE USER: показать 1 пользователя
'''
Response
200

{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
'''
def test_get_single_user():
    response = reqres_session().get(url='/api/users/2')
    assert response.status_code == 200
    assert response.json()["data"]
    assert response.json()["data"]["id"] == 2
    assert response.json()["data"]["email"] == "janet.weaver@reqres.in"
    assert response.json()["data"]["first_name"] == "Janet"
    assert response.json()["data"]["last_name"] == "Weaver"
    assert response.json() == S(schemas.get_single_user_schema)

#5 POST REGISTER - SUCCESSFUL: регистрация прошла успешно?
'''
Request
/api/register

{
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}
 
Response
200

{
    "id": 4,
    "token": "QpwL5tke4Pnpja7X4"
}
'''

def test_successful_register_user():
    email = 'eve.holt@reqres.in'
    password = 'pistol'
    response = reqres_session().post(
        url='/api/register',
        json={
            "email": email,
            "password": password
        }
    )
    assert response.status_code == 200
    assert response.json()["id"] == 4
    assert response.json()["token"] == "QpwL5tke4Pnpja7X4"
    assert response.json() == S(schemas.successful_register_user_schema)