CREATE TABLE autor (
    id_autor INT PRIMARY KEY,
    nombre VARCHAR(45)
);

CREATE TABLE libros (
    id_libro INT PRIMARY KEY,
    titulo VARCHAR(55),
    genero VARCHAR(55),
    id_autor INT,
    paginas INT,
    FOREIGN KEY (id_autor) REFERENCES autor(id_autor)
);

-- tabla intermedia -- 
CREATE TABLE autorLibro(
    libro id INT, 
    autor id INT
); 

CREATE TABLE lecturas (
    id_lectura INT PRIMARY KEY AUTO_INCREMENT,
    usuario_id INT, 
    libro_id INT, 
    fecha_inicio DATE, 
    fecha_fin DATE,
    estado VARCHAR(20), 
    puntuacion FLOAT,
    comentario TEXT,
    FOREIGN KEY (libro_id) REFERENCES autorLibro (libro_id)
    FOREIGN KEY (usuario_id) REFERENCES usuario (id_usuario)
    -- FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
    
    -- validaciones -- 
    CONSTRAINT chk_puntuacion CHECK (puntuacion BETWEEN 1 AND 5),
    CONSTRAINT chk_fechas CHECK (fecha_fin IS NULL Or (fecha_inicio IS NOT NULL AND fecha_fin >= fecha_inicio)),
    CONSTRAINT chk_comentario CHECK (comentario IN ('Excelente', 'Muy bueno', 'Bueno', 'Regular', 'Malo'))
    CONSTRAINT chk_estado CHECK (estado IN ('Pendiente', 'Leyendo', 'Abandonado', 'Terminado'))
);

CREATE TABLE usuario (
    id_usuario INT PRIMARY KEY, 
    nombre VARCHAR(55)
);

-- permite una unica lectura por libro en estado leyendo 
CREATE UNIQUE INDEX unica_lectura_activa 
ON lecturas (id_usuario, libro_id)
WHERE estado = 'Leyendo'; 

CREATE TABLE historial_comentarios (
    id_historial INT PRIMARY KEY AUTO_INCREMENT,
    id_lectura INT,
    comentario_anterior TEXT,
    comentario_nuevo TEXT,
    fecha_cambio DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_lectura) REFERENCES lecturas (id_lectura)
);
