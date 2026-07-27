import unittest
from unittest.mock import patch

from mysql.connector import IntegrityError

import app


DATOS_VALIDOS = {
    "rut": "16.666.666-6",
    "nombre": "Luis Soto",
    "email": "luis@ejemplo.cl",
    "carrera": "Diseño",
    "fecha_ingreso": "",
}


class NuevoEstudianteTest(unittest.TestCase):
    def setUp(self):
        app.app.config.update(TESTING=True, SECRET_KEY="clave-de-pruebas")
        self.client = app.app.test_client()

    def test_get_muestra_formulario(self):
        respuesta = self.client.get("/estudiantes/nuevo")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(b"Nuevo estudiante", respuesta.data)

    @patch.object(app, "crear_estudiante")
    def test_creacion_valida_redirige_y_envia_fecha_opcional(self, crear):
        respuesta = self.client.post("/estudiantes/nuevo", data=DATOS_VALIDOS)
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.headers["Location"], "/")
        crear.assert_called_once_with(
            "16.666.666-6", "Luis Soto", "luis@ejemplo.cl", "Diseño", None
        )

    @patch.object(app, "crear_estudiante")
    def test_campos_obligatorios_vacios_no_insertan(self, crear):
        respuesta = self.client.post("/estudiantes/nuevo", data={})
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("El RUT es obligatorio".encode(), respuesta.data)
        self.assertIn("El nombre es obligatorio".encode(), respuesta.data)
        self.assertIn("El email es obligatorio".encode(), respuesta.data)
        self.assertIn("La carrera es obligatoria".encode(), respuesta.data)
        crear.assert_not_called()

    @patch.object(app, "crear_estudiante")
    def test_email_invalido_conserva_los_datos(self, crear):
        datos = {**DATOS_VALIDOS, "email": "ana@", "nombre": "Ana Pérez"}
        respuesta = self.client.post("/estudiantes/nuevo", data=datos)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("formato válido".encode(), respuesta.data)
        self.assertIn("Ana Pérez".encode(), respuesta.data)
        self.assertIn(b'value="ana@"', respuesta.data)
        self.assertIn(DATOS_VALIDOS["rut"].encode(), respuesta.data)
        crear.assert_not_called()

    def comprobar_duplicado(self, detalle, mensaje):
        error = IntegrityError(msg=detalle, errno=1062)
        with patch.object(app, "crear_estudiante", side_effect=error):
            respuesta = self.client.post("/estudiantes/nuevo", data=DATOS_VALIDOS)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(mensaje.encode(), respuesta.data)
        self.assertIn(DATOS_VALIDOS["nombre"].encode(), respuesta.data)

    def test_rut_duplicado(self):
        self.comprobar_duplicado(
            "Duplicate entry for key 'estudiantes.rut'",
            "Ya existe un estudiante con ese RUT.",
        )

    def test_email_duplicado(self):
        self.comprobar_duplicado(
            "Duplicate entry for key 'estudiantes.email'",
            "Ya existe un estudiante con ese correo electrónico.",
        )

    @patch.object(app, "listar_estudiantes", return_value=[])
    @patch.object(app, "crear_estudiante")
    def test_mensaje_de_exito_aparece_despues_del_redirect(self, crear, listar):
        respuesta = self.client.post(
            "/estudiantes/nuevo", data=DATOS_VALIDOS, follow_redirects=True
        )
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("Estudiante creado correctamente".encode(), respuesta.data)


FILA_MARIA = (
    3,
    "13.333.333-3",
    "María Núñez",
    "maria@example.com",
    "Diseño",
    None,
)


