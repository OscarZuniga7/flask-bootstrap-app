# Semana 4: primera entidad del sistema académico

## 1. Qué aprenderemos

Esta semana resolveremos un problema pequeño: representar estudiantes reales del dominio académico mediante una tabla relacional y mostrarlos en el navegador. Aprenderemos a reconocer una **entidad**, sus **atributos** y sus **dominios**; a distinguir claves naturales y sustitutas; y a interpretar `PRIMARY KEY`, `AUTO_INCREMENT`, `NOT NULL`, `UNIQUE`, `VARCHAR`, `INT`, `DATE` y `NULL`.

No aprenderemos una tecnología nueva ni construiremos todavía un CRUD (*Create, Read, Update, Delete*; en español, **Crear, Leer/Consultar, Actualizar y Eliminar**). Semana 4 implementa solamente la **R de Read**, es decir, consultar. Todavía no implementamos C, U ni D. La meta es poder explicar el recorrido desde la idea `ESTUDIANTE` hasta filas almacenadas en MySQL.

## 2. Conexión con Semana 3

En la Semana 3 conectamos dos servicios y comprobamos que los datos persistían:

```text
Navegador → web (Flask) → db (MySQL 8.4) → mysql_data
```

Ese recorrido permanece igual. Conservamos Docker Compose, `mysql-connector-python`, variables de entorno, el *healthcheck*, el volumen, el puerto 5000 y `utf8mb4`. Solo cambia el tema de los datos y lo que Flask consulta.

## 3. Del dominio publicaciones al dominio académico

Antes usamos `posts` o publicaciones como ejemplo genérico. Ahora necesitamos que el proyecto comience a hablar el lenguaje de una institución educativa. Por eso el nuevo objeto de interés es el estudiante:

| Semana 3 | Semana 4 |
|---|---|
| Publicaciones: dominio genérico | Estudiantes: dominio académico |
| Servía para probar Flask y MySQL | Sirve para estudiar el paso a una tabla |

Eliminar el formulario y los botones de modificación también nos permite concentrarnos en el modelo, no en un CRUD.

## 4. ¿Qué es una entidad?

Una **entidad** es una persona, objeto, lugar o concepto del mundo sobre el cual necesitamos guardar información. No es todavía una tabla: primero es una idea del problema que estamos estudiando.

Por ejemplo, una institución necesita distinguir a sus estudiantes y conocer algunos datos de cada uno. Por ello, **ESTUDIANTE es una entidad** del dominio académico.

## 5. La entidad ESTUDIANTE

En esta primera versión interesa conocer el RUT, el nombre, el email, la carrera y la fecha de ingreso. Cada estudiante puede tener valores distintos, pero todos se describen mediante el mismo conjunto de características.

Usaremos pocos datos y ninguna otra entidad. En consecuencia, aún no existen relaciones ni claves foráneas.

## 6. ¿Qué es un atributo?

Un **atributo** es una característica que describe una entidad. `nombre` describe cómo se llama un estudiante y `carrera` indica qué estudia. Al implementar el modelo relacional, cada atributo pasa a ser una **columna** y cada estudiante pasa a ser una **fila**.

## 7. Dominio y tipo de datos

El **dominio** es el conjunto de valores que aceptamos para un atributo. El tipo de datos es una parte de esa definición; las restricciones aportan otras reglas.

| Atributo | Tipo | Explicación sencilla |
|---|---|---|
| `id_estudiante` | `INT` | Guarda un número entero. |
| `rut` | `VARCHAR(15)` | Guarda texto de longitud variable, hasta 15 caracteres. |
| `nombre` | `VARCHAR(100)` | Los nombres son texto, no cantidades numéricas. |
| `email` | `VARCHAR(120)` | Un correo combina letras y otros caracteres. |
| `carrera` | `VARCHAR(100)` | Una carrera se expresa como texto. |
| `fecha_ingreso` | `DATE` | Guarda una fecha con significado de calendario. |

`VARCHAR` no obliga a que todos los textos ocupen el máximo indicado. `DATE` es preferible a escribir una fecha como texto porque MySQL conoce que el valor representa una fecha. `utf8mb4` permite conservar correctamente nombres como “María Núñez”.

