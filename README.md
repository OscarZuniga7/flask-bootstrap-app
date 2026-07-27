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

---

# Semana 3: conexión Flask-MySQL con Docker Compose

> Esta sección continúa las Semanas 1 y 2. En esta semana se usa Docker Compose; no ejecutes `python app.py` directamente, porque la aplicación necesita el servidor MySQL del segundo contenedor.

## 1. ¿Qué cambia respecto de Semana 2?

La pantalla y las acciones siguen siendo las mismas: listar, crear y eliminar **publicaciones**. Cambia el lugar donde se guardan. En Semana 2 Flask usaba SQLite y un archivo `database.db`; ahora Flask se conecta a MySQL mediante `mysql-connector-python`.

```text
Semana 2: navegador → Flask → SQLite → archivo database.db
Semana 3: navegador → web (Flask) → db (MySQL) → volumen mysql_data
```

MySQL es un **servidor de base de datos**: un programa independiente que recibe conexiones y consultas SQL. SQLite, en cambio, lee y escribe directamente un archivo desde la aplicación. `database.db` puede permanecer como recuerdo de semanas anteriores, pero ya no es la base activa de Semana 3.

## 2. Dos servicios: `web` y `db`

En Docker Compose, un **servicio** describe una parte de la aplicación que se ejecutará en su propio contenedor.

- `web` construye y ejecuta Flask, recibe al navegador en el puerto `5000` y envía SQL a MySQL.
- `db` ejecuta MySQL 8.4, guarda las publicaciones y solo es accesible por `web` dentro de Compose. No publicamos el puerto 3306 hacia Windows porque no hace falta para esta actividad.

Separarlos permite observar que Flask y la base de datos son programas distintos, aunque colaboran.

## 3. Variables de entorno y credenciales

Una **variable de entorno** es un valor que se entrega a un programa desde fuera de su código. En este proyecto son `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` y `MYSQL_ROOT_PASSWORD`. Así no escribimos credenciales directamente en `app.py` y podemos cambiar la configuración sin modificar Python.

- `.env.example` es una plantilla con valores didácticos, sin secretos reales; sí se versiona para enseñar qué variables hacen falta.
- `.env` es tu copia local. Puede contener tus contraseñas, está incluido en `.gitignore` y **no debe subirse a GitHub**.

### Crear `.env` en Windows 10/11

1. Abre la carpeta del proyecto en VS Code.
2. Abre **Terminal > New Terminal**. Comprueba que la terminal está ubicada en la carpeta del proyecto.
3. En PowerShell ejecuta:

```powershell
Copy-Item .env.example .env
```

Si la terminal muestra `cmd` en vez de PowerShell, usa:

```bat
copy .env.example .env
```

4. Abre `.env` desde el explorador de archivos de VS Code. Cambia los textos `cambia_esta_clave` y `cambia_esta_clave_root` por claves solo para tu entorno de clase. No agregues espacios alrededor de `=`.
5. Guarda el archivo. Nunca ejecutes `git add .env`.

## 4. ¿Por qué `DB_HOST=db` y no `localhost`?

Docker Compose permite que un servicio encuentre a otro usando su nombre. La conexión es:

```text
web → db:3306
```

Por eso Flask usa `DB_HOST=db` y el puerto interno `3306`. Dentro del contenedor `web`, `localhost` significa “este mismo contenedor web”; no significa el contenedor MySQL. Como MySQL vive en el servicio `db`, usar `localhost` buscaría MySQL en el lugar equivocado.

## 5. Inicialización de MySQL

Compose monta `database/init.sql` en `/docker-entrypoint-initdb.d/init.sql`. La imagen oficial de MySQL ejecuta automáticamente los scripts de ese directorio **cuando inicializa por primera vez un volumen de datos vacío**. El script crea `posts` (`id`, `title`, `content`) e inserta tres ejemplos.

