import pandas as pd

# Función para verificar las columnas requeridas
def verify_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise KeyError(f"Faltan las columnas: {', '.join(missing_columns)}")
    return df

# Función para limpiar los datos
def clean_data(df):
    # Eliminar columnas irrelevantes
    columns_to_drop = ["route_desc", "route_url"]  # Puedes ajustar según lo que necesites
    df = df.drop(columns=columns_to_drop, errors='ignore')
    
    # Manejar valores nulos (puedes ajustar los valores por defecto)
    df.fillna({
        "route_color": "000000",  # Color por defecto
        "route_text_color": "FFFFFF"  # Texto por defecto
    }, inplace=True)

    # Asegurarse que las columnas numéricas sean realmente numéricas
    df["route_id"] = pd.to_numeric(df["route_id"], errors='coerce')
    
    # Agregar un ID único si lo deseas
    df["ruta_id"] = df.index + 1
    
    return df

# Función para procesar los datos
def process_data(file_path, cleaned_file_path):
    # 1. Cargar el archivo
    df = pd.read_csv(file_path, sep=",", encoding="utf-8-sig")
    
    # 2. Verificar las columnas esenciales
    df = verify_columns(df, ["route_id", "route_short_name"])

    # 3. Limpiar los datos
    df = clean_data(df)

    # 4. Guardar los datos limpios
    df.to_csv(cleaned_file_path, index=False)
    
    return df

# Ruta del archivo y salida
file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Metrobus_GTFS_ESTATICO\routes.txt"
cleaned_file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Datos_Procesados\Rutas.csv"

# Procesar los datos
processed_df = process_data(file_path, cleaned_file_path)

# Mostrar los datos procesados
print("\nDatos procesados:")
print(processed_df.head())
