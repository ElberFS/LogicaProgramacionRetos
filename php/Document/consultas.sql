-- ===========================================
-- 2.1. MySQL Avanzado: Consultas Complejas
-- ===========================================

-- -------------------------------------------
-- Ejemplo 1: Consulta Simple
-- Descripción: Obtener todos los choferes y su información básica.
-- -------------------------------------------
-- SELECT * FROM choferes;
SELECT id, nombres, apellidos, dni FROM choferes;

-- -------------------------------------------
-- Ejemplo 2: JOIN (INNER JOIN)
-- Descripción: Obtener todas las multas con el nombre del chofer, la placa del vehículo y la descripción de la multa.
-- -------------------------------------------
SELECT
    m.id AS multa_id,
    c.nombres,
    c.apellidos,
    v.placa,
    tm.descripcion AS tipo_multa,
    m.fecha,
    m.lugar
FROM
    multas m
JOIN
    choferes c ON m.chofer_id = c.id
JOIN
    vehiculos v ON m.vehiculo_id = v.id
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id;

-- -------------------------------------------
-- Ejemplo 3: JOIN (LEFT JOIN)
-- Descripción: Listar todos los choferes y, si tienen multas, mostrar la fecha de su primera multa.
--              Incluye choferes que no tienen multas.
-- -------------------------------------------
SELECT
    c.nombres,
    c.apellidos,
    MIN(m.fecha) AS primera_multa_fecha
FROM
    choferes c
LEFT JOIN
    multas m ON c.id = m.chofer_id
GROUP BY
    c.id, c.nombres, c.apellidos;

-- -------------------------------------------
-- Ejemplo 4: Subconsulta (en la cláusula WHERE)
-- Descripción: Obtener los choferes que han sido multados por "Exceso de velocidad".
-- -------------------------------------------
SELECT
    nombres,
    apellidos,
    dni
FROM
    choferes
WHERE
    id IN (SELECT chofer_id FROM multas WHERE tipo_multa_id = (SELECT id FROM tipos_multas WHERE codigo = 'M100'));

-- -------------------------------------------
-- Ejemplo 5: Subconsulta (en la cláusula SELECT - Correlated Subquery)
-- Descripción: Mostrar el nombre de cada tipo de multa y la cantidad total de veces que ha sido impuesta.
-- -------------------------------------------
SELECT
    tm.descripcion,
    (SELECT COUNT(*) FROM multas m WHERE m.tipo_multa_id = tm.id) AS total_multas_impuestas
FROM
    tipos_multas tm;

-- -------------------------------------------
-- Ejemplo 6: Subconsulta (en la cláusula FROM - Derived Table)
-- Descripción: Obtener el promedio de las multas impuestas por cada tipo de autoridad.
-- -------------------------------------------
SELECT
    a.nombre AS autoridad,
    AVG(sub.monto_multa) AS promedio_multa
FROM
    autoridades a
JOIN (
    SELECT
        m.autoridad_id,
        tm.monto AS monto_multa
    FROM
        multas m
    JOIN
        tipos_multas tm ON m.tipo_multa_id = tm.id
) AS sub ON a.id = sub.autoridad_id
GROUP BY
    a.nombre;

-- -------------------------------------------
-- Ejemplo 7: Uso de HAVING
-- Descripción: Encontrar los choferes que tienen más de 2 multas.
-- -------------------------------------------
SELECT
    c.nombres,
    c.apellidos,
    COUNT(m.id) AS cantidad_multas
FROM
    choferes c
JOIN
    multas m ON c.id = m.chofer_id
GROUP BY
    c.id, c.nombres, c.apellidos
HAVING
    cantidad_multas > 2;

-- -------------------------------------------
-- Ejemplo 8: UNION (Combinando resultados de consultas)
-- Descripción: Obtener una lista única de DNI de choferes que han tenido multas de velocidad (M100) o multas por pasar luz roja (L101).

