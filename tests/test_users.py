import pytest
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_create_user():
    payload = {
        'email': 'testuser@mail.com',
        'password': 'testpassword'
    }
    response = client.post('/users/', payload)

    data = response.data
    assert data['email'] == 'testuser@mail.com'


@pytest.mark.django_db
def test_login_user():
    payload = {
        'email': 'testuser@mail.com',
        'password': 'testpassword'
    }
    client.post('/users/', payload)
    response = client.post('/jwt/create/', payload)

    assert response.status_code == 200