No es un sistema de migraciones. Si se modifica `init.sql` después de que `mysql_data` ya fue inicializado, reiniciar los contenedores normalmente no vuelve a ejecutar el script.

Las consultas `INSERT` y `DELETE` de `app.py` usan parámetros (`%s`). El conector envía los valores separados del SQL; esto evita formar instrucciones concatenando texto escrito por el usuario y reduce el riesgo de inyección SQL.

## 6. Volumen nombrado `mysql_data`

En Semana 2, `./data:/app/data` era un **bind mount**: una carpeta visible del proyecto se enlazaba al contenedor para guardar el archivo SQLite. Ahora `mysql_data` es un **volumen nombrado administrado por Docker**: Docker decide su ubicación y MySQL guarda allí sus archivos internos.

```bash
docker compose down
```

Este comando elimina los contenedores, pero conserva `mysql_data` y las publicaciones.

> **Advertencia:** `docker compose down -v` también elimina los volúmenes asociados y puede borrar todos los datos MySQL de este proyecto. No uses `-v` durante la actividad normal de persistencia.

## 7. Healthcheck

Que el contenedor MySQL esté iniciado no significa necesariamente que MySQL ya esté listo para recibir conexiones. El `healthcheck` ejecuta una comprobación sencilla con `mysqladmin ping`. `web` tiene `depends_on` con `condition: service_healthy`, por lo que Compose espera a que `db` esté saludable antes de iniciar Flask.

## 8. Construir y ejecutar paso a paso

Antes de comenzar, abre Docker Desktop y espera a que indique que está funcionando. Luego usa la terminal integrada de VS Code en la carpeta del proyecto.

1. Crea `.env` como se explicó antes.
2. Comprueba la configuración combinada (no inicia contenedores):

```bash
docker compose config
```

3. Construye la imagen de Flask e inicia ambos servicios en segundo plano:

```bash
docker compose up --build -d
```

4. Comprueba los contenedores:

```bash
docker compose ps
```

Deben aparecer `web` y `db`; `db` debe llegar a estado `healthy`.

5. Revisa los logs de ambos servicios:

```bash
docker compose logs
```

Para observarlos mientras se generan:

```bash
docker compose logs -f
```

Pulsa `Ctrl+C` para dejar de seguir los logs; los contenedores continúan ejecutándose.

6. Abre <http://localhost:5000>. Completa título y contenido y pulsa **Agregar**. Para borrar una fila, pulsa su botón **Eliminar**. Ambas acciones llegan a Flask y ejecutan SQL parametrizado en MySQL.

7. Detén y elimina los contenedores sin borrar los datos:

```bash
docker compose down
```

## 9. Comprobar la persistencia

1. Crea una publicación fácil de reconocer en el navegador.
2. Ejecuta `docker compose down` (sin `-v`).
3. Inicia nuevamente:

```bash
docker compose up -d
```

4. Espera a que `docker compose ps` muestre `db` saludable y recarga <http://localhost:5000>. La publicación continúa porque `mysql_data` no fue eliminado.

## 10. Problemas frecuentes

- **“no configuration file”**: abre en VS Code la carpeta que contiene `docker-compose.yml` y ejecuta allí los comandos.
- **Falta `.env` o una variable está vacía**: crea `.env` desde `.env.example`, guarda el archivo y revisa la escritura de los seis nombres.
- **Access denied**: las credenciales del volumen se establecieron la primera vez. Revisa que `DB_USER` y `DB_PASSWORD` coincidan con los usados al crear ese volumen; no borres el volumen sin autorización del docente.
- **Unknown MySQL server host o conexión rechazada**: confirma `DB_HOST=db`, no `localhost`, y consulta `docker compose ps` y `docker compose logs db`.
- **La web aún no abre**: MySQL puede estar iniciándose. Espera a que `db` indique `healthy` y revisa `docker compose logs web`.
- **Los ejemplos nuevos de `init.sql` no aparecen**: el script solo se ejecuta normalmente al inicializar un volumen vacío; un reinicio no reinicializa datos existentes.
- **El puerto 5000 está ocupado**: detén otra aplicación que use ese puerto y repite el comando.