-- -------------------------------------------
SELECT c.dni FROM choferes c JOIN multas m ON c.id = m.chofer_id JOIN tipos_multas tm ON m.tipo_multa_id = tm.id WHERE tm.codigo = 'M100'
UNION
SELECT c.dni FROM choferes c JOIN multas m ON c.id = m.chofer_id JOIN tipos_multas tm ON m.tipo_multa_id = tm.id WHERE tm.codigo = 'M101';

-- -------------------------------------------
-- Ejemplo 9: CTE (Common Table Expression - MySQL 8+)
-- Descripción: Calcular el total de multas por cada chofer y luego filtrar aquellos con un monto total de multas superior al promedio general.
-- -------------------------------------------
WITH ChoferMontoTotal AS (
    SELECT
        c.id AS chofer_id,
        c.nombres,
        c.apellidos,
        SUM(tm.monto) AS monto_total_multas
    FROM
        choferes c
    JOIN
        multas m ON c.id = m.chofer_id
    JOIN
        tipos_multas tm ON m.tipo_multa_id = tm.id
    GROUP BY
        c.id, c.nombres, c.apellidos
)
SELECT
    cmt.nombres,
    cmt.apellidos,
    cmt.monto_total_multas
FROM
    ChoferMontoTotal cmt
WHERE
    cmt.monto_total_multas > (SELECT AVG(monto_total_multas) FROM ChoferMontoTotal);

-- -------------------------------------------
-- Ejemplo 10: Funciones de Ventana (MySQL 8+)
-- Descripción: Asignar un número de fila a cada multa de un chofer, ordenadas por fecha de multa.
-- -------------------------------------------
SELECT
    c.nombres,
    c.apellidos,
    v.placa,
    tm.descripcion AS tipo_multa,
    m.fecha,
    ROW_NUMBER() OVER (PARTITION BY c.id ORDER BY m.fecha) AS numero_multa_chofer
FROM
    multas m
JOIN
    choferes c ON m.chofer_id = c.id
JOIN
    vehiculos v ON m.vehiculo_id = v.id
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id
ORDER BY
    c.nombres, m.fecha;

-- ===========================================
-- Índices y Optimización de Consultas
-- ===========================================

-- -------------------------------------------
-- Problema: Consultas lentas al buscar multas por fecha o por chofer.
-- Solución: Crear índices en las columnas `fecha` de `multas` y `chofer_id` de `multas`.
-- -------------------------------------------
CREATE INDEX idx_multas_fecha ON multas (fecha);
CREATE INDEX idx_multas_chofer_id ON multas (chofer_id);

-- Explicación:
-- Estos índices mejoran significativamente el rendimiento de las consultas que filtran
-- o ordenan por fecha o que buscan multas específicas de un chofer, ya que el motor de la base de datos
-- puede encontrar los datos de forma más rápida sin tener que escanear toda la tabla.

-- -------------------------------------------
-- Problema: Consultas lentas al buscar choferes por DNI o licencia.
-- Solución: Los campos `dni` y `licencia_conducir` ya tienen `UNIQUE` constraints, que implícitamente
--           crean índices únicos, optimizando estas búsquedas.
-- -------------------------------------------
-- No se requiere acción adicional, ya están optimizados por UNIQUE.

-- -------------------------------------------
-- Problema: Consultas lentas al unir `multas` con `tipos_multas` por `tipo_multa_id`.
-- Solución: Crear un índice en `tipo_multa_id` de `multas`.
-- -------------------------------------------
CREATE INDEX idx_multas_tipo_multa_id ON multas (tipo_multa_id);
-- Explicación: Este índice acelerará las operaciones JOIN entre 'multas' y 'tipos_multas'.

-- ===========================================
-- Transacciones y Concurrencia
-- ===========================================

-- -------------------------------------------
-- Problema: Necesidad de asegurar la integridad de los datos al registrar una multa
--           y simultáneamente actualizar el saldo pendiente del chofer (si tuviéramos una tabla).
--           O, por ejemplo, registrar una multa y actualizar un contador en otra tabla.
-- Solución: Usar una transacción.
-- -------------------------------------------

-- Ejemplo de Transacción: Registrar una nueva multa y, teóricamente,
-- decrementar el presupuesto de una autoridad (ejemplo conceptual para transacción).
-- En este caso, simularemos la actualización de una tabla ficticia `autoridades_presupuesto`.

