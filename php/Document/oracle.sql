
-- ********************************************************************************
-- A. LENGUAJE DE MANIPULACIÓN DE DATOS (DML) Y CONSULTAS SIMPLES
-- ********************************************************************************

-- Este apartado cubre las operaciones básicas de INSERT, UPDATE, DELETE y SELECT.

-- --------------------------------------------------------------------------------
-- A.1. CONSULTAS DE SELECCIÓN SIMPLES (SELECT)
-- --------------------------------------------------------------------------------

-- Las consultas SELECT son fundamentales para recuperar datos de una o más tablas.
-- Aquí se muestran ejemplos básicos.

-- Ejemplo 1.1: Seleccionar todos los clientes.
-- Objetivo: Obtener una vista completa de todos los clientes registrados.
SELECT
    cliente_id,
    nombre,
    apellido,
    telefono,
    email
FROM
    CLIENTES
FETCH FIRST 100 ROWS ONLY; -- Limitar a 100 filas para previsualización en bases de datos grandes

-- Ejemplo 1.2: Seleccionar préstamos activos con monto superior a $50,000.
-- Objetivo: Filtrar préstamos por estado y monto para identificar préstamos importantes.
SELECT
    prestamo_id,
    cliente_id,
    monto_principal,
    fecha_solicitud,
    estado
FROM
    PRESTAMOS
WHERE
        estado = 'ACTIVO'
    AND monto_principal > 50000
FETCH FIRST 50 ROWS ONLY; -- Limitar a 50 filas para previsualización

-- Ejemplo 1.3: Seleccionar empleados con un cargo específico, ordenados por apellido.
-- Objetivo: Encontrar y organizar información sobre empleados con un rol particular.
SELECT
    empleado_id,
    nombre,
    apellido,
    cargo,
    fecha_contratacion
FROM
    EMPLEADOS
WHERE
    cargo = 'Asesor de Crédito'
ORDER BY
    apellido ASC, nombre ASC
FETCH FIRST 20 ROWS ONLY; -- Limitar a 20 filas para previsualización

-- --------------------------------------------------------------------------------
-- A.2. INSERCIÓN DE DATOS (INSERT)
-- --------------------------------------------------------------------------------

-- Las sentencias INSERT INTO se utilizan para añadir nuevas filas (registros) a una tabla.

-- Ejemplo 2.1: Insertar un nuevo cliente.
-- Objetivo: Añadir un nuevo registro de cliente al sistema.
INSERT INTO CLIENTES (
    nombre,
    apellido,
    direccion,
    telefono,
    email,
    fecha_registro
) VALUES (
    'Juan',
    'Pérez',
    'Av. Siempreviva 123',
    '987654321',
    'juan.perez@example.com',
    SYSDATE
);
COMMIT; -- Confirmar la transacción

-- Ejemplo 2.2: Insertar un nuevo tipo de préstamo.
-- Objetivo: Añadir una nueva categoría de préstamo ofrecida por la entidad.
INSERT INTO TIPOS_PRESTAMO (
    nombre_tipo,
    descripcion,
    tasa_interes
) VALUES (
    'PyME',
    'Préstamo para pequeñas y medianas empresas',
    0.12
);
COMMIT;

-- Ejemplo 2.3: Insertar un nuevo préstamo para un cliente y tipo de préstamo existentes.
-- Nota: Asegúrate de que los cliente_id, tipo_prestamo_id y empleado_id existan.
-- Objetivo: Registrar un nuevo préstamo solicitado en el sistema.
INSERT INTO PRESTAMOS (
    cliente_id,
    tipo_prestamo_id,
    empleado_id,
    monto_principal,
    fecha_solicitud,
    plazo_meses,
    estado
) VALUES (
    1, -- Asume que el cliente_id 1 existe
    1, -- Asume que el tipo_prestamo_id 1 (Personal) existe
    1, -- Asume que el empleado_id 1 existe
    7500.00,
    SYSDATE - 30, -- Solicitado hace 30 días
    36,
    'APROBADO'
);
COMMIT;

