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

def intervalos(resultados):
    uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez = [],[],[],[],[],[],[],[],[],[]

    for i in range(len(resultados)):
        if resultados[i] >= 0 and resultados[i] <= 999:
            uno.append(resultados[i])
        elif resultados[i] >= 1000 and resultados[i] <= 1999:
            dos.append(resultados[i])
        elif resultados[i] >= 2000 and resultados[i] <= 2999:
            tres.append(resultados[i])
        elif resultados[i] >= 3000 and resultados[i] <= 3999:
            cuatro.append(resultados[i])
        elif resultados[i] >= 4000 and resultados[i] <= 4999:
            cinco.append(resultados[i])
        elif resultados[i] >= 5000 and resultados[i] <= 5999:
            seis.append(resultados[i])
        elif resultados[i] >= 6000 and resultados[i] <= 6999:
            siete.append(resultados[i])
        elif resultados[i] >= 7000 and resultados[i] <= 7999:
            ocho.append(resultados[i])
        elif resultados[i] >= 8000 and resultados[i] <= 8999:
            nueve.append(resultados[i])
        elif resultados[i] >= 9000 and resultados[i] <= 9999:
            diez.append(resultados[i])

    return uno,dos,tres,cuatro,cinco,seis,siete,ocho,nueve,diez

def prueba(listas):
  Ei = len(resultadosLoteria)/10 #Frecuencia esperada
  estadístico = 0
  alpha = 0.05 #Significancia
  gl = 9 #Grados de libertad = categorías(10) - 1 = 10 - 1 = 9
  valorCritico = chi2.ppf(1 - alpha, gl)

  for i in range(10):
      estadístico += ((len(listas[i])-Ei)**2/Ei)

  if estadístico <= valorCritico:
      print(f'El estádístico {estadístico:.2f} es <= al valor crítico {valorCritico:.2f}, por lo tanto, no tenemos suficiente información para rechazar Ho, por lo cual podemos decir que los números se distribuyen de manera uniforme.\n')
  if estadístico > valorCritico:
      print(f'Como el estadístico {estadístico:.2f} es mayor al valor crítico {valorCritico:.2f}, es suficiente información para rechazar Ho, por lo tanto, los datos no se distribuyen de manera uniforme.\n')

#Prueba 2 - Prueba de frecuencia para uniformidad usando Chi-cuadrado

print()
print("Se trabajará con un CSV que contiene cierta cantidad de resultados de la lotería de Bogotá.")
print("Las hipótesis planteadas son:")
print("Ho: Los números están distribuidos uniformemente.")
print("Ha: Los números no están distribuidos uniformemente.\n")

listas = intervalos(resultadosLoteria)
prueba(listas)