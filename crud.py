import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from settings import DATABASE_PATH

# Conexión a la base de datos
def conectar():
    return psycopg2.connect(DATABASE_PATH)

# Operaciones CRUD para la tabla Empresa
def crear_empresa(razon_social, ruc, direccion_matriz, direccion_sucursal):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Empresa (razon_social, ruc, direccion_matriz, direccion_sucursal) VALUES (%s, %s, %s, %s) RETURNING id_empresa",
                   (razon_social, ruc, direccion_matriz, direccion_sucursal))
    id_empresa = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_empresa

def obtener_empresas():
    conn = conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Empresa")
    empresas = cursor.fetchall()
    conn.close()
    return empresas

# Puedes agregar funciones similares para actualizar y eliminar empresas si es necesario.

# Operaciones CRUD para la tabla Factura
def crear_factura(fecha_emision, guia_remision, descripcion, total_pagar, id_empresa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Factura (fecha_emision, guia_remision, descripcion, total_pagar, id_empresa) VALUES (%s, %s, %s, %s, %s) RETURNING id_factura",
                   (fecha_emision, guia_remision, descripcion, total_pagar, id_empresa))
    id_factura = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_factura

def obtener_facturas():
    conn = conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Factura")
    facturas = cursor.fetchall()
    conn.close()
    return facturas

# Puedes agregar funciones similares para actualizar y eliminar facturas si es necesario.

# Operaciones CRUD para las otras tablas (Forma_Pago, Pago, Factura_Adquirente) de manera similar.

if _name_ == "_main_":
    # Aquí puedes probar las funciones según tus necesidades.
    pass