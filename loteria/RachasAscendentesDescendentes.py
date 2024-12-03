import csv
from matplotlib import pyplot as plt
from scipy.stats import chi2
import math as m

# Lista para almacenar los resultados
resultadosLoteria = []
rutaArchivo = 'loteriaBOG.csv'

# Leer el archivo
with open(rutaArchivo, 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        v = int(row[0])  # Convertir a entero
        resultadosLoteria.append(v)

def rachas(resultados):
    corridasAscendentes = 0
    corridasDescendentes = 0
    tendenciaActual = None  # Para identificar la tendencia actual

    for i in range(len(resultados)):
        if resultados[i] > resultados[i - 1]:  # Ascendente
            if tendenciaActual != "ascendente":
                corridasAscendentes += 1
                tendenciaActual = "ascendente"
        elif resultados[i] < resultados[i - 1]:  # Descendente
            if tendenciaActual != "descendente":
                corridasDescendentes += 1
                tendenciaActual = "descendente"

    return corridasAscendentes, corridasDescendentes

def prueba(asc, des, tamaño):
    total_rachas = asc + des
    miu = ((2 * tamaño) - 1) / 3  # Frecuencia esperada
    sigmaC = ((16 * tamaño) - 29) / 90  # Desviación estándar
    estadistico = (total_rachas - miu) / m.sqrt(sigmaC)  # Estadístico de prueba estandarizado

    print(f"\nEstadístico de prueba calculado: {abs(estadistico):.2f}")
    print("Valor crítico (nivel de significancia del 5%): 1.96\n")

    if abs(estadistico) <= 1.96:
        print(f"Como el estadístico calculado ({abs(estadistico):.2f}) es menor o igual al valor crítico (1.96):")
        print("No hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, se concluye que las observaciones son independientes.\n")
    else:
        print(f"Como el estadístico calculado ({abs(estadistico):.2f}) es mayor al valor crítico (1.96):")
        print("Hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, se concluye que las observaciones no son independientes.\n")

# Prueba 3 - Pruebas de rachas ascendentes/descendentes para independencia
print("\nAnálisis de independencia basado en rachas ascendentes y descendentes")
print("Planteamiento de hipótesis:")
print("Ho: Los números están en una secuencia independiente.")
print("Ha: Los números no están en una secuencia independiente.\n")

# Calcular rachas
asc, desc = rachas(resultadosLoteria)
print(f"Resultados de las rachas:")
print(f" - Rachas ascendentes: {asc}")
print(f" - Rachas descendentes: {desc}\n")

# Realizar la prueba de hipótesis
prueba(asc, desc, len(resultadosLoteria))

# Prueba espectral
# Crear pares adyacentes
pares = [(resultadosLoteria[i], resultadosLoteria[i+1]) for i in range(len(resultadosLoteria)-1)]

# Separar en dos listas para graficar
x_vals = [par[0] for par in pares]
y_vals = [par[1] for par in pares]

# Graficar los pares en un plano cartesiano
plt.figure(figsize=(10, 6))
plt.scatter(x_vals, y_vals, alpha=0.6, edgecolor='k', color='blue')
plt.title("Prueba espectral: Pares adyacentes de la secuencia")
plt.xlabel("x_j")
plt.ylabel("x_j+1")
plt.grid(True)
plt.show()
