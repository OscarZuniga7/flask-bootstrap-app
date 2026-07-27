# Semana 7: actualizar estudiantes con UPDATE

## 1. Qué aprenderemos

Aprenderemos a seleccionar una fila, mostrar sus datos, validarlos y modificarla
con `UPDATE`, `WHERE` y `commit()`.

## 2. De dónde venimos

En Semana 5 leímos con `SELECT`. En Semana 6 creamos con `INSERT`. Ya conocemos
formularios GET/POST, parámetros, validaciones y Post/Redirect/Get.

## 3. CRUD: ahora agregamos UPDATE

```text
Semana 5          Semana 6             Semana 7
C                 C ← INSERT           C ← INSERT
R ← SELECT        R ← SELECT           R ← SELECT
U                 U                    U ← UPDATE
D                 D                    D
```

DELETE todavía no está implementado.

## 4. Qué significa actualizar

Actualizar significa cambiar datos de una fila que ya existe. Por ejemplo,
corregir un nombre o cambiar una carrera.

## 5. INSERT frente a UPDATE

- `INSERT`: crea una fila nueva.
- `UPDATE`: cambia una fila existente.

## 6. Nuestra primera instrucción UPDATE

```sql
UPDATE estudiantes
SET nombre = 'Ana Pérez'
WHERE id_estudiante = 3;
```

`UPDATE estudiantes` elige la tabla. `SET` indica las columnas que recibirán
valores nuevos. `nombre = ...` es el nuevo valor. `WHERE` indica la fila exacta.
UPDATE no crea otra fila.

## 7. SET

`SET` une una columna con su nuevo valor. Podemos cambiar una o varias columnas,
pero solo las indicadas.

## 8. WHERE

`WHERE id_estudiante = 3` limita el cambio a la fila identificada con 3.

> **ATENCIÓN: antes de ejecutar un UPDATE, siempre debemos preguntarnos qué filas afectará la cláusula WHERE.**

## 9. ¿Qué ocurriría sin WHERE?

```sql
UPDATE estudiantes
SET carrera = 'Ingeniería';
```

Sin `WHERE`, esta instrucción podría cambiar **todos** los estudiantes. No la
ejecutaremos. Esta versión tiene un alcance preciso:

```sql
UPDATE estudiantes
SET carrera = 'Ingeniería'
WHERE id_estudiante = 3;
```

## 10. La clave primaria para localizar una fila

`id_estudiante` es una clave primaria sustituta. Identifica una fila de forma
estable. Por eso lo usamos en `WHERE` y no permitimos editarlo manualmente. Sí se
pueden editar RUT, nombre, email, carrera y fecha de ingreso.

## 11. SELECT antes de editar

```sql
SELECT id_estudiante, rut, nombre, email, carrera, fecha_ingreso
FROM estudiantes
WHERE id_estudiante = %s;
```

El ID se envía como parámetro. Un `SELECT` puede devolver una fila o ninguna; la
aplicación debe manejar las dos posibilidades.

## 12. Formulario prellenado

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

Así podemos ver los valores anteriores y modificar solo lo necesario.

## 13. UPDATE parametrizado

```sql
UPDATE estudiantes
SET rut = %s,
    nombre = %s,
    email = %s,
    carrera = %s,
    fecha_ingreso = %s
WHERE id_estudiante = %s;
```

Los parámetros siguen exactamente ese orden:

```python
(
    rut,
    nombre,
    email,
    carrera,
    fecha_ingreso,
    id_estudiante
)
```

El orden importa: cada dato ocupa el lugar de su `%s`. Nunca concatenamos datos
ni usamos f-strings para construir SQL. La regla sigue siendo **SQL y datos
viajan separados**: SELECT en Semana 5, INSERT en Semana 6 y UPDATE en Semana 7.

## 14. commit

Después de un UPDATE correcto llamamos a `connection.commit()`: **commit confirma
que el cambio debe quedar guardado**. Es la misma idea usada con INSERT, sin
entrar todavía en teoría avanzada de transacciones.

## 15. Validaciones