### Tipos de atributos en el modelo conceptual

Antes de crear columnas podemos reconocer distintos tipos de atributos en `ESTUDIANTE`:

- **Atributo clave:** puede identificar de forma única a la entidad. `rut` puede identificar al estudiante en el mundo real. En el modelo relacional elegimos `id_estudiante` como clave primaria sustituta y conservamos `rut` como `UNIQUE`.
- **Atributo simple:** para los objetivos actuales se trata como un valor indivisible. `email`, `carrera` y `fecha_ingreso` son ejemplos.
- **Atributo compuesto:** conceptualmente puede descomponerse en partes con significado. El nombre completo `"María Elena González Soto"` podría dividirse en `nombres = "María Elena"`, `apellido_paterno = "González"` y `apellido_materno = "Soto"`. En Semana 4 mantenemos `nombre VARCHAR(100)` por simplicidad pedagógica. Es una decisión de modelamiento que podría refinarse más adelante.
- **Atributo derivado:** puede calcularse a partir de otros datos. No almacenamos `años_cursados`: con `fecha_ingreso = 2024-03-01`, podemos calcular los años transcurridos en una fecha posterior. Si un dato puede obtenerse de manera confiable a partir de otros datos, a veces conviene calcularlo en vez de almacenarlo. En situaciones específicas sí se almacenan datos derivados, pero eso no se estudiará todavía.
- **Atributo multivaluado:** puede contener varios valores para una entidad. Un estudiante podría tener teléfono personal, de emergencia y adicional. Guardar `"987654321,912345678"` en una sola columna dificultaría separar y consultar cada teléfono. **En Semana 4 no implementaremos todavía atributos multivaluados**. Más adelante, estos casos normalmente conducen a nuevas tablas y relaciones.

| Tipo de atributo | Ejemplo en ESTUDIANTE | ¿Se almacena en Semana 4? |
| --- | --- | --- |
| Clave | `rut` | Sí |
| Sustituto | `id_estudiante` | Sí |
| Simple | `email` | Sí |
| Compuesto | `nombre` → nombres + apellidos | Por ahora se almacena como `nombre` |
| Derivado | `años_cursados` | No |
| Multivaluado | `teléfonos` | No |

Esta tabla resume decisiones pedagógicas del modelo actual. No significa que hayamos agregado `años_cursados`, teléfonos, columnas o tablas nuevas.

## 8. Modelo conceptual de ESTUDIANTE

Primero expresamos qué información existe, sin detallar todavía su implementación:

```text
ESTUDIANTE
- rut
- nombre
- email
- carrera
- fecha_ingreso
```

Esto es un **modelo conceptual**: habla del dominio y es comprensible sin conocer MySQL.

En este nivel pensamos en la realidad: qué es un estudiante, qué datos lo describen y si sus atributos son claves, simples, compuestos, derivados o multivaluados. Todavía no decidimos necesariamente una columna para cada idea.

## 9. Transformación al modelo relacional

Al pasar al modelo relacional agregamos un identificador interno y expresamos reglas:

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

La entidad se convierte en una tabla; los atributos, en columnas; los dominios, en tipos y restricciones; y cada caso concreto, en una fila. El plural `estudiantes` es el nombre elegido para la tabla que reúne muchas filas de estudiantes.

La transformación no siempre es una copia literal. Podemos agregar una clave sustituta, dividir un atributo compuesto, decidir no almacenar un atributo derivado o concluir que un atributo multivaluado requerirá otra tabla. En Semana 4 solo agregamos `id_estudiante`: mantenemos `nombre` en una columna, no almacenamos `años_cursados` ni teléfonos y no creamos relaciones. Estas posibilidades preparan decisiones posteriores sin introducir todavía normalización formal.

## 10. Tabla `estudiantes`

El problema siguiente es comunicar ese modelo a MySQL. Para ello usamos `CREATE TABLE`, una instrucción SQL que define la estructura antes de guardar filas.

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

Al leerla, observa que cada línea corresponde a una columna y que el final mantiene la configuración de caracteres de la Semana 3.

