# Semana 3: conexión Flask-MySQL con Docker Compose

En Semana 2 teníamos Flask y SQLite. Ahora separaremos la aplicación y la base de datos en dos servicios.

## Propósito de la semana

Mantendremos el mismo dominio de publicaciones: listar, crear y eliminar `posts` con `id`, `title` y `content`. No agregaremos nuevas entidades ni actualización. El objetivo es reconocer este recorrido:

```text
Navegador → web (Flask) → db:3306 (MySQL) → mysql_data
```

Un **servicio** de Compose describe una parte de la aplicación que corre en su propio contenedor. `web` atiende solicitudes y ejecuta Python. `db` es un servidor de base de datos: permanece esperando conexiones y ejecuta SQL para guardar o consultar datos.

SQLite era una biblioteca que trabajaba directamente con el archivo `database.db`. MySQL es otro programa, separado de Flask, y recibe conexiones mediante `mysql-connector-python`. El antiguo `database.db` ya no es la base activa.

## Las variables de entorno

Una variable de entorno entrega configuración a un programa sin escribirla en el código. Flask recibe `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` y `DB_PASSWORD`; MySQL también recibe `MYSQL_ROOT_PASSWORD`.

`.env.example` es la plantilla pública y versionada: muestra los nombres y valores didácticos, pero no contiene secretos reales. Cada estudiante crea `.env`, cambia sus claves y lo mantiene fuera de GitHub porque `.gitignore` lo excluye.

En la terminal PowerShell integrada de VS Code para Windows 10/11:

```powershell
Copy-Item .env.example .env
```

En una terminal `cmd`:

```bat
copy .env.example .env
```

Luego abre `.env`, reemplaza las claves de ejemplo y guarda. No cambies `DB_HOST=db`: Compose permite que `web` encuentre a MySQL por el nombre del servicio. `web → db:3306`. `localhost` dentro de `web` solo apunta al mismo contenedor `web`, no a `db`.

## Inicio, datos y espera

`database/init.sql` crea `posts` e inserta ejemplos. Compose lo coloca en `/docker-entrypoint-initdb.d/`; MySQL ejecuta automáticamente estos scripts normalmente **solo la primera vez que inicializa un volumen vacío**. Editar el SQL y reiniciar no lo vuelve a aplicar a un volumen ya creado. Esta semana no usamos migraciones.

`mysql_data` es un volumen nombrado administrado por Docker para los archivos de MySQL. A diferencia del bind mount `./data:/app/data` de Semana 2, no corresponde a una carpeta del proyecto elegida por nosotros.

El healthcheck pregunta mediante `mysqladmin ping` si MySQL responde. Que el contenedor esté iniciado no significa que MySQL ya esté listo para recibir conexiones; Compose espera el estado saludable antes de iniciar `web`.

Las consultas que agregan y borran usan parámetros. Los datos escritos por el usuario se entregan aparte del texto SQL, en vez de concatenarlos, para reducir el riesgo de inyección SQL.

### Codificación de caracteres y español

Una **codificación de caracteres** es una regla que relaciona los caracteres que vemos con los números que guarda el computador. En este proyecto indicamos explícitamente `utf8mb4` tanto al servidor MySQL, como a la tabla y a la conexión de Python. Es una codificación moderna de Unicode que representa correctamente letras acentuadas, la `ñ` y muchos otros símbolos.

Todos los componentes deben interpretar los bytes con la misma codificación. Si un texto UTF-8 se interpreta por error usando otra codificación, `publicación` puede mostrarse como `publicaciÃ³n`, aunque la intención original fuera correcta.

#### Volver a ejecutar `database/init.sql` en el entorno de prueba

MySQL ejecuta `database/init.sql` solamente al inicializar un volumen vacío. Si `mysql_data` ya existe, aplicar esta corrección y reiniciar no modifica automáticamente los registros anteriores. **En un entorno local de prueba donde se pueden perder todas las publicaciones**, ejecuta:

```bash
docker compose down -v
```