Reutilizamos las reglas de creación: RUT, nombre, email y carrera son
obligatorios; el email tiene una comprobación básica; la fecha es opcional. Si
algo falla, conservamos todos los valores escritos para corregir solo el error.

## 16. UNIQUE al editar

MySQL mantiene `UNIQUE` para RUT y email. Un estudiante puede conservar sus
propios valores. El conflicto aparece al intentar usar el RUT o email de **otro**
estudiante. Flask muestra una explicación amable y MySQL conserva la protección
final de la integridad.

## 17. Excluir el registro actual

Una comprobación previa puede preguntar si existe otro estudiante:

```sql
WHERE rut = %s
  AND id_estudiante <> %s
```

`<>` significa “distinto de”. Es decir: “buscamos otro estudiante que tenga ese
mismo RUT”. La misma idea sirve para email. La aplicación deja la decisión final
a las restricciones `UNIQUE`, que aceptan conservar el valor de la propia fila.

## 18. Estudiante inexistente

Si `/estudiantes/999/editar` no encuentra una fila, no mostramos un traceback.
Mostramos “No se encontró el estudiante solicitado.” y volvemos al listado.

## 19. Post/Redirect/Get

```text
POST → UPDATE → commit() → flash() → redirect → GET / → listado actualizado
```

Reutilizamos el patrón de INSERT. Al refrescar el listado no se repite el UPDATE.

## 20. Actividad guiada

Antes:

```text
id_estudiante = 3
nombre = "María Núñez"
carrera = "Diseño"
```

Queremos cambiar únicamente `carrera = "Diseño Digital"`:

```sql
UPDATE estudiantes
SET carrera = 'Diseño Digital'
WHERE id_estudiante = 3;
```

Antes de probar en la aplicación, responde:

1. ¿Qué tabla se modifica?
2. ¿Qué columna cambia?
3. ¿Qué fila cambia?
4. ¿Qué función cumple `WHERE`?
5. ¿Cambian los demás estudiantes?
6. ¿Cambia `id_estudiante`?

Luego pulsa **Editar** junto a María y realiza el mismo cambio.

## 21. PREDICCIÓN → EJECUCIÓN → OBSERVACIÓN → EXPLICACIÓN

### Actividad A: una carrera

**PREDICCIÓN:** ¿qué ocurrirá si cambiamos la carrera de María Núñez? ¿Cambiará
también la carrera de Ana Muñoz?

**EJECUCIÓN:** edita únicamente a María.

**OBSERVACIÓN:** vuelve al listado y compara ambas filas.

**EXPLICACIÓN:** relaciona el resultado con `UPDATE`, `SET`, `WHERE` y `PRIMARY
KEY`.

### Actividad B: UNIQUE

**PREDICCIÓN:** ¿qué ocurrirá si intentamos cambiar el RUT de María por el RUT
que ya tiene Ana?

**EJECUCIÓN:** inténtalo mediante el formulario.

**OBSERVACIÓN:** lee el mensaje y comprueba que se conservan los datos escritos.

**EXPLICACIÓN:** relaciona el resultado con `UNIQUE`, integridad,
`id_estudiante`, registro actual y otro registro. El propio RUT es válido; el de
otra fila no.

## 22. Preguntas de reflexión

- ¿Por qué UPDATE no aumenta la cantidad de filas?
- ¿Qué podría suceder si faltara `WHERE`?
- ¿Por qué usamos la clave primaria para elegir la fila?
- ¿Por qué importa el orden de los parámetros?
- ¿Qué responsabilidades tienen Flask y MySQL ante un duplicado?
- ¿Por qué el formulario conserva los datos cuando hay un error?

## 23. Qué todavía NO hemos implementado

No implementamos DELETE, botón Eliminar, ORM, autenticación, JavaScript, edición
masiva, columnas dinámicas, procedimientos, triggers ni transacciones avanzadas.
La semana se concentra exclusivamente en **UPDATE + WHERE**.

## 24. Qué aprendimos

Seleccionamos una fila por su clave primaria, prellenamos un formulario,
reutilizamos validaciones, ejecutamos un UPDATE parametrizado con un WHERE
preciso, confirmamos con commit y regresamos al listado mediante
Post/Redirect/Get.
