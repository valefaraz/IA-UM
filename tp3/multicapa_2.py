from math import e
from time import process_time_ns


def entrenar_perceptron(tabla, lr):

    #Capa oculta
    w10, w11, w12 = 0.9, 0.7, 0.5
    w20, w21, w22 = 0.3, -0.9, -1
    w30, w31, w32 = 0.8, 0.35, 0.1

    # Ultima Neurona
    w40, w41, w42, w43 = -0.23, -0.79, 0.56, 0.6

    combinacion = '000'
    

    print("Fila de la tabla de la verdad:", combinacion)
    solucion_deseada = int(combinacion[2])
    # entradas iniciales
    e0 = 1
    e1 = int(combinacion[0])
    e2 = int(combinacion[1])
    # x es sumatoria de cada peso por su entrada
    
    # salida de la neurona 1 capa oculta
    x1 = (e0*w10) + (e1*w11) + (e2*w12)
    salida1 = round(1/(1+e**(-x1)), 4)
    print(salida1)
    # salida de la neurona 2 capa oculta
    x2 = (e0*w20) + (e1*w21) + (e2*w22)
    salida2 = round(1/(1+e**(-x2)), 4)
    print(salida2)
    # salida de la neurona 3 capa oculta
    x3 = (e0*w30) + (e1*w31) + (e2*w32)
    salida3 = round(1/(1+e**(-x3)), 4)
    print(salida3)

    # salida de la ultima neurona
    x4 = (e0*w40) + (salida1*w41) + (salida2*w42) + (salida3*w43)
    print(x4)

    salida6 = round(1/(1+e**(-x4)), 4)
    salida_real=salida6
    print("Salida real:", salida6)
    print("Salida deseada:",solucion_deseada)
    error=solucion_deseada-salida_real
    deltaf=salida_real*(1-salida_real)*error
    dw9=lr*e0*deltaf
    dw10=lr*salida1*deltaf
    dw11=lr*salida2*deltaf
    dw12=lr*salida3*deltaf
    print("Deltaf:",deltaf)
    print("dw9:",dw9)
    print("dw10:",dw10)
    print("dw11:",dw11)
    print("dw12:",dw12)
    #sumar los deltas a los pesos y son los nuevos pesos
    #w0

if __name__ == "__main__":
    tabla_xor = ['000', '011', '101', '110']

    lr = 0.1
    entrenar_perceptron(tabla_xor, lr)




"""BackPropagation
error=salidadeseada-salidareal
deltafinal=salidareal*(1-salidareal)*error
dw=lr*entrada*deltafinal

w1=w1+dw1


"""