import os
import sqlite3

from flask import Flask, render_template, request, redirect, url_for

from init_db import init_database

app = Flask(__name__)
DATABASE_PATH = os.environ.get('DATABASE_PATH', 'database.db')
init_database(DATABASE_PATH)

# Ruta para mostrar la página principal (index.html)
@app.route('/')
def index():
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    connection.close()
    return render_template('index.html', posts=posts)

# Ruta para agregar una nueva publicación
@app.route('/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    connection.commit()
    connection.close()
    
    # Redirigir a la ruta principal
    return redirect(url_for('index'))

@app.route('/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    connection = sqlite3.connect(DATABASE_PATH)
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
