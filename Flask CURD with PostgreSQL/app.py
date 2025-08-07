# app.py

from flask import Flask, request, jsonify
from db_operations import connect, create_table, create_user, read_users, update_user, delete_user

app = Flask(__name__)

# Initialize database connection
connection, cursor = connect()

# Create table on startup
create_table(cursor)

# Route to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400
    create_user(cursor, name, email)
    return jsonify({'message': 'User created successfully'}), 201

# Route to get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = read_users(cursor)
    return jsonify({'users': users}), 200

# Route to update a user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user_route(user_id):
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({'error': 'Name and email are required'}), 400
    update_user(cursor, user_id, name, email)
    return jsonify({'message': 'User updated successfully'}), 200

# Route to delete a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user_route(user_id):
    delete_user(cursor, user_id)
    return jsonify({'message': 'User deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)


'''

Add a new user (POST /users):

curl -X POST \
  http://localhost:5000/users \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Pawan Mane",
    "email": "pawan@example.com"
}'

Get all users (GET /users):

curl -X GET \
  http://localhost:5000/users


Update a user (PUT /users/<user_id>):

curl -X PUT \
  http://localhost:5000/users/12 \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Test Test",
    "email": "Test@example.com"
}'

Delete a user (DELETE /users/<user_id>):

curl -X DELETE \
  http://localhost:5000/users/9


'''