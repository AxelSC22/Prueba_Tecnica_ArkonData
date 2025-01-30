import pandas as pd
from functools import reduce

# Ruta del archivo stop_times.txt
file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Metrobus_GTFS_ESTATICO\stop_times.txt"

# 1. Cargar el archivo con la codificación adecuada
def load_file(file_path):
    try:
        return pd.read_csv(file_path, sep=",", encoding="utf-8-sig")
    except UnicodeDecodeError:
        return pd.read_csv(file_path, sep=",", encoding="latin1")

# 2. Normalizar columnas (eliminar espacios y convertir a minúsculas)
def normalize_columns(df):
    df.columns = df.columns.str.strip().str.lower()
    return df

# 3. Verificar columnas necesarias
def verify_columns(df, required_columns):
    missing_columns = list(filter(lambda col: col not in df.columns, required_columns))
    if missing_columns:
        raise KeyError(f"Faltan las columnas: {', '.join(missing_columns)}")
    return df

# 4. Ajustar tiempos fuera de rango
def fix_time_format(df, time_columns):
    def correct_time(value):
        try:
            hours, minutes, seconds = map(int, value.split(":"))
            hours = hours % 24  # Asegurar horas en el rango [0, 23]
            return f"{hours:02}:{minutes:02}:{seconds:02}"
        except (ValueError, AttributeError):
            return value  # Retorna el valor original si no es válido
    for col in time_columns:
        if col in df.columns:
            df[col] = df[col].apply(correct_time)
    return df

# 5. Agregar un ID 
def add_unique_id(df):
    df["stop_times_id"] = list(range(1, len(df) + 1))
    return df

# 6. Eliminar columnas irrelevantes
def drop_columns(df, columns_to_drop):
    return df.drop(columns=list(filter(lambda col: col in df.columns, columns_to_drop)))

# 7. Manejar valores nulos
def handle_missing_values(df, fill_values):
    return df.fillna(fill_values)

# 8. Guardar el archivo procesado
def save_file(df, output_path):
    df.to_csv(output_path, index=False, encoding="utf-8-sig")
    print(f"\nArchivo limpio guardado en: {output_path}")

# Composición de funciones (programación funcional)
def process_data(file_path, output_path):
    # Cargar los datos
    df = load_file(file_path)
    
    # Procesamiento funcional
    df = (
        df
        .pipe(normalize_columns)
        .pipe(verify_columns, ["trip_id", "arrival_time", "departure_time", "stop_id"])  # Verificar columnas esenciales
        .pipe(fix_time_format, ["arrival_time", "departure_time"])  # Ajustar formato de tiempo
        .pipe(add_unique_id)  # Agregar ID único
        .pipe(drop_columns, ["stop_headsign", "pickup_type", "drop_off_type", "continuous_pickup", "continuous_drop_off", "shape_dist_traveled", "timepoint"])  # Eliminar columnas innecesarias
        .pipe(handle_missing_values, {"stop_sequence": 0})  # Manejar valores nulos
    )

    # Guardar el archivo procesado
    save_file(df, output_path)
    
    # Retornar el DataFrame procesado (opcional)
    return df

# Ejecutar el procesamiento
cleaned_file_path = r"C:\Users\colme\Desktop\Pruebatecnica\Datos_Procesados\stop_times_cleaned.csv"
processed_df = process_data(file_path, cleaned_file_path)

# Mostrar los datos procesados como verificación
print("\nDatos procesados:")
print(processed_df.head())
