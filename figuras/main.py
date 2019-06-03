import os
exec(open(str(os.getcwd())+"\\"+"lector.py").read())

def comparacion(matriz_1,matriz_2):
    if (matriz_1[0]==matriz_2[0]):
        fila=int(matriz_1[0][0])
        columna=int(matriz_1[0][1])-1
        area=fila*columna
        temp=area
        for i in range(1,fila+1):
            for o in range(1,columna):
                print(i)
                print(o)
                if(matriz_1[i][o]==matriz_2[i][o]):
                    temp=temp-1
        similitud=temp/area
        return similitud
    else:
        print("La copia difiere de la original.")

print(comparacion(lineas_1,colecion[0]))