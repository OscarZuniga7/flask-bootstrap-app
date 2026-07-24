# Flask Bootstrap App

Este proyecto es una aplicación web pequeña hecha con **Python**, **Flask**, **SQLite** y **Bootstrap**.

Está pensada para estudiantes de primer año de Ingeniería que están comenzando a trabajar con herramientas de desarrollo. No necesitas experiencia previa con Git, GitHub, Python, entornos virtuales ni Docker para seguir esta guía.

## 1. ¿Qué hace esta aplicación?

La aplicación muestra una página web con una lista de publicaciones. Desde el navegador puedes:

- ver publicaciones guardadas;
- agregar una publicación nueva con título y contenido;
- eliminar publicaciones existentes.

La información se guarda en un archivo llamado `database.db`. Ese archivo es una base de datos **SQLite**, es decir, una base de datos sencilla que vive en un solo archivo dentro del proyecto.

## 2. Conceptos básicos antes de empezar

### ¿Qué es un proyecto de software?

Un proyecto de software es una carpeta que contiene archivos de código, documentación, imágenes, configuraciones y otros recursos necesarios para que una aplicación funcione.

En este caso, la carpeta del proyecto contiene archivos como:

- `app.py`: el archivo principal de la aplicación Flask;
- `requirements.txt`: la lista de librerías de Python necesarias;
- `templates/index.html`: la página HTML que se ve en el navegador;
- `database.db`: la base de datos SQLite;
- `README.md`: este documento de instrucciones.

### ¿Qué es Python?

Python es un lenguaje de programación. En este proyecto lo usamos para crear el servidor web, es decir, el programa que responde cuando abres la aplicación en el navegador.

Ejemplo sencillo: cuando entras a `http://127.0.0.1:5000`, Python ejecuta el código de `app.py` y devuelve una página web.

### ¿Qué es Flask?

Flask es una librería de Python para crear aplicaciones web de forma sencilla.

Una librería es código creado por otras personas que podemos reutilizar. Gracias a Flask no tenemos que programar desde cero todo lo necesario para recibir solicitudes del navegador y devolver páginas web.

### ¿Qué es Bootstrap?

Bootstrap es una librería de diseño web. Sirve para que una página HTML tenga botones, tablas y formularios con mejor apariencia sin escribir mucho CSS.

### ¿Qué es Git?

Git es una herramienta para guardar el historial de cambios de un proyecto.

Puedes imaginarlo como una bitácora: cada vez que avanzas en el proyecto, Git puede guardar una “foto” del estado de los archivos. Esa foto se llama **commit**.

### ¿Qué es GitHub?

GitHub es una plataforma en internet donde se pueden guardar proyectos que usan Git.

Git vive en tu computador. GitHub vive en internet. Ambos suelen usarse juntos para compartir código con otras personas.

### ¿Qué es un repositorio?

Un repositorio, o “repo”, es una carpeta de proyecto controlada por Git.

Ejemplo: si este proyecto está en GitHub, el repositorio es el lugar donde están guardados todos sus archivos y su historial de cambios.

### ¿Qué significa clonar un repositorio?

Clonar significa copiar un repositorio desde GitHub a tu computador.

Es parecido a descargar una carpeta, pero con una diferencia importante: al clonar también descargas el historial de Git, lo que permite actualizar el proyecto o guardar tus propios cambios más adelante.

### ¿Qué es una rama?

Una rama es una línea de trabajo dentro de Git.

Ejemplo sencillo: imagina que el proyecto principal es un cuaderno. Una rama es como sacar una fotocopia del cuaderno para hacer cambios sin rayar el original.

### ¿Qué es un commit?

Un commit es un punto guardado en la historia del proyecto.

Ejemplo: después de corregir un error o terminar una parte del trabajo, puedes hacer un commit para guardar ese avance con un mensaje como “Agrega formulario de publicaciones”.

### ¿Qué es un pull request?

