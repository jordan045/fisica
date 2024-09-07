import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de velocidad
velocidad = data['Speed GPS']

# Crear un eje de tiempo basado en la cantidad de filas
tiempo = range(len(velocidad))

# Aplicar un promedio móvil para suavizar los datos
window_size = 10  # Tamaño de la ventana para suavizar
velocidad_suavizado = velocidad.rolling(window=window_size).mean()

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, velocidad, label='velocidad original', color='g')

# Etiquetas y título
plt.xlabel('Tiempo (Relativo a la cantidad de líneas del CSV)')
plt.ylabel('velocidad')
plt.title('velocidad en función del tiempo (con suavizado)')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()

