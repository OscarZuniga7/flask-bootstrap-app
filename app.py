from flask import Flask, render_template, request

from estudiante_repository import listar_estudiantes

app = Flask(__name__)


# Esta semana la aplicación solo consulta y muestra estudiantes.
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


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
