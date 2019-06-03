import os

nueva_linea_1 = []
nueva_linea_2 = []
print("Archivo 1:")
nombre_del_archivo_1 = input()
archivo_1 = open(str(os.getcwd())+"\\"+nombre_del_archivo_1+".txt", "r+")
lineas_1 = archivo_1.readlines()
print("Archivo 2:")
nombre_del_archivo_2 = input()
archivo_2 = open(str(os.getcwd())+"\\"+nombre_del_archivo_2+".txt", "r+")
lineas_2 = archivo_2.readlines()

for n in range(len(lineas_1)-1):
    lineas_1[n] = lineas_1[n].replace('\n', '')
lineas_1[0] = lineas_1[0].split(" ")
print(lineas_1)

for n in range(len(lineas_2)-1):
    lineas_2[n] = lineas_2[n].replace('\n', '')
lineas_2[0] = lineas_2[0].split(" ")
print(lineas_1)