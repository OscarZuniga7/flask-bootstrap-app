from flask import Flask, flash, redirect, render_template, request, url_for
from mysql.connector import IntegrityError

from estudiante_repository import (
    actualizar_estudiante,
    crear_estudiante,
    listar_estudiantes,
    obtener_estudiante_por_id,
)

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


def validar_datos_estudiante(datos):
    """Reúne las validaciones compartidas por creación y edición."""
    errores = {}
    for campo, mensaje in (
        ("rut", "El RUT es obligatorio."),
        ("nombre", "El nombre es obligatorio."),
        ("email", "El email es obligatorio."),
        ("carrera", "La carrera es obligatoria."),
    ):
        if not datos[campo]:
            errores[campo] = mensaje

    if datos["email"] and not email_basico_valido(datos["email"]):
        errores["email"] = "Escribe un email con un formato válido, por ejemplo ana@ejemplo.cl."
    return errores


def agregar_error_de_integridad(errores, error, otro=False):
    """Convierte un error UNIQUE de MySQL en una explicación amable."""
    detalle = str(error).lower()
    palabra = "otro estudiante con ese" if otro else "un estudiante con ese"
    if error.errno == 1062 and "rut" in detalle:
        errores["rut"] = f"Ya existe {palabra} RUT."
    elif error.errno == 1062 and "email" in detalle:
        sujeto = "otro estudiante" if otro else "un estudiante"
        errores["email"] = f"Ya existe {sujeto} con ese correo electrónico."
    else:
        errores["general"] = "No fue posible guardar el estudiante. Inténtalo nuevamente."


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

        errores = validar_datos_estudiante(datos)

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
                agregar_error_de_integridad(errores, error)
            else:
                flash("Estudiante creado correctamente.", "success")
                return redirect(url_for("index"))

    return render_template("nuevo_estudiante.html", datos=datos, errores=errores)


@app.route("/estudiantes/<int:id_estudiante>/editar", methods=["GET", "POST"])
def editar_estudiante(id_estudiante):
    estudiante = obtener_estudiante_por_id(id_estudiante)
    if estudiante is None:
        flash("No se encontró el estudiante solicitado.", "warning")
        return redirect(url_for("index"))

    datos = {
        "rut": estudiante[1],
        "nombre": estudiante[2],
        "email": estudiante[3],
        "carrera": estudiante[4],
        "fecha_ingreso": estudiante[5].isoformat() if estudiante[5] else "",
    }
    errores = {}

    if request.method == "POST":
        datos = {campo: request.form.get(campo, "").strip() for campo in datos}
        errores = validar_datos_estudiante(datos)
        if not errores:
            try:
                actualizar_estudiante(
                    id_estudiante,
                    datos["rut"],
                    datos["nombre"],
                    datos["email"],
                    datos["carrera"],
                    datos["fecha_ingreso"] or None,
                )
            except IntegrityError as error:
                agregar_error_de_integridad(errores, error, otro=True)
            else:
                flash("Estudiante actualizado correctamente.", "success")
                return redirect(url_for("index"))

    return render_template(
        "editar_estudiante.html",
        id_estudiante=id_estudiante,
        datos=datos,
        errores=errores,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
