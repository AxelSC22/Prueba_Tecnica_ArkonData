# queries.py

def get_unidades(conn):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT route_short_name, route_long_name FROM rutas;")
    unidades = cur.fetchall()
    cur.close()
    return unidades

def get_ubicaciones_unidad(conn, unidad_id):
    cur = conn.cursor()
    cur.execute("""
        SELECT s.stop_name, s.stop_lat, s.stop_lon
        FROM stop_times st
        JOIN stops s ON st.stop_id = s.stop_id
        WHERE st.trip_id = %s;
    """, (unidad_id,))
    ubicaciones = cur.fetchall()
    cur.close()
    return ubicaciones

def get_alcaldias(conn):
    cur = conn.cursor()
    cur.execute("SELECT DISTINCT stop_name FROM stops;")
    alcaldias = cur.fetchall()
    cur.close()
    return alcaldias

def get_paradas_por_alcaldia(conn, alcaldia):
    cur = conn.cursor()
    cur.execute("""
        SELECT stop_name, stop_lat, stop_lon
        FROM stops
        WHERE alcaldia = %s;
    """, (alcaldia,))
    paradas = cur.fetchall()
    cur.close()
    return paradas