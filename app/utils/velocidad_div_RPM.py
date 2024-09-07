import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de RPM y velocidad
rpm = data['RPM']
velocidad = data['Speed GPS']

# Calcular RPM dividido por Velocidad
relacion_rpm_velocidad = rpm / velocidad

# Crear un eje de tiempo basado en la cantidad de filas
tiempo = range(len(rpm))

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(tiempo, relacion_rpm_velocidad, label='RPM/Velocidad en función del tiempo', color='m')

# Etiquetas y título
plt.xlabel('Tiempo (Relativo a la cantidad de líneas del CSV)')
plt.ylabel('RPM / Velocidad')
plt.title('Relación de RPM dividido por Velocidad en función del tiempo')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
