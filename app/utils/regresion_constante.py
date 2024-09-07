import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap6.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de RPM y velocidad
rpm = data['RPM']
velocidad = data['Speed GPS']

# Calcular RPM dividido por Velocidad
relacion_rpm_velocidad = rpm / velocidad

# Definir el tiempo total en segundos
tiempo_total = 50.83  # Tiempo total en segundos

# Calcular el tiempo para cada fila distribuyendo el tiempo total
num_filas = len(rpm)
tiempo = np.linspace(0, tiempo_total, num_filas)

# Ajustar una línea recta (regresión lineal)
coeficientes = np.polyfit(tiempo, relacion_rpm_velocidad, 1)  # Grado 1 para una línea recta
polinomio = np.poly1d(coeficientes)  # Crear la función del polinomio
relacion_lineal = polinomio(tiempo)  # Evaluar la función en los puntos de tiempo

# Crear el gráfico
plt.figure(figsize=(10, 6))

# Graficar los datos originales
plt.plot(tiempo, relacion_rpm_velocidad, label='RPM/Velocidad en función del tiempo', color='m')

# Graficar la aproximación lineal
plt.plot(tiempo, relacion_lineal, label='Aproximación Lineal', color='b', linestyle='--')

# Etiquetas y título
plt.xlabel('Tiempo (segundos)')
plt.ylabel('RPM / Velocidad')
plt.title('Relación de RPM dividido por Velocidad en función del tiempo (con Aproximación Lineal)')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
