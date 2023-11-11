from database import create_connection

def get_medicamentos():
    cursor = create_connection()
    cursor.execute("SELECT * FROM medicamentos;")
    return cursor.fetchall()

def get_medicamento_by_id(medicamento_id):
    cursor = create_connection()
    cursor.execute(f"SELECT * FROM medicamentos WHERE Id={medicamento_id};")
    return cursor.fetchone()

# Agregar funciones según sea necesario
