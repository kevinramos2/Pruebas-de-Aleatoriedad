import matplotlib.pyplot as plt

# Función para graficar la función acumulada empírica y teórica
def funcionesAcumuladas(xEmpirica, yEmpirica):
    """
    Genera una gráfica de la función acumulada empírica y la teórica (uniforme).
    
    x_empirica: Lista de valores en el eje x de la función empírica (R(i)).
    y_empirica: Lista de valores en el eje y de la función empírica (i/N).
    """
    # Datos para la función acumulada teórica
    xTeorica = [0, 1]
    yTeorica = [0, 1]
    
    # Crear la gráfica
    plt.figure(figsize=(8, 6))
    
    # Graficar la función acumulada empírica
    plt.step(xEmpirica, yEmpirica, where='post', label='Función acumulada empírica', color='blue')
    
    # Graficar la función acumulada teórica
    plt.plot(xTeorica, yTeorica, label='Función acumulada teórica (Uniforme)', color='red', linestyle='--')
    
    # Personalizar la gráfica
    plt.title('Comparación de funciones acumuladas')
    plt.xlabel('Valores de R(i)')
    plt.ylabel('Probabilidad acumulada')
    plt.legend()
    plt.grid()
    plt.show()

# Ejemplo: Inserta aquí tus valores de R(i) y i/N
xEmpirica = [0.011275108
, 0.023668758, 0.024679322, 0.065576676, 0.301312312, 0.364036823, 0.387098992, 0.39290273, 0.41182687, 0.445683802, 0.498697885, 0.675030559, 0.761584601, 0.832712086, 0.850680979, 0.851352038, 0.852003769, 0.876077564, 0.877583479, 0.944881255]
yEmpirica = [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 1.0]

# Llamar a la función para graficar
funcionesAcumuladas(xEmpirica, yEmpirica)
