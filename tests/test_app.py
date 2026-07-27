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


if __name__ == "__main__":
    unittest.main()
