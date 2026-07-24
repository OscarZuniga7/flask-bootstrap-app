# Semana 2: ejecución reproducible con Docker

## 1. Qué aprenderemos

Esta semana aprenderemos a ejecutar la misma aplicación Flask + SQLite de la Semana 1 usando Docker Compose. El objetivo no es memorizar comandos, sino comprender por qué existen y qué problema resuelven.

Al final deberías poder explicar qué es Docker, qué es una imagen, qué es un contenedor, para qué sirven `Dockerfile` y `docker-compose.yml`, por qué publicamos un puerto y cómo conservamos `database.db` con persistencia.

## 2. Conexión con la Semana 1

En la Semana 1 ejecutamos Flask directamente con Python:

```bash
python app.py
```

También inicializamos SQLite y trabajamos con la tabla `posts`. En esta semana no cambiamos el dominio funcional: seguiremos creando, viendo y eliminando publicaciones.

## 3. El problema que queremos resolver

Un problema común en programación es que una aplicación funcione en un computador y falle en otro. Puede ocurrir por diferencias de Python, librerías, rutas o configuración.

Docker ayuda a describir un entorno reproducible. Así, el proyecto no solo contiene código, sino también instrucciones para crear un ambiente de ejecución conocido.

## 4. ¿Qué es Docker?

Docker es una herramienta que permite ejecutar aplicaciones dentro de contenedores. Un contenedor es como una caja aislada: dentro están la aplicación y lo necesario para ejecutarla.

Para nuestra aplicación, Docker permite ejecutar Flask con sus dependencias sin depender tanto de la instalación local de Python del estudiante.

## 5. Imagen vs. contenedor

Una imagen es la plantilla. Un contenedor es una ejecución concreta de esa plantilla.

Analogía sencilla:

- imagen: receta de cocina;
- contenedor: plato preparado siguiendo la receta.

En este proyecto, construimos una imagen con Python, Flask y el código. Luego Docker crea un contenedor que ejecuta `python app.py`.

## 6. Dockerfile

`Dockerfile` explica cómo construir la imagen de la aplicación.

Nuestro `Dockerfile` hace esto de forma simple:

1. usa una imagen base de Python;
2. define `/app` como carpeta de trabajo;
3. copia `requirements.txt`;
4. instala las dependencias;
5. copia el resto del proyecto;
6. expone el puerto `5000`;
7. arranca la aplicación con `python app.py`.

## 7. Docker Compose

Docker Compose permite describir cómo levantar la aplicación usando un archivo llamado `docker-compose.yml`.

Esta semana usamos un único servicio: `flask_app`. No agregamos MySQL, redes avanzadas ni múltiples contenedores porque el objetivo es entender lo esencial.

## 8. Puerto

Flask escucha dentro del contenedor en el puerto `5000`. Pero el navegador está fuera del contenedor, en tu computador. Por eso publicamos el puerto:

```yaml
ports:
  - "5000:5000"
```

El número de la izquierda es el puerto del computador. El número de la derecha es el puerto dentro del contenedor.

## 9. Volumen y bind mount

Un volumen Docker y un bind mount son mecanismos distintos. Ambos pueden permitir que ciertos datos se conserven o se compartan fuera del ciclo de vida normal del contenedor.

En este proyecto de Semana 2 usamos específicamente un **bind mount** porque es fácil de ver para principiantes. Aunque `docker-compose.yml` usa la sección `volumes:`, la línea siguiente representa un bind mount:

```text
./data del computador  ->  /app/data dentro del contenedor
```

`./data` es una carpeta visible del computador del estudiante. `/app/data` es la carpeta que ve Flask dentro del contenedor. Así puedes encontrar la base en `data/database.db` después de ejecutar la aplicación con Docker, y ese archivo permanece aunque el contenedor se destruya y vuelva a crearse.

El repositorio incluye `data/.gitkeep` porque Git normalmente no conserva carpetas vacías. Ese pequeño archivo permite que `data` exista después de clonar el proyecto. En condiciones normales no necesitas crearla manualmente: al ejecutar por primera vez la aplicación con Docker se creará `data/database.db`, y ese archivo no se versionará porque está incluido en `.gitignore`.

