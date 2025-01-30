from flask import Flask, jsonify, render_template
from database import get_db_connection
from query import get_unidades, get_ubicaciones_unidad, get_alcaldias, get_paradas_por_alcaldia

app = Flask(__name__)

# Manejo de errores global
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Ocurrió un error interno"}), 500

@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Recurso no encontrado"}), 404

# Endpoint raíz
@app.route('/')
def index():
    return render_template('index.html')

# Obtener lista de unidades
@app.route('/unidades', methods=['GET'])
def unidades():
    try:
        conn = get_db_connection()
        unidades = get_unidades(conn)
        conn.close()
        return jsonify(unidades)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener ubicaciones de una unidad
@app.route('/unidades/<id>/ubicaciones', methods=['GET'])
def ubicaciones_unidad(id):
    try:
        conn = get_db_connection()
        ubicaciones = get_ubicaciones_unidad(conn, id)
        conn.close()
        if not ubicaciones:
            return jsonify({"message": "No se encontraron ubicaciones para esta unidad"}), 404
        return jsonify(ubicaciones)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener lista de alcaldías disponibles
@app.route('/alcaldias', methods=['GET'])
def alcaldias():
    try:
        conn = get_db_connection()
        alcaldias = get_alcaldias(conn)
        conn.close()
        return jsonify(alcaldias)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Obtener paradas por alcaldía
@app.route('/alcaldias/<nombre>/paradas', methods=['GET'])
def paradas_por_alcaldia(nombre):
    try:
        conn = get_db_connection()
        paradas = get_paradas_por_alcaldia(conn, nombre)
        conn.close()
        if not paradas:
            return jsonify({"message": "No se encontraron paradas para esta alcaldía"}), 404
        return jsonify(paradas)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)