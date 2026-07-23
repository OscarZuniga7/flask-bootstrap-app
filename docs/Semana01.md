# Semana 1: Primer contacto con la aplicación Flask y SQLite

## Propósito de la semana

En esta primera semana trabajaremos con calma para ejecutar el proyecto por primera vez en el computador. La idea principal no es memorizar comandos, sino entender qué hace cada parte y cómo se conectan entre sí.

Durante la Semana 1 la ejecución será **local con Python**. Esto significa que la aplicación se ejecutará directamente desde el computador, sin Docker y sin Docker Compose.

Docker Desktop **no es necesario para esta semana**. Más adelante estudiaremos Docker como una forma de ejecutar la misma aplicación en un entorno reproducible.

## Objetivos de aprendizaje

Al finalizar esta semana, deberías poder:

- preparar el computador con las herramientas básicas de trabajo;
- obtener el proyecto desde GitHub;
- abrir una terminal en la carpeta del proyecto;
- crear y activar un entorno virtual de Python;
- instalar las dependencias del proyecto;
- inicializar la base de datos SQLite;
- ejecutar Flask localmente;
- abrir la aplicación en el navegador;
- comprender el flujo general **Navegador → Flask → SQLite**;
- crear y eliminar publicaciones desde la interfaz web.

## Antes de comenzar: preparación del computador

Antes de ejecutar la aplicación, necesitamos reconocer algunas herramientas que usaremos durante el curso.

### Python

Python es el lenguaje de programación con el que está construida la aplicación. En esta semana lo usaremos para ejecutar archivos como `init_db.py` y `app.py`.

### Git

Git es una herramienta que permite guardar versiones de un proyecto. También permite descargar una copia de un proyecto desde internet y trabajar con sus archivos en el computador.

### GitHub

GitHub es una plataforma en línea donde se publican repositorios. Un repositorio es una carpeta de proyecto que contiene código, documentación y otros archivos necesarios para trabajar.

### Visual Studio Code

Visual Studio Code, o VS Code, es un editor de código. Lo usaremos para abrir la carpeta del proyecto, leer los archivos, editar código en próximas semanas y usar una terminal integrada.

### Entorno virtual

Un entorno virtual es una carpeta especial que guarda las librerías de Python necesarias para un proyecto. Esto ayuda a que las dependencias de este proyecto no se mezclen con las de otros proyectos.

En este proyecto el entorno virtual se creará en una carpeta llamada `.venv`.

## Comprobar instalaciones

En Windows 10 y Windows 11 se recomienda usar **PowerShell** o la terminal integrada de VS Code. En macOS y Linux puedes usar la aplicación **Terminal**.

Para comprobar que Git está instalado, ejecuta:

```bash
git --version
```

Si Git está instalado, aparecerá un número de versión.

Para comprobar que Python está instalado, ejecuta:

```bash
python --version
```

Si Python está instalado, aparecerá un número de versión. En algunos computadores con macOS o Linux puede ser necesario usar este comando alternativo:

```bash
python3 --version
```

Para comprobar que pip está instalado, ejecuta:

```bash
pip --version
```

`pip` es la herramienta que instala librerías de Python. En algunos computadores con macOS o Linux puede ser necesario usar este comando alternativo:

```bash
python3 -m pip --version
```

Si alguno de estos comandos no funciona, revisa la sección **Problemas frecuentes** al final de este documento.

## Cómo obtener el proyecto

Para trabajar con la aplicación necesitas tener una copia de los archivos en tu computador. Puedes hacerlo de dos formas.

### Alternativa 1: clonar el repositorio con Git

Clonar un repositorio significa descargar una copia completa del proyecto desde GitHub hacia tu computador. Esa copia conserva la información de Git, por lo que más adelante podrás ver cambios, crear versiones y trabajar de forma ordenada.

Primero, abre una terminal en la carpeta donde quieras guardar tus proyectos. Por ejemplo, puedes usar una carpeta llamada `Documentos`, `Documents`, `Proyectos` o `Projects`.

