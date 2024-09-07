import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = '../objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de latitud y longitud
lat = data['Lat.']
lon = data['Lon.']

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(lon, lat, label='Latitud vs Longitud', color='b')

# Etiquetas y título
plt.xlabel('Longitud')
plt.ylabel('Latitud')
plt.title('Posición GPS (Latitud vs Longitud)')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()