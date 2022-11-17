import random
from math import e


def entrenar_perceptron(tabla,lr):
    w0= round(random.uniform(-1,1),4)
    w1= round(random.uniform(-1,1),4)
    w2= round(random.uniform(-1,1),4)
    i=0
    print(w0,w1,w2)
    while True:
        i=i+1
        for combinacion in tabla:
            print(combinacion)
            solucion_deseada=int(combinacion[2])
            e0=1
            e1=int(combinacion[0])
            e2=int(combinacion[1])
            x= (e1*w1) + (e2*w2) + (e0*w0)    
            solucion_real = round(1/(1+e**x),4)
            error=solucion_real-solucion_deseada

            s=solucion_real*(1-solucion_real)*error

            deltaw0=lr*e0*s
            w0=w0+deltaw0

            deltaw1=lr*e1*s
            w1=w1+deltaw1

            deltaw2=lr*e2*s
            w2=w2+deltaw2
        
            print('Vuelta numero',i)
            print('Solucion Real:',solucion_real)
            print('Solucion Deseada:',solucion_deseada)

        if i > 100:
            break


if __name__ == "__main__":

    tabla_or=['000','011','101','111']
    tabla_and=['000','010','100','111']
    
    lr=0.1
    #entrenar_perceptron(tabla_or,lr)

    #entrenar_perceptron(tabla_and,lr)




