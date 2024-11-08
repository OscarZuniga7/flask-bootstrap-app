from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Ruta para la página original (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# Ruta para la página CRUD (index_.html)
@app.route('/crud')
def crud_index():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM posts")
    posts = cursor.fetchall()
    connection.close()
    return render_template('index_.html', posts=posts)

# Ruta para agregar una nueva publicación
@app.route('/crud/add_post', methods=['POST'])
def add_post():
    title = request.form['title']
    content = request.form['content']
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO posts (title, content) VALUES (?, ?)", (title, content))
    connection.commit()
    connection.close()
    # Redirigir a la URL completa sin el puerto
    return redirect('https://fuzzy-couscous-jjjg999qxrj3pv9q-5000.app.github.dev/crud')
    #return redirect(url_for('crud_index'))



# Ruta para eliminar una publicación
@app.route('/crud/delete_post/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM posts WHERE id = ?", (post_id,))
    connection.commit()
    connection.close()
    return redirect(url_for('crud_index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