-- --------------------------------------------------------------------------------
-- A.3. ACTUALIZACIÓN DE DATOS (UPDATE)
-- --------------------------------------------------------------------------------

-- Las sentencias UPDATE se utilizan para modificar los datos de filas existentes en una tabla.

-- Ejemplo 3.1: Actualizar el estado de un préstamo a 'PAGADO'.
-- Objetivo: Cambiar el estado de un préstamo específico una vez saldado.
UPDATE PRESTAMOS
SET
    estado = 'PAGADO',
    fecha_aprobacion = SYSDATE -- Se asume que al pagarse, también se actualiza la fecha de aprobación/finalización
WHERE
    prestamo_id = 100; -- Reemplaza con un ID de préstamo real
COMMIT;

-- Ejemplo 3.2: Aumentar el salario de los empleados en un cargo específico.
-- Objetivo: Realizar un ajuste salarial masivo para un grupo de empleados.
UPDATE EMPLEADOS
SET
    salario = salario * 1.05 -- Aumentar 5%
WHERE
    cargo = 'Asesor de Crédito';
COMMIT;

-- Ejemplo 3.3: Actualizar el número de teléfono de un cliente por su email.
-- Objetivo: Modificar la información de contacto de un cliente basándose en un identificador único.
UPDATE CLIENTES
SET
    telefono = '999888777'
WHERE
    email = 'juan.perez@example.com';
COMMIT;

-- --------------------------------------------------------------------------------
-- A.4. ELIMINACIÓN DE DATOS (DELETE)
-- --------------------------------------------------------------------------------

-- Las sentencias DELETE FROM se utilizan para eliminar filas de una tabla.
-- ¡ATENCIÓN! Siempre usa una cláusula WHERE con DELETE para evitar borrar todos los registros.

-- Ejemplo 4.1: Eliminar un pago específico.
-- Objetivo: Borrar un registro de pago individual (e.g., por error de ingreso).
DELETE FROM PAGOS
WHERE
    pago_id = 1; -- Reemplaza con un ID de pago real
COMMIT;

-- Ejemplo 4.2: Eliminar préstamos rechazados de hace más de 5 años.
-- Objetivo: Limpiar registros antiguos de préstamos que no se concretaron.
DELETE FROM PRESTAMOS
WHERE
        estado = 'RECHAZADO'
    AND fecha_solicitud < ADD_MONTHS(SYSDATE, - (5 * 12)); -- Más de 5 años
COMMIT;

-- Ejemplo 4.3: Eliminar un cliente y sus registros relacionados en el historial de crédito.
-- Nota: Para eliminar un cliente que tiene préstamos, primero tendrías que eliminar sus préstamos (y pagos/garantías asociadas),
-- o bien definir las FKs con ON DELETE CASCADE. Aquí, solo eliminamos el historial.
-- Objetivo: Borrar la información de un cliente que ya no opera con la entidad (y su historial).
DELETE FROM HISTORIAL_CREDITO
WHERE
    cliente_id = 100; -- Reemplaza con un ID de cliente real
COMMIT;

-- ********************************************************************************
-- B. CONSULTAS MÚLTIPLES (JOINS)
-- ********************************************************************************

-- Las consultas múltiples combinan datos de dos o más tablas usando JOINs.

-- Ejemplo 5.1: Listar préstamos con el nombre del cliente y el tipo de préstamo.
-- Uso de JOIN simple (INNER JOIN es el predeterminado si no se especifica)
-- Objetivo: Obtener una vista consolidada de los préstamos mostrando quién los solicitó y de qué tipo son.
SELECT
    p.prestamo_id,
    c.nombre AS nombre_cliente,
    c.apellido AS apellido_cliente,
    tp.nombre_tipo AS tipo_de_prestamo,
    p.monto_principal,
    p.estado,
    p.fecha_solicitud
