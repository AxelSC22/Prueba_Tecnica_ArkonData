import psycopg2

def get_db_connection():
    conn = psycopg2.connect(
        dbname="Prueba_Tecnica",
        user="postgres",
        password="1234",
        host="localhost",
        port="5433"  # Especifica el puerto correcto
    )
    return conn

# Prueba la conexión
try:
    conn = get_db_connection()
    print("✅ Conexión exitosa a la base de datos")
    conn.close()
except psycopg2.Error as e:
    print(f"❌ Error al conectar a la base de datos: {e}")