Luego ejecuta el comando de clonación que indique tu profesor o profesora. Tendrá una forma parecida a esta:

```bash
git clone URL_DEL_REPOSITORIO
```

Después entra a la carpeta del proyecto. El nombre exacto de la carpeta dependerá del repositorio, pero puede ser similar a este:

```bash
cd flask-bootstrap-app
```

### Alternativa 2: descargar el repositorio como archivo ZIP

Si todavía no tienes Git instalado o si el profesor lo permite, puedes descargar el proyecto como archivo ZIP desde GitHub.

Pasos generales:

1. Abre el repositorio en GitHub desde el navegador.
2. Presiona el botón **Code**.
3. Elige **Download ZIP**.
4. Descomprime el archivo descargado.
5. Entra a la carpeta descomprimida del proyecto.

Esta opción permite ejecutar el proyecto, pero no conserva toda la información de Git. Por eso, para el curso se recomienda aprender a clonar el repositorio con Git cuando sea posible.

## Abrir una terminal en la carpeta del proyecto

Para ejecutar los comandos correctamente, la terminal debe estar ubicada dentro de la carpeta principal del proyecto, donde se encuentran archivos como `app.py`, `init_db.py` y `requirements.txt`.

### Opción recomendada en Windows 10 y Windows 11 con VS Code

1. Abre Visual Studio Code.
2. Selecciona **File** o **Archivo**.
3. Selecciona **Open Folder** o **Abrir carpeta**.
4. Elige la carpeta del proyecto.
5. Abre la terminal integrada desde **Terminal → New Terminal** o **Terminal → Nueva terminal**.

La terminal debería abrirse directamente dentro de la carpeta del proyecto.

### Opción desde el Explorador de archivos de Windows

1. Abre la carpeta del proyecto.
2. Haz clic en la barra de dirección del Explorador de archivos.
3. Escribe `powershell`.
4. Presiona **Enter**.

Esto abrirá PowerShell en esa carpeta.

### Opción en macOS o Linux

Abre una terminal y usa `cd` para entrar a la carpeta del proyecto. Por ejemplo:

```bash
cd ruta/a/flask-bootstrap-app
```

## Crear y activar el entorno virtual

El entorno virtual se crea una sola vez por proyecto. Sirve para guardar las librerías que la aplicación necesita.

Para crear el entorno virtual en una carpeta llamada `.venv`, ejecuta:

```bash
python -m venv .venv
```

En macOS o Linux, si `python` no funciona, usa:

```bash
python3 -m venv .venv
```

Ahora debes activar el entorno virtual. Activarlo significa decirle a la terminal que use el Python y las librerías guardadas dentro de `.venv`.

En Windows PowerShell, ejecuta:

```powershell
.venv\Scripts\Activate.ps1
```

En Windows CMD, ejecuta:

```cmd
.venv\Scripts\activate.bat
```

En macOS o Linux, ejecuta:

```bash
source .venv/bin/activate
```

Cuando el entorno virtual está activo, normalmente aparece `(.venv)` al inicio de la línea de la terminal. Por ejemplo:

```text
(.venv) PS C:\Users\estudiante\flask-bootstrap-app>
```

Si no aparece exactamente igual, no te preocupes: lo importante es que la terminal indique de alguna forma que `.venv` está activo.

## Instalar dependencias

Las dependencias son librerías que el proyecto necesita para funcionar. En este caso, Flask está incluido en el archivo `requirements.txt`.

Con el entorno virtual activo, instala las dependencias con:

```bash
pip install -r requirements.txt
```

Este comando lee el archivo `requirements.txt` e instala las librerías necesarias dentro del entorno virtual.

## Inicializar SQLite

SQLite es una base de datos sencilla que se guarda en un archivo local. En este proyecto, la base de datos se llama `database.db`.

Para crear la tabla `posts`, ejecuta:

```bash
python init_db.py
```

