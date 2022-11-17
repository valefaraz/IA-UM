from math import e
import matplotlib.pyplot as plt


def entrenar_perceptron(tabla, lr):
    # Listas para luego graficar
    l_error = []
    lw10 = []
    lw11 = []
    lw12 = []
    lw20 = []
    lw21 = []
    lw22 = []
    lw30 = []
    lw31 = []
    lw32 = []
    lw40 = []
    lw41 = []
    lw42 = []
    lw43 = []

    # Pesos de la Capa oculta
    w10, w11, w12 = 0.9, 0.7, 0.5
    w20, w21, w22 = 0.3, -0.9, -1
    w30, w31, w32 = 0.8, 0.35, 0.1

    # Pesos de la Ultima Neurona
    w40, w41, w42, w43 = -0.23, -0.79, 0.56, 0.6

    #
    for i in range(1):
        print("Iteracion: ", i)
        for combinacion in tabla:
            print("Fila de la tabla de la verdad:", combinacion)
            solucion_deseada = int(combinacion[2])
            # entradas iniciales
            e0 = 1
            e1 = int(combinacion[0])
            e2 = int(combinacion[1])
            # x es sumatoria de cada peso por su entrada
            # salida de la neurona 1 capa oculta
            x1 = (e0*w10) + (e1*w11) + (e2*w12)
            salida1 = 1/(1+e**(-x1))
            # salida de la neurona 2 capa oculta
            x2 = (e0*w20) + (e1*w21) + (e2*w22)
            salida2 = 1/(1+e**(-x2))
            # salida de la neurona 3 capa oculta
            x3 = (e0*w30) + (e1*w31) + (e2*w32)
            salida3 = 1/(1+e**(-x3))
            # salida de la ultima neurona
            x4 = (e0*w40) + (salida1*w41) + (salida2*w42) + (salida3*w43)
            salida_real = 1/(1+e**(-x4))
            print("Pesos capa oculta:",w10,w11,w12,w20,w21,w22,w30,w31,w32)
            print("Salida de capa oculta:",salida1,salida2,salida3)


            # error=salida_real-solucion_deseada
            error = solucion_deseada-salida_real

            deltaf = salida_real*(1-salida_real)*error
            # Deltas de la neurona de salida
            dw40 = lr*e0*deltaf
            dw41 = lr*salida1*deltaf
            dw42 = lr*salida2*deltaf
            dw43 = lr*salida3*deltaf
            print("Deltas ultima neurona:")
            print(dw40)
            print(dw41)
            print(dw42)
            print(dw43)
            print("------------")

            # sumar los deltas a los pesos y son los nuevos pesos
            w40 = w40+dw40
            w41 = w41+dw41
            w42 = w42+dw42
            w43 = w43+dw43

            # Deltas de la capa oculta
            delta_co_neurona1 = salida1*(1-salida1)*deltaf
            delta_co_neurona2 = salida2*(1-salida2)*deltaf
            delta_co_neurona3 = salida3*(1-salida3)*deltaf
            print("Pesos ultima neurona:")
            print(w40)
            print(w41)
            print(w42)
            print(w43)
            print("------------")

            # Delta de los pesos de la capa oculta
            dwco10 = lr*e0*delta_co_neurona1
            dwco11 = lr*e1*delta_co_neurona1
            dwco12 = lr*e2*delta_co_neurona1
            dwco20 = lr*e0*delta_co_neurona2
            dwco21 = lr*e1*delta_co_neurona2
            dwco22 = lr*e2*delta_co_neurona2
            dwco30 = lr*e0*delta_co_neurona3
            dwco31 = lr*e1*delta_co_neurona3
            dwco32 = lr*e2*delta_co_neurona3

            #Nuevos pesos de la capa oculta
            w10 = w10+dwco10
            w11 = w11+dwco11
            w12 = w12+dwco12
            w20 = w20+dwco20
            w21 = w21+dwco21
            w22 = w22+dwco22
            w30 = w30+dwco30
            w31 = w31+dwco31
            w32 = w32+dwco32

            print("Nuevos pesos:",w10,w11,w12,w20,w21,w22,w30,w31,w32)


            #Guardamos los valores en listas para graficarlas
            lw10.append(w10)
            lw11.append(w11)
            lw12.append(w12)
            lw20.append(w20)
            lw21.append(w21)
            lw22.append(w22)
            lw30.append(w30)
            lw31.append(w31)
            lw32.append(w32)
            lw40.append(w40)
            lw41.append(w41)
            lw42.append(w42)
            lw43.append(w43)

            print("Salida real:", salida_real)
            print("Salida deseada:", solucion_deseada)
            print("Error:",error)

        l_error.append(-error)

    #Graficamos los pesos y el error
    plt.plot(lw10)
    plt.plot(lw11)
    plt.plot(lw12)
    plt.plot(lw20)
    plt.plot(lw21)
    plt.plot(lw22)
    plt.plot(lw30)
    plt.plot(lw31)
    plt.plot(lw32)
    plt.plot(lw40)
    plt.plot(lw41)
    plt.plot(lw42)
    plt.plot(lw43)
    plt.ylabel('Pesos')
    plt.xlabel('Iteraciones')
    plt.show()

    plt.plot(l_error)
    plt.ylabel('Error')
    plt.xlabel('Iteraciones')
    plt.show()


if __name__ == "__main__":
    #Tabla de la verdad de XOR
    tabla_xor = ['000', '011', '101', '110']

    lr = 0.5
    entrenar_perceptron(tabla_xor, lr)
