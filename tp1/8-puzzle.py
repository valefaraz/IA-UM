import random 

def info_tablero(tablero):
    pos_moviles=[]
    direccion=[]
    for n in range(len(tablero)):
        #print(n)
        if n <= 7:
            if tablero[n+1] == 0:
                print("La posicion",n,"se puede mover a la derecha")
                pos_moviles.append(n)
                direccion.append('derecha')
                
        if n <= 5:
            if tablero[n+3]==0:
                print("La posicion",n,"se puede mover hacia abajo")
                pos_moviles.append(n)
                direccion.append('abajo')
    
        if n >= 1:
            if tablero[n-1] == 0:
                print("La posicion",n,"se puede mover a la izquierda")
                pos_moviles.append(n)
                direccion.append('izquierda')
    
        if n >= 3:
            if tablero[n-3]==0:
                print("La posicion",n,"se puede mover hacia arriba")
                pos_moviles.append(n)
                direccion.append('arriba')

    print(pos_moviles)
    print(direccion)
    return(pos_moviles,direccion)

def mezclar(tablero):
    movimientos=50
    while movimientos > 0:
        movimientos=movimientos-1
        pos_moviles, direccion = info_tablero(tablero)
        ran = random.choice(pos_moviles)
        print('Movemos la posición: ',ran)
        if ran==0:
            indice = pos_moviles.index(0)

            if direccion[indice]=='derecha':
                pos1= tablero[0]
                pos2=tablero[0+1]
                tablero[0]=pos2
                tablero[0+1]=pos1

            #LA POSICION 0 NO SE PUEDE MOVER NI A LA IZQUIERDA NI ARRIBA
            if direccion[indice]=='abajo':
                pos1= tablero[0]
                pos2=tablero[0+3]
                tablero[0]=pos2
                tablero[0+3]=pos1

        if ran==1:
            indice = pos_moviles.index(1)

            if direccion[indice]=='derecha':
                pos1= tablero[1]
                pos2=tablero[1+1]
                tablero[1]=pos2
                tablero[1+1]=pos1

            if direccion[indice]=='izquierda':
                pos1= tablero[1]
                pos2=tablero[1-1]
                tablero[1]=pos2
                tablero[1-1]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[1]
                pos2=tablero[1+3]
                tablero[1]=pos2
                tablero[1+3]=pos1

        if ran==2:
            indice = pos_moviles.index(2)

            if direccion[indice]=='izquierda':
                pos1= tablero[2]
                pos2=tablero[2-1]
                tablero[2]=pos2
                tablero[2-1]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[2]
                pos2=tablero[2+3]
                tablero[2]=pos2
                tablero[2+3]=pos1

        if ran==3:
            indice = pos_moviles.index(3)

            if direccion[indice]=='derecha':
                pos1= tablero[3]
                pos2=tablero[3+1]
                tablero[3]=pos2
                tablero[3+1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[3]
                pos2=tablero[3-3]
                tablero[3]=pos2
                tablero[3-3]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[3]
                pos2=tablero[3+3]
                tablero[3]=pos2
                tablero[3+3]=pos1

        if ran==4:
            indice = pos_moviles.index(4)

            if direccion[indice]=='derecha':
                pos1= tablero[4]
                pos2=tablero[4+1]
                tablero[4]=pos2
                tablero[4+1]=pos1

            if direccion[indice]=='izquierda':
                pos1= tablero[4]
                pos2=tablero[4-1]
                tablero[4]=pos2
                tablero[4-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[4]
                pos2=tablero[4-3]
                tablero[4]=pos2
                tablero[4-3]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[4]
                pos2=tablero[4+3]
                tablero[4]=pos2
                tablero[4+3]=pos1

        if ran==5:
            indice = pos_moviles.index(5)

            if direccion[indice]=='izquierda':
                pos1= tablero[5]
                pos2=tablero[5-1]
                tablero[5]=pos2
                tablero[5-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[5]
                pos2=tablero[5-3]
                tablero[5]=pos2
                tablero[5-3]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[5]
                pos2=tablero[5+3]
                tablero[5]=pos2
                tablero[5+3]=pos1

        if ran==6:
            indice = pos_moviles.index(6)

            if direccion[indice]=='derecha':
                pos1= tablero[6]
                pos2=tablero[6+1]
                tablero[6]=pos2
                tablero[6+1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[6]
                pos2=tablero[6-3]
                tablero[6]=pos2
                tablero[6-3]=pos1

        if ran==7:
            indice = pos_moviles.index(7)
            if direccion[indice]=='derecha':
                pos1= tablero[7]
                pos2=tablero[7+1]
                tablero[7]=pos2
                tablero[7+1]=pos1

            if direccion[indice]=='izquierda':
                pos1= tablero[7]
                pos2=tablero[7-1]
                tablero[7]=pos2
                tablero[7-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[7]
                pos2=tablero[7-3]
                tablero[7]=pos2
                tablero[7-3]=pos1

        if ran==8:
            indice = pos_moviles.index(8)

            if direccion[indice]=='izquierda':
                pos1= tablero[8]
                pos2=tablero[8-1]
                tablero[8]=pos2
                tablero[8-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[8]
                pos2=tablero[8-3]
                tablero[8]=pos2
                tablero[8-3]=pos1



        print(tablero)
        print('_________________________________________')
    return tablero


def busqueda_random(tablero):
    pasos=0
    while tablero != [1,2,3,4,5,6,7,8,0]:
        pasos=pasos+1
        pos_moviles, direccion = info_tablero(tablero)
        ran = random.choice(pos_moviles)
        print('Movemos la posición: ',ran)
        if ran==0:
            indice = pos_moviles.index(0)

            if direccion[indice]=='derecha':
                pos1= tablero[0]
                pos2=tablero[0+1]
                tablero[0]=pos2
                tablero[0+1]=pos1

            #LA POSICION 0 NO SE PUEDE MOVER NI A LA IZQUIERDA NI ARRIBA
            if direccion[indice]=='abajo':
                pos1= tablero[0]
                pos2=tablero[0+3]
                tablero[0]=pos2
                tablero[0+3]=pos1

        if ran==1:
            indice = pos_moviles.index(1)

            if direccion[indice]=='derecha':
                pos1= tablero[1]
                pos2=tablero[1+1]
                tablero[1]=pos2
                tablero[1+1]=pos1

            if direccion[indice]=='izquierda':
                pos1= tablero[1]
                pos2=tablero[1-1]
                tablero[1]=pos2
                tablero[1-1]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[1]
                pos2=tablero[1+3]
                tablero[1]=pos2
                tablero[1+3]=pos1

        if ran==2:
            indice = pos_moviles.index(2)

            if direccion[indice]=='izquierda':
                pos1= tablero[2]
                pos2=tablero[2-1]
                tablero[2]=pos2
                tablero[2-1]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[2]
                pos2=tablero[2+3]
                tablero[2]=pos2
                tablero[2+3]=pos1

        if ran==3:
            indice = pos_moviles.index(3)

            if direccion[indice]=='derecha':
                pos1= tablero[3]
                pos2=tablero[3+1]
                tablero[3]=pos2
                tablero[3+1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[3]
                pos2=tablero[3-3]
                tablero[3]=pos2
                tablero[3-3]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[3]
                pos2=tablero[3+3]
                tablero[3]=pos2
                tablero[3+3]=pos1

        if ran==4:
            indice = pos_moviles.index(4)

            if direccion[indice]=='derecha':
                pos1= tablero[4]
                pos2=tablero[4+1]
                tablero[4]=pos2
                tablero[4+1]=pos1

            if direccion[indice]=='izquierda':
                pos1= tablero[4]
                pos2=tablero[4-1]
                tablero[4]=pos2
                tablero[4-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[4]
                pos2=tablero[4-3]
                tablero[4]=pos2
                tablero[4-3]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[4]
                pos2=tablero[4+3]
                tablero[4]=pos2
                tablero[4+3]=pos1

        if ran==5:
            indice = pos_moviles.index(5)

            if direccion[indice]=='izquierda':
                pos1= tablero[5]
                pos2=tablero[5-1]
                tablero[5]=pos2
                tablero[5-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[5]
                pos2=tablero[5-3]
                tablero[5]=pos2
                tablero[5-3]=pos1

            if direccion[indice]=='abajo':
                pos1= tablero[5]
                pos2=tablero[5+3]
                tablero[5]=pos2
                tablero[5+3]=pos1

        if ran==6:
            indice = pos_moviles.index(6)

            if direccion[indice]=='derecha':
                pos1= tablero[6]
                pos2=tablero[6+1]
                tablero[6]=pos2
                tablero[6+1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[6]
                pos2=tablero[6-3]
                tablero[6]=pos2
                tablero[6-3]=pos1

        if ran==7:
            indice = pos_moviles.index(7)
            if direccion[indice]=='derecha':
                pos1= tablero[7]
                pos2=tablero[7+1]
                tablero[7]=pos2
                tablero[7+1]=pos1

            if direccion[indice]=='izquierda':
                pos1= tablero[7]
                pos2=tablero[7-1]
                tablero[7]=pos2
                tablero[7-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[7]
                pos2=tablero[7-3]
                tablero[7]=pos2
                tablero[7-3]=pos1

        if ran==8:
            indice = pos_moviles.index(8)

            if direccion[indice]=='izquierda':
                pos1= tablero[8]
                pos2=tablero[8-1]
                tablero[8]=pos2
                tablero[8-1]=pos1

            if direccion[indice]=='arriba':
                pos1= tablero[8]
                pos2=tablero[8-3]
                tablero[8]=pos2
                tablero[8-3]=pos1
    print('Pasos:',pasos)
    print(tablero)
    return pasos

def busqueda_anchura(pos_moviles,tablero):        
    aux=tablero
    for i in pos_moviles:
        mov = aux.index(i)
        vacio = aux.index(0)
        aux[mov] = 0
        aux[vacio] = i
        print(aux)
    
        


        







if __name__ == "__main__":

    tablero=[1,2,3,
             4,5,6,
             7,8,0]
    
    pos_moviles, direccion = info_tablero(tablero)
    

    tablero_mezclado = mezclar(tablero)
    print('-------------')
    print('|',tablero_mezclado[0],'|',tablero_mezclado[1],'|',tablero_mezclado[2],'|')
    print('-------------')
    print('|',tablero_mezclado[3],'|',tablero_mezclado[4],'|',tablero_mezclado[5],'|')
    print('-------------')
    print('|',tablero_mezclado[6],'|',tablero_mezclado[7],'|',tablero_mezclado[8],'|')
    print('-------------')

    #busqueda_random(tablero_mezclado)
    
    #Encontro la solucion una vez en el paso n° 190.245 y otra vez en el paso n° 1.738.696

    #pos_moviles, direccion = info_tablero(tablero_mezclado)
    #busqueda_anchura(pos_moviles,tablero_mezclado)
    