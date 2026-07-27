# Semana 6: crear estudiantes con INSERT

## 1. Qué aprenderemos

Agregaremos **CREATE** sin perder **READ**. Crearemos una fila con `INSERT`, la
confirmaremos con `commit` y volveremos a verla en el listado. No haremos UPDATE
ni DELETE.

## 2. De dónde venimos: Semana 5

En Semana 5 leímos filas con `SELECT`, ordenamos con `ORDER BY` y buscamos con un
parámetro. La lista, búsqueda por nombre, RUT o carrera, botón **Limpiar** y
contador siguen disponibles.

## 3. CRUD: ahora agregamos CREATE

```text
Semana 5             Semana 6
C                    C ← nuevo
R ← trabajado        R ← se conserva
U                    U
D                    D
```

CRUD agrupa crear, leer, actualizar y eliminar. Esta semana usamos solo C + R.

## 4. Nuestra primera instrucción INSERT

```sql
INSERT INTO estudiantes
    (rut, nombre, email, carrera, fecha_ingreso)
VALUES
    ('16.666.666-6', 'Luis Soto', 'luis@ejemplo.cl', 'Diseño', NULL);
```

Esta instrucción agrega una nueva fila a la tabla existente.

## 5. INSERT palabra por palabra

- `INSERT INTO estudiantes`: indica en qué tabla agregamos la fila.
- `(rut, nombre, email, carrera, fecha_ingreso)`: nombra las columnas receptoras.
- `VALUES`: introduce los valores, que corresponden por posición a las columnas.
- `NULL`: indica que aquí la fecha opcional no tiene valor.

## 6. AUTO_INCREMENT

En Semana 4 definimos `id_estudiante` como `PRIMARY KEY AUTO_INCREMENT`. Por eso
no lo incluimos: MySQL asigna un ID distinto automáticamente.

## 7. Del formulario a las columnas

| Campo visible | Columna |
|---|---|
| RUT | `rut` |
| Nombre | `nombre` |
| Email | `email` |
| Carrera | `carrera` |
| Fecha de ingreso | `fecha_ingreso` |

El ID no aparece como campo editable: lo genera MySQL.

## 8. GET: mostrar el formulario

GET significa aquí: “el navegador solicita ver el formulario”.

```text
GET /estudiantes/nuevo
        ↓
Flask muestra el formulario
```

## 9. POST: enviar el formulario

POST significa aquí: “el navegador envía a Flask los datos que escribimos”.

```text
Usuario completa formulario → POST /estudiantes/nuevo → Flask recibe los datos
```

No necesitamos profundizar todavía en HTTP para reconocer estas dos tareas.

## 10. Validar antes de guardar

Flask comprueba que RUT, nombre, email y carrera no estén vacíos. Fecha de ingreso
puede quedar vacía. La comprobación de email solo detecta errores evidentes: debe
haber texto, una `@` y un dominio con punto. No pretende validar todos los emails
del mundo.

Si algo falla, el formulario conserva lo escrito. Así la persona corrige solo el
campo incorrecto en vez de comenzar nuevamente; esto mejora su experiencia sin
JavaScript.

## 11. INSERT parametrizado

```sql
INSERT INTO estudiantes
    (rut, nombre, email, carrera, fecha_ingreso)
VALUES
    (%s, %s, %s, %s, %s)
```

Los marcadores `%s` no se reemplazan armando texto. El conector recibe por un
lado el SQL y por otro una tupla de valores. Es la misma idea de Semana 5:

```sql
SELECT ... WHERE nombre LIKE %s
```

**SQL y datos viajan separados.**

## 12. commit

El INSERT prepara un cambio en la base de datos. `connection.commit()` confirma
que ese cambio debe quedar guardado. Dejaremos la teoría avanzada de
transacciones para más adelante.

## 13. NOT NULL y campos obligatorios

Los asteriscos del formulario ayudan a reconocer los cuatro datos obligatorios.
En MySQL, sus columnas mantienen `NOT NULL`. La fecha mantiene `NULL` permitido.

