import os

import mysql.connector


def get_db_connection():
    """Crea una conexión a MySQL con la configuración del entorno."""
    return mysql.connector.connect(
        host=os.environ["DB_HOST"],
        port=int(os.environ["DB_PORT"]),
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        charset="utf8mb4",
        collation="utf8mb4_0900_ai_ci",
    )
