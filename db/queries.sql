-- Top 5 libros mejor puntuados -- 
    SELECT titulo, puntuacion
    FROM libros
    JOIN lecturas USING(id_libro)
    ORDER BY puntuacion DESC
    LIMIT 5

-- Buscar libro -- 
    SELECT libros.titulo, autor.nombre, libros.genero
    FROM libros 
    JOIN autor USING (id_autor)
    WHERE libros.titulo LIKE %s -- parámetro = titulo del libro
    LIMIT 1;

-- Agregar libro -- 
    INSERT INTO libros (id_libro, titulo, genero, id_autor, paginas)
    VALUES (%s, %s, %s, %s, %s) -- parámetros del libro a agregar

-- Total libros leidos --
    SELECT COUNT(*) FROM lecturas

-- Libro más largo leido --
    SELECT titulo,  paginas
    FROM lecturas
    JOIN libros USING (id_libro)
    GROUP BY titulo, paginas
    ORDER BY paginas DESC
    LIMIT 1;

-- promedio de puntuaciones -- 
    SELECT AVG(puntuacion) FROM lecturas

-- Libro mejor puntuado --
    SELECT titulo
    JOIN lecturas USING(id_libro)
    FROM libros
    ORDER BY puntuacion DESC
    LIMIT 1

-- Libro peor puntuado -- 
    SELECT titulo
    FROM libros
    JOIN lecturas USING(id_libro)
    ORDER BY puntuacion ASC
    LIMIT 1

-- Autor más leido -- 
    SELECT autor.nombre, COUNT(*) AS Cantidad 
    FROM autor 
    JOIN libros USING(id_autor)
    JOIN lecturas USING (id_libro)
    GROUP BY autor.nombre 
    ORDER BY cantidad DESC 
    LIMIT 1

-- Género favortito --
    SELECT libros.genero, COUNT(*) AS Cantidad
    FROM libros
    JOIN lecturas USING (id_libro)
    GROUP BY genero 
    ORDER BY Cantidad DESC
    LIMIT 1; 

-- Cantidad de libros leidos por año --
    SELECT YEAR(fecha_fin), COUNT(*)
    FROM lecturas
    GROUP BY YEAR(fecha_fin)

-- Registrar lectura --
    INSERT INTO lecturas (id_libro, fecha_inicio, fecha_fin, puntuacion, comentario)
    VALUES (%s, %s, %s, %s, %s) -- parámetros de la lectura a registrar 

-- Registrar autor --
    INSERT INTO autor(id_autor, nombre)
    VALUES (%s, %s) -- parámetros del autor a registrar