FROM
    PRESTAMOS     p
    JOIN CLIENTES      c ON p.cliente_id = c.cliente_id
    JOIN TIPOS_PRESTAMO tp ON p.tipo_prestamo_id = tp.tipo_prestamo_id
FETCH FIRST 100 ROWS ONLY;

-- Ejemplo 5.2: Mostrar todos los empleados y los préstamos que han gestionado (incluyendo los que no han gestionado ninguno).
-- Uso de LEFT JOIN para incluir empleados que no tienen préstamos asignados.
-- Objetivo: Evaluar la carga de trabajo de los empleados en relación con los préstamos.
SELECT
    e.nombre AS nombre_empleado,
    e.apellido AS apellido_empleado,
    e.cargo,
    COUNT(p.prestamo_id) AS total_prestamos_gestionados
FROM
    EMPLEADOS e
    LEFT JOIN PRESTAMOS p ON e.empleado_id = p.empleado_id
GROUP BY
    e.nombre,
    e.apellido,
    e.cargo
ORDER BY
    total_prestamos_gestionados DESC,
    e.apellido ASC
FETCH FIRST 50 ROWS ONLY;

-- Ejemplo 5.3: Clientes que tienen un préstamo activo y al menos una garantía asociada.
-- Uso de INNER JOINs múltiples y DISTINCT para evitar duplicados.
-- Objetivo: Identificar clientes de alto riesgo o con grandes préstamos que tienen garantías registradas.
SELECT DISTINCT
    c.cliente_id,
    c.nombre,
    c.apellido,
    p.prestamo_id,
    p.monto_principal,
    p.estado,
    g.descripcion AS descripcion_garantia
FROM
    CLIENTES  c
    JOIN PRESTAMOS p ON c.cliente_id = p.cliente_id
    JOIN GARANTIAS g ON p.prestamo_id = g.prestamo_id
WHERE
    p.estado = 'ACTIVO'
ORDER BY
    c.cliente_id
FETCH FIRST 100 ROWS ONLY;

-- ********************************************************************************
-- C. CONSULTAS DE RESUMEN Y SUBCONSULTAS
-- ********************************************************************************

-- Este apartado cubre funciones de agregación (SUM, AVG, COUNT, MAX, MIN) y subconsultas.

-- --------------------------------------------------------------------------------
-- C.1. CONSULTAS DE RESUMEN (FUNCIONES DE AGREGACIÓN Y GROUP BY)
-- --------------------------------------------------------------------------------

-- Las funciones de agregación calculan un único valor a partir de un conjunto de filas.
-- GROUP BY se usa para agrupar filas que tienen los mismos valores en columnas especificadas en conjuntos de resumen.

-- Ejemplo 6.1: Monto total de préstamos por estado.
-- Objetivo: Obtener un resumen financiero de los préstamos agrupados por su situación actual.
SELECT
    estado,
    COUNT(prestamo_id)   AS numero_de_prestamos,
    SUM(monto_principal) AS monto_total
FROM
    PRESTAMOS
GROUP BY
    estado
ORDER BY
    monto_total DESC;

-- Ejemplo 6.2: Monto promedio de pagos por tipo de préstamo.
-- Objetivo: Analizar el promedio de pagos en diferentes categorías de préstamos.
SELECT
    tp.nombre_tipo,
    AVG(pago.monto_pago) AS monto_promedio_pago
FROM
    PAGOS         pago
    JOIN PRESTAMOS   p ON pago.prestamo_id = p.prestamo_id
    JOIN TIPOS_PRESTAMO tp ON p.tipo_prestamo_id = tp.tipo_prestamo_id
GROUP BY
    tp.nombre_tipo
HAVING
    COUNT(pago.pago_id) > 100 -- Solo tipos de préstamo con más de 100 pagos
ORDER BY
    monto_promedio_pago DESC;

