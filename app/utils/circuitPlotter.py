import pandas as pd
import matplotlib.pyplot as plt

def plot_track(csv_file, lat_column, lon_column):
    """
    Traza la pista de karting a partir de los datos de latitud y longitud.

    Args:
    csv_file (str): Ruta al archivo CSV que contiene los datos.
    lat_column (str): Nombre de la columna de latitud.
    lon_column (str): Nombre de la columna de longitud.
    """
    # Cargar el archivo CSV
    df = pd.read_csv(csv_file)
    
    # Extraer las columnas de latitud y longitud
    latitudes = df[lat_column]
    longitudes = df[lon_column]
    
    # Crear el gráfico de la pista
    plt.figure(figsize=(10, 10))
    plt.plot(longitudes, latitudes, label="Track", color='blue', linewidth=2)
    
    # Agregar título y etiquetas
    plt.title("Trazado de la Pista de Karting")
    plt.xlabel("Longitud")
    plt.ylabel("Latitud")
    
    # Mostrar la leyenda
    plt.legend()
    
    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

# Ejemplo de uso:
csv_file = "../static/24_07_25_13_29_00/input/lap1.csv"  # Ruta al archivo CSV
lat_column = "Lat."  # Columna de latitud
lon_column = "Lon."  # Columna de longitud

# Trazar la pista
plot_track(csv_file, lat_column, lon_column)