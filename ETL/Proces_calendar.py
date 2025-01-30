import pandas as pd

# Función para verificar las columnas requeridas
def verify_columns(df, required_columns):
    missing_columns = [col for col in required_columns if col not in df.columns]
    if missing_columns:
        raise KeyError(f"Faltan las columnas: {', '.join(missing_columns)}")
    return df

# Función para limpiar los datos
def clean_data(df):
    # Convertir las fechas de inicio y fin a formato datetime
    df['start_date'] = pd.to_datetime(df['start_date'], format='%Y%m%d', errors='coerce')
    df['end_date'] = pd.to_datetime(df['end_date'], format='%Y%m%d', errors='coerce')

    # Eliminar columnas irrelevantes (si hay alguna que no necesites)
    # Aquí no estamos eliminando ninguna columna, pero si quieres puedes hacerlo
    # columns_to_drop = ['columna_a_eliminar']
    # df = df.drop(columns=columns_to_drop, errors='ignore')

    # Verificar si los días de la semana tienen valores válidos (0 o 1)
    for col in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        df[col] = df[col].apply(lambda x: 1 if x == 1 else 0)  # Asegurarse de que solo haya 1 o 0

    # Agregar un ID único
    df['fecha_id'] = df.index + 1

    return df

# Función para procesar los datos
def process_data(file_path, cleaned_file_path):
    # 1. Cargar el archivo
    df = pd.read_csv(file_path, sep=",", encoding="utf-8-sig")
    
    # 2. Verificar las columnas esenciales
    df = verify_columns(df, ["service_id", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"])

    # 3. Limpiar los datos
    df = clean_data(df)

    # 4. Guardar los datos limpios
    df.to_csv(cleaned_file_path, index=False)
    
    return df

# Ruta del archivo y salida
file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Metrobus_GTFS_ESTATICO\calendar.txt"
cleaned_file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Datos_Procesados\calendar_cleaned.csv"

# Procesar los datos
processed_df = process_data(file_path, cleaned_file_path)

# Mostrar los datos procesados
print("\nDatos procesados:")
print(processed_df.head())
