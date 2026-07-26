# Semana 5: consultas SELECT y búsqueda de estudiantes

## 1. Qué aprenderemos

Aprenderemos a recuperar columnas con `SELECT` y `FROM`, ordenar filas con `ORDER BY`, elegir filas con `WHERE` y buscar partes de textos con `LIKE`. Finalmente relacionaremos una búsqueda del navegador con una consulta SQL parametrizada.

Al terminar, deberías poder explicar para qué sirven `SELECT`, `FROM`, `WHERE`, `ORDER BY`, `LIKE` y `%`, y por qué el texto del usuario no se concatena en SQL.

## 2. Qué sabemos desde Semana 4

Conocemos la entidad `ESTUDIANTE`, sus atributos y su tabla `estudiantes`:

```text
id_estudiante, rut, nombre, email, carrera, fecha_ingreso
```

No cambiaremos columnas, entidades ni relaciones. Seguimos trabajando solamente con lectura.

## 3. SELECT y FROM

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes;
```

- `SELECT` dice **qué columnas** queremos recuperar.
- `FROM` dice **de qué tabla** proceden.

## 4. Seleccionar columnas específicas

No usamos `SELECT *` como consulta principal. Nombrar las columnas permite ver exactamente qué datos pedimos, comprobar su orden y relacionarlos con los atributos. Si solo necesitáramos dos columnas podríamos escribir, por ejemplo, `SELECT nombre, carrera FROM estudiantes;`.

## 5. ORDER BY

Sin `ORDER BY`, no debemos suponer un orden de presentación. La aplicación usa:

```sql
ORDER BY nombre ASC;
```

`ORDER BY` ordena y `ASC` indica orden ascendente: Ana, José, María, Sofía, Tomás. `DESC` haría el orden descendente; no agregaremos controles para cambiarlo.

## 6. WHERE

`WHERE` indica una condición que deben cumplir las filas:

```sql
WHERE carrera = 'Diseño'
```

Solo se recuperan estudiantes cuya carrera sea Diseño.

## 7. LIKE

`LIKE` compara un texto con un patrón. Por ejemplo:

```sql
WHERE nombre LIKE 'Mar%'
```

Puede encontrar María, Mario y Marcela.

## 8. El comodín `%`

`%` representa cero o más caracteres. Su posición cambia el patrón:

- `Mar%`: comienza con `Mar`.
- `%ría`: termina con `ría`.
- `%ría%`: contiene `ría` en cualquier posición.

Nuestra aplicación busca contenido, por eso forma conceptualmente `%texto%`. No estudiaremos aún expresiones regulares ni búsqueda de texto completo.

## 9. Combinar condiciones con OR

`OR` significa que basta con que una de las condiciones sea verdadera:

```sql
WHERE nombre LIKE %s
   OR rut LIKE %s
   OR carrera LIKE %s
ORDER BY nombre ASC;
```

Así un solo campo permite buscar `María`, `11.111` o `Informática`.

## 10. Consultas parametrizadas

La consulta anterior contiene marcadores `%s`. El conector recibe el SQL y luego los valores:

```python
patron = f"%{texto}%"
cursor.execute(sql, (patron, patron, patron))
```

**El SQL y los datos ingresados por el usuario se envían por separado.**

```text
INCORRECTO: texto del usuario → se concatena dentro del SQL
CORRECTO:   SQL con marcadores → parámetros enviados por separado
```

No se concatena `texto` ni se inserta mediante un *f-string* dentro de `sql`. El *f-string* del ejemplo solo construye el **dato** `%texto%`, que después se entrega como parámetro.

## 11. Qué es SQL Injection

**SQL Injection o inyección SQL es un problema de seguridad que puede ocurrir cuando el texto ingresado por un usuario termina siendo interpretado como parte de una instrucción SQL.** Los parámetros ayudan a prevenirlo porque permiten que el conector trate el valor como dato, no como una parte nueva de la instrucción.

## 12. Cómo funciona la búsqueda

`get_db_connection()` concentra las instrucciones repetidas para conectarse mediante `DB_HOST`, `DB_PORT`, `DB_NAME`, `DB_USER` y `DB_PASSWORD`, usando `utf8mb4`.

`app.py` recibe la petición y muestra la respuesta. `estudiante_repository.py` conversa con MySQL. En este proyecto, **repositorio** significa solamente el archivo sencillo que reúne consultas de estudiantes; es una separación pedagógica, no una arquitectura profesional obligatoria.

```text
Usuario escribe "María" → formulario → Flask → acceso a datos
    → SELECT con WHERE, LIKE y parámetros → MySQL devuelve filas
    → Flask entrega resultados a index.html → navegador los muestra
