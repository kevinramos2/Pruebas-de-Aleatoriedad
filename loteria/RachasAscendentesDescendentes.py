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

def rachas(resultados):
  corridasAscendentes = 0
  corridasDescendentes = 0
  tendenciaActual = None  # Puede ser 'ascendente' descendente', o None
  for i in range(1, len(resultados)):
      if resultados[i] > resultados[i - 1]:  # Ascendente
          if tendenciaActual != "ascendente":
              corridasAscendentes += 1
              tendenciaActual = "ascendente"
      elif resultados[i] < resultados[i - 1]: # Descendente
          if tendenciaActual != "descendente":
              corridasDescendentes += 1    
              tendenciaActual = "descendente"
  return corridasAscendentes, corridasDescendentes

def prueba(asc,des,tamaño):
   Ei = tamaño/2 #Frecuencia esperada
   return
#Prueba 3 - Pruebas de rachas ascendentes/descendentes para independencia
print()
print("Se trabajará con un CSV que contiene cierta cantidad de resultados de la lotería de Bogotá.")
print("Las hipótesis planteadas son:")
print("Ho: Los números están en una secuencia independiente.")
print("Ha: Los números no están en una secuencia independiente.\n")
asc,desc = rachas(resultadosLoteria)
print(f"Rachas ascendentes: {asc}, Rachas descendentes: {desc}")
#prueba(asc,desc,len(resultadosLoteria))