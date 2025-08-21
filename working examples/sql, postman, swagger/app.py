from flask import Flask, request, jsonify

app = Flask(__name__)

# Простая база в памяти
users = [
  {
    "id": 1,
    "name": "Иванов Иван Иванович",
    "birth_year": 1990,
    "children": [
      {
        "name": "Маша",
        "birth_year": 2010,
        "relationship": "дочь"
      },
      {
        "name": "Коля",
        "birth_year": 2020,
        "relationship": "сын"
      }
    ]
  },
  {
    "id": 2,
    "name": "Смирнова Виктория",
    "birth_year": 1995,
    "children": [
      {
        "name": "Катя",
        "birth_year": 2015,
        "relationship": "дочь"
      },
      {
        "name": "Настя",
        "birth_year": 2020,
        "relationship": "дочь"
      }
    ]
  },
  {
    "id": 3,
    "name": "Петров Петр Петрович",
    "birth_year": 2000,
    "children": []
  }
]

# Получить всех пользователей
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Получить одного пользователя по ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# Добавить нового пользователя
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    new_user = {
        "id": len(users) + 1,
        "name": data["name"]
    }
    users.append(new_user)
    return jsonify(new_user), 201

# Удалить пользователя по ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted"})

if __name__ == '__main__':
    app.run(debug=True)