-- Primero, creamos una tabla ficticia para demostrar la transacción
CREATE TABLE IF NOT EXISTS autoridades_presupuesto (
    autoridad_id INT PRIMARY KEY,
    presupuesto_disponible DECIMAL(15,2),
    FOREIGN KEY (autoridad_id) REFERENCES autoridades(id)
);

INSERT INTO autoridades_presupuesto (autoridad_id, presupuesto_disponible) VALUES
(1, 100000.00), -- Municipalidad de Lima
(2, 50000.00),  -- Policía Nacional del Perú - Tránsito
(3, 75000.00);  -- Municipalidad de Miraflores

-- Transacción para registrar una multa y "deducir" del presupuesto de la autoridad
START TRANSACTION;

-- Paso 1: Insertar la nueva multa
INSERT INTO multas (chofer_id, vehiculo_id, autoridad_id, tipo_multa_id, fecha, lugar, observaciones) VALUES
(4, 1, 1, 3, '2024-05-20', 'Av. La Paz 500', 'Multa por pasar luz roja, registrada en transacción');

-- Paso 2: Obtener el monto de la multa recién insertada
SET @monto_nueva_multa = (SELECT monto FROM tipos_multas WHERE id = 3); -- L02 (650.00)

-- Paso 3: Actualizar el presupuesto de la autoridad que impuso la multa
-- (En un escenario real, esto podría ser más complejo, como un presupuesto para gastos de operación o ingresos por multas)
UPDATE autoridades_presupuesto
SET presupuesto_disponible = presupuesto_disponible - @monto_nueva_multa
WHERE autoridad_id = 1; -- Asumiendo que la autoridad 1 es la que multó

-- Verificamos si ambos pasos fueron exitosos antes de confirmar
-- (En un script real, se verificarían errores o condiciones)

-- Si todo está bien, confirmamos los cambios
COMMIT;

-- Si algo sale mal (ej: error de inserción, presupuesto insuficiente, etc.), se revierte todo
-- ROLLBACK;

-- Verificar los cambios después de la transacción
SELECT * FROM multas WHERE observaciones LIKE '%registrada en transacción%';
SELECT * FROM autoridades_presupuesto WHERE autoridad_id = 1;

-- Explicación:
-- Una transacción asegura que un conjunto de operaciones de base de datos se traten como una sola unidad atómica.
-- Esto significa que o todas las operaciones se completan con éxito (COMMIT), o ninguna de ellas lo hace (ROLLBACK).
-- Esto es crucial para mantener la integridad de los datos, especialmente en escenarios donde múltiples tablas
-- están interconectadas y los cambios en una dependen de los cambios en otra.
-- El ejemplo simula la inserción de una multa y la deducción de un presupuesto, asegurando que ambos
-- sucedan o ninguno.

-- ===========================================
-- Problemas Combinados y Soluciones
-- ===========================================

-- Problema 1: Identificar a los choferes con el mayor número de multas por "exceso de velocidad" en el último año (desde el 2023-05-28)
-- y mostrar su información personal, el número de multas y el monto total acumulado solo para esas multas.
-- Combinación: JOIN, WHERE con fechas, Subconsulta (para el tipo de multa), GROUP BY, ORDER BY, SUM, COUNT.

SELECT
    c.nombres,
    c.apellidos,
    c.dni,
    COUNT(m.id) AS total_multas_velocidad,
    SUM(tm.monto) AS monto_total_velocidad
FROM
    choferes c
JOIN
    multas m ON c.id = m.chofer_id
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id
WHERE
    tm.codigo = 'M100' -- Código para "Exceso de velocidad"
    AND m.fecha >= '2023-05-28' -- Último año desde la fecha actual (se asume 2023-05-28 como inicio)
GROUP BY
    c.id, c.nombres, c.apellidos
ORDER BY
    total_multas_velocidad DESC, monto_total_velocidad DESC
LIMIT 5; -- Los 5 principales

