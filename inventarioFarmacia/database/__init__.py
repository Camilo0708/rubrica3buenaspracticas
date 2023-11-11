import pyodbc

def create_connection():
    conn_str = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=inventarioFarmacia\farmaciadb.accdb;'
    conn = pyodbc.connect(conn_str)
    return conn.cursor()

def update_medicamento(medicamento_id, cantidad, precio):
    cursor = create_connection()
    query = f"UPDATE Medicamentos SET Cantidad={cantidad}, Precio={precio} WHERE Id={medicamento_id};"
    cursor.execute(query)
    cursor.commit()

def add_medicamento(medicamento, cantidad, precio, presentacion):
    cursor = create_connection()
    query = f"INSERT INTO Medicamentos (Medicamento, Cantidad, Precio, Presentacion) VALUES ('{medicamento}', {cantidad}, {precio}, '{presentacion}');"
    cursor.execute(query)
    cursor.commit()

# Agregar funciones según sea necesario
