import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de RPM
rpm = data['RPM']

# Crear un eje de tiempo basado en la cantidad de filas
tiempo = range(len(rpm))

# Aplicar un promedio móvil para suavizar los datos
window_size = 10  # Tamaño de la ventana para suavizar
rpm_suavizado = rpm.rolling(window=window_size).mean()

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, rpm, label='RPM original', color='b')

# Etiquetas y título
plt.xlabel('Tiempo (Relativo a la cantidad de líneas del CSV)')
plt.ylabel('RPM')
plt.title('RPM en función del tiempo (con suavizado)')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()

