-- Interpretamos este archivo como UTF-8 antes de crear o insertar datos.
SET NAMES utf8mb4 COLLATE utf8mb4_0900_ai_ci;

-- ESTUDIANTE se transforma en una tabla; cada columna representa un atributo.
CREATE TABLE IF NOT EXISTS estudiantes (
    id_estudiante INT AUTO_INCREMENT PRIMARY KEY,
    rut VARCHAR(15) NOT NULL UNIQUE,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(120) NOT NULL UNIQUE,
    carrera VARCHAR(100) NOT NULL,
    fecha_ingreso DATE NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

-- Datos completamente ficticios para la actividad de laboratorio.
INSERT INTO estudiantes (rut, nombre, email, carrera, fecha_ingreso) VALUES
    ('11.111.111-1', 'Ana Muñoz', 'ana.munoz@example.com', 'Ingeniería Informática', '2026-03-02'),
    ('12.222.222-2', 'José Pérez', 'jose.perez@example.com', 'Administración Pública', '2026-03-02'),
    ('13.333.333-3', 'María Núñez', 'maria.nunez@example.com', 'Diseño', '2025-03-03'),
    ('14.444.444-4', 'Tomás Peña', 'tomas.pena@example.com', 'Contabilidad', NULL),
    ('15.555.555-5', 'Sofía González', 'sofia.gonzalez@example.com', 'Ingeniería Comercial', '2026-03-02');