Un pull request es una solicitud para que tus cambios sean revisados y, si están correctos, se integren al proyecto principal en GitHub.

Ejemplo: si trabajas en una rama distinta, haces cambios y quieres que el profesor o tu equipo los revise, puedes abrir un pull request.

### ¿Qué es un entorno virtual?

Un entorno virtual es una carpeta especial donde Python instala las librerías necesarias para un proyecto específico.

Sirve para no mezclar las librerías de este proyecto con las de otros proyectos.

Ejemplo: este proyecto necesita Flask 2.0.1. Otro proyecto podría necesitar una versión distinta. El entorno virtual ayuda a que no se estorben.

### ¿Qué es Docker?

Docker es una herramienta para ejecutar aplicaciones dentro de un ambiente aislado llamado **contenedor**.

Un contenedor se parece a una caja que trae lo necesario para ejecutar una aplicación. Una **imagen** es como el molde o receta para crear esa caja.

### ¿Qué es Docker Compose?

Docker Compose es una herramienta que permite iniciar uno o varios contenedores usando un archivo de configuración, normalmente llamado `docker-compose.yml`.

En la Semana 1 no necesitas Docker ni Docker Compose. El método principal de esta semana es ejecutar la aplicación con:

```bash
python app.py
```

Docker Compose se menciona más adelante solo como adelanto para próximas semanas.

## 3. Herramientas necesarias para la Semana 1

Para la Semana 1 necesitas instalar y verificar estas herramientas:

1. Visual Studio Code, recomendado para editar archivos.
2. Python, necesario para ejecutar la aplicación.
3. Git, necesario si vas a clonar el proyecto desde GitHub.

Docker no es necesario para la Semana 1.

## 4. Instalar Visual Studio Code

### ¿Qué es Visual Studio Code?

Visual Studio Code, también llamado VS Code, es un editor de código. Sirve para abrir la carpeta del proyecto, leer archivos, editar código y usar una terminal integrada.

### ¿Por qué lo necesitamos?

Lo usamos porque facilita trabajar con proyectos que tienen varios archivos.

### Cómo instalarlo en Windows 10 u 11

1. Abre tu navegador.
2. Entra a <https://code.visualstudio.com/>.
3. Descarga el instalador para Windows.
4. Ejecuta el instalador.
5. Durante la instalación, si aparece la opción **Add to PATH**, actívala.
6. Finaliza la instalación.

### Cómo instalarlo en macOS

1. Abre tu navegador.
2. Entra a <https://code.visualstudio.com/>.
3. Descarga la versión para macOS.
4. Abre el archivo descargado.
5. Arrastra Visual Studio Code a la carpeta `Applications`.

### Cómo verificar que VS Code funciona

Abre Visual Studio Code desde el menú de inicio en Windows o desde Applications en macOS.

Si la aplicación abre correctamente, ya está instalada.

## 5. Instalar Python

### ¿Qué es Python?

Python es el programa que ejecutará el archivo `app.py`.

### ¿Por qué lo necesitamos?

Sin Python, tu computador no sabe cómo ejecutar esta aplicación.

### Cómo instalar Python en Windows 10 u 11

1. Abre tu navegador.
2. Entra a <https://www.python.org/downloads/>.
3. Descarga la versión recomendada para Windows.
4. Ejecuta el instalador.
5. Muy importante: marca la casilla **Add Python to PATH** antes de presionar Install.
6. Presiona **Install Now**.
7. Espera a que termine la instalación.

### Cómo instalar Python en macOS

1. Abre tu navegador.
2. Entra a <https://www.python.org/downloads/>.
3. Descarga la versión recomendada para macOS.
4. Abre el instalador descargado.
5. Sigue los pasos del instalador.

### Cómo verificar que Python quedó instalado

Primero debes abrir una terminal.

En Windows puedes usar **PowerShell**:

1. Presiona la tecla Windows.
2. Escribe `PowerShell`.
3. Abre Windows PowerShell.

