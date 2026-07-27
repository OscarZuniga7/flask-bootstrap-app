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

SQL_CREAR_ESTUDIANTE = """
    INSERT INTO estudiantes
        (rut, nombre, email, carrera, fecha_ingreso)
    VALUES
        (%s, %s, %s, %s, %s)
"""


def listar_estudiantes(busqueda=""):
    """Recupera estudiantes, opcionalmente filtrados por un texto."""
    texto = busqueda.strip()
    connection = get_db_connection()
    cursor = connection.cursor()

    if texto:
        patron = f"%{texto}%"
        # El SQL y los datos se entregan por separado al conector de MySQL.
        cursor.execute(SQL_BUSCAR_ESTUDIANTES, (patron, patron, patron))
    else:
        cursor.execute(SQL_LISTAR_ESTUDIANTES)

    estudiantes = cursor.fetchall()
    cursor.close()
    connection.close()
    return estudiantes


def crear_estudiante(rut, nombre, email, carrera, fecha_ingreso=None):
    """Inserta un estudiante; MySQL genera id_estudiante automáticamente."""
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # La instrucción SQL y los valores viajan separados.
        cursor.execute(
            SQL_CREAR_ESTUDIANTE,
            (rut, nombre, email, carrera, fecha_ingreso),
        )
        # El commit confirma que el cambio debe quedar guardado.
        connection.commit()
    finally:
        cursor.close()
        connection.close()
