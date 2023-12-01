# CRUD para las Facturas 
def create_factura(num_factura, fecha_emision, ruc, nombre_cliente, monto_total):
    factura = Factura(num_factura=num_factura, fecha_emision=fecha_emision, ruc=ruc, nombre_cliente=nombre_cliente, monto_total=monto_total)
    session.add(factura)
    session.commit()

def update_factura(id, num_factura, fecha_emision, ruc, nombre_cliente, monto_total):
    factura = session.query(Factura).filter_by(id=id).first()
    factura.num_factura = num_factura
    factura.fecha_emision = fecha_emision
    factura.ruc = ruc
    factura.nombre_cliente = nombre_cliente
    factura.monto_total = monto_total
    session.commit()

def delete_factura(id):
    factura = session.query(Factura).filter_by(id=id).first()
    session.delete(factura)
    session.commit()

def read_factura(id):
    factura = session.query(Factura).filter_by(id=id).first()
    return factura