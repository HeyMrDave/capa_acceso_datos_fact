import psycopg2
from psycopg2 import sql
from psycopg2.extras import RealDictCursor
from settings import DB_CONNECTION_STRING

# Conexión a la base de datos
def conectar():
    return psycopg2.connect(DB_CONNECTION_STRING)

# Operaciones CRUD para la tabla Empresa
def crear_empresa(razon_social, ruc, direccion_matriz, direccion_sucursal):
    conn = conectar()
    cursor = conn.cursor()
    sql = "INSERT INTO Empresa (id_empresa, razon_social, ruc, direccion_matriz, direccion_sucursal) VALUES (%s, %s, %s, %s)"
    id_empresa = int(input("Ingrese el id de su empresa: "))
    razon_social = input("Ingrese razon social: ")
    ruc = input("Ingrese su ruc")
    direccion_matriz = input("Ingrese su direccion matriz: ")
    direccion_sucursal = input("Ingrese su direccion sucursal: ")
    datos = (razon_social, ruc, direccion_matriz, direccion_sucursal)
    cursor.execute(sql,datos)
    conn.commit()
    conn.close()
    registros = cursor.rowcount
    return id_empresa

def obtener_empresas():
    conn = conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Empresa")
    empresas = cursor.fetchall()
    conn.close()
    return empresas

def actualizar_empresa(id_empresa, razon_social, ruc, direccion_matriz, direccion_sucursal):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Empresa SET razon_social = %s, ruc = %s, direccion_matriz = %s, direccion_sucursal = %s WHERE id_empresa = %s",
                   (razon_social, ruc, direccion_matriz, direccion_sucursal, id_empresa))
    conn.commit()
    conn.close()

def eliminar_empresa(id_empresa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Empresa WHERE id_empresa = %s", (id_empresa,))
    conn.commit()
    conn.close()

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

def actualizar_factura(id_factura, fecha_emision, guia_remision, descripcion, total_pagar, id_empresa):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Factura SET fecha_emision = %s, guia_remision = %s, descripcion = %s, total_pagar = %s, id_empresa = %s WHERE id_factura = %s",
                   (fecha_emision, guia_remision, descripcion, total_pagar, id_empresa, id_factura))
    conn.commit()
    conn.close()

def eliminar_factura(id_factura):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Factura WHERE id_factura = %s", (id_factura,))
    conn.commit()
    conn.close()

# Operaciones CRUD para la tabla Forma_Pago
def crear_forma_pago(forma_pago):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Forma_Pago (forma_pago) VALUES (%s) RETURNING id_forma_pago", (forma_pago,))
    id_forma_pago = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_forma_pago

def obtener_formas_pago():
    conn = conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Forma_Pago")
    formas_pago = cursor.fetchall()
    conn.close()
    return formas_pago

def actualizar_forma_pago(id_forma_pago, forma_pago):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Forma_Pago SET forma_pago = %s WHERE id_forma_pago = %s", (forma_pago, id_forma_pago))
    conn.commit()
    conn.close()

def eliminar_forma_pago(id_forma_pago):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Forma_Pago WHERE id_forma_pago = %s", (id_forma_pago,))
    conn.commit()
    conn.close()

# Operaciones CRUD para la tabla Pago
def crear_pago(monto, fecha_pago, id_forma_pago, id_factura):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Pago (monto, fecha_pago, id_forma_pago, id_factura) VALUES (%s, %s, %s, %s) RETURNING id_pago",
                   (monto, fecha_pago, id_forma_pago, id_factura))
    id_pago = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_pago

def obtener_pagos():
    conn = conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Pago")
    pagos = cursor.fetchall()
    conn.close()
    return pagos

def actualizar_pago(id_pago, monto, fecha_pago, id_forma_pago, id_factura):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Pago SET monto = %s, fecha_pago = %s, id_forma_pago = %s, id_factura = %s WHERE id_pago = %s",
                   (monto, fecha_pago, id_forma_pago, id_factura, id_pago))
    conn.commit()
    conn.close()

def eliminar_pago(id_pago):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pago WHERE id_pago = %s", (id_pago,))
    conn.commit()
    conn.close()

# Operaciones CRUD para la tabla Factura_Adquirente
def crear_factura_adquirente(nombre_adquirente, ruc_adquirente, id_factura):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Factura_Adquirente (nombre_adquirente, ruc_adquirente, id_factura) VALUES (%s, %s, %s) RETURNING id_factura_adquirente",
                   (nombre_adquirente, ruc_adquirente, id_factura))
    id_factura_adquirente = cursor.fetchone()[0]
    conn.commit()
    conn.close()
    return id_factura_adquirente

def obtener_facturas_adquirente():
    conn = conectar()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Factura_Adquirente")
    facturas_adquirente = cursor.fetchall()
    conn.close()
    return facturas_adquirente

def actualizar_factura_adquirente(id_factura_adquirente, nombre_adquirente, ruc_adquirente, id_factura):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Factura_Adquirente SET nombre_adquirente = %s, ruc_adquirente = %s, id_factura = %s WHERE id_factura_adquirente = %s",
                   (nombre_adquirente, ruc_adquirente, id_factura, id_factura_adquirente))
    conn.commit()
    conn.close()

def eliminar_factura_adquirente(id_factura_adquirente):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Factura_Adquirente WHERE id_factura_adquirente = %s", (id_factura_adquirente,))
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # Ejemplo de cómo crear una empresa
    id_empresa = crear_empresa("1,Empresa XYZ", "123456789", "Dirección Matriz", "Dirección Sucursal")
    print(f"Se creó la empresa con ID: {id_empresa}")

    # Ejemplo de cómo obtener todas las empresas
    empresas = obtener_empresas()
    print("Lista de empresas:")
    print(empresas)

    # Ejemplo de cómo actualizar la información de una empresa
    actualizar_empresa(id_empresa, "Nueva Razón Social", "987654321", "Nueva Dirección Matriz", "Nueva Dirección Sucursal")
    print("Se actualizó la información de la empresa.")

    # Ejemplo de cómo eliminar una empresa
    eliminar_empresa(id_empresa)
    print("Se eliminó la empresa.")

    # Puedes repetir un proceso similar para probar las funciones relacionadas con Facturas, Forma_Pago, Pago, y Factura_Adquirente.