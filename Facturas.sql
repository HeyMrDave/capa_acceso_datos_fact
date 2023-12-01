CREATE TABLE Empresa (
   id_empresa INT PRIMARY KEY,
   razon_social VARCHAR(255),
   ruc VARCHAR(20),
   direccion_matriz VARCHAR(255),
   direccion_sucursal VARCHAR(255)
);

CREATE TABLE Factura (
   id_factura INT PRIMARY KEY,
   fecha_emision DATE,
   guia_remision VARCHAR(20),
   descripcion VARCHAR(255),
   total_pagar DECIMAL(10,2),
   id_empresa INT,
   FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);

CREATE TABLE Forma_Pago (
   id_forma_pago INT PRIMARY KEY,
   forma_pago VARCHAR(255)
);

CREATE TABLE Pago (
   id_pago INT PRIMARY KEY,
   monto DECIMAL(10,2),
   fecha_pago DATE,
   id_forma_pago INT,
   id_factura INT,
   FOREIGN KEY (id_forma_pago) REFERENCES Forma_Pago(id_forma_pago),
   FOREIGN KEY (id_factura) REFERENCES Factura(id_factura)
);

CREATE TABLE Factura_Adquirente (
   id_factura_adquirente INT PRIMARY KEY,
   nombre_adquirente VARCHAR(255),
   ruc_adquirente VARCHAR(20),
   id_factura INT,
   FOREIGN KEY (id_factura) REFERENCES Factura(id_factura)
);