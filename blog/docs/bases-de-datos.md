# :material-database: Bases de Datos — PostgreSQL

Cheatsheet de referencia rápida para trabajar con **PostgreSQL**: la consola `psql`, comandos DDL/DML, y las queries más usadas en el día a día.

---

## El mapa del territorio

SQL se divide en tres grandes grupos de comandos:

```mermaid
mindmap
  root((SQL))
    DDL
      CREATE
      ALTER
      DROP
      TRUNCATE
    DML
      SELECT
      INSERT
      UPDATE
      DELETE
    DCL
      GRANT
      REVOKE
```

| Categoría | Nombre completo | Para qué sirve |
|-----------|----------------|----------------|
| **DDL** | Data Definition Language | Definir la *estructura*: crear tablas, columnas, índices |
| **DML** | Data Manipulation Language | Manipular los *datos*: leer, insertar, modificar, eliminar |
| **DCL** | Data Control Language | Controlar el *acceso*: permisos y roles de usuario |

---

## psql — La consola interactiva

`psql` es el cliente de línea de comandos oficial de PostgreSQL. Es una shell interactiva: escribís una query, presionás Enter, PostgreSQL la ejecuta y devuelve el resultado.

```mermaid
flowchart LR
    terminal["Terminal / CMD"] -->|psql -U postgres -d mi_base| psql["psql\n(cliente)"]
    psql <-->|"TCP / socket"| server["PostgreSQL Server\n:5432"]
    server --- db[("mi_base")]
```

### Conectarse

```bash
# Conectarse a una base de datos local con un usuario
psql -U postgres

# Conectarse a una base de datos específica
psql -U postgres -d mi_base

# Conectarse a un servidor remoto
psql -h localhost -p 5432 -U postgres -d mi_base

# Con URL de conexión
psql postgresql://usuario:password@localhost:5432/mi_base
```

### Comandos meta (empiezan con `\`)

Los comandos que empiezan con `\` no son SQL puro: son atajos del cliente `psql` para inspeccionar la base de datos sin escribir queries largas.

| Comando | Descripción |
|---------|-------------|
| `\l` | Listar todas las bases de datos |
| `\c nombre_db` | Conectarse a otra base de datos |
| `\dt` | Listar tablas del schema actual |
| `\dt schema.*` | Listar tablas de un schema específico |
| `\d nombre_tabla` | Describir estructura de una tabla (columnas, tipos, restricciones) |
| `\d+ nombre_tabla` | Descripción detallada (incluye tamaños y comentarios) |
| `\dn` | Listar schemas |
| `\du` | Listar roles y usuarios |
| `\df` | Listar funciones definidas |
| `\dv` | Listar vistas |
| `\di` | Listar índices |
| `\timing` | Activar/desactivar tiempo de ejecución de cada query |
| `\x` | Activar/desactivar salida expandida (cada columna en su propia línea) |
| `\e` | Abrir el editor de sistema ($EDITOR) para escribir la query |
| `\i archivo.sql` | Ejecutar un archivo SQL externo |
| `\o archivo.txt` | Redirigir todo el output hacia un archivo |
| `\copy` | Importar/exportar datos en formato CSV |
| `\q` | Salir de psql |
| `\?` | Mostrar ayuda sobre todos los comandos meta |
| `\h SELECT` | Mostrar ayuda de sintaxis de un comando SQL específico |

### Historial y shortcuts

```bash
# Navegar historial: flecha arriba/abajo
# Buscar en historial: Ctrl+R
# Limpiar línea: Ctrl+C
# Salir: \q  o  Ctrl+D
```

!!! tip "Modo expandido"
    Usá `\x` para activar el modo expandido cuando una tabla tiene muchas columnas. Cada fila se muestra verticalmente, más fácil de leer.

---

## DDL — Definición de estructura

DDL define el *esqueleto* de la base de datos. Son los comandos que crean, modifican o eliminan tablas, columnas e índices. **No tocan los datos.**

```mermaid
flowchart TD
    DDL["DDL"] --> CREATE["CREATE\nCrea objetos nuevos"]
    DDL --> ALTER["ALTER\nModifica objetos existentes"]
    DDL --> DROP["DROP\nElimina objetos"]
    DDL --> TRUNCATE["TRUNCATE\nVacía una tabla"]