## 10. Persistencia de SQLite

SQLite guarda datos en un archivo. Si el archivo estuviera solo dentro del contenedor, podríamos perderlo al recrear el contenedor.

Por eso configuramos la ruta:

```text
DATABASE_PATH=/app/data/database.db
```

Y conectamos `/app/data` con `./data`.

Flujo:

```text
Navegador
    ↓
Contenedor Flask
    ↓
SQLite
    ↓
Almacenamiento persistente en ./data/database.db
```

La inicialización es idempotente: si la tabla `posts` ya existe, no se borra ni se vuelve a crear desde cero.

## 11. Preparación del computador

### Windows 10/11

1. Consulta la documentación oficial de Docker Desktop para Windows en <https://www.docker.com/products/docker-desktop/> y sigue los requisitos e instrucciones vigentes de instalación.
2. Descarga Docker Desktop para Windows.
3. Ejecuta el instalador.
4. Acepta las opciones recomendadas por Docker Desktop si aparece alguna solicitud adicional. Según la configuración del equipo, puede solicitar WSL 2, virtualización u otros componentes.
5. Reinicia si el instalador lo solicita.
6. Abre Docker Desktop desde el menú Inicio.
7. Espera a que Docker indique que está funcionando.

Como comprobación sencilla, asegúrate de contar con permisos de instalación, conexión a internet y espacio libre en disco.

Comprueba en PowerShell o en la terminal de VS Code:

```bash
docker --version
```

```bash
docker compose version
```

## 12. Ejecución paso a paso

Abre una terminal en la carpeta raíz del proyecto.

### Construir y levantar

Antes del comando: Docker leerá `docker-compose.yml`, construirá la imagen desde `Dockerfile` y arrancará el contenedor.

```bash
docker compose up --build -d
```

Deberías observar que se construye la imagen y se inicia `flask_app`. Si termina sin errores, continúa.

### Comprobar estado

```bash
docker compose ps
```

Funciona correctamente si `flask_app` aparece como iniciado y muestra el puerto `5000`.

### Ver logs

```bash
docker compose logs
```

Los logs deben mostrar mensajes de Flask. Si algo falla, este comando es la primera herramienta de investigación.

### Abrir en navegador

Visita:

```text
http://localhost:5000
```

Si aparece la lista de publicaciones, Flask está funcionando dentro del contenedor.

## 13. Actividad guiada de persistencia

Antes de continuar: ¿qué crees que ocurrirá con la publicación cuando ejecutemos `docker compose down`? Anota tu respuesta antes de realizar la prueba. La actividad seguirá esta secuencia: predecir → ejecutar → observar → explicar.

1. Ejecuta:

   ```bash
   docker compose up --build -d
   ```

2. Abre `http://localhost:5000`.
3. Crea una publicación llamada `Prueba de persistencia`.
4. Verifica que aparece en la página.
5. Detén el contenedor:

   ```bash
   docker compose down
   ```

6. Vuelve a levantarlo:

   ```bash
   docker compose up --build -d
   ```

7. Entra otra vez a `http://localhost:5000`.
8. Comprueba que la publicación sigue allí.

Esto ocurre porque la base se guarda en `data/database.db`, una carpeta del proyecto conectada al contenedor mediante bind mount.

## 14. Cómo detener y volver a levantar la aplicación

Para detener:

```bash
docker compose down
```

Para volver a levantar:

```bash
docker compose up --build -d
```

Detener el contenedor no elimina `data/database.db`.

## 15. Cómo comprobar que todo funciona

Lista de comprobación:

- `docker --version` muestra una versión;
- `docker compose version` muestra una versión;
- `docker compose ps` muestra `flask_app` iniciado;
- `docker compose logs` no muestra errores críticos;
- `http://localhost:5000` abre la aplicación;
- puedes crear una publicación;
- la publicación permanece después de `docker compose down` y un nuevo `docker compose up --build -d`.

