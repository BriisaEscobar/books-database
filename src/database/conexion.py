import mysql.connector

def obtenerConexion():
    return mysql.connector.connect (
    user        = 'root',
    password    = '',
    host        = 'localhost',
    database    = 'proyecto - libros'
)