## 14. UNIQUE y duplicados

Las reglas de Semana 4 siguen vigentes:

- `rut` es `UNIQUE`;
- `email` es `UNIQUE`.

Si repetimos uno, MySQL rechaza el INSERT. Flask muestra “Ya existe un estudiante
con ese RUT” o “Ya existe un estudiante con ese correo electrónico”, nunca el
mensaje técnico interno.

## 15. Aplicación y base de datos: quién valida qué

La aplicación revisa datos para responder de forma amable. La base de datos
protege finalmente sus reglas con `NOT NULL` y `UNIQUE`, incluso si alguien no
usa nuestro formulario. Por eso no debemos confiar únicamente en la interfaz.

## 16. Qué ocurre si hay un error

Flask muestra una alerta Bootstrap, marca el campo y vuelve a colocar sus valores.
No se ejecuta un INSERT si faltan campos o el email básico es inválido. El botón
**Cancelar** vuelve al listado sin guardar.

## 17. Post/Redirect/Get

```text
POST: entrego la ficha
  ↓ INSERT + commit
REDIRECT: Flask indica volver al listado
  ↓
GET: el navegador solicita la lista actualizada
```

Así, actualizar el navegador después del éxito no reenvía accidentalmente la
ficha. `flash()` guarda un mensaje corto para mostrarlo una sola vez tras la
redirección.

## 18. Actividad guiada

Lee primero:

```sql
INSERT INTO estudiantes
    (rut, nombre, email, carrera, fecha_ingreso)
VALUES
    ('17.777.777-7', 'Elena Díaz', 'elena@ejemplo.cl', 'Historia', NULL);
```

Antes de ejecutar, responde:

1. ¿En qué tabla se insertará la nueva fila?
2. ¿Qué columnas recibirán valores?
3. ¿Por qué no aparece `id_estudiante`?
4. ¿Qué columna puede quedar sin valor?
5. ¿Qué ocurriría si repetimos el RUT?

Ahora crea los mismos datos con **Nuevo estudiante** y búscalos en el listado.
Ambas vías llegan a la misma tabla:

```text
SQL manual ↔ Formulario Flask ↔ misma tabla MySQL
```

## 19. Predicción → ejecución → observación → explicación

### Actividad A: el ID

- **PREDICCIÓN:** ¿qué ocurrirá con `id_estudiante` si no escribimos ningún ID?
- **EJECUCIÓN:** crea un estudiante desde el formulario.
- **OBSERVACIÓN:** vuelve al listado y observa el ID nuevo.
- **EXPLICACIÓN:** relaciónalo con `PRIMARY KEY`, `AUTO_INCREMENT` e `INSERT`.

### Actividad B: un RUT repetido

- **PREDICCIÓN:** ¿qué ocurrirá al ingresar nuevamente el mismo RUT?
- **EJECUCIÓN:** inténtalo desde el formulario.
- **OBSERVACIÓN:** lee el mensaje y comprueba que tus datos siguen visibles.
- **EXPLICACIÓN:** relaciónalo con `UNIQUE` y la integridad de los datos.

## 20. Preguntas de reflexión

1. ¿Por qué SQL y valores se envían separados?
2. ¿Qué diferencia hay entre validar en Flask y aplicar `UNIQUE` en MySQL?
3. ¿Qué confirma `commit()`?
4. ¿Por qué redirigimos después de guardar?
5. ¿Por qué conservar lo escrito ayuda a la persona usuaria?

## 21. Qué todavía NO hemos implementado

No hay UPDATE, DELETE, botones Editar o Eliminar, ORM, autenticación, JavaScript,
validación compleja ni nuevas tablas o relaciones.

## 22. Qué aprendimos

```text
Nuevo estudiante → GET → formulario → POST → validación
                                      ↓ correcto
                         INSERT parametrizado → commit
                                      ↓
                               redirect → GET /
                                      ↓
                              listado actualizado
```

Ahora la aplicación crea y lee estudiantes, mientras MySQL conserva las reglas
del mismo modelo relacional.
