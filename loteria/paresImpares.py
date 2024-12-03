import csv
from scipy.stats import chi2

# Lista para almacenar los resultados
resultadosLoteria = []
rutaArchivo = 'loteriaBOG.csv'

# Leer el archivo
with open(rutaArchivo, 'r') as read_obj:
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        v = int(row[0])  # Convertir a entero
        resultadosLoteria.append(v)

def paresImpares(resultadosLoteria):
    pares = 0
    impares = 0
    for i in range(len(resultadosLoteria)):
        if resultadosLoteria[i] % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def pruebaFinal(estadístico, valorC):
    print(f"El estadístico de prueba chi-cuadrado calculado es: {estadístico:.2f}")
    print(f"El valor crítico para un nivel de significancia del 5% es: {valorC:.2f}\n")
    if estadístico <= valorC:
        print(f"Como el estadístico calculado ({estadístico:.2f}) es menor o igual al valor crítico ({valorC:.2f}):")
        print("No hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, se concluye que la cantidad de números pares e impares en esta secuencia se puede considerar igual.\n")
    else:
        print(f"Como el estadístico calculado ({estadístico:.2f}) es mayor al valor crítico ({valorC:.2f}):")
        print("Hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, se concluye que la cantidad de números pares e impares en esta secuencia es significativamente diferente.\n")

# Prueba 1 - Frecuencia de Números Pares/Impares usando Chi-cuadrado
p, i = paresImpares(resultadosLoteria)

print("\nSe trabajará con un conjunto de resultados de la lotería de Bogotá.")
print("Planteamiento de hipótesis:")
print("Ho: La cantidad de números pares e impares es igual.")
print("Ha: La cantidad de números pares e impares es diferente.\n")

print(f"En un total de {len(resultadosLoteria)} resultados:")
print(f" - Números pares: {p}")
print(f" - Números impares: {i}\n")

# Cálculo de frecuencias esperadas y estadístico de prueba
Ei = len(resultadosLoteria) // 2  # Frecuencia esperada para pares e impares
pruebaChi2 = ((p - Ei) ** 2 / Ei) + ((i - Ei) ** 2 / Ei)  # Estadístico chi-cuadrado
alpha = 0.05  # Nivel de significancia
gl = 1  # Grados de libertad = categorías(par/impar) - 1 = 2 - 1 = 1
valorCritico = chi2.ppf(1 - alpha, gl)

# Presentación de resultados
pruebaFinal(pruebaChi2, valorCritico)