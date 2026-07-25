import os

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    """Crea una conexión al servidor MySQL usando el entorno del contenedor."""
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        charset="utf8mb4",
        collation="utf8mb4_0900_ai_ci",
    )

# Ruta para mostrar la página principal (index.html)
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT id, title, content FROM posts ORDER BY id")
    posts = cursor.fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Ruta para agregar una nueva publicación
@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO posts (title, content) VALUES (%s, %s)",
        (title, content),
    )
    connection.commit()
    connection.close()
    
    # Redirigir a la ruta principal
    return redirect(url_for('index'))

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE id = %s", (post_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
