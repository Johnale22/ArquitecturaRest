from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos simulada
users = [
    {"id": 1, "name": "John Guerra"},
    {"id": 2, "name": "Juan Perez"},
]

# Endpoint GET para obtener usuarios
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Endpoint POST para agregar un nuevo usuario
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    users.append(new_user)
    return jsonify(new_user), 201

if __name__ == '__main__':
    app.run(debug=True)
