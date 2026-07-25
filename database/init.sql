CREATE TABLE IF NOT EXISTS posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    content TEXT NOT NULL
);

INSERT INTO posts (title, content) VALUES
    ('Primera publicación', 'Este registro fue creado al inicializar MySQL.'),
    ('Aprendiendo MySQL', 'Ahora los datos viven en un servidor de base de datos.'),
    ('Flask conectado a una base de datos', 'El servicio web se comunica con el servicio db.');
