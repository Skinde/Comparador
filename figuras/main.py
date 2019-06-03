import os

exec(open(str(os.getcwd())+"\\"+"lector.py").read())

def comparacion(matriz_1,matriz_2):
    if (matriz_1[0]==matriz_2[0]):
        fila=int(matriz_1[0][0])
        columna=int(matriz_1[0][1])-1
        area=fila*columna
        temp=area
        for i in range(1,fila+1):
            for o in range(columna):
                if(matriz_1[i][o]!=matriz_2[i][o]):
                    temp-=1
        similitud=round(temp/area,2)
        if similitud < 0.8:
            print("La copia difiere de la original.")
        elif similitud == 1:
            print("La copia es idéntica a la original.")
        elif similitud >= 0.8:
            print("La copia es parcialmente identica con",(similitud*100),'%',"de similitud.")

        return    
    else:
        print("No se puede comparar las figuras.")



for i in range(len(colecion)):
    print(comparacion(lineas_1,colecion[i]))
    for o in range(1,len(lineas_1)):
        print(lineas_1[o])
    for z in range(1,len(colecion[i])):
        print(colecion[i][z])
    print()

         