En macOS puedes usar **Terminal**:

1. Presiona `Command + Space`.
2. Escribe `Terminal`.
3. Presiona Enter.

El siguiente comando muestra la versión instalada de Python. Sirve para confirmar que el computador reconoce Python correctamente.

```bash
python --version
```

Si en Windows ese comando no funciona, prueba este otro. El comando `py` es el lanzador de Python que muchas instalaciones de Windows incluyen.

```bash
py --version
```

Deberías ver algo parecido a:

```text
Python 3.11.0
```

No es necesario que el número sea exactamente igual, pero debe comenzar con `Python 3`.

## 6. Instalar Git

### ¿Qué es Git?

Git es la herramienta que permite descargar el proyecto desde GitHub y guardar cambios en el historial del proyecto.

### ¿Por qué lo necesitamos?

Lo necesitas si vas a clonar el repositorio desde GitHub. También lo usarás más adelante para trabajar con commits, ramas y pull requests.

### Cómo instalar Git en Windows 10 u 11

1. Abre tu navegador.
2. Entra a <https://git-scm.com/downloads>.
3. Descarga Git para Windows.
4. Ejecuta el instalador.
5. Puedes aceptar las opciones recomendadas si el profesor no indicó algo distinto.
6. Finaliza la instalación.

### Cómo instalar Git en macOS

Opción simple:

1. Abre Terminal.
2. El siguiente comando pregunta al sistema si Git está disponible. Si no lo está, macOS puede ofrecer instalar las herramientas necesarias.

```bash
git --version
```

3. Si aparece una ventana para instalar herramientas de desarrollador, acepta la instalación.

También puedes descargar Git desde <https://git-scm.com/downloads>.

### Cómo verificar que Git quedó instalado

El siguiente comando muestra la versión instalada de Git. Sirve para confirmar que el computador reconoce Git correctamente.

```bash
git --version
```

Deberías ver algo parecido a:

```text
git version 2.45.0
```

No importa si tu número de versión es diferente.

## 7. Obtener el proyecto en tu computador

Hay dos formas comunes de obtener el proyecto. Usa la que indique tu profesor.

### Opción A: clonar desde GitHub

Usa esta opción si el profesor te entregó un enlace de GitHub.

Primero elige una carpeta donde guardarás tus proyectos. Por ejemplo, puedes crear una carpeta llamada `proyectos` en tu usuario.

El siguiente comando cambia la ubicación de la terminal a tu carpeta de usuario. `cd` significa “change directory”, o cambiar de carpeta.

En Windows PowerShell:

```bash
cd $HOME
```

En macOS Terminal:

```bash
cd ~
```

El siguiente comando crea una carpeta llamada `proyectos`. `mkdir` significa “make directory”, o crear carpeta.

```bash
mkdir proyectos
```

El siguiente comando entra a la carpeta `proyectos`.

```bash
cd proyectos
```

Ahora clona el repositorio. Este comando copia el proyecto desde GitHub a tu computador. Debes reemplazar `URL_DEL_REPOSITORIO` por el enlace que te entregó tu profesor.

```bash
git clone URL_DEL_REPOSITORIO
```

Después de clonar, entra a la carpeta del proyecto. Si el repositorio se llama `flask-bootstrap-app`, usa este comando.

```bash
cd flask-bootstrap-app
```

### Opción B: descargar ZIP desde GitHub

Usa esta opción solo si tu profesor permite descargar el proyecto como archivo ZIP.

1. Abre el enlace del proyecto en GitHub.
2. Presiona el botón verde **Code**.
3. Presiona **Download ZIP**.
4. Descomprime el archivo ZIP.
5. Abre la carpeta descomprimida.

Importante: descargar ZIP es más simple, pero no trae todo el historial de Git. Para aprender Git, es mejor clonar.

## 8. Abrir el proyecto en Visual Studio Code

Abre VS Code.

Luego:

