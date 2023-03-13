from flask import Flask, request, jsonify
import psycopg2
app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password="yourpassword"
)

# Endpoint for creating a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (%s, %s)", (data['name'], data['age']))
    conn.commit()
    cursor.close()
    return jsonify({"message": "User created successfully"})

# Endpoint for retrieving all users
@app.route('/users', methods=['GET'])
def get_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    cursor.close()
    return jsonify({"users": users})

if __name__ == '__main__':
    app.run(debug=True)

