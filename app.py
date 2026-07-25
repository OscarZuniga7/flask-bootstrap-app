import os

from flask import Flask, render_template
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


# Esta semana la aplicación solo consulta y muestra estudiantes.
@app.route("/")
def index():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(
        """
        SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
        FROM estudiantes
        ORDER BY id_estudiante
        """
    )
    estudiantes = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template("index.html", estudiantes=estudiantes)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