1. Presiona **File**.
2. Presiona **Open Folder**.
3. Busca la carpeta `flask-bootstrap-app`.
4. Presiona **Select Folder** u **Open**.

Ahora abre la terminal integrada de VS Code:

1. Presiona **Terminal**.
2. Presiona **New Terminal**.

La terminal debería abrirse dentro de la carpeta del proyecto.

Para verificarlo, usa este comando. Sirve para mostrar la carpeta actual donde está parada la terminal.

En Windows PowerShell:

```bash
pwd
```

En macOS Terminal:

```bash
pwd
```

Deberías ver una ruta que termina en `flask-bootstrap-app`.

## 9. Crear un entorno virtual

### ¿Por qué crear un entorno virtual?

El entorno virtual separa las librerías de este proyecto de las librerías de otros proyectos.

Esto evita problemas cuando dos proyectos necesitan versiones distintas de una misma librería.

### Crear el entorno virtual

El siguiente comando crea una carpeta llamada `.venv`. Esa carpeta guardará una copia aislada de Python y las librerías del proyecto.

En Windows, si `python` no funciona, usa `py`.

```bash
python -m venv .venv
```

Alternativa para Windows:

```bash
py -m venv .venv
```

### Activar el entorno virtual en Windows PowerShell

Activar el entorno virtual significa decirle a la terminal: “usa las librerías de este proyecto”.

El siguiente comando activa el entorno virtual en Windows PowerShell.

```bash
.\.venv\Scripts\Activate.ps1
```

Si PowerShell muestra un error de permisos al activar, ejecuta este comando. Sirve para permitir scripts solo en la terminal actual.

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Luego intenta activar nuevamente:

```bash
.\.venv\Scripts\Activate.ps1
```

### Activar el entorno virtual en macOS

El siguiente comando activa el entorno virtual en macOS.

```bash
source .venv/bin/activate
```

### Verificar que el entorno virtual está activo

Cuando está activo, normalmente aparece `(.venv)` al inicio de la línea de la terminal.

También puedes verificar qué Python se está usando.

En Windows PowerShell, este comando muestra la ubicación del Python activo.

```bash
where python
```

En macOS, este comando muestra la ubicación del Python activo.

```bash
which python
```

La ruta debería incluir `.venv`.

## 10. Instalar las librerías del proyecto

Las librerías necesarias están escritas en `requirements.txt`.

El siguiente comando instala esas librerías dentro del entorno virtual activo. `pip` es el instalador de librerías de Python.

```bash
pip install -r requirements.txt
```

Para verificar que Flask quedó instalado, usa este comando. Sirve para mostrar información de la librería Flask instalada.

```bash
pip show Flask
```

Deberías ver información como nombre, versión y ubicación de instalación.

## 11. Preparar la base de datos

Este proyecto usa el archivo `database.db` como base de datos SQLite.

Si el archivo `database.db` ya existe, puedes continuar al paso siguiente.

Si el archivo no existe, debes crearlo ejecutando `init_db.py`. El siguiente comando crea la tabla `posts`, donde se guardan las publicaciones.

```bash
python init_db.py
```

Importante: si ejecutas este comando cuando la tabla ya existe, SQLite puede mostrar un error indicando que la tabla `posts` ya existe. En ese caso, no significa que Python esté mal instalado; solo significa que la base de datos ya estaba creada.

## 12. Ejecutar la aplicación en Semana 1

Este es el método principal para la Semana 1.

El siguiente comando inicia la aplicación Flask. Al ejecutarlo, Python lee el archivo `app.py` y levanta un servidor web local en tu computador.

```bash
python app.py
```

Si estás en Windows y `python` no funciona, prueba:

```bash
py app.py
```

Cuando funcione, deberías ver un mensaje parecido a:

```text
Running on http://127.0.0.1:5000
```

Ahora abre tu navegador y entra a esta dirección:

```text
http://127.0.0.1:5000
```

También puedes probar:

```text
http://localhost:5000
```