-- Problema 2: Listar los vehículos que han sido multados por al menos dos autoridades diferentes en el año 2024,
-- mostrando la placa, marca, modelo y la cantidad de autoridades distintas que los multaron.
-- Combinación: JOIN, GROUP BY, HAVING, COUNT(DISTINCT), WHERE con año.
SELECT
    v.placa,
    v.marca,
    v.modelo,
    COUNT(DISTINCT m.autoridad_id) AS cantidad_autoridades_distintas
FROM
    vehiculos v
JOIN
    multas m ON v.id = m.vehiculo_id
WHERE
    YEAR(m.fecha) = 2024
GROUP BY
    v.id, v.placa, v.marca, v.modelo
HAVING
    cantidad_autoridades_distintas >= 2;

-- Problema 3: Encontrar la autoridad que ha impuesto el monto total de multas más alto en el primer trimestre de 2024,
-- y cuál fue ese monto.
-- Combinación: JOIN, GROUP BY, SUM, ORDER BY, LIMIT, WHERE con rango de fechas.
SELECT
    a.nombre AS autoridad,
    SUM(tm.monto) AS monto_total_impuesto
FROM
    autoridades a
JOIN
    multas m ON a.id = m.autoridad_id
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id
WHERE
    m.fecha >= '2024-01-01' AND m.fecha <= '2024-03-31'
GROUP BY
    a.id, a.nombre
ORDER BY
    monto_total_impuesto DESC
LIMIT 1;

-- Problema 4: Obtener la multa más reciente para cada chofer que tenga al menos una multa,
-- mostrando el nombre del chofer, la fecha de la multa más reciente, y la descripción del tipo de multa.
-- Combinación: JOIN, Subconsulta correlacionada (o CTE con ROW_NUMBER si se prefiere), GROUP BY.
-- Opción 1: Con Subconsulta correlacionada (puede ser menos eficiente para grandes volúmenes)
SELECT
    c.nombres,
    c.apellidos,
    m.fecha AS ultima_multa_fecha,
    tm.descripcion AS tipo_ultima_multa
FROM
    choferes c
JOIN
    multas m ON c.id = m.chofer_id
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id
WHERE
    m.fecha = (SELECT MAX(fecha) FROM multas WHERE chofer_id = c.id);

-- Opción 2: Con CTE y ROW_NUMBER (preferida para MySQL 8+)
WITH UltimaMultaChofer AS (
    SELECT
        chofer_id,
        fecha,
        tipo_multa_id,
        ROW_NUMBER() OVER (PARTITION BY chofer_id ORDER BY fecha DESC) AS rn
    FROM
        multas
)
SELECT
    c.nombres,
    c.apellidos,
    umc.fecha AS ultima_multa_fecha,
    tm.descripcion AS tipo_ultima_multa
FROM
    choferes c
JOIN
    UltimaMultaChofer umc ON c.id = umc.chofer_id
JOIN
    tipos_multas tm ON umc.tipo_multa_id = tm.id
WHERE
    umc.rn = 1;


-- Problema 5: Listar todos los choferes que han sido multados por un vehículo que no tienen asignado
-- en la tabla `relacion_chofer_vehiculo` (en la fecha de la multa o si no hay registro).
-- Este problema implica identificar inconsistencias o escenarios donde un chofer pudo manejar un vehículo
-- sin que esté registrado oficialmente su asignación.
-- Combinación: LEFT JOIN (para encontrar ausencias), WHERE IS NULL, NOT EXISTS.
SELECT
    c.nombres,
    c.apellidos,
    v.placa AS vehiculo_multado,
    m.fecha AS fecha_multa,
    m.lugar AS lugar_multa
FROM
    choferes c
JOIN
    multas m ON c.id = m.chofer_id
JOIN
    vehiculos v ON m.vehiculo_id = v.id
LEFT JOIN
    relacion_chofer_vehiculo rcv ON c.id = rcv.chofer_id AND v.id = rcv.vehiculo_id
WHERE
    rcv.id IS NULL; -- Si rcv.id es NULL, significa que no hay una asignación registrada para ese chofer y vehículo.
    -- AND m.fecha >= rcv.fecha_asignacion_inicio AND m.fecha <= rcv.fecha_asignacion_fin (si tuvieras rango de asignación)

