import pytest
from ..app import app  # Importa la aplicación Flask

# Fixture para el cliente de pruebas de Flask
@pytest.fixture
def client():
    # Configura la aplicación en modo de prueba
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client  # Proporciona el cliente a las pruebas

# Prueba para el endpoint raíz
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert b"Bienvenido" in response.data  # Verifica que el mensaje de bienvenida esté presente

# Prueba para el endpoint /unidades
def test_unidades(client):
    response = client.get('/unidades')
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert isinstance(response.json, list)  # Verifica que la respuesta sea una lista

# Prueba para el endpoint /unidades/<id>/ubicaciones
def test_ubicaciones_unidad(client):
    # Usa un ID de unidad válido (debe existir en la base de datos)
    unidad_id = 'fc73eb8fc73e9P1'
    response = client.get(f'/unidades/{unidad_id}/ubicaciones')
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert isinstance(response.json, list)  # Verifica que la respuesta sea una lista

# Prueba para el endpoint /alcaldias
def test_alcaldias(client):
    response = client.get('/alcaldias')
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert isinstance(response.json, list)  # Verifica que la respuesta sea una lista

# Prueba para el endpoint /alcaldias/<nombre>/paradas
def test_paradas_por_alcaldia(client):
    # Usa un nombre de alcaldía válido (debe existir en la base de datos)
    alcaldia = 'NombreDeLaAlcaldia'
    response = client.get(f'/alcaldias/{alcaldia}/paradas')
    assert response.status_code == 200  # Verifica que la respuesta sea exitosa
    assert isinstance(response.json, list)  # Verifica que la respuesta sea una lista

# Prueba para un endpoint que no existe
def test_endpoint_no_existente(client):
    response = client.get('/endpoint_inexistente')
    assert response.status_code == 404  # Verifica que la respuesta sea 404 (No encontrado)