from math import e
from random import random, uniform
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np


def entrenar_perceptron(imagenes, lr, iteraciones, n,solucion):
    errores= [[],[],[],[],[],[],[],[],[],[]]
    # Pesos de la Capa oculta
    w_oculta = []
    # Pesos ultima Neurona
    w_salida = []

    for i in range(n):
        w_oculta.append([])
        for _ in range(7681):
            w_oculta[i].append(round(uniform(-0.01, 0.01), 2))

    # Pesos de la Ultima Neurona
    for i in range(n+1):
        w_salida.append(round(uniform(-0.01, 0.01), 2))

    #print("Pesos capa oculta:", w_oculta)
    #print("Pesos ultima neurona:", w_salida)

    for iteraciones in range(iteraciones):
        print("Iteracion: ", iteraciones+1)
        for pix in range(len(imagenes)):
            x = 0
            # Salida de las neuronas de la capa oculta
            salida = [1]
            # Delta de los pesos de la neurona de salida
            dw_n_salida = []
            # Delta de las neuronas capa oculta
            delta_co = []
            # Delta de los pesos de las neuronas capa oculta
            dw_co = []
            
            solucion_deseada = int(solucion[pix])
            #print(solucion_deseada)
            x_neu_salida = 0
            #print(imagenes[pix][0])
            #print(len(imagenes[pix]))            
            for i in range(n):
                x = 0
                for j in range(len(imagenes[pix])):
                    # x es sumatoria de cada peso por su entrada
                    x = x + imagenes[pix][j]*w_oculta[i][j]     
                # salida de las neuronas capa oculta
                salida.append(1/(1+e**(-x)))
            
            #print(salida)

            for i in range(n+1):
                # salida de la ultima neurona
                x_neu_salida += salida[i]*w_salida[i]

            salida_real = 1/(1+e**(-x_neu_salida))
            error = solucion_deseada-salida_real
            deltaf = salida_real*(1-salida_real)*error

            # Delta de los pesos de la neurona de salida

            for i in range(n+1):
                dw_n_salida.append(lr*salida[i]*deltaf)
                # Nuevos pesos ultima Neurona
                w_salida[i] = w_salida[i]+dw_n_salida[i]

            salida.pop(0)
            for i in range(n):
                # Deltas de las neuronas capa oculta
                delta_co.append(salida[i]*(1-salida[i])*deltaf)
                for en in imagenes[pix]:
                    # Delta de los pesos de la capa oculta
                    dw_co.append(lr*en*delta_co[i])
                    dw_co.append(lr*en*delta_co[i])
                    dw_co.append(lr*en*delta_co[i])
            count = 0
            for i in range(n):
                for j in range(3):
                    # Nuevos pesos de la capa oculta
                    w_oculta[i][j] = w_oculta[i][j]+dw_co[count]
                    count += 1
            #print("Deltas de los pesos ultima Neurona:",dw_n_salida)
            #print("Pesos ultima neurona:",w_salida)
            #print("Nuevos pesos:",w_oculta)

            #print("Salida real:", salida_real)
            #print("Salida deseada:", solucion_deseada)
            #print("error:", error)
            #print("-------------------------")
            errores[pix].append(error)

    plt.plot(errores[0])
    plt.plot(errores[1])
    plt.plot(errores[2])
    plt.plot(errores[3])
    plt.plot(errores[4])
    plt.plot(errores[5])
    plt.plot(errores[6])
    plt.plot(errores[7])
    plt.plot(errores[8])
    plt.plot(errores[9])

    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.show()


def leer_imagenes():
    ruta='/home/valentin/Escritorio/5to/InteligenciaArtificial/tp6/fotos/'
    lista=[]
    imagenes=[]
    for gesto in range(1,6):
        for persona in 'AB':

            nombre=str(gesto)+persona+'58018.jpg'
            print(nombre)
            img = Image.open(ruta+nombre)
            w,h=img.size
            #print("entradas:",w*h)
            #print(h)
            pixel=img.load()
            for i in range(w):
                for j in range(h):
                    lista.append(pixel[i,j][0])
            lista.insert(0,1)
            imagenes.append(lista)
            lista=[]

    #print(len(imagenes))
    return(imagenes)

if __name__ == "__main__":

    imagenes=leer_imagenes()
    lr = 0.5
    iteraciones = 100
    neuronas = 100
    solucion=(0,1,0,1,0,1,0,1,0,1)
    entrenar_perceptron(imagenes, lr, iteraciones, neuronas,solucion)