## 11. Comparación didáctica

| Concepto | Semana 2 | Semana 3 |
|---|---|---|
| Motor | SQLite | MySQL |
| Base de datos | archivo local | servidor de base de datos |
| Servicios | 1 | 2 (`web` y `db`) |
| Persistencia | bind mount | volumen Docker nombrado |
| Host de BD | archivo local | `db` |
| Puerto interno MySQL | no aplica | `3306` |

La interfaz casi no cambia. El cambio central de esta semana es comprender el recorrido **Flask ↔ MySQL** y la comunicación **web ↔ db**.

# Semana 4: primera entidad del sistema académico

## 1. El problema que resolvemos y lo que permanece igual

En la Semana 3 usamos `posts` como dominio genérico para comprobar la conexión. En la Semana 4 comenzamos un dominio académico real: reemplazamos **publicaciones** por **estudiantes**. No estamos construyendo un CRUD (*Create, Read, Update, Delete*; en español, **Crear, Leer/Consultar, Actualizar y Eliminar**). Esta semana implementamos únicamente la **R de Read**, es decir, consultar; todavía no implementamos C, U ni D. Queremos observar cómo una idea del modelo conceptual llega a ser una tabla consultable.

La arquitectura no cambia:

```text
Navegador → web (Flask) → db (MySQL 8.4) → mysql_data
```

También conservamos Docker Compose, las variables de entorno, el *healthcheck*, `mysql-connector-python`, el puerto 5000 y `utf8mb4`.

## 2. Entidad, atributos y dominios

Una **entidad** es algo del mundo que nos interesa representar. `ESTUDIANTE` es una entidad porque necesitamos guardar y distinguir estudiantes. Sus características, como nombre o carrera, son **atributos**. Al transformarla en una tabla, cada atributo se representa mediante una columna y cada estudiante mediante una fila.

El **dominio de un atributo** indica qué valores son válidos. Aquí usamos `INT` para un identificador numérico, `VARCHAR` para textos de longitud variable y `DATE` para una fecha. Además del tipo, restricciones como `NOT NULL` y `UNIQUE` forman parte de las reglas que limitan esos valores.

### Tipos de atributos que podemos reconocer

Al pensar en `ESTUDIANTE` también podemos clasificar los atributos. Un **atributo clave**, como `rut`, puede identificar al estudiante en el mundo real. Un **atributo simple**, como `email`, `carrera` o `fecha_ingreso`, se trata como un valor indivisible para los objetivos actuales.

Un **atributo compuesto** puede dividirse en partes con significado propio. Por ejemplo, el nombre completo `"María Elena González Soto"` podría modelarse como `nombres = "María Elena"`, `apellido_paterno = "González"` y `apellido_materno = "Soto"`. En Semana 4 conservamos `nombre VARCHAR(100)` por simplicidad pedagógica; es una decisión de modelamiento que podría refinarse después.

Un **atributo derivado** se puede calcular desde otros datos. No almacenamos `años_cursados`: si `fecha_ingreso = 2024-03-01`, los años transcurridos pueden calcularse en una fecha posterior. Si un dato puede obtenerse de manera confiable a partir de otros datos, a veces conviene calcularlo en vez de almacenarlo. Existen razones específicas para almacenar ciertos datos derivados, pero todavía no las estudiaremos.

Un **atributo multivaluado** puede tener varios valores para una entidad. `telefonos` podría incluir un teléfono personal, uno de emergencia y otro adicional. Guardarlos juntos en una sola columna dificultaría distinguirlos y consultarlos. **En Semana 4 no implementaremos todavía atributos multivaluados**; más adelante, estos casos normalmente conducen a nuevas tablas y relaciones.