Este comando prepara la base de datos para que la aplicación pueda guardar publicaciones.

Si ya ejecutaste este comando antes y aparece un mensaje indicando que la tabla ya existe, revisa la sección **Problemas frecuentes**.

## Ejecutar Flask localmente

Flask es la herramienta que recibe solicitudes desde el navegador, consulta o modifica la base de datos y devuelve una página web como respuesta.

Para iniciar la aplicación, ejecuta:

```bash
python app.py
```

Si todo está correcto, Flask quedará ejecutándose en la terminal. Mientras la aplicación esté activa, no cierres esa terminal.

Abre el navegador y visita:

```text
http://localhost:5000
```

`localhost` significa “este mismo computador”. El número `5000` es el puerto donde Flask está atendiendo la aplicación.

## Cómo comprobar que la aplicación funciona

Realiza estas acciones en el navegador:

1. Abre `http://localhost:5000`.
2. Verifica que se muestra la página principal de publicaciones.
3. Escribe un título y un contenido en el formulario.
4. Presiona el botón para agregar la publicación.
5. Comprueba que la nueva publicación aparece en la tabla.
6. Presiona el botón para eliminar una publicación.
7. Comprueba que la publicación desaparece de la tabla.

Si puedes completar estos pasos, la aplicación está funcionando localmente.

## Flujo principal: Navegador → Flask → SQLite

La aplicación tiene tres acciones importantes durante esta semana.

### Consulta de la página principal

Cuando escribes `http://localhost:5000` en el navegador, ocurre este flujo:

1. El navegador solicita la página principal.
2. Flask recibe la solicitud en la ruta `/`.
3. Flask se conecta a SQLite.
4. SQLite entrega las publicaciones guardadas en la tabla `posts`.
5. Flask usa la plantilla HTML para construir la página.
6. El navegador muestra la tabla de publicaciones.

En palabras simples: el navegador pide información, Flask la busca en la base de datos y luego construye la página que vemos.

### Inserción de una publicación

Cuando completas el formulario y presionas el botón para agregar, ocurre este flujo:

1. El navegador envía el título y el contenido a Flask.
2. Flask recibe esos datos en una ruta preparada para crear publicaciones.
3. Flask se conecta a SQLite.
4. SQLite guarda la nueva publicación en la tabla `posts`.
5. Flask redirige nuevamente a la página principal.
6. El navegador muestra la tabla actualizada.

En palabras simples: escribimos datos en el navegador, Flask los recibe y SQLite los guarda.

### Eliminación de una publicación

Cuando presionas el botón para eliminar, ocurre este flujo:

1. El navegador envía a Flask la solicitud de eliminación.
2. Flask identifica qué publicación debe eliminarse.
3. Flask se conecta a SQLite.
4. SQLite elimina la publicación correspondiente.
5. Flask redirige nuevamente a la página principal.
6. El navegador muestra la tabla sin la publicación eliminada.

En palabras simples: pedimos borrar un dato, Flask transmite la instrucción y SQLite actualiza la información guardada.

## Actividad breve de la Semana 1

Trabaja paso a paso y registra en tu cuaderno o documento de trabajo qué ocurrió en cada etapa.

1. Obtén el proyecto desde GitHub usando Git o descargando el ZIP.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Abre una terminal en la carpeta del proyecto.
4. Comprueba que `git`, `python` y `pip` estén disponibles.
5. Crea el entorno virtual con `python -m venv .venv`.
6. Activa el entorno virtual según tu sistema operativo.
7. Instala las dependencias con `pip install -r requirements.txt`.
8. Inicializa SQLite con `python init_db.py`.
9. Ejecuta Flask con `python app.py`.
10. Abre `http://localhost:5000` en el navegador.
11. Crea una publicación de prueba.
12. Verifica que aparece en la tabla.
13. Elimina la publicación.
14. Verifica que desaparece.

## Preguntas de reflexión

Responde con tus propias palabras:

