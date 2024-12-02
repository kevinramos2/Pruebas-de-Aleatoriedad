import csv
from scipy.stats import chi2
import math as m
import numpy as np

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

def rachas(resultados,media):
  corridasArriba = 0
  corridasAbajo = 0
  tendenciaActual = None  # Para saber la actual corrida en qué va
  for i in range(len(resultados)):
      if resultados[i] > media:  # Por arriba de la media
          if tendenciaActual != "arriba":
              corridasArriba += 1
              tendenciaActual = "arriba"
      elif resultados[i] < media: # Por debajo de la media
          if tendenciaActual != "abajo":
              corridasAbajo += 1    
              tendenciaActual = "abajo"
  return corridasArriba, corridasAbajo

def prueba(arriba,abajo,tamaño):
  n1 = arriba
  n2 = abajo
  N = arriba+abajo
  b = N
  miu = ((2*n1*n2)/N) + 1/2 #Frecuencia esperada
  sigmaC = (2*n1*n2*(2*n1*n2-N))/((N**2)*(N-1))#Desviación
  estadistico = (b-miu)/m.sqrt(sigmaC) #Estadístico estandarizado

  if abs(estadistico) <= 1.96:
    print(f'Como el estadístico calculado ({abs(estadistico):.2f}) es <= al valor crítico (1.96). NO hay suficiente evidencia para descartar Ho, por lo tanto las observaciones son independientes.')
  else:
     print(f'Como el estadístico calculado ({abs(estadistico):.2f}) es > al valor crítico (1.96), hay suficiente evidencia para descartar Ho, por lo tanto las observaciones NO son independientes.')

#Prueba 4 - Prueba de rachas por encima y debajo de la media para independencia
print()
print("Se trabajará con un CSV que contiene cierta cantidad de resultados de la lotería de Bogotá.")
print("Las hipótesis planteadas son:")
print("Ho: Los números están en una secuencia independiente.")
print("Ha: Los números no están en una secuencia independiente.\n")
media = np.mean(resultadosLoteria)
arriba, abajo = rachas(resultadosLoteria,media)
print(f"Rachas ascendentes: {arriba}, Rachas descendentes: {abajo}")
prueba(arriba,abajo,len(resultadosLoteria))
