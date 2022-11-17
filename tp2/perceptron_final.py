import random
from math import e
import numpy as np
import matplotlib.pyplot as plt
 
 
def entrenar_perceptron(tabla,lr):
   #pessos iniciales ramdon
   #w0= round(random.uniform(-1,1),4)
   #w1= round(random.uniform(-1,1),4)
   #w2= round(random.uniform(-1,1),4)

   w0= 0.9
   w1= 0.66
   w2= -0.2
   lista_w0=[]
   lista_w1=[]
   lista_w2=[]
   iteraciones=[]
   lista_e=[]
   i=0
   print(w0,w1,w2)
   while True:
       iteraciones.append(i)

       i=i+1
       lista_w0.append(w0)
       lista_w1.append(w1)
       lista_w2.append(w2)
       for combinacion in tabla:
           print("Fila de la tabla de la verdad:",combinacion)
           solucion_deseada=int(combinacion[2])
           #entradas
           e0=1
           e1=int(combinacion[0])
           e2=int(combinacion[1])
           #sumatoria de cada peso por su entrada
           x= (e1*w1) + (e2*w2) + (e0*w0)
           print(x)

           solucion_real = round(1/(1+e**(-x)),4)
           
           error=solucion_deseada-solucion_real
           #delta
           s=solucion_real*(1-solucion_real)*error
 
           deltaw0=lr*e0*s
           w0=w0+deltaw0
 
           deltaw1=lr*e1*s
           w1=w1+deltaw1
 
           deltaw2=lr*e2*s
           w2=w2+deltaw2
           print('Vuelta numero',i)
           print("pesos:",w0,w1,w2)
           print("Delta:",s)
           print('Solucion Real:',solucion_real)
           print('Solucion Deseada:',solucion_deseada)
           print('Error:',error)
           print('-----------')
 
       lista_e.append(error)
       if i==1000:
       #if error < 0.1:
            #print(lista_w0)
            #print(iteraciones)

            plt.plot (lista_w0)
            plt.plot (lista_w1)
            plt.plot (lista_w2)
            plt.ylabel ('W0-W1-W2')
            plt.xlabel ('Iteraciones')



            #plt.plot (w1,iteraciones)
            #plt.plot (w2,iteraciones)
            plt.show()
            plt.plot (lista_e)
            plt.ylabel ('Error')
            plt.xlabel ('Iteraciones')
            plt.show()
            
            break



 
if __name__ == "__main__":
 
   tabla_or=['000','011','101','111']
   tabla_and=['000','010','100','111']
   tabla_xor=['000','011','101','110']
 
   lr=0.1
  
   #entrenar_perceptron(tabla_or,lr)
 
   #entrenar_perceptron(tabla_and,lr)
 
   entrenar_perceptron(tabla_xor,lr)