1. ¿Qué significa clonar un repositorio?
2. ¿Por qué es útil abrir la terminal dentro de la carpeta del proyecto?
3. ¿Para qué sirve un entorno virtual?
4. ¿Qué archivo se ejecuta para crear la base de datos SQLite?
5. ¿Qué archivo se ejecuta para iniciar la aplicación Flask?
6. ¿Qué ocurre cuando el navegador visita `http://localhost:5000`?
7. ¿Qué papel cumple Flask entre el navegador y SQLite?
8. ¿Qué cambia en la base de datos cuando agregas una publicación?
9. ¿Qué cambia en la base de datos cuando eliminas una publicación?
10. ¿Qué parte del proceso te resultó más difícil y cómo la resolviste?

## Problemas frecuentes

### `git` no se reconoce

Si aparece un mensaje como “git no se reconoce como un comando”, probablemente Git no está instalado o no quedó agregado al PATH del sistema.

Solución breve:

- instala Git desde su sitio oficial;
- cierra y vuelve a abrir la terminal;
- ejecuta nuevamente `git --version`.

### `python` no se reconoce

Si Windows indica que `python` no se reconoce, Python puede no estar instalado o puede faltar la opción de agregarlo al PATH.

Solución breve:

- instala Python desde su sitio oficial;
- durante la instalación en Windows, marca la opción **Add Python to PATH**;
- cierra y vuelve a abrir la terminal;
- ejecuta nuevamente `python --version`.

En macOS o Linux prueba también:

```bash
python3 --version
```

### `pip` no se reconoce

Si `pip` no se reconoce, intenta ejecutarlo desde Python.

En Windows, prueba:

```bash
python -m pip --version
```

En macOS o Linux, prueba:

```bash
python3 -m pip --version
```

Si funciona, también puedes instalar dependencias usando:

```bash
python -m pip install -r requirements.txt
```

### PowerShell impide activar el entorno virtual

Si PowerShell bloquea la activación del entorno virtual, puede aparecer un mensaje relacionado con permisos de ejecución de scripts.

Solución breve para la sesión actual de PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Luego intenta activar nuevamente el entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

Este cambio se aplica solo a la ventana actual de PowerShell.

### Flask no está instalado

Si aparece un error indicando que Flask no está instalado, probablemente las dependencias no se instalaron en el entorno virtual activo.

Solución breve:

1. Activa el entorno virtual.
2. Verifica que aparezca `(.venv)` en la terminal.
3. Ejecuta:

```bash
pip install -r requirements.txt
```

4. Vuelve a iniciar la aplicación con:

```bash
python app.py
```

### `database.db` o la tabla `posts` no existen

Si la aplicación muestra un error relacionado con `database.db` o con la tabla `posts`, probablemente falta inicializar la base de datos.

Solución breve:

```bash
python init_db.py
```

Luego vuelve a ejecutar la aplicación:

```bash
python app.py
```

Si el archivo `database.db` existe pero la tabla no quedó bien creada, pide ayuda antes de borrar archivos, para no perder datos importantes.

### El puerto 5000 está ocupado

Si Flask indica que el puerto `5000` ya está en uso, significa que otra aplicación está usando ese puerto o que dejaste otra ejecución de Flask abierta.

Solución breve:

- revisa si ya hay una terminal ejecutando `python app.py`;
- detén la ejecución anterior con `Ctrl + C`;
- vuelve a ejecutar:

```bash
python app.py
```

Si el problema continúa, pide apoyo para identificar qué programa está usando el puerto.

## Próxima evolución

En esta semana ejecutamos la aplicación localmente con Python para comprender el flujo básico **Navegador → Flask → SQLite**.

Más adelante estudiaremos Docker para ejecutar esta misma aplicación en un entorno reproducible. Por ahora, lo importante es sentirse cómodo obteniendo el proyecto, preparando el entorno virtual, instalando dependencias, inicializando SQLite y ejecutando Flask de manera local.