-- Ejemplo 6.3: Cliente con el mayor número de préstamos activos.
-- Objetivo: Identificar a los clientes con más actividad de préstamo.
SELECT
    c.cliente_id,
    c.nombre,
    c.apellido,
    COUNT(p.prestamo_id) AS total_prestamos_activos
FROM
    CLIENTES  c
    JOIN PRESTAMOS p ON c.cliente_id = p.cliente_id
WHERE
    p.estado = 'ACTIVO'
GROUP BY
    c.cliente_id,
    c.nombre,
    c.apellido
ORDER BY
    total_prestamos_activos DESC
FETCH FIRST 1 ROW ONLY;

-- --------------------------------------------------------------------------------
-- C.2. SUBCONSULTAS (SUBQUERIES)
-- --------------------------------------------------------------------------------

-- Las subconsultas son consultas anidadas que se ejecutan antes de la consulta principal.
-- Pueden ser usadas en la cláusula WHERE, FROM, o SELECT.

-- Ejemplo 7.1: Clientes que tienen al menos un préstamo "ATRASADO".
-- Subconsulta en la cláusula WHERE (IN).
-- Objetivo: Obtener la lista de clientes con préstamos morosos.
SELECT
    cliente_id,
    nombre,
    apellido
FROM
    CLIENTES
WHERE
    cliente_id IN (
        SELECT DISTINCT
            cliente_id
        FROM
            PRESTAMOS
        WHERE
            estado = 'ATRASADO'
    )
FETCH FIRST 50 ROWS ONLY;

-- Ejemplo 7.2: Empleados que gestionan préstamos con un monto principal mayor al promedio general.
-- Subconsulta en la cláusula WHERE (escalar).
-- Objetivo: Identificar empleados que trabajan con préstamos de alto valor.
SELECT
    e.empleado_id,
    e.nombre,
    e.apellido,
    e.cargo
FROM
    EMPLEADOS e
WHERE
    e.empleado_id IN (
        SELECT DISTINCT
            p.empleado_id
        FROM
            PRESTAMOS p
        WHERE
            p.monto_principal > (
                SELECT
                    AVG(monto_principal)
                FROM
                    PRESTAMOS
            )
            AND p.empleado_id IS NOT NULL
    )
ORDER BY e.apellido
FETCH FIRST 50 ROWS ONLY;

-- Ejemplo 7.3: Mostrar el nombre del cliente y el monto total de sus préstamos, junto con el promedio global.
-- Subconsulta escalar en la cláusula SELECT.
-- Objetivo: Comparar el volumen de préstamos de cada cliente con el promedio del sistema.
SELECT
    c.nombre,
    c.apellido,
    (
        SELECT
            SUM(p.monto_principal)
        FROM
            PRESTAMOS p
        WHERE
            p.cliente_id = c.cliente_id
    ) AS monto_total_prestamos_cliente,
    (
        SELECT
            AVG(monto_principal)
        FROM
            PRESTAMOS
    ) AS promedio_global_monto_prestamo
FROM
    CLIENTES c
WHERE
    (
        SELECT
            SUM(p.monto_principal)
        FROM
            PRESTAMOS p
        WHERE
            p.cliente_id = c.cliente_id
    ) IS NOT NULL -- Solo clientes con préstamos
ORDER BY
    monto_total_prestamos_cliente DESC
FETCH FIRST 100 ROWS ONLY;
-- Consulta Optimizado
-- Versión OPTIMIZADA: Mostrar el nombre del cliente y el monto total de sus préstamos,
--                     junto con el promedio global.
-- Objetivo: Comparar el volumen de préstamos de cada cliente con el promedio del sistema,
--           pero de manera eficiente para grandes volúmenes de datos.

