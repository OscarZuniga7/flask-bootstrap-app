from flask import Flask, flash, redirect, render_template, request, url_for
from mysql.connector import IntegrityError

from estudiante_repository import crear_estudiante, listar_estudiantes

app = Flask(__name__)
# flash necesita una clave para conservar un mensaje corto hasta la página siguiente.
app.secret_key = "clave-local-para-mensajes-de-clase"


@app.route("/")
def index():
    busqueda = request.args.get("busqueda", "").strip()
    estudiantes = listar_estudiantes(busqueda)
    return render_template(
        "index.html",
        estudiantes=estudiantes,
        busqueda=busqueda,
        cantidad=len(estudiantes),
    )


def email_basico_valido(email):
    """Detecta errores evidentes sin usar una validación compleja."""
    if email.count("@") != 1:
        return False
    usuario, dominio = email.split("@")
    return bool(usuario and dominio and "." in dominio and not dominio.startswith(".") and not dominio.endswith("."))


@app.route("/estudiantes/nuevo", methods=["GET", "POST"])
def nuevo_estudiante():
    datos = {
        "rut": "",
        "nombre": "",
        "email": "",
        "carrera": "",
        "fecha_ingreso": "",
    }
    errores = {}

    if request.method == "POST":
        datos = {campo: request.form.get(campo, "").strip() for campo in datos}

        for campo, etiqueta in (
            ("rut", "El RUT es obligatorio."),
            ("nombre", "El nombre es obligatorio."),
            ("email", "El email es obligatorio."),
            ("carrera", "La carrera es obligatoria."),
        ):
            if not datos[campo]:
                errores[campo] = etiqueta

        if datos["email"] and not email_basico_valido(datos["email"]):
            errores["email"] = "Escribe un email con un formato válido, por ejemplo ana@ejemplo.cl."

        if not errores:
            try:
                crear_estudiante(
                    datos["rut"],
                    datos["nombre"],
                    datos["email"],
                    datos["carrera"],
                    datos["fecha_ingreso"] or None,
                )
            except IntegrityError as error:
                detalle = str(error).lower()
                if error.errno == 1062 and "rut" in detalle:
                    errores["rut"] = "Ya existe un estudiante con ese RUT."
                elif error.errno == 1062 and "email" in detalle:
                    errores["email"] = "Ya existe un estudiante con ese correo electrónico."
                else:
                    errores["general"] = "No fue posible guardar el estudiante. Inténtalo nuevamente."
            else:
                flash("Estudiante creado correctamente.", "success")
                return redirect(url_for("index"))

    return render_template("nuevo_estudiante.html", datos=datos, errores=errores)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
