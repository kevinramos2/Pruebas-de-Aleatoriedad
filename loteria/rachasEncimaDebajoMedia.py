import csv
from matplotlib import pyplot as plt
from scipy.stats import chi2
import math as m
import numpy as np

# Lista para almacenar los resultados
resultadosLoteria = []
rutaArchivo = 'loteriaBOG.csv'

# Leer el archivo
with open(rutaArchivo, 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        v = int(row[0])  # Convertir a entero
        resultadosLoteria.append(v)

def rachasYFrecuencias(resultados, media):
    corridasArriba = 0
    corridasAbajo = 0
    n1, n2 = 0, 0
    tendenciaActual = None  # Para saber la tendencia actual de la corrida

    for i in range(len(resultados)):
        if resultados[i] > media:  # Por encima de la media
            n1 += 1
            if tendenciaActual != "arriba":
                corridasArriba += 1
                tendenciaActual = "arriba"
        elif resultados[i] < media:  # Por debajo de la media
            n2 += 1
            if tendenciaActual != "abajo":
                corridasAbajo += 1
                tendenciaActual = "abajo"

    return corridasArriba, corridasAbajo, n1, n2

def prueba(arriba, abajo, tamaño, n1, n2):
    N = tamaño
    b = arriba + abajo
    miu = ((2 * n1 * n2) / N) + 0.5  # Frecuencia esperada de rachas
    sigmaC = (2 * n1 * n2 * (2 * n1 * n2 - N)) / ((N ** 2) * (N - 1))  # Desviación estándar
    estadistico = (b - miu) / m.sqrt(sigmaC)  # Estadístico de prueba estandarizado
    print(N,b,miu,sigmaC)
    print(f"\nEstadístico de prueba calculado: {(estadistico):.2f}")
    print("Valor crítico (nivel de significancia del 5%): 1.96\n")

    if abs(estadistico) <= 1.96:
        print(f"Como el estadístico calculado ({abs(estadistico):.2f}) es menor o igual al valor crítico (1.96):")
        print("No hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, se concluye que las observaciones son independientes.\n")
    else:
        print(f"Como el estadístico calculado ({abs(estadistico):.2f}) es mayor al valor crítico (1.96):")
        print("Hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, se concluye que las observaciones no son independientes.\n")

# Prueba 4 - Prueba de rachas por encima y por debajo de la media
print("\nAnálisis de independencia basado en rachas por encima y por debajo de la media")
print("Planteamiento de hipótesis:")
print("Ho: Los números están en una secuencia independiente.")
print("Ha: Los números no están en una secuencia independiente.\n")

# Calcular la media
media = np.mean(resultadosLoteria)
print(f"Media de los resultados: {media:.2f}\n")

# Calcular rachas y frecuencias
arriba, abajo, n1, n2 = rachasYFrecuencias(resultadosLoteria, media)
print(f"Resultados de las rachas:")
print(f" - Número de rachas por encima de la media: {arriba}")
print(f" - Número de rachas por debajo de la media: {abajo}\n")
print(f"Frecuencias observadas:")
print(f" - Número de observaciones por encima de la media: {n1}")
print(f" - Número de observaciones por debajo de la media: {n2}\n")

# Realizar la prueba de hipótesis
prueba(arriba, abajo, len(resultadosLoteria), n1, n2)

# Prueba espectral
# Crear pares adyacentes
pares = [(resultadosLoteria[i], resultadosLoteria[i-1]) for i in range(len(resultadosLoteria)-1)]

# Separar en dos listas para graficar
x_vals = [par[0] for par in pares]
y_vals = [par[1] for par in pares]

# Graficar los pares en un plano cartesiano
plt.figure(figsize=(10, 6))
plt.scatter(x_vals, y_vals, alpha=0.6, edgecolor='k', color='blue')
plt.title("Prueba espectral: Pares adyacentes de la secuencia")
plt.xlabel("x_j")
plt.ylabel("x_j-1")
plt.grid(True)
plt.show()