WITH
    -- CTE 1: Calcula el monto total de préstamos por cada cliente.
    -- Se ejecuta una sola vez y agrupa todos los préstamos para cada cliente.
    TotalPrestamosPorCliente AS (
        SELECT
            p.cliente_id,
            SUM(p.monto_principal) AS monto_total_prestamos
        FROM
            PRESTAMOS p
        GROUP BY
            p.cliente_id
    ),
    -- CTE 2: Calcula el promedio global del monto principal de todos los préstamos.
    -- Esta subconsulta se ejecuta una sola vez.
    PromedioGlobalPrestamos AS (
        SELECT
            AVG(monto_principal) AS promedio_global_monto
        FROM
            PRESTAMOS
    )
SELECT
    c.nombre,
    c.apellido,
    tpc.monto_total_prestamos,
    pgp.promedio_global_monto
FROM
    CLIENTES c
    -- Unir con la CTE de totales por cliente. Usamos INNER JOIN porque solo queremos
    -- clientes que tienen préstamos (ya que TotalPrestamosPorCliente solo incluye esos).
    JOIN TotalPrestamosPorCliente tpc ON c.cliente_id = tpc.cliente_id
    -- Unir con la CTE del promedio global. Esto es un CROSS JOIN conceptualmente
    -- porque el promedio global es una única fila que se replica para todas las filas resultantes.
    CROSS JOIN PromedioGlobalPrestamos pgp
ORDER BY
    tpc.monto_total_prestamos DESC
FETCH FIRST 100 ROWS ONLY;
-- ********************************************************************************
-- D. PROBLEMAS DE NIVEL INTERMEDIO A AVANZADO
-- ********************************************************************************

-- Estos problemas requieren un conocimiento más profundo de SQL, incluyendo
-- funciones de ventana, CTEs (Common Table Expressions), y combinaciones complejas.

-- Problema 1: Préstamos con pagos incompletos o atrasados que superan el monto principal original.
-- Objetivo: Identificar préstamos problemáticos donde la suma de los pagos no cubre aún el principal,
--           o donde hay pagos, pero el estado es 'ATRASADO'.
SELECT
    p.prestamo_id,
    c.nombre AS cliente_nombre,
    c.apellido AS cliente_apellido,
    p.monto_principal,
    p.estado,
    NVL(SUM(pa.monto_pago), 0) AS monto_total_pagado,
    (p.monto_principal - NVL(SUM(pa.monto_pago), 0)) AS monto_pendiente
FROM
    PRESTAMOS p
    JOIN CLIENTES c ON p.cliente_id = c.cliente_id
    LEFT JOIN PAGOS pa ON p.prestamo_id = pa.prestamo_id
WHERE
    p.estado IN ('ACTIVO', 'ATRASADO') -- Nos interesan los préstamos activos o atrasados
GROUP BY
    p.prestamo_id,
    c.nombre,
    c.apellido,
    p.monto_principal,
    p.estado,
    p.fecha_solicitud,
    p.plazo_meses
HAVING
    (p.estado = 'ATRASADO' AND NVL(SUM(pa.monto_pago), 0) < p.monto_principal)
    OR (p.estado = 'ACTIVO' AND NVL(SUM(pa.monto_pago), 0) < p.monto_principal AND p.fecha_solicitud < ADD_MONTHS(SYSDATE, -p.plazo_meses)) -- Préstamos activos que deberían haber terminado
ORDER BY
    monto_pendiente DESC
FETCH FIRST 100 ROWS ONLY;