`localhost` significa “este mismo computador”.

## 13. Probar la aplicación manualmente

Cuando la página esté abierta en el navegador:

1. Escribe un título en el campo **Título**.
2. Escribe un texto en el campo **Contenido**.
3. Presiona **Agregar**.
4. Verifica que la publicación aparece en la tabla.
5. Presiona **Eliminar** en una publicación.
6. Verifica que desaparece de la tabla.

## 14. Detener la aplicación

Mientras la aplicación está ejecutándose, la terminal queda ocupada mostrando mensajes.

Para detenerla, vuelve a la terminal y presiona:

```text
Ctrl + C
```

Esto detiene el servidor local.

## 15. Problemas frecuentes

### La terminal dice que `python` no se reconoce

En Windows, prueba este comando:

```bash
py --version
```

Si funciona, usa `py` en lugar de `python` para crear el entorno virtual y ejecutar la aplicación.

### La terminal dice que `pip` no se reconoce

Verifica que el entorno virtual esté activo. Si no ves `(.venv)` al inicio de la línea, actívalo nuevamente.

Windows PowerShell:

```bash
.\.venv\Scripts\Activate.ps1
```

macOS:

```bash
source .venv/bin/activate
```

### PowerShell no deja activar el entorno virtual

Ejecuta este comando para permitir scripts en la sesión actual:

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```

Después activa otra vez:

```bash
.\.venv\Scripts\Activate.ps1
```

### El navegador no abre la página

Revisa lo siguiente:

1. Confirma que la terminal sigue ejecutando `python app.py`.
2. Confirma que no cerraste la terminal.
3. Abre exactamente `http://127.0.0.1:5000`.
4. Si aparece otro puerto en la terminal, usa el puerto que indique la terminal.

### Aparece un error sobre la tabla `posts`

Si estabas ejecutando `python init_db.py`, puede significar que la tabla ya existía.

Si estabas ejecutando `python app.py`, revisa que exista el archivo `database.db` en la carpeta del proyecto.

## 16. Adelanto: Docker y Docker Compose para próximas semanas

No necesitas esta sección para la Semana 1.

Más adelante, Docker puede servir para ejecutar la aplicación en un contenedor. Un contenedor es un ambiente aislado que incluye lo necesario para correr una aplicación de forma más consistente entre computadores.

Docker Compose permite iniciar el contenedor usando el archivo `docker-compose.yml`.

Cuando sea pedagógicamente necesario, el profesor podrá pedir ejecutar la aplicación con Docker Compose. Ese flujo no reemplaza el método principal de Semana 1, que es:

```bash
python app.py
```

## 17. Resumen rápido de Semana 1

Estos son los pasos principales, pero recuerda leer las secciones anteriores si es tu primera vez.

1. Instalar VS Code.
2. Instalar Python y verificarlo.
3. Instalar Git y verificarlo.
4. Clonar o descargar el proyecto.
5. Abrir la carpeta en VS Code.
6. Crear el entorno virtual.
7. Activar el entorno virtual.
8. Instalar dependencias con `pip install -r requirements.txt`.
9. Verificar o crear `database.db`.
10. Ejecutar la aplicación con `python app.py`.
11. Abrir `http://127.0.0.1:5000` en el navegador.

## 18. Comandos principales de Semana 1

Cada comando se explicó antes. Esta lista sirve solo como recordatorio.

```bash
python --version
```

```bash
git --version
```

```bash
git clone URL_DEL_REPOSITORIO
```

