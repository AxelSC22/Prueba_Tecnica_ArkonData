import pandas as pd
from geopy.geocoders import Nominatim
import time

# Lista de alcaldías
alcaldias_lista = [
    "Álvaro Obregón", "Azcapotzalco", "Benito Juárez", "Coyoacán", 
    "Cuajimalpa de Morelos", "Cuauhtémoc", "Gustavo A. Madero", 
    "Iztacalco", "Iztapalapa", "La Magdalena Contreras", "Miguel Hidalgo", 
    "Milpa Alta", "Tláhuac", "Tlalpan", "Venustiano Carranza", "Xochimilco"
]

# Configuración de geolocalizador
geolocator = Nominatim(user_agent="myGeocoder")

def get_alcaldia(lat, lon):
    try:
        location = geolocator.reverse((lat, lon), language='es', timeout=10)
        if location:
            # Imprimir la dirección completa para depuración
            print(f"Dirección encontrada: {location.address}")
            
            # Extraer las partes de la dirección
            address_parts = location.address.split(", ")
            
            # Buscar alcaldía en la lista
            for part in address_parts:
                for alcaldia in alcaldias_lista:
                    if alcaldia in part:
                        print(f"Alcaldía encontrada: {alcaldia}")
                        return alcaldia
            
            # Si no se encuentra ninguna coincidencia
            return "Desconocido"
        return "Desconocido"
    except Exception as e:
        print(f"Error al obtener alcaldía para lat {lat}, lon {lon}: {e}")
        return "Error"

def process_data(file_path, cleaned_file_path):
    # 1. Cargar el archivo con la codificación adecuada
    try:
        stops_df = pd.read_csv(file_path, sep=",", encoding="utf-8-sig")
    except UnicodeDecodeError:
        stops_df = pd.read_csv(file_path, sep=",", encoding="latin1")

    # Normalizar nombres de columnas
    stops_df.columns = stops_df.columns.str.strip().str.lower()

    # Verificar si 'stop_name' está presente
    if "stop_name" not in stops_df.columns:
        raise KeyError("La columna 'stop_name' no está presente en los datos.")

    # Corregir problemas de codificación en los nombres
    stops_df["stop_name"] = stops_df["stop_name"].str.encode("latin1").str.decode("utf-8", errors="ignore")

    # Agregar un ID único
    stops_df["paradas_id"] = pd.Series(range(1, len(stops_df) + 1))

    # Eliminar columnas irrelevantes
    columns_to_drop = ["stop_desc", "zone_id", "stop_url", "stop_timezone", "level_id", "platform_code"]
    stops_df = stops_df.drop(columns=[col for col in columns_to_drop if col in stops_df.columns])

    # Manejar valores nulos
    stops_df.fillna({
        "stop_code": "N/A",  # Rellenar códigos vacíos con "N/A"
        "parent_station": "N/A",  # Paradas sin estación principal
        "wheelchair_boarding": 0  # Asumir que no son accesibles si el dato está vacío
    }, inplace=True)

    # Validar el rango de coordenadas
    stops_df = stops_df[
        (stops_df["stop_lat"].between(-90, 90)) & 
        (stops_df["stop_lon"].between(-180, 180))
    ]
    
    # Obtener la alcaldía para cada parada
    stops_df["alcaldia"] = stops_df.apply(
        lambda row: get_alcaldia(row["stop_lat"], row["stop_lon"]), axis=1
    )
    
    # Guardar los datos limpios en un archivo CSV
    stops_df.to_csv(cleaned_file_path, index=False, encoding="utf-8-sig")
    print(f"\nArchivo limpio guardado en: {cleaned_file_path}")

    return stops_df

# Ejemplo de uso
file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Metrobus_GTFS_ESTATICO\stops.txt"
cleaned_file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Datos_Procesados\stops_cleaned.csv"
process_data(file_path, cleaned_file_path)