-- Problema 6: Para cada tipo de multa, mostrar el monto promedio, el monto máximo y el monto mínimo.
-- Combinación: GROUP BY, AVG, MAX, MIN.
SELECT
    descripcion AS tipo_multa,
    AVG(monto) AS monto_promedio,
    MAX(monto) AS monto_maximo,
    MIN(monto) AS monto_minimo
FROM
    tipos_multas
GROUP BY
    id, descripcion;

-- Problema 7: Obtener los choferes que tienen multas pendientes (es decir, no han pagado, si tuviéramos un estado de pago),
-- o, en este caso, simplemente listarlos por multas impuestas en 2024.
-- Y además, mostrar cuántas multas tienen y el monto total de esas multas.
-- Combinación: JOIN, GROUP BY, COUNT, SUM, WHERE con año.
SELECT
    c.nombres,
    c.apellidos,
    COUNT(m.id) AS cantidad_multas_2024,
    SUM(tm.monto) AS monto_total_multas_2024
FROM
    choferes c
JOIN
    multas m ON c.id = m.chofer_id
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id
WHERE
    YEAR(m.fecha) = 2024
GROUP BY
    c.id, c.nombres, c.apellidos
HAVING
    COUNT(m.id) > 0; -- Asegurarse de que tienen al menos una multa en 2024

-- Problema 8: Para cada mes del año 2023, contar cuántas multas se impusieron y cuál fue el monto total de esas multas.
-- Combinación: GROUP BY (por año y mes), COUNT, SUM, WHERE con rango de fechas, YEAR(), MONTH().
SELECT
    YEAR(fecha) AS anio,
    MONTH(fecha) AS mes,
    COUNT(m.id) AS total_multas,
    SUM(tm.monto) AS monto_recaudado
FROM
    multas m
JOIN
    tipos_multas tm ON m.tipo_multa_id = tm.id
WHERE
    YEAR(fecha) = 2023
GROUP BY
    anio, mes
ORDER BY
    anio, mes;

-- Problema 9: Encontrar el vehículo con más multas y el chofer que más lo ha manejado (según `relacion_chofer_vehiculo`).
-- Este problema es un poco más complejo y combina múltiples niveles de agregación.
-- Combinación: Subconsultas, JOINs, GROUP BY, ORDER BY, LIMIT.
SELECT
    v.placa,
    v.marca,
    v.modelo,
    (SELECT COUNT(*) FROM multas WHERE vehiculo_id = v.id) AS total_multas_vehiculo,
    c.nombres AS chofer_mas_asociado,
    c.apellidos AS apellidos_chofer_mas_asociado,
    (SELECT COUNT(*) FROM relacion_chofer_vehiculo r WHERE r.vehiculo_id = v.id AND r.chofer_id = c.id) AS veces_asociado
FROM
    vehiculos v
LEFT JOIN (
    SELECT
        vehiculo_id,
        chofer_id,
        COUNT(*) AS asignaciones
    FROM
        relacion_chofer_vehiculo
    GROUP BY
        vehiculo_id, chofer_id
    ORDER BY
        asignaciones DESC
) AS rcv_top ON v.id = rcv_top.vehiculo_id
LEFT JOIN
    choferes c ON rcv_top.chofer_id = c.id
ORDER BY
    total_multas_vehiculo DESC
LIMIT 1;

-- Problema 10: Listar todos los choferes que tienen multas de tipo 'Exceso de velocidad' (M20)
-- y también multas de tipo 'No respetar luz roja del semáforo' (L02).
-- Combinación: UNION, Subconsultas, JOINs.

SELECT
    c.nombres,
    c.apellidos,
    c.dni
FROM
    choferes c
WHERE
    c.id IN (SELECT chofer_id FROM multas m JOIN tipos_multas tm ON m.tipo_multa_id = tm.id WHERE tm.codigo = 'M100')
AND
    c.id IN (SELECT chofer_id FROM multas m JOIN tipos_multas tm ON m.tipo_multa_id = tm.id WHERE tm.codigo = 'M101');
    