La opción `-v` elimina el volumen `mysql_data` y todos sus datos. No la uses sobre datos que necesites conservar ni durante la actividad normal de persistencia. Después, crea nuevamente los contenedores y el volumen vacío:

```bash
docker compose up --build -d
```

MySQL volverá a ejecutar `database/init.sql`. Cuando `docker compose ps` muestre `db` como saludable, abre <http://localhost:5000> y comprueba que `publicación`, `conexión`, `aplicación` e `información` se vean correctamente.

## Actividad guiada: PREDICCIÓN → EJECUCIÓN → OBSERVACIÓN → EXPLICACIÓN

### 1. PREDICCIÓN

Antes de ejecutar nada, dibuja qué programas esperas encontrar. Predice:

- ¿Aparecerá uno o dos servicios?
- Si creamos una publicación y eliminamos los contenedores, ¿sobrevivirá?
- ¿Qué componente guardará los datos?

### 2. EJECUCIÓN

Abre Docker Desktop. En la terminal integrada de VS Code, ubicada en el proyecto, crea `.env` y ejecuta cada comando por separado:

```bash
docker compose config
```

Este comando valida y muestra la configuración resultante.

```bash
docker compose up --build -d
```

Este comando construye `web` e inicia `web` y `db` en segundo plano.

```bash
docker compose ps
```

Identifica los dos servicios y espera hasta que `db` aparezca saludable. Si necesitas observar el inicio:

```bash
docker compose logs -f
```

Pulsa `Ctrl+C` para dejar de seguir los logs. Abre <http://localhost:5000>, crea una publicación con un título reconocible y comprueba que aparece. También puedes probar **Eliminar** sobre otra publicación.

Ahora detén y elimina los contenedores, pero conserva el volumen:

```bash
docker compose down
```

Antes de continuar, predice otra vez si tu publicación sobrevivirá. Luego inicia los servicios:

```bash
docker compose up -d
```

Comprueba el estado:

```bash
docker compose ps
```

### 3. OBSERVACIÓN

Cuando `db` esté saludable, recarga <http://localhost:5000>. Registra:

- los nombres de los dos servicios;
- el estado de `db`;
- si tu publicación continúa;
- qué ocurrió con los contenedores y qué ocurrió con los datos.

### 4. EXPLICACIÓN

`docker compose down` eliminó los contenedores, pero no `mysql_data`. Al crear contenedores nuevos, MySQL volvió a montar ese volumen y encontró la publicación. Por eso persistió.

> **No uses `docker compose down -v` en la actividad normal.** La opción `-v` sí elimina los volúmenes asociados y puede borrar los datos MySQL del proyecto.

## Preguntas para discutir

1. ¿Dónde están ahora los datos?
2. ¿Por qué ya no existe `database.db` como base activa?
3. ¿Por qué Flask utiliza `db` y no `localhost`?
4. ¿Qué diferencia existe entre `web` y `db`?
5. ¿Qué ocurriría si eliminamos `mysql_data`?
6. ¿Qué problema resuelve el healthcheck?
7. ¿Por qué `init.sql` no se ejecuta en cada reinicio?
8. ¿Por qué las consultas parametrizadas son preferibles a concatenar el texto del usuario?

## Comparación Semana 2 y Semana 3

| Concepto | Semana 2 | Semana 3 |
|---|---|---|
| Motor | SQLite | MySQL |
| Base de datos | archivo local | servidor de base de datos |
| Servicios | 1 | 2 |
| Persistencia | bind mount | volumen Docker nombrado |
| Host de BD | archivo local | `db` |
| Puerto interno MySQL | no aplica | `3306` |

## Si algo no funciona

1. Confirma que Docker Desktop esté activo.
2. Confirma que `.env` exista y contenga las seis variables sin espacios alrededor de `=`.
3. Confirma que `DB_HOST` sea `db`.
4. Ejecuta `docker compose ps`.
5. Revisa por separado:

```bash
docker compose logs db
```

```bash
docker compose logs web
```

Si MySQL aún está iniciando, espera a que el healthcheck indique `healthy`. Si las credenciales de `.env` cambiaron después de inicializar el volumen, pide ayuda al docente antes de borrar datos.
