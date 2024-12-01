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

def paresImpares(resultadosLoteria):
  pares = 0
  impares = 0
  for i in range(len(resultadosLoteria)):
    if resultadosLoteria[i]%2 == 0:
      pares += 1
    else:
      impares += 1
  return pares, impares

def pruebaFinal(estadístico, valorC):
  print(f'El estadístico es {estadístico}')
  print(f'El valor crítico es {valorC}\n')
  if estadístico <= valorC:
    print(f'Como {estadístico:.2f} <= {valorC:.2f}:')
    print("No hay suficiente evidencia para rechazar Ho, por lo tanto la cantidad de pares e impares en esta secuencia se puede considerar igual.\n")
  else:
    print(f'Como {estadístico:.2f} > {valorC:.2f}:')
    print("Hay suficiente evidencia para rechazar Ho, por lo tanto, aceptamos Ha y sabemos que la cantidad de pares e impares en esta secuencia es diferente.\n")

#Prueba 1 - Frecuencia de Números Pares/Impares usando Chi-cuadrado
p,i = paresImpares(resultadosLoteria)
print()
print("Se trabajará con un CSV que contiene cierta cantidad de resultados de la lotería de Bogotá.")
print("Las hipótesis planteadas son:")
print("Ho: La cantidad de números pares e impares es igual")
print("Ha: La cantidad de números pares e impares es diferente\n")
print(f'En los {len(resultadosLoteria)} resultados de la lotería, hay {p} resultados pares y {i} impares\n')

Ei = len(resultadosLoteria)//2 #Frecuencia esperada
pruebaChi2 = ((p-Ei)**2/Ei) + ((i-Ei)**2/Ei) #Prueba chi-cuadrado para obtener el estadístico
alpha = 0.05 #Significancia
gl = 1 #Grados de libertad = categorías(par/impar) - 1 = 2 - 1 = 1
valorCritico = chi2.ppf(1 - alpha, gl)

pruebaFinal(pruebaChi2,valorCritico)

#Prueba 2 - Prueba de frecuencia para uniformidad usando Chi-cuadrado


 