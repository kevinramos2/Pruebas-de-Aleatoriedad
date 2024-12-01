import csv
from scipy.stats import chi2

# Lista para almacenar los resultados
resultadosLoteria = []
rutaArchivo = 'loteriaBOG.csv'  
# Leer el archivo
with open(rutaArchivo, 'r') as read_obj:
    # Crear un objeto lector de CSV
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        v = int(row[0])  # Convertir a entero
        resultadosLoteria.append(v)

def rachas(resutlados):
  ascendente = 0
  descendente = 0

  return
#Prueba 3 - Pruebas de rachas ascendentes/descendentes para independencia
print()
print("Se trabajará con un CSV que contiene cierta cantidad de resultados de la lotería de Bogotá.")
print("Las hipótesis planteadas son:")
print("Ho: Los números están en una secuencia independiente.")
print("Ha: Los números no están en una secuencia independiente.\n")
rachas(resultadosLoteria)