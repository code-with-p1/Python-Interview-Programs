import unittest
from app import app

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.client.testing = True

    def test_login_success(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Login successful'})

    def test_login_wrong_password(self):
        response = self.client.post('/login', json={'username': 'testuser', 'password': 'wrongpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid username or password'})

    def test_login_nonexistent_user(self):
        response = self.client.post('/login', json={'username': 'nonexistent', 'password': 'testpassword'})
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json, {'error': 'Invalid username or password'})

    def test_login_missing_username(self):
        response = self.client.post('/login', json={'password': 'testpassword'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Missing username or password'})

    def test_login_missing_password(self):
        response = self.client.post('/login', json={'username': 'testuser'})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Missing username or password'})

    def test_login_empty_payload(self):
        response = self.client.post('/login', json={})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Missing username or password'})

if __name__ == "__main__":
    unittest.main()
