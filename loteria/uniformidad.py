import csv
from matplotlib import pyplot as plt
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

def intervalos(resultados):
    uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez = [], [], [], [], [], [], [], [], [], []

    for i in range(len(resultados)):
        if 0 <= resultados[i] <= 999:
            uno.append(resultados[i])
        elif 1000 <= resultados[i] <= 1999:
            dos.append(resultados[i])
        elif 2000 <= resultados[i] <= 2999:
            tres.append(resultados[i])
        elif 3000 <= resultados[i] <= 3999:
            cuatro.append(resultados[i])
        elif 4000 <= resultados[i] <= 4999:
            cinco.append(resultados[i])
        elif 5000 <= resultados[i] <= 5999:
            seis.append(resultados[i])
        elif 6000 <= resultados[i] <= 6999:
            siete.append(resultados[i])
        elif 7000 <= resultados[i] <= 7999:
            ocho.append(resultados[i])
        elif 8000 <= resultados[i] <= 8999:
            nueve.append(resultados[i])
        elif 9000 <= resultados[i] <= 9999:
            diez.append(resultados[i])

    return uno, dos, tres, cuatro, cinco, seis, siete, ocho, nueve, diez

def prueba(listas):
    Ei = len(resultadosLoteria) / 10  # Frecuencia esperada
    estadístico = 0
    alpha = 0.05  # Nivel de significancia
    gl = 9  # Grados de libertad = categorías(10) - 1 = 9
    valorCritico = chi2.ppf(1 - alpha, gl)

    # Calcular el estadístico de prueba
    for i in range(10):
        estadístico += ((len(listas[i]) - Ei) ** 2 / Ei)

    # Mostrar resultados de la prueba
    print(f"Estadístico de prueba chi-cuadrado calculado: {estadístico:.2f}")
    print(f"Valor crítico para un nivel de significancia del 5%: {valorCritico:.2f}\n")

    if estadístico <= valorCritico:
        print(f"Como el estadístico calculado ({estadístico:.2f}) es menor o igual al valor crítico ({valorCritico:.2f}):")
        print("No hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, los números están distribuidos uniformemente.\n")
    else:
        print(f"Como el estadístico calculado ({estadístico:.2f}) es mayor al valor crítico ({valorCritico:.2f}):")
        print("Hay suficiente evidencia para rechazar la hipótesis nula (Ho).")
        print("Por lo tanto, los números no están distribuidos uniformemente.\n")

# Prueba 2 - Prueba de frecuencia para uniformidad usando Chi-cuadrado
print("\nAnálisis de uniformidad en los resultados de la lotería de Bogotá")
print("Planteamiento de hipótesis:")
print("Ho: Los números están distribuidos uniformemente.")
print("Ha: Los números no están distribuidos uniformemente.\n")

listas = intervalos(resultadosLoteria)
print("Se analizaron los intervalos para determinar la frecuencia de los resultados.")
prueba(listas)

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