-- Problema 2: Clientes con un historial de múltiples solicitudes de préstamo (aprobadas o rechazadas) en un corto período.
-- Uso de Funciones de Ventana (LAG o LEAD) o CTE para analizar secuencias de eventos.
-- Objetivo: Detectar patrones de comportamiento de cliente que podrían indicar riesgo o necesidad recurrente.
WITH ClienteEventos AS (
    SELECT
        hc.cliente_id,
        hc.fecha_evento,
        hc.tipo_evento,
        LAG(hc.fecha_evento, 1, hc.fecha_evento) OVER (PARTITION BY hc.cliente_id ORDER BY hc.fecha_evento) AS fecha_evento_anterior
    FROM
        HISTORIAL_CREDITO hc
    WHERE
        hc.tipo_evento IN ('SOLICITUD', 'APROBACION', 'RECHAZO')
)
SELECT
    cli.cliente_id, -- Usar el alias correcto 'cli'
    cli.nombre,     -- Usar el alias correcto 'cli'
    cli.apellido,   -- Usar el alias correcto 'cli'
    COUNT(*) AS numero_solicitudes_cortas,
    MIN(ce.fecha_evento) AS primera_solicitud_periodo,
    MAX(ce.fecha_evento) AS ultima_solicitud_periodo
FROM
    CLIENTES cli -- Alias a la tabla CLIENTES como 'cli'
    JOIN ClienteEventos ce ON cli.cliente_id = ce.cliente_id -- Usar 'cli' para CLIENTES
WHERE
    (ce.fecha_evento - ce.fecha_evento_anterior) <= 30 -- Eventos con menos de 30 días de diferencia
GROUP BY
    cli.cliente_id,
    cli.nombre,
    cli.apellido
HAVING
    COUNT(*) >= 3 -- Al menos 3 solicitudes en un período corto
ORDER BY
    numero_solicitudes_cortas DESC
FETCH FIRST 50 ROWS ONLY;


-- Problema 3: Empleados que gestionaron el mayor volumen de préstamos aprobados en el último año,
--             y su impacto en la tasa de mora (préstamos 'ATRASADO').
-- Uso de CTEs y agrupaciones con filtros de fecha.
-- Objetivo: Evaluar el rendimiento de los empleados no solo por volumen, sino también por calidad de préstamos.
WITH EmpleadoRendimiento AS (
    SELECT
        e.empleado_id,
        e.nombre,
        e.apellido,
        COUNT(p.prestamo_id) AS total_prestamos_aprobados_ultimo_anio,
        SUM(CASE WHEN p.estado = 'ATRASADO' THEN 1 ELSE 0 END) AS total_prestamos_atrasados_ultimo_anio
    FROM
        EMPLEADOS e
        JOIN PRESTAMOS p ON e.empleado_id = p.empleado_id
    WHERE
            p.fecha_aprobacion >= ADD_MONTHS(SYSDATE, -12) -- Último año
        AND p.estado IN ('APROBADO', 'ACTIVO', 'PAGADO', 'ATRASADO') -- Solo préstamos aprobados
    GROUP BY
        e.empleado_id,
        e.nombre,
        e.apellido
)
SELECT
    er.nombre,
    er.apellido,
    er.total_prestamos_aprobados_ultimo_anio,
    er.total_prestamos_atrasados_ultimo_anio,
    CASE
        WHEN er.total_prestamos_aprobados_ultimo_anio > 0 THEN
            ROUND((er.total_prestamos_atrasados_ultimo_anio / er.total_prestamos_aprobados_ultimo_anio) * 100, 2)
        ELSE
            0
    END AS tasa_mora_porcentaje
FROM
    EmpleadoRendimiento er
WHERE
    er.total_prestamos_aprobados_ultimo_anio > 0 -- Solo empleados con al menos un préstamo aprobado en el periodo
ORDER BY
    tasa_mora_porcentaje DESC,
    er.total_prestamos_aprobados_ultimo_anio DESC
FETCH FIRST 100 ROWS ONLY;


-- Problema 4: Calcular el saldo restante estimado para cada préstamo activo o atrasado,
--             asumiendo que todos los pagos son para el principal.
-- Uso de CTEs y funciones de agregación.
-- Objetivo: Tener una estimación rápida del capital pendiente de cada préstamo.
WITH SaldoPagado AS (
    SELECT
        prestamo_id,
        NVL(SUM(monto_pago), 0) AS total_pagado
    FROM
        PAGOS
    GROUP BY
        prestamo_id
)
SELECT
    p.prestamo_id,
    c.nombre AS cliente_nombre,
    c.apellido AS cliente_apellido,
    tp.nombre_tipo,
    p.monto_principal,
    p.estado,
    sp.total_pagado,
    (p.monto_principal - sp.total_pagado) AS saldo_estimado_pendiente
