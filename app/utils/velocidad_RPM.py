import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
file_path = 'app/objetivosMateria/static/24_07_25_13_29_00/input/lap1.csv'  # Cambia por la ruta de tu archivo
data = pd.read_csv(file_path)

# Extraer los datos de velocidad y RPM
velocidad = data['Speed GPS']
rpm = data['RPM']

# Crear el gráfico
plt.figure(figsize=(10, 6))
plt.plot(rpm, velocidad, label='Velocidad vs RPM', color='r')

# Etiquetas y título
plt.xlabel('RPM')
plt.ylabel('Velocidad (GPS)')
plt.title('Velocidad en función de los RPM')
plt.grid(True)
plt.legend()

# Mostrar el gráfico
plt.show()
