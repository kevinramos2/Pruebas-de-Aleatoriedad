import csv

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

p,i = paresImpares(resultadosLoteria)
print(f'En {len(resultadosLoteria)} datos hay {p} pares y {i} impares')