```bash
cd flask-bootstrap-app
```

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\Activate.ps1
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
python app.py
```

---

# Semana 2: ejecución reproducible con Docker

En la Semana 1 ejecutamos la aplicación directamente en el computador con Python:

```bash
python app.py
```

En la Semana 2 aprenderemos una alternativa: ejecutar la **misma aplicación Flask + SQLite** dentro de un contenedor usando Docker Compose. No estamos diciendo que Docker sea “mejor” en todos los casos. Lo usaremos porque permite practicar una idea muy importante en ingeniería: construir un entorno de ejecución reproducible, aislado y fácil de compartir.

## 1. Ideas básicas antes de usar comandos Docker

### ¿Qué problema resuelve Docker?

Cuando una aplicación funciona en un computador pero falla en otro, muchas veces el problema no está en el código, sino en el entorno: versión de Python, librerías instaladas, variables de entorno o rutas de archivos.

Docker ayuda a resolver ese problema empaquetando la aplicación con un entorno conocido. En vez de pedir a cada estudiante que configure exactamente igual su computador, el proyecto describe cómo debe ser el entorno en archivos como `Dockerfile` y `docker-compose.yml`.

### ¿Qué es Docker?

Docker es una herramienta para construir y ejecutar aplicaciones dentro de **contenedores**. Un contenedor es un ambiente aislado donde la aplicación ve sus propios archivos, dependencias y configuración.

En este proyecto, Docker ejecutará Flask dentro de un contenedor, pero la aplicación seguirá usando SQLite y la tabla `posts`.

### ¿Qué es Docker Desktop?

Docker Desktop es la aplicación que instala Docker en Windows 10/11 y macOS. En Windows, normalmente también configura los componentes necesarios para que Docker pueda ejecutar contenedores Linux.

Para estudiantes que usan Windows, Docker Desktop es la forma recomendada de empezar.

### ¿Qué es una imagen?

Una imagen Docker es una plantilla para crear contenedores. Puedes imaginarla como una receta congelada: contiene instrucciones y archivos necesarios para crear un ambiente de ejecución.

En este proyecto, la imagen se construye a partir del `Dockerfile`: parte de Python, instala Flask desde `requirements.txt` y copia el código de la aplicación.

### ¿Qué es un contenedor?

Un contenedor es una ejecución concreta de una imagen. Si la imagen es la receta, el contenedor es el plato preparado y funcionando.

Cuando levantamos el proyecto, el contenedor ejecuta:

```bash
python app.py
```

pero lo hace dentro del ambiente definido por Docker.

### ¿Qué es Dockerfile?

`Dockerfile` es el archivo que explica cómo construir la imagen de la aplicación. Indica, por ejemplo:

- qué versión base de Python usar;
- dónde estará la aplicación dentro del contenedor;
- cómo instalar las dependencias;
- qué comando iniciar al arrancar el contenedor.

### ¿Qué es docker-compose.yml?

`docker-compose.yml` es un archivo de configuración para Docker Compose. En vez de escribir un comando Docker largo, Compose permite describir el servicio de la aplicación de forma legible.

En esta semana usamos un único servicio: `flask_app`.

### ¿Qué es un puerto?

Un puerto es como una puerta numerada por donde entran conexiones de red. Flask escucha dentro del contenedor en el puerto `5000`. Para abrir la aplicación desde el navegador del computador, publicamos ese puerto también como `5000` en el equipo anfitrión.

Por eso accederemos a:

```text
http://localhost:5000
```

### ¿Qué significa persistencia?

Persistencia significa conservar datos aunque el programa se detenga. SQLite guarda la información en un archivo llamado `database.db`. Si ese archivo vive solo dentro del contenedor, puede perderse al recrearlo.

### ¿Qué es un volumen?

Un volumen Docker es almacenamiento administrado por Docker para conservar datos fuera del ciclo de vida normal del contenedor.

### ¿Qué es un bind mount?

Un bind mount es un mecanismo distinto: conecta una carpeta visible del computador con una carpeta vista dentro del contenedor. Ambos mecanismos pueden ayudar a conservar o compartir datos, pero en este proyecto de Semana 2 usamos específicamente un **bind mount**.

Aunque `docker-compose.yml` usa la sección `volumes:`, la línea siguiente representa un bind mount:

```text
./data  ->  /app/data
```

`./data` corresponde a una carpeta visible del computador del estudiante. `/app/data` corresponde a la carpeta que ve Flask dentro del contenedor. La base SQLite del contenedor se guarda en `/app/data/database.db`, que corresponde a `data/database.db` en tu carpeta del proyecto. Ese archivo permanece en el computador aunque el contenedor se destruya y vuelva a crearse.

El repositorio incluye `data/.gitkeep` porque Git normalmente no conserva carpetas vacías. Ese pequeño archivo permite que la carpeta `data` exista después de clonar el proyecto. En condiciones normales no necesitas crearla manualmente: al ejecutar por primera vez la aplicación con Docker se creará `data/database.db`, y ese archivo no se versionará porque está incluido en `.gitignore`.

Flujo de la Semana 2:

```text
Navegador
    ↓
