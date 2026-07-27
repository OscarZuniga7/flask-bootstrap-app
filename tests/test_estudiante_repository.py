import unittest
from unittest.mock import Mock, patch

import estudiante_repository


class EstudianteRepositoryTest(unittest.TestCase):
    def setUp(self):
        self.cursor = Mock()
        self.connection = Mock()
        self.connection.cursor.return_value = self.cursor
        self.filas_ordenadas = [
            (1, "11.111.111-1", "Ana Muñoz", "ana@example.com", "Ingeniería Informática", None),
            (2, "13.333.333-3", "María Núñez", "maria@example.com", "Diseño", None),
        ]
        self.cursor.fetchall.return_value = self.filas_ordenadas
        self.connection_patch = patch.object(
            estudiante_repository, "get_db_connection", return_value=self.connection
        )
        self.connection_patch.start()

    def tearDown(self):
        self.connection_patch.stop()

    def test_listar_todos_ordenados_por_nombre(self):
        resultado = estudiante_repository.listar_estudiantes()

        self.assertEqual(resultado, self.filas_ordenadas)
        sql = self.cursor.execute.call_args.args[0]
        self.assertIn("SELECT id_estudiante, rut, nombre, email, carrera", sql)
        self.assertIn("ORDER BY nombre ASC", sql)
        self.assertNotIn("WHERE", sql)

    def test_busqueda_vacia_lista_todos(self):
        estudiante_repository.listar_estudiantes("   ")

        self.assertEqual(len(self.cursor.execute.call_args.args), 1)

    def comprobar_busqueda(self, texto):
        estudiante_repository.listar_estudiantes(texto)

        sql, parametros = self.cursor.execute.call_args.args
        self.assertIn("WHERE nombre LIKE %s", sql)
        self.assertIn("OR rut LIKE %s", sql)
        self.assertIn("OR carrera LIKE %s", sql)
        self.assertIn("ORDER BY nombre ASC", sql)
        self.assertEqual(parametros, (f"%{texto}%",) * 3)
        self.assertNotIn(texto, sql)

    def test_busqueda_por_nombre_parametrizada(self):
        self.comprobar_busqueda("María")

    def test_busqueda_por_rut_parametrizada(self):
        self.comprobar_busqueda("11.111")

    def test_busqueda_por_carrera_parametrizada(self):
        self.comprobar_busqueda("Informática")

    def test_busqueda_sin_coincidencias(self):
        self.cursor.fetchall.return_value = []

        resultado = estudiante_repository.listar_estudiantes("Astronomía")

        self.assertEqual(resultado, [])


if __name__ == "__main__":
    unittest.main()


class CrearEstudianteRepositoryTest(unittest.TestCase):
    @patch.object(estudiante_repository, "get_db_connection")
    def test_insert_es_parametrizado_y_confirma_el_cambio(self, get_connection):
        connection = Mock()
        cursor = Mock()
        connection.cursor.return_value = cursor
        get_connection.return_value = connection

        estudiante_repository.crear_estudiante(
            "16.666.666-6", "Luis Soto", "luis@ejemplo.cl", "Diseño", None
        )

        sql, parametros = cursor.execute.call_args.args
        self.assertIn("INSERT INTO estudiantes", sql)
        self.assertIn("VALUES\n        (%s, %s, %s, %s, %s)", sql)
        self.assertEqual(
            parametros,
            ("16.666.666-6", "Luis Soto", "luis@ejemplo.cl", "Diseño", None),
        )
        self.assertNotIn("Luis Soto", sql)
        connection.commit.assert_called_once_with()
        cursor.close.assert_called_once_with()
        connection.close.assert_called_once_with()