## 16. Problemas frecuentes

### `docker` no se reconoce

Docker no está instalado, la terminal no se reinició después de instalarlo o el PATH no se actualizó. Instala Docker Desktop desde la fuente oficial y abre una terminal nueva.

### Docker Desktop no está iniciado

El comando Docker puede existir, pero el motor no está corriendo. Abre Docker Desktop y espera a que termine de iniciar.

### `docker compose` no funciona

Ejecuta:

```bash
docker compose version
```

Si falla, actualiza Docker Desktop. En este curso usamos `docker compose` con espacio.

### El puerto ya está ocupado

Otro programa usa el puerto `5000`. Puedes cerrar ese programa o cambiar temporalmente `5000:5000` por `5001:5000` en `docker-compose.yml`. En ese caso abrirías `http://localhost:5001`.

### El contenedor se detiene inesperadamente

Consulta:

```bash
docker compose logs
```

Busca mensajes de error de Python, Flask, SQLite o permisos.

### `database.db` no se crea

Recuerda que el repositorio incluye `data/.gitkeep`, por lo que la carpeta `data` debería existir después de clonar correctamente. Comprueba que `docker-compose.yml` tenga `DATABASE_PATH=/app/data/database.db`, el bind mount `./data:/app/data` y que tengas permisos de escritura en la carpeta del proyecto. La aplicación crea automáticamente `data/database.db` y la tabla si no existen.

### Los datos desaparecen después de recrear el contenedor

Puede haber ocurrido una de estas situaciones:

- se eliminó la carpeta `data`;
- se cambió la ruta `DATABASE_PATH`;
- se ejecutó la aplicación sin el bind mount;
- se está mirando otro puerto o copia del proyecto.

### Cómo consultar logs para investigar

Usa:

```bash
docker compose logs
```

Si quieres seguir los logs en vivo mientras pruebas la aplicación:

```bash
docker compose logs -f
```

## 17. Preguntas de reflexión

1. ¿Qué diferencias notas entre ejecutar `python app.py` y usar Docker Compose?
2. ¿Qué problema intenta resolver una imagen Docker?
3. ¿Por qué el contenedor necesita publicar el puerto `5000`?
4. ¿Qué pasaría si SQLite guardara `database.db` solo dentro del contenedor?
5. ¿Por qué la inicialización de la tabla debe ser idempotente?

## 18. Actividad breve para estudiantes

En parejas, expliquen con un dibujo el flujo:

```text
Navegador → Contenedor Flask → SQLite → data/database.db
```

Luego respondan: ¿qué parte corresponde al computador del estudiante y qué parte corresponde al contenedor?

## 19. Qué aprendimos

Aprendimos que Docker permite ejecutar la aplicación en un ambiente aislado y reproducible. También vimos que una imagen no es lo mismo que un contenedor, que Compose simplifica la ejecución y que SQLite necesita persistencia para conservar publicaciones.

## 20. Próxima evolución del proyecto

Más adelante podremos estudiar otras formas de persistencia y separar responsabilidades en más servicios. Todavía no usaremos MySQL, Kubernetes, Swarm, CI/CD ni redes avanzadas: primero necesitábamos entender bien la ejecución reproducible de una sola aplicación Flask + SQLite.

## Comparación didáctica

| Aspecto | Semana 1: `python app.py` | Semana 2: `docker compose up --build -d` |
|---|---|---|
| Dónde se ejecuta Flask | En el sistema operativo del estudiante | Dentro de un contenedor |
| Dependencias | En el entorno virtual local | En la imagen Docker |
| Entorno virtual | Se crea y activa manualmente | No se activa manualmente para ejecutar el contenedor |
| Reproducibilidad | Depende de la configuración local | Se describe con `Dockerfile` y `docker-compose.yml` |
| Aislamiento | La app comparte más elementos con el sistema | La app corre en un ambiente aislado |
| Persistencia de SQLite | Archivo `database.db` local | Archivo `data/database.db` conectado al contenedor |
