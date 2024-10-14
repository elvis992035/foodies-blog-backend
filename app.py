from flask import Flask, request, jsonify
from flask_cors import CORS
from call_chatgpt import chat_with_gpt

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Enable CORS for all routes

users = [
    {"id": 1, "name": "Alice", "grade": 87, "email": 'aaa@gmail.com'},
    {"id": 2, "name": "Bob"}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

@app.route('/users/<int:user_id>', methods=['GET'])
def get_user_name(user_id):
    for user in users:
        if user_id == user.get('id'):
            return user.get('name')

    return "user not found", 404

@app.route('/users', methods=['POST'])
def add_user():
    body = request.get_json()
    new_user = {
        'id': len(users) + 1, # can use uuid
        'name': body.get('name')
    }
    users.append(new_user)
    return jsonify(new_user), 201

@app.route('/ask', methods=['POST'])
def ask_recipe():
    body = request.get_json()
    response = {'answer': chat_with_gpt(body.get('query'))}
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
