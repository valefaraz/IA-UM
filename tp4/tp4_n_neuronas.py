from math import e
from random import random, uniform
import matplotlib.pyplot as plt


def entrenar_perceptron(tabla, lr, iteraciones, n):
    # Pesos de la Capa oculta
    w_oculta = []
    # Pesos ultima Neurona
    w_salida = []
    l_error = []

    for i in range(n):
        w_oculta.append([])
        for _ in range(3):
            w_oculta[i].append(round(uniform(-1, 1), 2))

    # Pesos de la Ultima Neurona
    for i in range(n+1):
        w_salida.append(round(uniform(-1, 1), 2))

    print("Pesos capa oculta:", w_oculta)
    print("Pesos ultima neurona:", w_salida)

    for iteraciones in range(iteraciones):
        print("Iteracion: ", iteraciones+1)
        for combinacion in tabla:
            x = 0
            # Salida de las neuronas de la capa oculta
            salida = [1]
            # Delta de los pesos de la neurona de salida
            dw_n_salida = []
            # Delta de las neuronas capa oculta
            delta_co = []
            # Delta de los pesos de las neuronas capa oculta
            dw_co = []
            #print("listas vacias:",salida,dw_co,dw_n_salida,delta_co)

            print("Fila de la tabla de la verdad:", combinacion)
            # entradas iniciales
            e0 = 1
            e1 = int(combinacion[0])
            e2 = int(combinacion[1])
            solucion_deseada = int(combinacion[2])
            x_neu_salida = 0

            for i in range(n):
                # x es sumatoria de cada peso por su entrada
                x = (e0*w_oculta[i][0]) + \
                    (e1*(w_oculta[i][1])) + (e2*w_oculta[i][2])
                # salida de las neuronas capa oculta
                salida.append(1/(1+e**(-x)))

            for i in range(n+1):
                # salida de la ultima neurona
                x_neu_salida += salida[i]*w_salida[i]

            salida_real = 1/(1+e**(-x_neu_salida))
            error = solucion_deseada-salida_real
            deltaf = salida_real*(1-salida_real)*error

            # Delta de los pesos de la neurona de salida
            # dw_n_salida.append(lr*e0*deltaf)
            for i in range(n+1):
                dw_n_salida.append(lr*salida[i]*deltaf)
                # Nuevos pesos ultima Neurona
                w_salida[i] = w_salida[i]+dw_n_salida[i]

            salida.pop(0)
            for i in range(n):
                # Deltas de las neuronas capa oculta
                delta_co.append(salida[i]*(1-salida[i])*deltaf)
                # Delta de los pesos de la capa oculta
                dw_co.append(lr*e0*delta_co[i])
                dw_co.append(lr*e1*delta_co[i])
                dw_co.append(lr*e2*delta_co[i])
            count = 0
            for i in range(n):
                for j in range(3):
                    # Nuevos pesos de la capa oculta
                    w_oculta[i][j] = w_oculta[i][j]+dw_co[count]
                    count += 1
            #print("Deltas de los pesos ultima Neurona:",dw_n_salida)
            #print("Pesos ultima neurona:",w_salida)
            #print("Nuevos pesos:",w_oculta)

            print("Salida real:", salida_real)
            print("Salida deseada:", solucion_deseada)
            print("error:", error)
            print("-------------------------")

        l_error.append(-error)
    plt.plot(l_error)
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.show()


if __name__ == "__main__":
    # Tabla de la verdad de XOR
    tabla_xor = ['000', '011', '101', '110']

    lr = 0.5
    iteraciones = 2000
    neuronas = 50
    entrenar_perceptron(tabla_xor, lr, iteraciones, neuronas)
