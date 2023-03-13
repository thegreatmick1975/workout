from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Database connection
conn = psycopg2.connect(
    host="localhost",
    database="workout",
    user="postgres",
    password="yourpassword"
)

# Endpoint to return user data
@app.route('/users', methods=['GET'])
def get_users():
    cur = conn.cursor()
    cur.execute('SELECT * FROM users')
    rows = cur.fetchall()
    users = []
    for row in rows:
        user = {'id': row[0], 'name': row[1], 'age': row[2]}
        users.append(user)
    cur.close()
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)