| Tipo de atributo | Ejemplo en ESTUDIANTE | ¿Se almacena en Semana 4? |
| --- | --- | --- |
| Clave | `rut` | Sí |
| Sustituto | `id_estudiante` | Sí |
| Simple | `email` | Sí |
| Compuesto | `nombre` → nombres + apellidos | Por ahora se almacena como `nombre` |
| Derivado | `años_cursados` | No |
| Multivaluado | `teléfonos` | No |

La tabla resume decisiones pedagógicas del modelo actual; no agrega columnas ni tablas a la implementación.

## 3. Del modelo conceptual al modelo relacional

Primero expresamos la idea sin pensar aún en detalles de MySQL:

```text
ESTUDIANTE
- rut
- nombre
- email
- carrera
- fecha_ingreso
```

Luego la convertimos al modelo relacional:

```text
ESTUDIANTES(
    id_estudiante PK,
    rut UNIQUE NOT NULL,
    nombre NOT NULL,
    email UNIQUE NOT NULL,
    carrera NOT NULL,
    fecha_ingreso
)
```

En el **modelo conceptual** pensamos en la realidad y analizamos qué significa y de qué tipo es cada atributo. En el **modelo relacional** decidimos cómo representarlo mediante tablas, columnas, tipos y restricciones. La transformación no siempre es una copia literal: podemos agregar una clave sustituta, dividir un atributo compuesto, no almacenar un atributo derivado o reconocer que un atributo multivaluado necesitará otra tabla. Esta semana solo agregamos `id_estudiante`; no dividimos `nombre` ni implementamos nuevas tablas o relaciones.

La **clave primaria** (`PRIMARY KEY`) identifica sin ambigüedad cada fila. Una **clave candidata** es un atributo, o conjunto mínimo de atributos, que podría identificar de forma única una entidad. En este ejemplo, `rut` puede considerarse una clave candidata y natural, mientras que `id_estudiante` es la candidata elegida como clave primaria.

Una **clave natural** ya existe en el mundo real: por ejemplo, `rut = "12.345.678-9"`. Una **clave sustituta** es creada especialmente por el sistema: por ejemplo, `id_estudiante = 27`. `AUTO_INCREMENT` permite que MySQL genere ese identificador automáticamente.

```text
Estudiante A: id_estudiante = 1, rut = 11.111.111-1
Estudiante B: id_estudiante = 2, rut = 22.222.222-2
```

Ambos valores pueden identificar al estudiante, pero cumplen roles distintos. Usamos `id_estudiante` como `PRIMARY KEY` porque es pequeña, estable, no depende de datos del mundo real, facilita futuras relaciones y evita que un cambio administrativo del RUT afecte muchas referencias. Mantenemos `rut UNIQUE` para impedir que dos filas representen el mismo RUT. `email UNIQUE` aplica la misma regla al correo. `rut`, `nombre`, `email` y `carrera` usan `NOT NULL` porque son obligatorios. `fecha_ingreso` es opcional y puede contener `NULL`, es decir, un valor todavía desconocido o no registrado. `NULL` no es una cadena vacía.

Como existe una sola entidad, esta semana no necesitamos claves foráneas ni relaciones.

## 4. La tabla implementada

El problema ahora es expresar esas decisiones como SQL. `VARCHAR(n)` admite texto hasta la longitud indicada; `INT` representa enteros y `DATE` guarda fechas, no texto libre. Este es el código de `database/init.sql`:

```sql
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    carrera VARCHAR(100) NOT NULL,
    fecha_ingreso DATE NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
```

Al observarlo, relaciona cada columna con un atributo y cada tipo/restricción con su dominio. Los datos ficticios incluyen acentos y `ñ` para hacer visible que `utf8mb4` funciona correctamente.

## 5. Consulta realizada por Flask

