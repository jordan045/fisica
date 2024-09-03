import pandas as pd

def calculate_tangential_acceleration(dataframe, velocity_column, delta_t):
    """
    Calcula la aceleración tangencial a partir de la diferencia de velocidades entre filas.

    Args:
    dataframe (pd.DataFrame): DataFrame que contiene los datos de velocidad.
    velocity_column (str): Nombre de la columna que contiene las velocidades.
    delta_t (float): Intervalo de tiempo entre las filas (en segundos).

    Returns:
    pd.DataFrame: DataFrame con una columna adicional para la aceleración tangencial.
    """
    # Calcula la diferencia de velocidades entre filas consecutivas
    dataframe["Tangential Acceleration"] = dataframe[velocity_column].diff() / delta_t
    
    # Reemplaza el valor NaN en la primera fila por 0
    dataframe["Tangential Acceleration"] = dataframe["Tangential Acceleration"].fillna(0)
    
    return dataframe

def add_elapsed_time(dataframe, delta_t):
    """
    Agrega una columna de tiempo transcurrido al DataFrame.

    Args:
    dataframe (pd.DataFrame): DataFrame que contiene los datos.
    delta_t (float): Intervalo de tiempo entre las filas (en segundos).

    Returns:
    pd.DataFrame: DataFrame con una columna adicional para el tiempo transcurrido.
    """
    # Calcula el tiempo transcurrido acumulado
    dataframe["Elapsed time (s)"] = (dataframe.index * delta_t).round(4)
    
    return dataframe

def process_csv(input_csv, output_csv, velocity_column, delta_t):
    """
    Carga un archivo CSV, calcula la aceleración tangencial, agrega el tiempo transcurrido, y guarda el resultado en un nuevo archivo CSV.

    Args:
    input_csv (str): Ruta del archivo CSV de entrada.
    output_csv (str): Ruta del archivo CSV de salida.
    velocity_column (str): Nombre de la columna que contiene las velocidades.
    delta_t (float): Intervalo de tiempo entre las filas (en segundos).
    """
    # Carga el archivo CSV en un DataFrame
    df = pd.read_csv(input_csv)
    
    # Calcula la aceleración tangencial
    df = calculate_tangential_acceleration(df, velocity_column, delta_t)
    
    # Agrega el tiempo transcurrido
    df = add_elapsed_time(df, delta_t)
    
    # Guarda el DataFrame resultante en un nuevo archivo CSV
    df.to_csv(output_csv, index=False)
    
    print(f"Archivo procesado y guardado en {output_csv}")

# Ejemplo de uso:
if __name__ == "__main__":
    # Parámetros de entrada
    input_csv = "static/24_07_25_13_29_00/input/lap1.csv"  # Ruta del archivo CSV de entrada
    output_csv = "static/24_07_25_13_29_00/output/lap1.csv"  # Ruta del archivo CSV de salida
    velocity_column = "Speed GPS"  # Columna de velocidades
    delta_t = 0.1  # Intervalo de tiempo entre las filas (en segundos, 10 Hz)
    
    # Procesa el archivo CSV
    process_csv(input_csv, output_csv, velocity_column, delta_t)