Contenedor Flask
    ↓
SQLite
    ↓
Almacenamiento persistente en ./data/database.db
```

## 2. Preparación del computador en Windows 10/11

### Paso 1: consultar requisitos generales

Antes de instalar Docker Desktop, consulta la documentación oficial de Docker Desktop para Windows y sigue los requisitos e instrucciones vigentes de instalación. Según la configuración del equipo, Docker Desktop puede solicitar WSL 2, virtualización u otros componentes.

Como comprobación sencilla, asegúrate de contar con permisos para instalar programas, conexión a internet y espacio libre suficiente en disco.

### Paso 2: instalar Docker Desktop desde la fuente oficial

1. Abre el navegador.
2. Entra a <https://www.docker.com/products/docker-desktop/>.
3. Descarga Docker Desktop para Windows.
4. Ejecuta el instalador.
5. Acepta las opciones recomendadas por Docker Desktop si aparece alguna solicitud adicional.
6. Reinicia el computador si el instalador lo solicita.

### Paso 3: iniciar Docker Desktop

1. Abre el menú Inicio.
2. Busca **Docker Desktop**.
3. Inicia la aplicación.
4. Espera hasta que indique que Docker está funcionando.

No basta con tener Docker instalado: Docker Desktop debe estar abierto para que los comandos funcionen.

### Paso 4: comprobar Docker desde la terminal

Abre PowerShell o la terminal integrada de VS Code en la carpeta del proyecto.

Primero comprobamos que el comando `docker` existe:

```bash
docker --version
```

Luego comprobamos que Docker Compose está disponible:

```bash
docker compose version
```

Si ambos comandos muestran una versión, el computador está listo para continuar.

## 3. Ejecución guiada con Docker Compose

Asegúrate de estar en la carpeta raíz del proyecto, donde están `Dockerfile` y `docker-compose.yml`.

### Construir y levantar la aplicación

Antes de ejecutar el comando, piensa qué necesitamos: Docker debe leer el `Dockerfile`, construir una imagen y crear un contenedor para Flask.

```bash
docker compose up --build -d
```

Qué hace:

- `docker compose up` crea e inicia los servicios definidos en `docker-compose.yml`;
- `--build` reconstruye la imagen si hubo cambios;
- `-d` deja el contenedor ejecutándose en segundo plano.

Qué deberías observar:

- mensajes de construcción de imagen la primera vez;
- creación del servicio `flask_app`;
- la terminal queda disponible al finalizar.

Cómo saber si funcionó: ejecuta el comando de estado.

```bash
docker compose ps
```

Deberías ver el servicio `flask_app` en estado `running` o `Up`, y el puerto `5000` publicado.

### Ver logs

Los logs son los mensajes que imprime la aplicación. Sirven para investigar qué ocurrió dentro del contenedor.

```bash
docker compose logs
```

Qué deberías observar:

- mensajes de Flask;
- una línea indicando que la aplicación escucha en `0.0.0.0:5000`;
- si la base no existía, se crea automáticamente antes de atender solicitudes.

### Abrir la aplicación

Abre el navegador y entra a:

```text
http://localhost:5000
```

Si ves la página de publicaciones, la aplicación funciona dentro del contenedor.

### Detener la aplicación

Cuando quieras detener los contenedores de esta semana, usa:

```bash
docker compose down
```

Qué hace:

- detiene el contenedor;
- elimina el contenedor creado por Compose;
- conserva los archivos del proyecto, incluida la carpeta `data` que contiene la base persistente.

## 4. Actividad guiada: comprobar persistencia

Objetivo: demostrar que SQLite necesita almacenamiento persistente para conservar datos.

1. Inicia la aplicación:

   ```bash
   docker compose up --build -d
   ```

2. Abre `http://localhost:5000`.
3. Crea una publicación con un título fácil de reconocer, por ejemplo `Prueba de persistencia`.
4. Comprueba que aparece en la lista.
5. Detén la aplicación:

   ```bash
   docker compose down
   ```

