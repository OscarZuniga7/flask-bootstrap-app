-- Interpretamos este archivo como UTF-8 antes de crear o insertar datos.
SET NAMES utf8mb4 COLLATE utf8mb4_0900_ai_ci;

CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL
) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;

INSERT INTO posts (title, content) VALUES
    ('Primera publicación', 'Este registro fue creado al inicializar MySQL.'),
    ('Aprendiendo MySQL', 'Ahora los datos viven en un servidor de base de datos.'),
    ('Flask conectado a una base de datos', 'El servicio web se comunica con el servicio db.');