## 11. Explicación paso a paso del `CREATE TABLE`

1. `CREATE TABLE IF NOT EXISTS estudiantes` crea la tabla si aún no existe.
2. `id_estudiante INT` define un número entero.
3. `AUTO_INCREMENT` pide a MySQL generar automáticamente el siguiente identificador.
4. `PRIMARY KEY` convierte esa columna en el identificador principal de cada fila.
5. `rut VARCHAR(15) NOT NULL UNIQUE` admite texto, exige un valor y prohíbe repetirlo.
6. `nombre VARCHAR(100) NOT NULL` exige un nombre textual.
7. `email VARCHAR(120) NOT NULL UNIQUE` exige un correo diferente para cada estudiante.
8. `carrera VARCHAR(100) NOT NULL` exige indicar la carrera.
9. `fecha_ingreso DATE NULL` acepta una fecha o la ausencia de un valor conocido.
10. `CHARACTER SET` y `COLLATE` conservan correctamente caracteres del español.

La combinación de estas líneas lleva las decisiones del modelo hasta la base de datos, que puede hacerlas cumplir.

## 12. Clave primaria

Una **clave primaria** identifica de manera única cada fila. No puede repetirse ni ser `NULL`. Aquí es `id_estudiante`; por eso dos filas nunca comparten el mismo identificador, aunque dos personas pudieran tener nombres iguales.

## 13. Clave natural

Una **clave natural** es un atributo que ya existe en el mundo real y puede identificar una entidad. Por ejemplo, `rut = "12.345.678-9"` no fue inventado por nuestra aplicación y esperamos que distinga a una persona.

Una **clave candidata** es un atributo, o conjunto mínimo de atributos, que podría identificar de forma única una entidad. En nuestro ejemplo, `rut` puede considerarse una clave candidata y natural. Entre las posibilidades, elegimos `id_estudiante` como `PRIMARY KEY`.

## 14. Clave sustituta

Una **clave sustituta** es un identificador creado especialmente por el sistema para identificar cada fila. Por ejemplo, `id_estudiante = 27` no describe al estudiante: es un entero interno generado con `AUTO_INCREMENT`.

## 15. ¿Por qué `id_estudiante` y `rut` cumplen funciones distintas?

Observemos dos ejemplos sencillos:

```text
Estudiante A:
id_estudiante = 1
rut = 11.111.111-1

Estudiante B:
id_estudiante = 2
rut = 22.222.222-2
```

En cada caso, ambos valores pueden identificar al estudiante, pero cumplen roles distintos. `rut` es un dato natural del mundo real; `id_estudiante` es el identificador interno elegido como `PRIMARY KEY`. Mantenemos `rut UNIQUE`, de modo que su función identificadora no se pierde y MySQL rechaza duplicados.

Como ventajas introductorias, `id_estudiante` es pequeña, estable, no depende de datos del mundo real, facilita futuras relaciones entre tablas y evita que un cambio administrativo en una clave natural afecte muchas referencias. No profundizaremos todavía en rendimiento ni diseño físico avanzado.

Esta es una decisión introductoria del modelo. Más adelante se podrán analizar otros criterios y consecuencias, sin complicar la actividad actual.

## 16. Restricción `NOT NULL`

`NOT NULL` dice que una columna es obligatoria. Un estudiante de esta tabla debe tener `rut`, `nombre`, `email` y `carrera`. Si intentamos insertar una fila sin uno de ellos, MySQL la rechazará. La regla está en la base de datos y no depende solamente de la pantalla.

## 17. Restricción `UNIQUE`

`UNIQUE` prohíbe que se repita un valor entre filas. Lo aplicamos a `rut` y `email`. Si intentamos insertar un segundo RUT o correo igual, MySQL rechazará la operación. Nombre y carrera no son únicos: varias personas pueden llamarse igual o estudiar la misma carrera.

## 18. `fecha_ingreso`, un campo opcional, y `NULL`

Puede que todavía no conozcamos la fecha de ingreso. Por eso `fecha_ingreso` admite `NULL`. En esta introducción, `NULL` significa “no hay un valor conocido o registrado”. No equivale a `''`: una cadena vacía sí es un valor de texto, mientras que `NULL` representa ausencia de valor. La plantilla muestra esa ausencia como “Sin registrar”, pero el valor almacenado sigue siendo `NULL`.

