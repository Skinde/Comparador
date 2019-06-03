import os
nombres = ['f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7']
colecion = []
print("Archivo: ")
nombre_del_archivo_1 = input()
archivo_1 = open(str(os.getcwd())+"\\"+nombre_del_archivo_1+".txt", "r+")
lineas_1 = archivo_1.readlines()

for n in range(len(lineas_1)-1):
    lineas_1[n] = lineas_1[n].replace('\n', '')
lineas_1[0] = lineas_1[0].split(" ")

nombres.remove(nombre_del_archivo_1)
for x in range(5):
    lector = open(str(os.getcwd())+"\\"+nombres[x]+".txt", "r+").readlines()
    for n in range(len(lector)-1):   
        lector[n] = lector[n].replace('\n', '')
    lector[0] = lector[0].split(" ")
    colecion.append(lector)
