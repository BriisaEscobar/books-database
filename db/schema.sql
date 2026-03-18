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

CREATE TABLE lecturas (
    id_lectura INT PRIMARY KEY AUTO_INCREMENT,
    id_libro INT,
    fecha_inicio DATE,
    fecha_fin DATE,
    puntuacion FLOAT,
    comentario TEXT,
    FOREIGN KEY (id_libro) REFERENCES libros(id_libro)
    
    -- validaciones -- 
    CONSTRAINT chk_puntuacion CHECK (puntuacion BETWEEN 1 AND 5),
    CONSTRAINT chk_fechas CHECK (fecha_fin >= fecha_inicio),
    CONSTRAINT chk_comentario CHECK (comentario IN ('Excelente', 'Muy bueno', 'Bueno', 'Regular', 'Malo'))
); 
