import pandas as pd
import matplotlib.pyplot as plt
import glob

# Ruta de la carpeta que contiene los archivos CSV (ajusta esta ruta a la tuya)
folder_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/*.csv'

# Obtener una lista de todos los archivos CSV en la carpeta
csv_files = glob.glob(folder_path)

# Lista para almacenar los valores RPM/Speed GPS de todos los archivos
all_ratios = []

# Procesar cada archivo CSV
for file in csv_files:
    # Cargar el dataset
    data = pd.read_csv(file)
    
    # Calcular la división de RPM por Speed GPS para cada muestra
    rpm_speed_ratio = data['RPM'] / data['Speed GPS']
    
    # Añadir los valores al listado general
    all_ratios.extend(rpm_speed_ratio)

# Crear un histograma para los datos combinados
plt.figure(figsize=(8, 6))
plt.hist(all_ratios, bins=30, color='purple', edgecolor='black', alpha=0.7)

# Etiquetas del gráfico
plt.xlabel('RPM / Speed GPS')
plt.ylabel('Frecuencia')
plt.title('Distribución combinada de RPM / Speed GPS de múltiples archivos')

# Mostrar el gráfico
plt.show()
