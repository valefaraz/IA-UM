import random
from math import e


def entrenar_perceptron(tabla, lr):

    # primer capa
    w10, w11, w12 = 1, 0.7, 0.5
    w20, w21, w22 = 0.3, -0.9, -1

    # segunda capa
    w30, w31, w32 = 0.8, 0.35, 0.1
    w40, w41, w42 = -0.23, -0.79, 0.56
    w50, w51, w52 = 0.6, -0.6, 0.22

    # tercer capa
    w60, w61, w62, w63 = -0.22, -0.55, 0.31, -0.32

    combinacion = '000'
    print("Fila de la tabla de la verdad:", combinacion)
    solucion_deseada = int(combinacion[2])
    # entradas iniciales
    e0 = 1
    e1 = int(combinacion[0])
    e2 = int(combinacion[1])
    # x es sumatoria de cada peso por su entrada
    # salida de la neurona 1 capa1
    x1 = (e0*w10) + (e1*w11) + (e2*w12)
    salida1 = round(1/(1+e**(-x1)), 4)
    # salida de la neurona 2 capa1
    x2 = (e0*w20) + (e1*w21) + (e2*w22)
    salida2 = round(1/(1+e**(-x2)), 4)
    # salida de la neurona 3 capa 2
    x3 = (e0*w30) + (salida1*w31) + (salida2*w32)
    salida3 = round(1/(1+e**(-x3)), 4)
    # salida de la neurona 4 capa 2
    x4 = (e0*w40) + (salida1*w41) + (salida2*w42)
    salida4 = round(1/(1+e**(-x4)), 4)
    # salida de la neurona 5 capa 2
    x5 = (e0*w50) + (salida1*w51) + (salida2*w52)
    salida5 = round(1/(1+e**(-x5)), 4)
    # salida de la neurona 6 capa 3
    x6 = (e0*w60) + (salida3*w61) + (salida4*w62) + (salida5*w63)
    salida6 = round(1/(1+e**(-x6)), 4)
    print("Salida real:", salida6)
    print("Salida deseada:",solucion_deseada)


if __name__ == "__main__":
    tabla_xor = ['000', '011', '101', '110']

    lr = 0.1
    entrenar_perceptron(tabla_xor, lr)
