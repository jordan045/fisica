import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Reemplaza con la ruta correcta de tu archivo
data = pd.read_csv(file_path)

# Calcular la división de RPM por Speed GPS para cada muestra
rpm_speed_ratio = data['RPM'] / data['Speed GPS']

# Crear el histograma
plt.figure(figsize=(8, 6))
plt.hist(rpm_speed_ratio, bins=30, color='purple', edgecolor='black', alpha=0.7)

# Etiquetas del gráfico
plt.xlabel('RPM / Speed GPS')
plt.ylabel('Frecuencia')
plt.title('Distribución de RPM / Speed GPS')

# Mostrar el gráfico
plt.show()
