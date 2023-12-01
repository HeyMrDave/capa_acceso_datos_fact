import psycopg2

try:
    conexion = psycopg2.connect(
        database="Facturas",
        user="postgres",
        password="15963554",
        host="localhost",
        port="5432"
    )
    cursor = conexion.cursor()
    print("Conexión exitosa")

except (Exception, psycopg2.Error) as error:
    print("Error al conectar con la base de datos: ", error)