FROM
    PRESTAMOS p
    JOIN CLIENTES c ON p.cliente_id = c.cliente_id
    JOIN TIPOS_PRESTAMO tp ON p.tipo_prestamo_id = tp.tipo_prestamo_id
    LEFT JOIN SaldoPagado sp ON p.prestamo_id = sp.prestamo_id
WHERE
    p.estado IN ('ACTIVO', 'ATRASADO') -- Solo préstamos que aún no están pagados
    AND (p.monto_principal - NVL(sp.total_pagado, 0)) > 0 -- Saldo pendiente mayor que 0
ORDER BY
    saldo_estimado_pendiente DESC
FETCH FIRST 200 ROWS ONLY;

-- Problema 5: Distribución de préstamos aprobados por mes y año, mostrando el crecimiento.
-- Uso de GROUP BY con funciones de fecha y PIVOT (si se quisiera una vista de tabla cruzada).
-- Objetivo: Analizar las tendencias de aprobación de préstamos a lo largo del tiempo.
SELECT
    TO_CHAR(fecha_aprobacion, 'YYYY') AS anio_aprobacion,
    TO_CHAR(fecha_aprobacion, 'MM') AS mes_aprobacion,
    COUNT(prestamo_id) AS total_prestamos_aprobados,
    SUM(monto_principal) AS monto_total_aprobado
FROM
    PRESTAMOS
WHERE
    estado = 'APROBADO'
    AND fecha_aprobacion IS NOT NULL
GROUP BY
    TO_CHAR(fecha_aprobacion, 'YYYY'),
    TO_CHAR(fecha_aprobacion, 'MM')
ORDER BY
    anio_aprobacion ASC,
    mes_aprobacion ASC;

-- Problema 6: Identificar la garantía más común asociada a préstamos hipotecarios.
-- Uso de JOIN y agrupamiento con subconsulta para encontrar el valor TOP.
-- Objetivo: Conocer qué tipos de garantías son más frecuentes para ciertos tipos de préstamos.
SELECT
    g.descripcion, -- Especifica que es la descripción de la tabla GARANTIAS
    COUNT(*) AS cantidad
FROM
    GARANTIAS g
    JOIN PRESTAMOS p ON g.prestamo_id = p.prestamo_id
    JOIN TIPOS_PRESTAMO tp ON p.tipo_prestamo_id = tp.tipo_prestamo_id
WHERE
    tp.nombre_tipo = 'Hipotecario'
GROUP BY
    g.descripcion -- Especifica que es la descripción de la tabla GARANTIAS
ORDER BY
    cantidad DESC
FETCH FIRST 1 ROW ONLY;

-- Problema 7: Clientes que han tenido al menos un préstamo de cada tipo disponible.
-- Uso de GROUP BY y HAVING COUNT(DISTINCT) para verificar la cobertura de tipos de préstamo.
-- Objetivo: Encontrar clientes "multi-producto" que han utilizado varios servicios de préstamo.
SELECT
    c.cliente_id,
    c.nombre,
    c.apellido,
    COUNT(DISTINCT p.tipo_prestamo_id) AS tipos_prestamo_diferentes
FROM
    CLIENTES  c
    JOIN PRESTAMOS p ON c.cliente_id = p.cliente_id
GROUP BY
    c.cliente_id,
    c.nombre,
    c.apellido
HAVING
    COUNT(DISTINCT p.tipo_prestamo_id) = (
        SELECT
            COUNT(*)
        FROM
            TIPOS_PRESTAMO
    ) -- Igual al número total de tipos de préstamo
ORDER BY
    c.cliente_id;

