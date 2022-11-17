import random 

arbol=[]
arbol_b=[]

def info_tablero(tablero):
    pos_moviles=[]
    for n in range(len(tablero)):
        
        if n in [0,1,3,4,6,7]:
            #Se puede mover hacia la derecha
            if tablero[n+1] == 0:
                pos_moviles.append(n)
                
        if n in [0,1,2,3,4,5]:
            #Se puede mover hacia abiajo
            if tablero[n+3]==0:
                pos_moviles.append(n)
    
        if n in [1,2,4,5,7,8]:
            #Se puede mover hacia la izquierda
            if tablero[n-1] == 0:
                pos_moviles.append(n)
    
        if n in [3,4,5,6,7,8]:
            #Se puede mover hacia arriba
            if tablero[n-3]==0:
                pos_moviles.append(n)
    return(pos_moviles)

def mostrar(tablero):
    print('-------------')
    print('|',tablero[0],'|',tablero[1],'|',tablero[2],'|')
    print('-------------')
    print('|',tablero[3],'|',tablero[4],'|',tablero[5],'|')
    print('-------------')
    print('|',tablero[6],'|',tablero[7],'|',tablero[8],'|')
    print('-------------')

def mezclar(tablero_m):
    movimientos=50
    while movimientos > 0:
        movimientos=movimientos-1
        pos_moviles = info_tablero(tablero_m)
        ran = random.choice(pos_moviles)
        indice_vacio = tablero_m.index(0)
        tablero_m[indice_vacio]=tablero_m[ran]
        tablero_m[ran]=0
    return tablero_m

def busqueda_random(tablero):
    pasos=0
    while tablero != [1,2,3,4,5,6,7,8,0]:
        pasos=pasos+1
        pos_moviles = info_tablero(tablero)
        ran = random.choice(pos_moviles)
        indice_vacio = tablero.index(0)
        tablero[indice_vacio]=tablero[ran]
        tablero[ran]=0
    print(tablero)
    print("La solucion se encontro en",pasos,"pasos")
    return pasos

def busqueda_anchura(tablero):
    aux=tablero.copy()
    pos_moviles = info_tablero(tablero)
    indice_vacio = tablero.index(0)
    desarrollo_tablero=[]
    for n in pos_moviles:
        tablero=aux.copy()
        tablero[indice_vacio]=tablero[n]
        tablero[n]=0
        desarrollo_tablero.append(tablero)
    arbol.append(desarrollo_tablero)


def busqueda_bidireccional(tablero):
    aux=tablero.copy()
    pos_moviles = info_tablero(tablero)
    indice_vacio = tablero.index(0)
    desarrollo_tablero=[]
    for n in pos_moviles:
        tablero=aux.copy()
        tablero[indice_vacio]=tablero[n]
        tablero[n]=0
        desarrollo_tablero.append(tablero)
    arbol_b.append(desarrollo_tablero)


if __name__ == "__main__":
    tablero=[1,2,3,
             4,5,6,
             7,8,0]
    tablero_solucion=[1,2,3,
                      4,5,6,
                      7,8,0]
    #Mezclar el tablero
    tablero_mezclado = mezclar(tablero)
    print("Tablero mezclado")
    mostrar(tablero_mezclado)

    #Buscar random
    #Encontro la solucion una vez en el paso n° 190.245 y otra vez en el paso n° 1.738.696
    busqueda_random(tablero_mezclado)
    
    #Busqueda en anchura
    busqueda_anchura(tablero_mezclado)
    tabla=[]
    numero_nivel=0
    iteracion=0
    for nivel in arbol:
        #print('arbol:',iteracion,arbol)
        for tabla in nivel:
            #print (tabla)
            busqueda_anchura(tabla)
            if tabla==tablero_solucion:
                movimientos = arbol.index(nivel)
                print('Movimientos calculados en busqueda por anchura:',movimientos)
                quit()
    """   
    #Busqueda bidireccional
    busqueda_bidireccional(tablero_mezclado)
    busqueda_anchura(tablero_solucion)
    tabla=[]
    numero_nivel=0
    iteracion=0
    #recorro los dos arboles con los movimientos
    for nivel,nivel_b in zip(arbol, arbol_b):
        #recorro los niveles de cada arbol
        for tabla,tabla_b in zip(nivel,nivel_b):            
            #recorro uno de los dos arboles para validar si coinciden los tableros
            for validacion in arbol:
                #recorro el nivel del arbol con el que voy a validar
                for matriz in validacion:
                    #si una de las matrices de ese arbol de validacion coincide 
                    #con la que matriz que acabamos de encontrar significa que encontramos la interseccion 
                    if matriz==tabla_b:
                        movimientos = arbol.index(validacion)
                        print('Movimientos calculados en busqueda bidireccional:',movimientos)
                        print("Matriz intersección:",tabla_b)
                        quit()
            busqueda_bidireccional(tabla_b)
            busqueda_anchura(tabla)
"""