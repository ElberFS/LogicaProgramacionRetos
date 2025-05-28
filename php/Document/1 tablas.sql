-- ===========================================
-- BASE DE DATOS: Sistema de Control de Multas de Tránsito - Perú
-- DESCRIPCIÓN:
-- Controla las multas impuestas a vehículos, identificando al chofer,
-- tipo de infracción, autoridad sancionadora, lugar y fecha de la infracción.
-- ===========================================

-- ===========================================
-- TABLA 1: CHOFERES
-- Información personal y licencia del conductor
-- ===========================================
CREATE TABLE choferes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombres VARCHAR(50) NOT NULL,              -- Nombres del chofer
    apellidos VARCHAR(50) NOT NULL,            -- Apellidos del chofer
    dni CHAR(8) UNIQUE NOT NULL,               -- Documento Nacional de Identidad
    licencia_conducir VARCHAR(15) UNIQUE NOT NULL,  -- Número de licencia
    celular CHAR(9),                           -- Número de celular
    correo VARCHAR(60)                         -- Correo electrónico
);

-- ===========================================
-- TABLA 2: VEHICULOS
-- Detalles del vehículo involucrado
-- ===========================================
CREATE TABLE vehiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) UNIQUE NOT NULL,         -- Placa única del vehículo
    marca VARCHAR(30),                         -- Marca del vehículo
    modelo VARCHAR(30),                        -- Modelo del vehículo
    anio YEAR,                                 -- Año de fabricación
    color VARCHAR(20)                          -- Color del vehículo
);

-- ===========================================
-- TABLA 3: AUTORIDADES
-- Instituciones que imponen multas
-- ===========================================
CREATE TABLE autoridades (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,              -- Ejemplo: Municipalidad de Lima
    tipo ENUM('Policia', 'Municipalidad') NOT NULL -- Tipo de autoridad sancionadora
);

-- ===========================================
-- TABLA 4: TIPOS DE MULTAS
-- Catálogo de infracciones posibles
-- ===========================================
CREATE TABLE tipos_multas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descripcion VARCHAR(100) NOT NULL,         -- Descripción de la infracción
    codigo VARCHAR(10) UNIQUE NOT NULL,        -- Código oficial (Ej: M20, P01)
    monto DECIMAL(10,2) NOT NULL               -- Monto de la multa en soles
);

-- ===========================================
-- TABLA 5: MULTAS
-- Registro de cada multa emitida
-- ===========================================
CREATE TABLE multas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chofer_id INT NOT NULL,                    -- ID del chofer infractor
    vehiculo_id INT NOT NULL,                  -- ID del vehículo infractor
    autoridad_id INT NOT NULL,                 -- ID de la autoridad que multó
    tipo_multa_id INT NOT NULL,                -- ID del tipo de multa
    fecha DATE NOT NULL,                       -- Fecha de la multa
    lugar VARCHAR(100) NOT NULL,               -- Lugar donde ocurrió la infracción
    observaciones TEXT,                        -- Observaciones adicionales
    FOREIGN KEY (chofer_id) REFERENCES choferes(id),
    FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id),
    FOREIGN KEY (autoridad_id) REFERENCES autoridades(id),
    FOREIGN KEY (tipo_multa_id) REFERENCES tipos_multas(id)
);

-- ===========================================
-- TABLA 6: RELACIÓN CHOFER - VEHÍCULO
-- Historial de asignaciones de choferes a vehículos
-- (opcional pero recomendable para trazabilidad)
-- ===========================================
CREATE TABLE relacion_chofer_vehiculo (
    id INT AUTO_INCREMENT PRIMARY KEY,
    chofer_id INT NOT NULL,                    -- ID del chofer
    vehiculo_id INT NOT NULL,                  -- ID del vehículo
    fecha_asignacion DATE NOT NULL,            -- Fecha de asignación del vehículo
    FOREIGN KEY (chofer_id) REFERENCES choferes(id),
    FOREIGN KEY (vehiculo_id) REFERENCES vehiculos(id)
);
