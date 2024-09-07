import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de latitud
lat = data['Lon.']

# Crear un eje de tiempo basado en la cantidad de filas
tiempo = range(len(lat))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, lat, label='Longitud en función del tiempo', color='b')

# Etiquetas y título
plt.xlabel('Tiempo (Relativo a la cantidad de líneas del CSV)')
plt.ylabel('Longitud')
plt.title('Posición GPS (Longitud) en función del tiempo')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()