Una vez creada la tabla, Flask necesita recuperar las filas. Un **ORM** significa *Object-Relational Mapping* (**Mapeo Objeto-Relacional**): es una técnica o herramienta que permite trabajar con tablas y filas mediante objetos del lenguaje de programación. Todavía no usamos un ORM porque queremos observar directamente el SQL, las tablas, columnas, restricciones y consultas. Mantenemos el SQL directo y visible:

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
ORDER BY id_estudiante;
```

`SELECT` elige los atributos, `FROM` indica la tabla y `ORDER BY` presenta las filas según su identificador. `app.py` ejecuta esta consulta mediante `mysql-connector-python` y entrega el resultado a `index.html`; la plantilla lo muestra en una tabla Bootstrap.

La aplicación es deliberadamente de **solo consulta**. No permite agregar, editar ni eliminar estudiantes. Esas operaciones se introducirán posteriormente, cuando la tabla y sus reglas ya sean comprensibles.

## 6. Transición desde Semana 3

`database/init.sql` se ejecuta cuando MySQL inicializa un volumen vacío. Si `mysql_data` viene de la Semana 3, puede conservar la tabla `posts` y no crear automáticamente `estudiantes`. En este laboratorio, cuyos datos son ficticios, podemos reinicializarlo:

```bash
docker compose down -v
docker compose up --build -d
```

> **Advertencia:** `docker compose down -v` elimina el volumen MySQL y **todos sus datos**. Es aceptable solo para estos datos ficticios de laboratorio. No es una estrategia apropiada para conservar datos reales. Las herramientas de migración de esquemas se estudiarán más adelante y no se incorporan esta semana.

Después, espera a que `db` esté saludable y abre <http://localhost:5000>. Debes observar cinco estudiantes, sus seis atributos y una fecha presentada como “Sin registrar”. Esto conecta las reglas del modelo con filas reales mostradas por la aplicación. La guía progresiva y su actividad se encuentran en [`docs/Semana04.md`](docs/Semana04.md).

# Semana 5: consultas SELECT y búsqueda de estudiantes

## 1. El problema: consultar lo que necesitamos

Esta semana mantenemos exactamente la entidad y la tabla `estudiantes` de la Semana 4. El objetivo es **leer** sus filas, ordenarlas por nombre y permitir que una persona busque por nombre, RUT o carrera. No agregamos, editamos ni eliminamos datos.

La consulta básica es:

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes;
```

`SELECT` indica qué columnas queremos recuperar y `FROM` indica desde qué tabla. Escribir las seis columnas, en vez de `SELECT *`, hace visible qué datos solicitamos y ayuda a relacionarlos con los atributos estudiados.

## 2. Ordenar y filtrar filas

La lista de la aplicación agrega:

```sql
ORDER BY nombre ASC;
```

`ORDER BY` ordena el resultado y `ASC` significa ascendente. Por ejemplo: Ana, José, María, Sofía y Tomás. También existe `DESC` para el orden descendente, pero esta semana no crearemos controles de orden dinámico.

`WHERE` limita las filas a las que cumplen una condición. `LIKE` compara un texto con un patrón:

```sql
WHERE nombre LIKE 'Mar%';
```

El símbolo `%` representa **cero o más caracteres**. El ejemplo puede encontrar María, Mario y Marcela. `LIKE '%ría%'` busca `ría` en cualquier posición. Nuestra aplicación forma conceptualmente `%texto%` y usa `OR` para aceptar una coincidencia en cualquiera de tres columnas:

```sql
WHERE nombre LIKE %s
   OR rut LIKE %s
   OR carrera LIKE %s
ORDER BY nombre ASC;
```

## 3. Parámetros: SQL y datos por separado

No se debe concatenar lo escrito por una persona dentro del SQL.

```text
INCORRECTO: texto del usuario → se concatena dentro del SQL
CORRECTO:   SQL con marcadores → parámetros enviados por separado
```

La consulta usa marcadores `%s` y `mysql-connector-python` recibe por separado una tupla como `('%María%', '%María%', '%María%')`. **El SQL y los datos ingresados por el usuario se envían por separado.** Esto ayuda a prevenir **SQL Injection o inyección SQL**, un problema de seguridad que puede ocurrir cuando el texto ingresado por un usuario termina siendo interpretado como parte de una instrucción SQL.