6. Vuelve a iniciarla:

   ```bash
   docker compose up --build -d
   ```

7. Abre nuevamente `http://localhost:5000`.
8. Comprueba que la publicación continúa existiendo.

¿Por qué ocurre? Porque `docker-compose.yml` conecta la carpeta `./data` del proyecto con `/app/data` dentro del contenedor. La aplicación usa la variable `DATABASE_PATH=/app/data/database.db`, por lo que SQLite escribe la base en una carpeta persistente del computador.

## 5. Comparación didáctica Semana 1 vs Semana 2

| Aspecto | Semana 1: `python app.py` | Semana 2: `docker compose up --build -d` |
|---|---|---|
| Dónde se ejecuta Flask | Directamente en tu computador | Dentro de un contenedor |
| Dependencias | Se instalan en un entorno virtual local | Se instalan dentro de la imagen Docker |
| Entorno virtual | Lo creas y activas manualmente | No lo activas en tu terminal; la imagen contiene las dependencias |
| Reproducibilidad | Depende más de la configuración del computador | El entorno queda descrito en `Dockerfile` y `docker-compose.yml` |
| Aislamiento | Menor aislamiento | Mayor aislamiento respecto al sistema anfitrión |
| Persistencia SQLite | `database.db` queda en la carpeta del proyecto | `data/database.db` queda fuera del contenedor mediante bind mount |

## 6. Problemas frecuentes

### `docker` no se reconoce

Significa que Docker no está instalado o no quedó agregado al PATH. Instala Docker Desktop desde la página oficial, reinicia la terminal y prueba nuevamente `docker --version`.

### Docker Desktop no está iniciado

Si el comando existe pero no puede conectarse al motor de Docker, abre Docker Desktop y espera a que termine de iniciar.

### `docker compose` no funciona

Comprueba:

```bash
docker compose version
```

Si falla, revisa que Docker Desktop esté actualizado. En instalaciones antiguas existía `docker-compose` con guion, pero en este curso usaremos `docker compose`.

### El puerto ya está ocupado

Si otro programa usa el puerto `5000`, Docker no podrá publicarlo. Cierra el otro programa o cambia temporalmente el puerto izquierdo en `docker-compose.yml`, por ejemplo `5001:5000`, y entra a `http://localhost:5001`.

### El contenedor se detiene inesperadamente

Consulta los logs:

```bash
docker compose logs
```

Busca errores de Python, Flask, permisos o rutas de archivos.

### `database.db` no se crea

Recuerda que el repositorio incluye `data/.gitkeep`, por lo que la carpeta `data` debería existir después de clonar correctamente. Confirma que `DATABASE_PATH` apunte a `/app/data/database.db`, que el bind mount sea `./data:/app/data` y que tengas permisos de escritura en la carpeta del proyecto.

### Los datos desaparecen después de recrear el contenedor

Verifica que no hayas eliminado la carpeta `data`. La persistencia depende de que `data/database.db` permanezca en el computador.

## 7. Más detalle

La guía completa de la Semana 2 está en [`docs/Semana02.md`](docs/Semana02.md).
