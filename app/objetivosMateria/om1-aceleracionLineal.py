import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler

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

def normalize_coordinates(dataframe, lat_column, lon_column):
    """
    Normaliza las coordenadas de latitud y longitud utilizando Min-Max Scaling.

    Args:
    dataframe (pd.DataFrame): DataFrame que contiene las coordenadas.
    lat_column (str): Nombre de la columna que contiene las latitudes.
    lon_column (str): Nombre de la columna que contiene las longitudes.

    Returns:
    pd.DataFrame: DataFrame con las coordenadas normalizadas.
    """
    scaler = MinMaxScaler()
    coordinates = dataframe[[lat_column, lon_column]]
    normalized_coordinates = scaler.fit_transform(coordinates)
    
    dataframe[lat_column + '_norm'] = normalized_coordinates[:, 0]
    dataframe[lon_column + '_norm'] = normalized_coordinates[:, 1]
    
    return dataframe

def plot_acceleration_on_track(dataframe, lat_column, lon_column, acceleration_column):
    """
    Grafica la aceleración tangencial sobre el circuito utilizando Plotly.

    Args:
    dataframe (pd.DataFrame): DataFrame que contiene los datos de latitud, longitud y aceleración.
    lat_column (str): Nombre de la columna que contiene las latitudes.
    lon_column (str): Nombre de la columna que contiene las longitudes.
    acceleration_column (str): Nombre de la columna que contiene las aceleraciones tangenciales.
    """
    # Normaliza las coordenadas
    dataframe = normalize_coordinates(dataframe, lat_column, lon_column)
    
    fig = px.scatter_mapbox(dataframe,
                            lat=lat_column + '_norm', 
                            lon=lon_column + '_norm', 
                            color=acceleration_column, 
                            color_continuous_scale='Viridis',
                            size_max=15, 
                            zoom=10,  # Ajusta el zoom aquí
                            hover_data={lat_column + '_norm': False, lon_column + '_norm': False})
    
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(title="Aceleración Tangencial sobre el Circuito")

    fig.show()

def process_csv(input_csv, output_csv, velocity_column, lat_column, lon_column, delta_t):
    """
    Carga un archivo CSV, calcula la aceleración tangencial, agrega el tiempo transcurrido,
    grafica la aceleración sobre el circuito, y guarda el resultado en un nuevo archivo CSV.

    Args:
    input_csv (str): Ruta del archivo CSV de entrada.
    output_csv (str): Ruta del archivo CSV de salida.
    velocity_column (str): Nombre de la columna que contiene las velocidades.
    lat_column (str): Nombre de la columna que contiene las latitudes.
    lon_column (str): Nombre de la columna que contiene las longitudes.
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
    
    # Grafica la aceleración tangencial sobre el circuito
    plot_acceleration_on_track(df, lat_column, lon_column, "Tangential Acceleration")
    
    print(f"Archivo procesado y guardado en {output_csv}")

# Ejemplo de uso:
if __name__ == "__main__":
    # Parámetros de entrada
    input_csv = "../static/24_07_25_13_29_00/input/lap1.csv"  # Ruta del archivo CSV de entrada
    output_csv = "../static/24_07_25_13_29_00/output/lap1_processed.csv"  # Ruta del archivo CSV de salida
    velocity_column = "Speed GPS"  # Columna de velocidades
    lat_column = "Lat."  # Columna de latitud
    lon_column = "Lon."  # Columna de longitud
    delta_t = 0.1  # Intervalo de tiempo entre las filas (en segundos, 10 Hz)
    
    # Procesa el archivo CSV
    process_csv(input_csv, output_csv, velocity_column, lat_column, lon_column, delta_t)