## 4. Una separación sencilla de responsabilidades

`database_connection.py` contiene `get_db_connection()`. Esta función usa `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` y `DB_PASSWORD`, conserva `utf8mb4` y evita repetir en distintas partes las instrucciones para conectarse a MySQL.

`app.py` se preocupa de recibir la petición del navegador y mostrar la respuesta. `estudiante_repository.py` se preocupa de conversar con MySQL. Aquí **repositorio** solo significa un archivo sencillo donde reunimos las consultas de estudiantes; no presentamos esta separación como una arquitectura profesional obligatoria ni agregamos capas avanzadas.

```text
Usuario escribe "María"
        ↓
Formulario envía la búsqueda
        ↓
Flask recibe "María"
        ↓
Capa sencilla de acceso a datos
        ↓
SELECT ... WHERE ... LIKE ...
        ↓
MySQL devuelve filas
        ↓
Flask entrega los resultados a index.html
        ↓
Navegador muestra los estudiantes
```

El contador usa `len(estudiantes)`, es decir, las filas ya recuperadas; no necesita otra consulta `COUNT(*)`. **CRUD** significa Create, Read, Update y Delete (Crear, Leer, Actualizar y Eliminar). Semana 5 continúa exclusivamente con **R = Read**.

## 5. Probar antes del merge

Las pruebas unitarias reemplazan temporalmente la conexión por objetos simples. Así comprueban las consultas y la página sin convertir esta semana en una unidad de infraestructura de pruebas:

```bash
python -m unittest discover -s tests -v
```

Antes del merge también se debe realizar la comprobación integrada local:

```bash
docker compose config
docker compose up --build -d
docker compose ps
```

Abre <http://localhost:5000> y comprueba: (1) lista completa ordenada por nombre, (2) búsqueda por nombre, (3) por RUT, (4) por carrera, (5) sin resultados, (6) enlace **Limpiar**, (7) contador, (8) caracteres españoles y (9) ausencia de controles INSERT, UPDATE y DELETE. No uses `docker compose down -v`: el modelo no cambió y normalmente se debe conservar el volumen de MySQL. La guía completa está en [`docs/Semana05.md`](docs/Semana05.md).

---

# Semana 6: crear estudiantes con INSERT

Hasta la Semana 5 podíamos **leer** estudiantes. Ahora también podemos **crear** uno:

```text
CRUD
C ← nuevo: Create (crear)
R ← se conserva: Read (leer)
U ← todavía no
D ← todavía no
```

## Nuestra primera instrucción INSERT

```sql
INSERT INTO estudiantes
    (rut, nombre, email, carrera, fecha_ingreso)
VALUES
    ('16.666.666-6', 'Luis Soto', 'luis@ejemplo.cl', 'Diseño', NULL);
```

- `INSERT INTO estudiantes` indica la tabla donde agregaremos una fila.
- La lista entre paréntesis indica las columnas que recibirán datos.
- `VALUES` presenta, en el mismo orden, los valores que guardaremos.

No escribimos `id_estudiante`. Como vimos en la Semana 4, su columna tiene
`AUTO_INCREMENT`: MySQL crea el siguiente ID automáticamente.

En Flask usamos marcadores y enviamos los datos por separado:

```sql
INSERT INTO estudiantes
    (rut, nombre, email, carrera, fecha_ingreso)
VALUES
    (%s, %s, %s, %s, %s)
```

Es la continuidad de la consulta parametrizada de Semana 5 (`WHERE nombre LIKE
%s`): **SQL y datos viajan separados**. Nunca pegamos texto del formulario en el
SQL. Después de ejecutar el INSERT, `connection.commit()` confirma que el cambio
debe quedar guardado. Más adelante se podrán estudiar las transacciones en mayor
profundidad.

## Del formulario a la tabla

