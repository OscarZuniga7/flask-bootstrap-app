from database_connection import get_db_connection


SQL_LISTAR_ESTUDIANTES = """
    SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
    FROM estudiantes
    ORDER BY nombre ASC
"""

SQL_BUSCAR_ESTUDIANTES = """
    SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
    FROM estudiantes
    WHERE nombre LIKE %s
       OR rut LIKE %s
       OR carrera LIKE %s
    ORDER BY nombre ASC
"""


def listar_estudiantes(busqueda=""):
    """Recupera estudiantes, opcionalmente filtrados por un texto."""
    texto = busqueda.strip()
    connection = get_db_connection()
    cursor = connection.cursor()

    if texto:
        patron = f"%{texto}%"
        # El SQL y los datos se entregan por separado al conector de MySQL.
        cursor.execute(
            SQL_BUSCAR_ESTUDIANTES,
            (patron, patron, patron),
        )
    else:
        cursor.execute(SQL_LISTAR_ESTUDIANTES)

    estudiantes = cursor.fetchall()
    cursor.close()
    connection.close()
    return estudiantes
