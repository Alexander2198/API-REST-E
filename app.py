from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Datos iniciales (en memoria)
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"}
]

@app.route('/')
def index():
    return render_template('index.html')  # Sirve el archivo HTML

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# Ruta para agregar un nuevo usuario
@app.route('/users', methods=['POST'])
def add_user():
    new_user = request.get_json()
    new_user['id'] = len(users) + 1  
    users.append(new_user)
    return jsonify(new_user), 201

# Ruta para obtener un usuario por su ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