| Formulario | Tabla `estudiantes` |
|---|---|
| RUT | `rut` |
| Nombre | `nombre` |
| Email | `email` |
| Carrera | `carrera` |
| Fecha de ingreso | `fecha_ingreso` |

`id_estudiante` no es editable porque MySQL lo genera con `AUTO_INCREMENT`.
RUT, nombre, email y carrera son obligatorios; fecha de ingreso es opcional.
Flask también hace una comprobación deliberadamente básica del email.

**GET** significa aquí: “el navegador solicita ver el formulario”. **POST**
significa: “el navegador envía a Flask los datos escritos”.

```text
GET /estudiantes/nuevo → Flask muestra el formulario
Usuario completa el formulario
POST /estudiantes/nuevo → Flask recibe → valida → INSERT → MySQL
```

Si hay un error, Flask vuelve a mostrar el formulario y conserva lo escrito para
que solo haya que corregir el campo indicado. Los mensajes Bootstrap son breves
y no muestran detalles internos de MySQL.

## Validación y reglas de la base de datos

La **validación de la aplicación** permite detectar campos vacíos o un email
evidentemente incompleto y dar ayuda amable. La **restricción de la base de
datos** protege finalmente la integridad aunque los datos lleguen por otro medio.
Como vimos en la Semana 4, `rut` y `email` tienen `UNIQUE`. Por eso MySQL rechaza
un RUT o email repetido; Flask transforma ese resultado en “Ya existe…” sin
mostrar el error técnico. La base de datos no debe depender solo del formulario.

## POST → REDIRECT → GET

1. **POST:** “entrego la ficha del nuevo estudiante”.
2. Flask ejecuta el INSERT y el commit.
3. **REDIRECT:** “Flask me indica que vuelva al listado”.
4. **GET:** “el navegador solicita la lista actualizada”.

Esto ayuda a que actualizar el navegador no vuelva a enviar accidentalmente el
formulario. `flash()` guarda un mensaje corto (“Estudiante creado
correctamente.”) para mostrarlo en la página siguiente.

## Flujo completo

```text
Usuario pulsa "Nuevo estudiante"
        ↓ GET
Flask muestra formulario
        ↓
Usuario escribe datos
        ↓ POST
Flask valida
        ↓
¿Hay error? ── sí → formulario con los mismos datos
        │ no
        ↓
INSERT parametrizado → commit → redirect → GET /
                                      ↓
                              listado actualizado
```

La guía completa, las actividades y las preguntas están en
[`docs/Semana06.md`](docs/Semana06.md). Los `Mock` y `patch` usados en pruebas
solo aíslan MySQL durante la verificación; no son contenidos centrales de esta
semana.

# Semana 7: actualizar estudiantes con UPDATE

## 1. El problema y nuestro avance en CRUD

Ya podemos crear y consultar estudiantes. Ahora necesitamos corregir o cambiar
los datos de una fila existente sin crear otra fila. Esa operación es **Update**.

```text
Semana 5          Semana 6             Semana 7
C                 C ← INSERT           C ← INSERT
R ← SELECT        R ← SELECT           R ← SELECT
U                 U                    U ← UPDATE
D                 D                    D
```

**INSERT crea una fila nueva; UPDATE cambia una fila que ya existe.** DELETE aún
no está implementado.

## 2. Nuestra primera instrucción UPDATE

```sql
UPDATE estudiantes
SET nombre = 'Ana Pérez'
WHERE id_estudiante = 3;
```

- `UPDATE estudiantes` indica la tabla que queremos modificar.
- `SET` anuncia qué columnas recibirán valores nuevos.
- `nombre = 'Ana Pérez'` indica la columna y su nuevo valor.
- `WHERE` localiza exactamente la fila que se modificará.

`UPDATE` no crea una fila. En cambio, conserva la fila 3 y cambia su nombre.

## 3. WHERE protege el alcance

Esta instrucción no tiene `WHERE` y podría cambiar la carrera de **todos**:

