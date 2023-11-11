from database import create_connection

def get_precios():
    cursor = create_connection()
    cursor.execute("SELECT precio FROM medicamentos;")
    return cursor.fetchall()

# Agregar funciones según sea necesario