class EditarEstudianteTest(unittest.TestCase):
    def setUp(self):
        app.app.config.update(TESTING=True, SECRET_KEY="clave-de-pruebas")
        self.client = app.app.test_client()

    @patch.object(app, "obtener_estudiante_por_id", return_value=FILA_MARIA)
    def test_formulario_aparece_prellenado_y_sin_campo_id(self, obtener):
        respuesta = self.client.get("/estudiantes/3/editar")
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("María Núñez".encode(), respuesta.data)
        self.assertIn(b'value="13.333.333-3"', respuesta.data)
        self.assertNotIn(b'name="id_estudiante"', respuesta.data)
        obtener.assert_called_once_with(3)

    @patch.object(app, "listar_estudiantes", return_value=[])
    @patch.object(app, "obtener_estudiante_por_id", return_value=None)
    def test_estudiante_inexistente_muestra_mensaje(self, obtener, listar):
        respuesta = self.client.get("/estudiantes/999/editar", follow_redirects=True)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("No se encontró el estudiante solicitado".encode(), respuesta.data)

    @patch.object(app, "actualizar_estudiante")
    @patch.object(app, "obtener_estudiante_por_id", return_value=FILA_MARIA)
    def test_actualizacion_valida_conserva_rut_email_y_redirige(self, obtener, actualizar):
        datos = {
            "rut": FILA_MARIA[1],
            "nombre": "María González",
            "email": FILA_MARIA[3],
            "carrera": "Diseño Digital",
            "fecha_ingreso": "",
        }
        respuesta = self.client.post("/estudiantes/3/editar", data=datos)
        self.assertEqual(respuesta.status_code, 302)
        self.assertEqual(respuesta.headers["Location"], "/")
        actualizar.assert_called_once_with(
            3, FILA_MARIA[1], "María González", FILA_MARIA[3], "Diseño Digital", None
        )

    @patch.object(app, "actualizar_estudiante")
    @patch.object(app, "obtener_estudiante_por_id", return_value=FILA_MARIA)
    def test_campos_obligatorios_no_actualizan(self, obtener, actualizar):
        respuesta = self.client.post("/estudiantes/3/editar", data={})
        for mensaje in ("El RUT es obligatorio", "El nombre es obligatorio", "El email es obligatorio", "La carrera es obligatoria"):
            self.assertIn(mensaje.encode(), respuesta.data)
        actualizar.assert_not_called()

    @patch.object(app, "actualizar_estudiante")
    @patch.object(app, "obtener_estudiante_por_id", return_value=FILA_MARIA)
    def test_email_invalido_conserva_todos_los_datos(self, obtener, actualizar):
        datos = {
            "rut": FILA_MARIA[1], "nombre": "María González", "email": "maria@",
            "carrera": "Diseño Digital", "fecha_ingreso": "2025-03-01",
        }
        respuesta = self.client.post("/estudiantes/3/editar", data=datos)
        self.assertEqual(respuesta.status_code, 200)
        for valor in datos.values():
            self.assertIn(valor.encode(), respuesta.data)
        self.assertIn("formato válido".encode(), respuesta.data)
        actualizar.assert_not_called()

    def comprobar_duplicado(self, detalle, mensaje):
        error = IntegrityError(msg=detalle, errno=1062)
        datos = {
            "rut": FILA_MARIA[1], "nombre": FILA_MARIA[2], "email": FILA_MARIA[3],
            "carrera": FILA_MARIA[4], "fecha_ingreso": "",
        }
        with patch.object(app, "obtener_estudiante_por_id", return_value=FILA_MARIA), patch.object(
            app, "actualizar_estudiante", side_effect=error
        ):
            respuesta = self.client.post("/estudiantes/3/editar", data=datos)
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(mensaje.encode(), respuesta.data)
        self.assertIn("María Núñez".encode(), respuesta.data)

    def test_rut_duplicado_en_otro_estudiante(self):
        self.comprobar_duplicado("Duplicate entry for key 'estudiantes.rut'", "Ya existe otro estudiante con ese RUT.")

    def test_email_duplicado_en_otro_estudiante(self):
        self.comprobar_duplicado("Duplicate entry for key 'estudiantes.email'", "Ya existe otro estudiante con ese correo electrónico.")

    @patch.object(app, "listar_estudiantes", return_value=[])
    @patch.object(app, "actualizar_estudiante")
    @patch.object(app, "obtener_estudiante_por_id", return_value=FILA_MARIA)
    def test_mensaje_exito_despues_de_redirect(self, obtener, actualizar, listar):
        datos = {"rut": FILA_MARIA[1], "nombre": FILA_MARIA[2], "email": FILA_MARIA[3], "carrera": FILA_MARIA[4], "fecha_ingreso": ""}
        respuesta = self.client.post("/estudiantes/3/editar", data=datos, follow_redirects=True)
        self.assertIn("Estudiante actualizado correctamente".encode(), respuesta.data)


if __name__ == "__main__":
    unittest.main()