```sql
UPDATE estudiantes
SET carrera = 'Ingeniería';
```

La aplicación usa una condición precisa:

```sql
UPDATE estudiantes
SET carrera = 'Ingeniería'
WHERE id_estudiante = 3;
```

> **ATENCIÓN: antes de ejecutar un UPDATE, siempre debemos preguntarnos qué filas afectará la cláusula WHERE.**

## 4. Primero buscamos por clave primaria

Al pulsar **Editar**, Flask recibe el `id_estudiante`. Esta es una clave primaria
sustituta: identifica de forma estable una sola fila. Por eso se muestra como
información, pero no como campo editable.

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
WHERE id_estudiante = %s;
```

El ID viaja como parámetro, no pegado al SQL. El `SELECT` puede devolver una fila
o ninguna. Si no encuentra una, la aplicación dice “No se encontró el estudiante
solicitado.” y permite volver al listado. Si la encuentra, Flask entrega RUT,
nombre, email, carrera y fecha al formulario prellenado.

```text
id_estudiante = 3
        ↓
SELECT ... WHERE id_estudiante = %s
        ↓
MySQL devuelve una fila
        ↓
Flask entrega los datos al formulario
        ↓
Formulario aparece prellenado
```

## 5. UPDATE parametrizado y orden de los datos

La aplicación mantiene visible este SQL:

```sql
UPDATE estudiantes
SET rut = %s,
    nombre = %s,
    email = %s,
    carrera = %s,
    fecha_ingreso = %s
WHERE id_estudiante = %s;
```

Cada `%s` recibe el dato que ocupa su misma posición:

```python
(rut, nombre, email, carrera, fecha_ingreso, id_estudiante)
```

El orden importa. El último dato corresponde al `%s` de `WHERE`. SQL y datos
viajan separados: SELECT parametrizado en Semana 5, INSERT parametrizado en
Semana 6 y UPDATE parametrizado en Semana 7. Tras ejecutarlo,
`connection.commit()` confirma que el cambio debe quedar guardado, igual que con
INSERT.

## 6. Validaciones, duplicados y UNIQUE

Creación y edición reutilizan las mismas validaciones sencillas: RUT, nombre,
email y carrera obligatorios, además de un formato básico de email. La fecha
sigue siendo opcional. Si hay un error, el formulario conserva lo que el usuario
escribió para que solo corrija el campo problemático.

`rut` y `email` continúan siendo `UNIQUE`. Conservar el RUT o email del estudiante
actual es válido: sigue perteneciendo a la misma fila. Usar el valor de **otro**
estudiante no lo es. Una comprobación previa podría buscar otro registro así:

```sql
WHERE rut = %s
  AND id_estudiante <> %s
```

`<>` significa “distinto de”: buscamos otro estudiante con ese RUT. En esta
aplicación MySQL realiza la comprobación final mediante `UNIQUE`, y Flask convierte
el error en “Ya existe otro estudiante…”. Flask ayuda con mensajes amigables;
MySQL protege finalmente la integridad.

## 7. POST → Redirect → GET y flujo completo

Después de un cambio correcto reutilizamos el patrón de Semana 6:

```text
Usuario pulsa Editar
        ↓
GET /estudiantes/3/editar
        ↓
Flask obtiene id_estudiante = 3
        ↓
SELECT ... WHERE id_estudiante = %s
        ↓
MySQL devuelve el estudiante
        ↓
Formulario aparece con sus datos
        ↓
Usuario modifica campos
        ↓ POST
Flask valida
        ↓
UPDATE ... WHERE id_estudiante = %s
        ↓
commit() → flash() → redirect
        ↓
GET /
        ↓
listado actualizado
```

El redirect evita repetir el UPDATE al refrescar. Los mensajes de éxito, datos
duplicados y estudiante inexistente se muestran con alertas Bootstrap, sin
exponer mensajes internos de MySQL. La guía, actividades y preguntas están en
[`docs/Semana07.md`](docs/Semana07.md).