```

Una búsqueda vacía ejecuta la consulta de todos. **Limpiar** vuelve a `/` sin criterio. Ambas consultas ordenan por nombre. La cantidad mostrada se obtiene de la lista recuperada, sin otro `COUNT(*)`.

## 13. Actividad guiada SQL

Antes de cada ejecución, escribe tu respuesta a la pregunta.

### Consulta 1

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes;
```

**Predice:** ¿qué filas esperamos obtener?

### Consulta 2

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
ORDER BY nombre ASC;
```

**Pregunta:** ¿qué cambió respecto de la consulta anterior?

### Consulta 3

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
WHERE carrera = 'Diseño'
ORDER BY nombre ASC;
```

**Pregunta:** ¿qué función cumple `WHERE`?

### Consulta 4

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
WHERE nombre LIKE '%Mar%'
ORDER BY nombre ASC;
```

**Pregunta:** ¿qué significa `%`?

Compara estas consultas manuales con el repositorio: el formulario requiere tres condiciones `LIKE` unidas mediante `OR`, marcadores y parámetros porque el texto viene de una persona.

## 14. PREDICCIÓN → EJECUCIÓN → OBSERVACIÓN → EXPLICACIÓN

### PREDICCIÓN

Antes de buscar `Ingeniería`, anota qué estudiantes crees que aparecerán y en qué orden.

### EJECUCIÓN

Abre <http://localhost:5000>, escribe `Ingeniería` y pulsa **Buscar**.

### OBSERVACIÓN

Anota cuántos registros aparecieron, sus nombres y sus carreras. Pulsa **Limpiar** y observa qué cambia.

### EXPLICACIÓN

Explica el resultado usando las palabras `WHERE`, `LIKE`, `OR` y `%`. Indica también por qué los nombres están ordenados.

## 15. Preguntas de reflexión

1. ¿Qué diferencia existe entre `SELECT` y `FROM`?
2. ¿Qué filas elimina conceptualmente un `WHERE`?
3. ¿Qué diferencia hay entre `Mar%` y `%Mar%`?
4. ¿Por qué usamos tres condiciones unidas por `OR`?
5. ¿Por qué enviamos el SQL y el texto por separado?
6. ¿Por qué no necesitamos `COUNT(*)` para el contador actual?

## 16. Qué todavía NO hemos implementado

CRUD significa Create, Read, Update y Delete (Crear, Leer, Actualizar y Eliminar). Solo implementamos **R = Read**. No hay `INSERT`, formularios de creación, `UPDATE`, edición, `DELETE`, paginación, autenticación, JavaScript, ORM ni búsqueda avanzada.

## 17. Qué aprendimos

Podemos seleccionar columnas explícitas, indicar su tabla, filtrar y ordenar filas, y buscar partes de texto. También podemos seguir el recorrido navegador–Flask–MySQL y explicar por qué una consulta parametrizada mantiene separados el SQL y los datos.

Antes del merge ejecuta `docker compose config`, `docker compose up --build -d` y `docker compose ps`; abre la aplicación y revisa lista, tres tipos de búsqueda, cero resultados, Limpiar, contador, caracteres españoles y ausencia de controles de escritura. Como el modelo no cambia, no uses `docker compose down -v` normalmente: conserva el volumen existente.
