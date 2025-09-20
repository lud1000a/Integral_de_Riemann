import numpy as np

def soma_de_Riemann(a, b, numRetangulos):
    
    def funcao(x):
        return x**2
    
    h = (b-a)/numRetangulos
    
    # x0 = a, x1 = a+h, x2 = a+2b ..., xn= b 
    
    indices = []
    for i in range(numRetangulos+1): 
        indices.append(a + i * h)
    
    soma = 0 
    
    for i in range(numRetangulos):
        B = indices[i+1] - indices[i]
        H = funcao((indices[i] + indices[i+1])/2)#funcao aplicada no ponto (indices[i] + indices[i+1])/2 pq escolhi o ponto medio 

        area = B*H
        soma += area
        
    return soma; 

print(soma_de_Riemann(0, 1, 30))
    