```

### Bases de datos

```sql
-- Crear
CREATE DATABASE mi_base;

-- Eliminar
DROP DATABASE mi_base;

-- Listar (desde psql)
\l
```

### Tablas

```sql
-- Crear tabla básica
CREATE TABLE usuarios (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(100) NOT NULL,
    email       VARCHAR(255) UNIQUE NOT NULL,
    edad        INTEGER,
    activo      BOOLEAN DEFAULT TRUE,
    creado_en   TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Crear tabla solo si no existe
CREATE TABLE IF NOT EXISTS productos (
    id          SERIAL PRIMARY KEY,
    nombre      VARCHAR(200) NOT NULL,
    precio      NUMERIC(10, 2) NOT NULL,
    stock       INTEGER DEFAULT 0
);

-- Eliminar tabla
DROP TABLE usuarios;
DROP TABLE IF EXISTS usuarios;

-- Eliminar tabla y todo lo que depende de ella
DROP TABLE usuarios CASCADE;

-- Vaciar tabla (sin eliminarla)
TRUNCATE TABLE usuarios;
TRUNCATE TABLE usuarios RESTART IDENTITY; -- también resetea secuencias
```

### Modificar tablas (ALTER TABLE)

```sql
-- Agregar columna
ALTER TABLE usuarios ADD COLUMN telefono VARCHAR(20);

-- Eliminar columna
ALTER TABLE usuarios DROP COLUMN telefono;

-- Cambiar tipo de dato
ALTER TABLE usuarios ALTER COLUMN edad TYPE SMALLINT;

-- Renombrar columna
ALTER TABLE usuarios RENAME COLUMN nombre TO nombre_completo;

-- Renombrar tabla
ALTER TABLE usuarios RENAME TO clientes;

-- Agregar restricción NOT NULL
ALTER TABLE usuarios ALTER COLUMN email SET NOT NULL;

-- Quitar restricción NOT NULL
ALTER TABLE usuarios ALTER COLUMN edad DROP NOT NULL;

-- Agregar valor por defecto
ALTER TABLE usuarios ALTER COLUMN activo SET DEFAULT TRUE;
```

### Tipos de datos frecuentes

Al definir una columna, elegís su tipo de dato. Esto determina qué valores acepta y cuánto espacio ocupa en disco.

| Tipo | Cuándo usarlo | Ejemplo |
|------|--------------|---------|
| `SERIAL` / `BIGSERIAL` | ID autoincremental (clave primaria) | `id SERIAL PRIMARY KEY` |
| `INTEGER` | Números enteros pequeños/medianos | edades, cantidades |
| `BIGINT` | Enteros muy grandes | IDs de alto volumen |
| `NUMERIC(p, s)` | Decimal **exacto** — siempre para dinero | `precio NUMERIC(10, 2)` |
| `REAL` / `DOUBLE PRECISION` | Decimal aproximado (científico) | coordenadas GPS |
| `VARCHAR(n)` | Texto de longitud máxima conocida | nombres, emails |
| `TEXT` | Texto libre sin límite | descripciones, contenido |
| `BOOLEAN` | Verdadero o falso | `activo BOOLEAN DEFAULT TRUE` |
| `DATE` | Solo fecha (sin hora) | fecha de nacimiento |
| `TIME` | Solo hora (sin fecha) | horario de apertura |
| `TIMESTAMP` | Fecha y hora juntas | `creado_en TIMESTAMP` |
| `TIMESTAMPTZ` | Fecha y hora **con zona horaria** | recomendado para producción |
| `JSON` / `JSONB` | Datos semiestructurados. `JSONB` es indexable y más rápido | configuraciones |
| `UUID` | Identificador globalmente único | IDs distribuidos |

!!! tip "NUMERIC vs FLOAT para dinero"
    Nunca uses `REAL` o `FLOAT` para dinero. Son aproximaciones binarias y pueden acumular errores (0.1 + 0.2 ≠ 0.3). Usá siempre `NUMERIC(p, s)`.

---

## DML — Manipulación de datos

DML trabaja con los datos dentro de las tablas. Los cuatro comandos fundamentales forman el **CRUD**:

```mermaid
flowchart LR
    C["CREATE\n→ INSERT"] --> R["READ\n→ SELECT"]
    R --> U["UPDATE\n→ UPDATE"]
    U --> D["DELETE\n→ DELETE"]

    style C fill:#2d6a4f,color:#fff
    style R fill:#1d3557,color:#fff
    style U fill:#e76f51,color:#fff
    style D fill:#9b2226,color:#fff
```

### INSERT

```sql
-- Insertar un registro
INSERT INTO usuarios (nombre, email, edad)
VALUES ('Ana García', 'ana@email.com', 28);

-- Insertar múltiples registros
INSERT INTO usuarios (nombre, email, edad) VALUES
    ('Carlos López', 'carlos@email.com', 35),
    ('María Fernández', 'maria@email.com', 22),
    ('Juan Pérez', 'juan@email.com', 41);

-- Insertar y retornar el registro creado
INSERT INTO usuarios (nombre, email)
VALUES ('Laura Torres', 'laura@email.com')
RETURNING *;

-- Insertar o ignorar si ya existe (ON CONFLICT)
INSERT INTO usuarios (email, nombre)
VALUES ('ana@email.com', 'Ana García')
ON CONFLICT (email) DO NOTHING;

-- Insertar o actualizar si ya existe (UPSERT)
INSERT INTO usuarios (email, nombre, edad)
VALUES ('ana@email.com', 'Ana García', 29)
ON CONFLICT (email) DO UPDATE SET
    nombre = EXCLUDED.nombre,
    edad = EXCLUDED.edad;
```

### SELECT — Anatomía completa

`SELECT` es el comando más rico de SQL. Puede tener muchas cláusulas encadenadas. Lo importante: **el orden en que se escriben no es el orden en que se ejecutan**.

#### Orden de escritura vs orden de ejecución

```mermaid
flowchart TD
    subgraph escritura["📝 Orden de escritura"]
        direction TB
        e1["1. SELECT columnas"]
        e2["2. FROM tabla"]
        e3["3. JOIN otras_tablas ON ..."]
        e4["4. WHERE condición_fila"]
        e5["5. GROUP BY columna"]
        e6["6. HAVING condición_grupo"]
        e7["7. ORDER BY columna"]
        e8["8. LIMIT n OFFSET m"]
        e1 --> e2 --> e3 --> e4 --> e5 --> e6 --> e7 --> e8
    end

    subgraph ejecucion["⚙️ Orden de ejecución real"]
        direction TB
        x1["1. FROM + JOIN  → ¿de dónde?"]
        x2["2. WHERE        → filtrar filas"]
        x3["3. GROUP BY     → agrupar"]
        x4["4. HAVING       → filtrar grupos"]
        x5["5. SELECT       → elegir columnas"]
        x6["6. ORDER BY     → ordenar"]
        x7["7. LIMIT/OFFSET → paginar"]
        x1 --> x2 --> x3 --> x4 --> x5 --> x6 --> x7
    end
```

!!! info "¿Por qué importa el orden de ejecución?"
    Por eso no podés usar un alias definido en `SELECT` dentro de un `WHERE` — cuando `WHERE` se ejecuta, `SELECT` todavía no corrió. Sí podés usarlo en `ORDER BY` porque ese sí corre después.

#### Cada cláusula explicada

| Cláusula | Para qué sirve | Ejemplo |
|----------|---------------|---------|
| `SELECT col` | Define **qué columnas** mostrar en el resultado | `SELECT nombre, edad` |
| `SELECT *` | Devuelve **todas** las columnas (evitarlo en producción) | `SELECT * FROM usuarios` |
| `SELECT DISTINCT` | Elimina **filas duplicadas** del resultado | `SELECT DISTINCT ciudad` |
| `FROM tabla` | Define **de qué tabla** vienen los datos | `FROM usuarios` |
| `JOIN` | **Combina** filas de dos tablas según una condición | `JOIN pedidos ON usuarios.id = pedidos.usuario_id` |
| `WHERE condición` | Filtra **filas individuales** antes de agrupar | `WHERE activo = TRUE` |
| `GROUP BY col` | **Agrupa** filas que comparten el mismo valor para aplicar funciones de agregación | `GROUP BY ciudad` |
| `HAVING condición` | Filtra **grupos** (igual que WHERE pero después del GROUP BY) | `HAVING COUNT(*) > 5` |
| `ORDER BY col` | **Ordena** el resultado. `ASC` = ascendente (default), `DESC` = descendente | `ORDER BY edad DESC` |
| `LIMIT n` | Devuelve solo los primeros **n** resultados | `LIMIT 10` |
| `OFFSET m` | Salta los primeros **m** resultados (para paginación) | `OFFSET 20` |
| `AS alias` | Le pone un **nombre temporal** a una columna o tabla en el resultado | `COUNT(*) AS total` |

#### La query más completa — paso a paso

```sql
SELECT
    u.ciudad,                        -- columna de la tabla usuarios (alias u)
    COUNT(p.id)      AS total_pedidos,  -- cuenta pedidos por grupo
    AVG(p.total)     AS ticket_promedio, -- promedio del valor de pedidos
    MAX(p.total)     AS pedido_maximo
FROM usuarios u                      -- tabla principal, alias 'u'
INNER JOIN pedidos p                 -- combinar con la tabla pedidos
    ON u.id = p.usuario_id           -- condición del JOIN: relacionar por id
WHERE u.activo = TRUE                -- filtro ANTES de agrupar: solo usuarios activos
  AND p.fecha >= '2024-01-01'        -- segundo filtro: pedidos del 2024 en adelante
GROUP BY u.ciudad                    -- agrupar todos los resultados por ciudad
HAVING COUNT(p.id) > 10             -- filtro DESPUÉS de agrupar: solo ciudades con más de 10 pedidos
ORDER BY total_pedidos DESC          -- ordenar de mayor a menor cantidad de pedidos
LIMIT 5                              -- mostrar solo las 5 primeras ciudades
OFFSET 0;                            -- empezar desde el principio (página 1)
```

#### Filtros en WHERE — operadores disponibles

| Operador | Significado | Ejemplo |
|----------|-------------|---------|
| `=` | Igual | `WHERE activo = TRUE` |
| `<>` o `!=` | Distinto | `WHERE estado <> 'cancelado'` |
| `>`, `<`, `>=`, `<=` | Comparación numérica | `WHERE edad >= 18` |
| `BETWEEN a AND b` | Entre dos valores (inclusive) | `WHERE edad BETWEEN 18 AND 65` |
| `IN (...)` | Está en la lista | `WHERE ciudad IN ('Lima', 'Bogotá')` |
| `NOT IN (...)` | No está en la lista | `WHERE id NOT IN (1, 2, 3)` |
| `LIKE 'patrón'` | Coincidencia de texto (case-sensitive). `%` = cualquier cosa, `_` = un carácter | `WHERE nombre LIKE 'Ana%'` |
| `ILIKE 'patrón'` | Igual que LIKE pero **case-insensitive** | `WHERE nombre ILIKE '%garcía%'` |
| `IS NULL` | El valor es nulo | `WHERE telefono IS NULL` |
| `IS NOT NULL` | El valor no es nulo | `WHERE email IS NOT NULL` |
| `AND` | Las dos condiciones deben cumplirse | `WHERE activo = TRUE AND edad > 18` |
| `OR` | Al menos una condición debe cumplirse | `WHERE ciudad = 'Lima' OR ciudad = 'Bogotá'` |
| `NOT` | Niega la condición | `WHERE NOT activo` |

#### Funciones de agregación

Solo se pueden usar en `SELECT` o `HAVING` (no en `WHERE`):

| Función | Qué devuelve |
|---------|-------------|
| `COUNT(*)` | Cantidad de filas (incluyendo nulos) |
| `COUNT(col)` | Cantidad de filas donde `col` no es nulo |
| `SUM(col)` | Suma de todos los valores |
| `AVG(col)` | Promedio de los valores |
| `MIN(col)` | Valor mínimo |
| `MAX(col)` | Valor máximo |
| `ROUND(AVG(col), 2)` | Promedio redondeado a 2 decimales |

```sql
-- Ejemplo completo con varias funciones de agregación
SELECT
    COUNT(*)            AS total_usuarios,
    AVG(edad)           AS edad_promedio,
    MIN(edad)           AS mas_joven,
    MAX(edad)           AS mas_mayor,
    ROUND(AVG(edad), 1) AS promedio_redondeado
FROM usuarios
WHERE activo = TRUE;
```

#### Queries básicas de SELECT

```sql
-- Todos los registros y todas las columnas
SELECT * FROM usuarios;

-- Solo ciertas columnas
SELECT nombre, email FROM usuarios;

-- Con alias para las columnas
SELECT nombre AS "Nombre Completo", email AS "Correo" FROM usuarios;

-- Eliminar duplicados
SELECT DISTINCT ciudad FROM usuarios;

-- Ordenar
SELECT * FROM usuarios ORDER BY nombre ASC;
SELECT * FROM usuarios ORDER BY creado_en DESC;
SELECT * FROM usuarios ORDER BY edad DESC, nombre ASC; -- múltiples criterios

-- Paginación (página 3 de 10 resultados por página = saltear 20, mostrar 10)
SELECT * FROM usuarios
ORDER BY id
LIMIT 10 OFFSET 20;
```

### UPDATE

```sql
-- Actualizar un campo
UPDATE usuarios SET activo = FALSE WHERE id = 3;

-- Actualizar múltiples campos
UPDATE usuarios
SET nombre = 'Ana Martínez', edad = 29
WHERE email = 'ana@email.com';

-- Actualizar y retornar el registro modificado
UPDATE usuarios
SET activo = FALSE
WHERE id = 3
RETURNING *;

-- Actualizar con subconsulta
UPDATE productos
SET precio = precio * 1.10
WHERE id IN (SELECT id FROM productos WHERE stock = 0);
```

### DELETE

```sql
-- Eliminar registros específicos
DELETE FROM usuarios WHERE id = 5;

-- Eliminar con condición
DELETE FROM usuarios WHERE activo = FALSE;

-- Eliminar y retornar los registros eliminados
DELETE FROM usuarios WHERE id = 5 RETURNING *;
```

---

## JOINs — Combinar tablas

Los JOINs unen filas de dos tablas en base a una condición (generalmente una clave foránea).

```mermaid
flowchart LR
    subgraph A["Tabla A\nusuarios"]
        a1["id=1 Ana"]
        a2["id=2 Carlos"]
        a3["id=3 María"]
    end
    subgraph B["Tabla B\npedidos"]
        b1["usuario_id=1"]
        b2["usuario_id=1"]
        b3["usuario_id=2"]
    end
    a1 --- b1
    a1 --- b2
    a2 --- b3
```

| JOIN | Qué devuelve |
|------|-------------|
| `INNER JOIN` | Solo filas que tienen coincidencia **en ambas tablas** |
| `LEFT JOIN` | **Todas** las filas de la tabla izquierda + las que coinciden de la derecha (rellena con `NULL` si no hay match) |
| `RIGHT JOIN` | **Todas** las filas de la tabla derecha + las que coinciden de la izquierda |
| `FULL OUTER JOIN` | **Todas** las filas de ambas tablas, con `NULL` donde no hay coincidencia |

```sql
-- Tabla de ejemplo para los JOINs
CREATE TABLE pedidos (
    id          SERIAL PRIMARY KEY,
    usuario_id  INTEGER REFERENCES usuarios(id),
    total       NUMERIC(10, 2),
    fecha       DATE DEFAULT CURRENT_DATE
);
```

```sql
-- INNER JOIN: solo filas con coincidencia en ambas tablas
-- Resultado: usuarios que TIENEN pedidos
SELECT u.nombre, p.total, p.fecha
FROM usuarios u
INNER JOIN pedidos p ON u.id = p.usuario_id;

-- LEFT JOIN: todos los usuarios, con o sin pedidos
-- Los usuarios sin pedidos aparecen con NULL en columnas de pedidos
SELECT u.nombre, p.total
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id;

-- LEFT JOIN para encontrar usuarios SIN pedidos
SELECT u.nombre
FROM usuarios u
LEFT JOIN pedidos p ON u.id = p.usuario_id
WHERE p.id IS NULL;  -- el NULL indica que no hay coincidencia

-- RIGHT JOIN: todos los pedidos, aunque el usuario fue eliminado
SELECT u.nombre, p.total
FROM usuarios u
RIGHT JOIN pedidos p ON u.id = p.usuario_id;

-- FULL OUTER JOIN: todo de ambas tablas
SELECT u.nombre, p.total
FROM usuarios u
FULL OUTER JOIN pedidos p ON u.id = p.usuario_id;
```

---

## Índices

```sql
-- Crear índice simple (acelera búsquedas por esa columna)
CREATE INDEX idx_usuarios_email ON usuarios(email);

-- Índice único
CREATE UNIQUE INDEX idx_usuarios_email ON usuarios(email);

-- Índice compuesto
CREATE INDEX idx_nombre_ciudad ON usuarios(nombre, ciudad);

-- Ver índices de una tabla
\di usuarios*

-- Eliminar índice
DROP INDEX idx_usuarios_email;
```

---

## Consultas útiles del día a día

### Funciones de texto y fecha

| Función | Qué hace | Ejemplo |
|---------|---------|---------|
| `NOW()` | Fecha y hora actual | `SELECT NOW()` |
| `CURRENT_DATE` | Solo la fecha de hoy | `SELECT CURRENT_DATE` |
| `CURRENT_TIME` | Solo la hora actual | `SELECT CURRENT_TIME` |
| `TO_CHAR(fecha, formato)` | Formatea una fecha como texto | `TO_CHAR(NOW(), 'DD/MM/YYYY')` |
| `AGE(fecha)` | Tiempo transcurrido desde esa fecha | `AGE(fecha_nacimiento)` |
| `EXTRACT(part FROM fecha)` | Extrae una parte de la fecha | `EXTRACT(YEAR FROM NOW())` |
| `\|\|` | Concatena texto | `nombre \|\| ' ' \|\| apellido` |
| `CONCAT(a, b, c)` | Concatena texto (alternativa) | `CONCAT(nombre, ' ', apellido)` |
| `UPPER(texto)` | Convierte a mayúsculas | `UPPER(nombre)` |
| `LOWER(texto)` | Convierte a minúsculas | `LOWER(email)` |
| `TRIM(texto)` | Elimina espacios al inicio y fin | `TRIM(nombre)` |
| `LENGTH(texto)` | Largo del texto | `LENGTH(descripcion)` |
| `SUBSTRING(texto, inicio, largo)` | Extrae parte de un texto | `SUBSTRING(dni, 1, 2)` |

```sql
-- Fechas
SELECT NOW();
SELECT CURRENT_DATE;
SELECT TO_CHAR(NOW(), 'DD/MM/YYYY HH24:MI');
SELECT EXTRACT(YEAR FROM NOW());
SELECT AGE(NOW(), creado_en) AS antiguedad FROM usuarios;

-- Texto
SELECT nombre || ' <' || email || '>' AS contacto FROM usuarios;
SELECT CONCAT(nombre, ' - ', ciudad) AS etiqueta FROM usuarios;
SELECT UPPER(nombre), LOWER(email) FROM usuarios;
```

### CASE — lógica condicional

`CASE` funciona como un `if/elif/else` dentro de una query. Evalúa condiciones de arriba a abajo y devuelve el primer valor cuya condición sea verdadera.

```sql
-- Sintaxis buscada (evalúa condiciones)
SELECT nombre,
    CASE
        WHEN edad < 18           THEN 'menor de edad'
        WHEN edad BETWEEN 18 AND 65 THEN 'adulto'
        ELSE 'adulto mayor'
    END AS grupo_etario
FROM usuarios;

-- Sintaxis simple (compara contra un valor)
SELECT nombre,
    CASE estado
        WHEN 'activo'    THEN '✅ Activo'
        WHEN 'suspendido' THEN '⚠️ Suspendido'
        WHEN 'eliminado' THEN '❌ Eliminado'
        ELSE 'desconocido'
    END AS estado_legible
FROM usuarios;
```

### COALESCE — manejar NULLs

`COALESCE(a, b, c...)` devuelve el **primer valor no nulo** de la lista. Muy útil para poner valores por defecto al mostrar datos.

```sql
-- Si telefono es NULL, mostrar 'sin teléfono'
SELECT nombre, COALESCE(telefono, 'sin teléfono') AS telefono FROM usuarios;

-- Múltiples fallbacks: usa celular, si no teléfono fijo, si no 'sin contacto'
SELECT nombre, COALESCE(celular, telefono_fijo, 'sin contacto') AS contacto FROM usuarios;
```

### CTEs — WITH (subconsultas nombradas)

Un CTE (Common Table Expression) es como crear una tabla temporal para usar dentro de la misma query. Hace el código más legible que anidar subconsultas.

```sql
-- Sin CTE (difícil de leer)
SELECT u.nombre, COUNT(p.id) AS pedidos
FROM (SELECT * FROM usuarios WHERE activo = TRUE) u
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.nombre
ORDER BY pedidos DESC;

-- Con CTE (mucho más claro)
WITH usuarios_activos AS (
    SELECT * FROM usuarios WHERE activo = TRUE   -- esto se ejecuta primero
)
SELECT u.nombre, COUNT(p.id) AS pedidos
FROM usuarios_activos u                          -- acá usamos el CTE como si fuera una tabla
LEFT JOIN pedidos p ON u.id = p.usuario_id
GROUP BY u.nombre
ORDER BY pedidos DESC;

-- Múltiples CTEs encadenados
WITH
    activos AS (
        SELECT * FROM usuarios WHERE activo = TRUE
    ),
    con_pedidos AS (
        SELECT usuario_id, COUNT(*) AS total FROM pedidos GROUP BY usuario_id
    )
SELECT a.nombre, COALESCE(cp.total, 0) AS pedidos
FROM activos a
LEFT JOIN con_pedidos cp ON a.id = cp.usuario_id
ORDER BY pedidos DESC;
```

### Subconsultas

Una subconsulta es un `SELECT` dentro de otro `SELECT`. Se puede usar en `WHERE`, `FROM` o `SELECT`.

```sql
-- En WHERE: usuarios que hicieron pedidos de más de $1000
SELECT * FROM usuarios
WHERE id IN (SELECT usuario_id FROM pedidos WHERE total > 1000);

-- En WHERE con NOT IN: usuarios sin pedidos en 2024
SELECT * FROM usuarios
WHERE id NOT IN (
    SELECT usuario_id FROM pedidos
    WHERE fecha >= '2024-01-01'
    AND usuario_id IS NOT NULL
);

-- En FROM: tratar el resultado de un SELECT como si fuera una tabla
SELECT ciudad, AVG(total_pedidos) AS promedio_por_ciudad
FROM (
    SELECT u.ciudad, COUNT(p.id) AS total_pedidos
    FROM usuarios u
    LEFT JOIN pedidos p ON u.id = p.usuario_id
    GROUP BY u.ciudad, u.id
) AS sub
GROUP BY ciudad;
```

### Queries de diagnóstico

```sql
-- Ver versión de PostgreSQL
SELECT version();

-- Las tablas más grandes
SELECT
    relname                                           AS tabla,
    pg_size_pretty(pg_total_relation_size(relid))    AS tamaño_total,
    pg_size_pretty(pg_relation_size(relid))          AS solo_datos
FROM pg_stat_user_tables
ORDER BY pg_total_relation_size(relid) DESC;

-- Conexiones activas en este momento
SELECT pid, usename, application_name, state, query
FROM pg_stat_activity
WHERE state = 'active';

-- Cantidad de filas por tabla
SELECT relname AS tabla, n_live_tup AS filas_estimadas
FROM pg_stat_user_tables
ORDER BY n_live_tup DESC;
```

---

## Transactions

Una transacción es un bloque de operaciones que se ejecutan como una **unidad atómica**: o todo se guarda, o nada se guarda.

```mermaid
flowchart LR
    BEGIN --> op1["UPDATE cuenta A\n-500"]
    op1 --> op2["UPDATE cuenta B\n+500"]
    op2 --> decision{{"¿Todo OK?"}}
    decision -->|Sí| COMMIT["COMMIT\n✅ cambios guardados"]
    decision -->|Error| ROLLBACK["ROLLBACK\n↩ todo deshecho"]
```

| Comando | Qué hace |
|---------|---------|
| `BEGIN` | Inicia la transacción. Nada se guarda hasta el `COMMIT` |
| `COMMIT` | Confirma y persiste todos los cambios de la transacción |
| `ROLLBACK` | Deshace todos los cambios desde el último `BEGIN` |
| `SAVEPOINT nombre` | Crea un punto de restauración parcial dentro de la transacción |
| `ROLLBACK TO nombre` | Deshace solo hasta el savepoint, no toda la transacción |

```sql
-- Transacción clásica: transferencia entre cuentas
BEGIN;

UPDATE cuentas SET saldo = saldo - 500 WHERE id = 1;
UPDATE cuentas SET saldo = saldo + 500 WHERE id = 2;

-- Si llegamos acá sin error:
COMMIT;

-- Si algo falló, en el bloque EXCEPT o manualmente:
-- ROLLBACK;

-- Con savepoints
BEGIN;
UPDATE cuentas SET saldo = saldo - 500 WHERE id = 1;
SAVEPOINT despues_del_debito;
UPDATE cuentas SET saldo = saldo + 500 WHERE id = 2;
-- Si el segundo UPDATE falla, podemos volver al savepoint:
ROLLBACK TO despues_del_debito;
COMMIT;
```

!!! warning "Siempre usá transacciones para operaciones críticas"
    Un `UPDATE` o `DELETE` sin `WHERE` en producción puede ser catastrófico. Envolvé las operaciones importantes en `BEGIN` / `COMMIT` para poder hacer `ROLLBACK` si algo falla.

---

## Roles y permisos

```sql
-- Crear usuario
CREATE USER mi_usuario WITH PASSWORD 'contraseña_segura';

-- Crear rol
CREATE ROLE solo_lectura;

-- Dar permisos
GRANT SELECT ON ALL TABLES IN SCHEMA public TO solo_lectura;
GRANT solo_lectura TO mi_usuario;

-- Dar todos los permisos sobre una tabla
GRANT ALL PRIVILEGES ON TABLE usuarios TO mi_usuario;

-- Quitar permisos
REVOKE ALL PRIVILEGES ON TABLE usuarios FROM mi_usuario;

-- Ver roles
\du
```

---

## Importar / Exportar datos

```sql
-- Exportar tabla a CSV (desde psql)
\copy usuarios TO 'usuarios.csv' WITH CSV HEADER;

-- Importar desde CSV
\copy usuarios (nombre, email, edad) FROM 'usuarios.csv' WITH CSV HEADER;

-- Exportar query a CSV
\copy (SELECT nombre, email FROM usuarios WHERE activo = TRUE) TO 'activos.csv' WITH CSV HEADER;
```

```bash
# Backup completo de la base de datos (desde terminal)
pg_dump -U postgres mi_base > backup.sql

# Restaurar
psql -U postgres mi_base < backup.sql

# Backup en formato comprimido
pg_dump -U postgres -F c mi_base > backup.dump
pg_restore -U postgres -d mi_base backup.dump
```