-- Problema 8: Préstamos donde el monto de los pagos supera el monto principal (sobrepago).
-- Objetivo: Identificar posibles errores o casos de sobrepago en los préstamos.
SELECT
    p.prestamo_id,
    c.nombre AS cliente_nombre,
    c.apellido AS cliente_apellido,
    p.monto_principal,
    SUM(pa.monto_pago) AS monto_total_pagado,
    (SUM(pa.monto_pago) - p.monto_principal) AS sobrepago_cantidad
FROM
    PRESTAMOS p
    JOIN CLIENTES c ON p.cliente_id = c.cliente_id
    JOIN PAGOS pa ON p.prestamo_id = pa.prestamo_id
GROUP BY
    p.prestamo_id,
    c.nombre,
    c.apellido,
    p.monto_principal
HAVING
    SUM(pa.monto_pago) > p.monto_principal
ORDER BY
    sobrepago_cantidad DESC
FETCH FIRST 50 ROWS ONLY;

-- Problema 9: Top 5 clientes con el mayor monto total de préstamos (activos y pagados).
-- Uso de funciones analíticas (ROW_NUMBER) o TOP N.
-- Objetivo: Identificar a los clientes más valiosos en términos de volumen de préstamos.
SELECT
    cliente_id,
    nombre,
    apellido,
    monto_total_prestamos
FROM
    (
        SELECT
            c.cliente_id,
            c.nombre,
            c.apellido,
            SUM(p.monto_principal) AS monto_total_prestamos,
            ROW_NUMBER() OVER (
                ORDER BY
                    SUM(p.monto_principal) DESC
            ) rn
        FROM
            CLIENTES  c
            JOIN PRESTAMOS p ON c.cliente_id = p.cliente_id
        WHERE
            p.estado IN ('ACTIVO', 'PAGADO')
        GROUP BY
            c.cliente_id,
            c.nombre,
            c.apellido
    )
WHERE
    rn <= 5;

-- Problema 10: Clientes que solicitaron un préstamo, fue rechazado, y luego solicitaron otro que fue aprobado,
--              todo dentro del mismo año.
-- Uso de CTEs y uniones para analizar secuencias de eventos de historial de crédito y préstamos.
-- Objetivo: Identificar clientes con un historial de "segundas oportunidades" de préstamo.
WITH ClienteHistorialAnual AS (
    SELECT
        cliente_id,
        tipo_evento,
        fecha_evento,
        TO_CHAR(fecha_evento, 'YYYY') AS anio_evento
    FROM
        HISTORIAL_CREDITO
    WHERE
        tipo_evento IN ('SOLICITUD', 'RECHAZO', 'APROBACION')
), ClienteSecuencia AS (
    SELECT
        cha1.cliente_id,
        cha1.anio_evento,
        cha1.fecha_evento AS fecha_rechazo,
        cha2.fecha_evento AS fecha_aprobacion,
        cha1.tipo_evento AS tipo_rechazo,
        cha2.tipo_evento AS tipo_aprobacion
    FROM
        ClienteHistorialAnual cha1
        JOIN ClienteHistorialAnual cha2 ON cha1.cliente_id = cha2.cliente_id
                                       AND cha1.anio_evento = cha2.anio_evento
    WHERE
            cha1.tipo_evento = 'RECHAZO'
        AND cha2.tipo_evento = 'APROBACION'
        AND cha2.fecha_evento > cha1.fecha_evento -- Aprobación posterior al rechazo
)
SELECT DISTINCT
    c.cliente_id,
    c.nombre,
    c.apellido,
    cs.anio_evento,
    cs.fecha_rechazo,
    cs.fecha_aprobacion
FROM
    CLIENTES c
    JOIN ClienteSecuencia cs ON c.cliente_id = cs.cliente_id
ORDER BY
    c.cliente_id, cs.anio_evento;

-- ********************************************************************************
-- FIN DEL SCRIPT
-- ********************************************************************************