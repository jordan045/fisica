import pandas as pd
import numpy as np
import plotly.express as px

def calculate_triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = np.sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def calculate_turn_radius(lat1, lon1, lat2, lon2, lat3, lon3):
    a = np.sqrt((lat2 - lat1)**2 + (lon2 - lon1)**2)
    b = np.sqrt((lat3 - lat2)**2 + (lon3 - lon2)**2)
    c = np.sqrt((lat3 - lat1)**2 + (lon3 - lon1)**2)
    area = calculate_triangle_area(a, b, c)
    if area == 0:
        return np.inf
    radius = (a * b * c) / (4 * area)
    return radius

def calculate_centripetal_acceleration(velocity, radius):
    if radius == np.inf:
        return 0
    return (velocity ** 2) / radius

def analyze_track_radius_and_acceleration(csv_file, lat_column, lon_column, velocity_column):
    df = pd.read_csv(csv_file)
    latitudes = df[lat_column].values
    longitudes = df[lon_column].values
    velocities = df[velocity_column].values
    radii = []
    accelerations = []
    
    for i in range(1, len(latitudes) - 1):
        lat1, lon1 = latitudes[i - 1], longitudes[i - 1]
        lat2, lon2 = latitudes[i], longitudes[i]
        lat3, lon3 = latitudes[i + 1], longitudes[i + 1]
        radius = calculate_turn_radius(lat1, lon1, lat2, lon2, lat3, lon3)
        radii.append(radius)
        velocity = velocities[i]
        acceleration = calculate_centripetal_acceleration(velocity, radius)
        accelerations.append(acceleration)
    
    accelerations = [np.nan] + accelerations + [np.nan]
    
    df_plot = pd.DataFrame({
        'Latitud': latitudes,
        'Longitud': longitudes,
        'Aceleración centrípeta (m/s²)': accelerations
    })

    # Normalizar latitud y longitud si es necesario
    df_plot['Latitud'] = df_plot['Latitud'] / 1e7
    df_plot['Longitud'] = df_plot['Longitud'] / 1e7

    fig = px.scatter_mapbox(df_plot,
                            lat='Latitud', 
                            lon='Longitud', 
                            color='Aceleración centrípeta (m/s²)', 
                            color_continuous_scale='Viridis',
                            size_max=15, 
                            zoom=10,
                            hover_data={'Latitud': True, 'Longitud': True})
    
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(title="Trazado de la Pista con Aceleración Centrípeta")

    fig.show()

# Ejemplo de uso:
csv_file = "../static/24_07_25_13_29_00/input/lap1.csv"
lat_column = "Lat."
lon_column = "Lon."
velocity_column = "Speed GPS"

analyze_track_radius_and_acceleration(csv_file, lat_column, lon_column, velocity_column)
