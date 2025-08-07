import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_login_success(client):
    response = client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200
    assert response.json == {'message': 'Login successful'}

def test_login_wrong_password(client):
    response = client.post('/login', json={'username': 'testuser', 'password': 'wrongpassword'})
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid username or password'}

def test_login_nonexistent_user(client):
    response = client.post('/login', json={'username': 'nonexistent', 'password': 'testpassword'})
    assert response.status_code == 401
    assert response.json == {'error': 'Invalid username or password'}

def test_login_missing_username(client):
    response = client.post('/login', json={'password': 'testpassword'})
    assert response.status_code == 400
    assert response.json == {'error': 'Missing username or password'}

def test_login_missing_password(client):
    response = client.post('/login', json={'username': 'testuser'})
    assert response.status_code == 400
    assert response.json == {'error': 'Missing username or password'}

def test_login_empty_payload(client):
    response = client.post('/login', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Missing username or password'}


'''

Test Commands : 

pytest

pytest test_login.py

pytest test_login.py::test_login_success

pytest -v test_login.py

pytest -v test_login.py::test_login_success

'''