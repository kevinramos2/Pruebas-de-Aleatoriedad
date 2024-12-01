import csv
from scipy.stats import chi2

# Lista para almacenar los resultados
resultadosLoteria = []
ruta_archivo = 'loteriaBOG.csv'  
# Leer el archivo
with open(ruta_archivo, 'r') as read_obj:
    # Crear un objeto lector de CSV
    csv_reader = csv.reader(read_obj)
    for row in csv_reader:
        v = int(row[0])  # Convertir a entero
        resultadosLoteria.append(v)

#Prueba 1 - Frecuencia de Números Pares/Impares usando Chi-cuadrado

# Ho: La cantidad de números pares e impares es igual
# Ha: La cantidad de números pares e impares es diferente

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
  if estadístico <= valorC:
    print("No hay suficiente evidencia para rechazar Ho, por lo tanto la cantidad de pares e impares en esta secuencia se puede considerar igual.")
  else:
    print("Hay suficiente evidencia para rechazar Ho, por lo tanto, aceptamos Ha y sabemos que la cantidad de pares e impares en esta secuencia es diferente.")


p,i = paresImpares(resultadosLoteria)
print(f'En {len(resultadosLoteria)} datos hay {p} pares y {i} impares')

Ei = len(resultadosLoteria)//2 #Frecuencia esperada
pruebaChi2 = ((p-Ei)**2/Ei) + ((i-Ei)**2/Ei) #Prueba chi-cuadrado para obtener el estadístico
alpha = 0.05 #Significancia
gl = 1 #Grados de libertad
valorCritico = chi2.ppf(1 - alpha, gl)

print(f'El estadístico es {pruebaChi2}')
print(f'El valor crítico es {valorCritico}')
pruebaFinal(pruebaChi2,valorCritico)


 