## 19. Datos ficticios iniciales

Después de crear la tabla, `database/init.sql` inserta cinco estudiantes completamente ficticios:

```sql
INSERT INTO estudiantes (rut, nombre, email, carrera, fecha_ingreso) VALUES
    ('11.111.111-1', 'Ana Muñoz', 'ana.munoz@example.com', 'Ingeniería Informática', '2026-03-02'),
    ('12.222.222-2', 'José Pérez', 'jose.perez@example.com', 'Administración Pública', '2026-03-02'),
    ('13.333.333-3', 'María Núñez', 'maria.nunez@example.com', 'Diseño', '2025-03-03'),
    ('14.444.444-4', 'Tomás Peña', 'tomas.pena@example.com', 'Contabilidad', NULL),
    ('15.555.555-5', 'Sofía González', 'sofia.gonzalez@example.com', 'Ingeniería Comercial', '2026-03-02');
```

Observa que omitimos `id_estudiante` para que `AUTO_INCREMENT` lo genere y que una fila usa `NULL`. Los acentos y las eñes permiten comprobar visualmente `utf8mb4`. Estos RUT y correos existen solo para la demostración y no representan personas reales.

## 20. Consulta `SELECT` utilizada por Flask

Ahora necesitamos leer, no modificar. Un **ORM** significa *Object-Relational Mapping* (**Mapeo Objeto-Relacional**): es una técnica o herramienta que permite trabajar con tablas y filas de una base de datos mediante objetos del lenguaje de programación. No usamos un ORM todavía porque queremos observar directamente SQL, tablas, columnas, restricciones y consultas. Flask ejecuta SQL directo con `mysql-connector-python`:

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
ORDER BY id_estudiante;
```

`SELECT` enumera las columnas que queremos observar; `FROM` identifica la tabla; `ORDER BY` ordena el resultado por ID. No hay valores externos en esta consulta. Cuando más adelante una consulta los reciba, se mantendrá el uso de parámetros en lugar de concatenar texto.

## 21. Cómo Flask obtiene los estudiantes desde MySQL

Al visitar `/`, el navegador solicita la página. La función `index` abre una conexión usando las variables `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` y `DB_PASSWORD`; crea un cursor, ejecuta el `SELECT`, recupera las filas y cierra cursor y conexión. Finalmente entrega `estudiantes` a la plantilla.

Qué observar: Flask no contiene una lista fija de estudiantes. Los datos vienen de la tabla MySQL. Esto mantiene visible la responsabilidad de cada parte: MySQL almacena y consulta; Flask coordina la solicitud.

## 22. Cómo `index.html` presenta los datos

La plantilla recorre las filas con `{% for estudiante in estudiantes %}` y produce una fila HTML por estudiante. La tabla Bootstrap muestra ID, RUT, Nombre, Email, Carrera y Fecha de ingreso. Si la fecha es `NULL`, presenta “Sin registrar”.

La plantilla no agrega, edita ni elimina. Su tarea de esta semana es solamente convertir el resultado de la consulta en información legible en el navegador.

## 23. Actividad guiada: predicción → ejecución → observación → explicación

### PREDICCIÓN

**Problema:** queremos anticipar el comportamiento de la base de datos leyendo su estructura, antes de confiar en la pantalla.

Abre `database/init.sql`, observa el `CREATE TABLE` y responde por escrito:

- ¿Qué columna identifica de manera única cada fila?
- ¿Pueden existir dos estudiantes con el mismo RUT?
- ¿Pueden existir dos estudiantes con el mismo email?
- ¿Puede existir un estudiante sin `fecha_ingreso`?
- ¿Puede existir un estudiante sin `nombre`?
- ¿Qué valores esperas que MySQL genere automáticamente?

### EJECUCIÓN

`init.sql` solo se ejecuta cuando MySQL inicializa un volumen vacío. Si vienes de la Semana 3, `mysql_data` puede contener todavía `posts`. Como el laboratorio usa exclusivamente datos ficticios, reinicia la base de prueba:

```bash
docker compose down -v
docker compose up --build -d
```

> **Advertencia importante:** `docker compose down -v` elimina el volumen MySQL y todos sus datos. Aquí es aceptable por tratarse de datos ficticios de laboratorio. **No** es un procedimiento apropiado para conservar datos reales. No introduciremos herramientas de migración todavía; se estudiarán más adelante.

Comprueba el estado:

```bash
docker compose ps
```

Espera a que `db` indique `healthy` y abre <http://localhost:5000>.

### OBSERVACIÓN

Busca cinco filas, IDs generados, nombres con tildes o `ñ` y la fila cuya fecha dice “Sin registrar”. Comprueba que no existen formularios ni botones para modificar datos.

### EXPLICACIÓN

Relaciona cada observación con el modelo:

- Los IDs diferentes provienen de `PRIMARY KEY` y `AUTO_INCREMENT`.
- RUT y email no repetidos respetan `UNIQUE`.
- Los datos obligatorios corresponden a `NOT NULL`.
- “Sin registrar” representa el `NULL` de la fecha opcional.
- RUT, nombre, email y carrera usan `VARCHAR` porque son textos variables.
- El valor de ingreso usa `DATE` porque representa una fecha.

El navegador es la evidencia visible; las reglas que explican esa evidencia están definidas en la tabla relacional.

## 24. Preguntas de reflexión

1. ¿Por qué no usamos el RUT directamente como `PRIMARY KEY`?
2. ¿Qué ventajas tiene utilizar `id_estudiante`?
3. ¿Qué ocurriría si intentáramos insertar dos estudiantes con el mismo RUT?
4. ¿Qué ocurriría con dos emails iguales?
5. ¿Por qué `fecha_ingreso` puede ser `NULL`?
6. ¿Cuál es la diferencia entre `NULL` y una cadena vacía?
7. ¿Por qué `nombre` se representa mediante `VARCHAR` y no mediante `INT`?
8. ¿Qué diferencia existe entre una entidad conceptual y una tabla física?
9. ¿Por qué varias filas sí pueden compartir una carrera?
10. ¿Qué regla explica que podamos omitir el ID al insertar?
11. ¿Por qué `rut` puede identificar a una persona y aun así usamos `id_estudiante`?
12. ¿Qué diferencia existe entre una clave natural y una sustituta?
13. ¿Qué pasaría si el formato del RUT cambiara en el futuro?
14. ¿Deberíamos guardar `años_cursados` o calcularlo desde `fecha_ingreso`?
15. ¿Por qué `nombre` podría considerarse compuesto?
16. ¿Qué problema habría en guardar `"987654321,912345678"` en una sola columna llamada `telefonos`?
17. ¿Por qué un atributo multivaluado puede conducir a otra tabla?
18. ¿Qué significa que Semana 4 solo implemente la R de CRUD?
19. ¿Por qué evitamos un ORM en esta etapa?

## 25. Qué aprendimos

Partimos de una entidad del dominio, identificamos atributos y dominios, y los transformamos en una tabla. Distinguimos la PK sustituta `id_estudiante` de la clave natural/candidata `rut`. Vimos cómo tipos y restricciones expresan reglas, cómo Flask ejecuta un `SELECT` visible y cómo una plantilla presenta sus filas.

## 26. Qué NO hemos implementado todavía

Deliberadamente no hay altas, ediciones, eliminaciones, formularios CRUD adicionales, búsquedas avanzadas, autenticación ni paginación. Tampoco hay ORM, otras entidades, relaciones, claves foráneas, normalización formal o herramientas de migración. No dividimos `nombre`, ni agregamos `años_cursados` o teléfonos. Agregar cualquiera de estas implementaciones desviaría la atención del objetivo de esta semana.

## 27. Próxima evolución del proyecto

En una evolución posterior podrán incorporarse operaciones de modificación y nuevas partes del dominio académico. Antes de hacerlo, debemos poder explicar con claridad por qué existe cada columna y qué reglas protege MySQL. Esta guía no adelanta esa implementación: cierra con una aplicación de **solo consulta**.
