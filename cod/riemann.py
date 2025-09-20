import numpy as np
import matplotlib
matplotlib.use("TkAgg")  # Para plotar os gráficos no Linux 
import matplotlib.pyplot as plt

def soma_de_Riemann(funcao, a, b, numRetangulos):
    
    h = (b - a) / numRetangulos
    xMedio = np.linspace(a + h/2, b - h/2, numRetangulos)
    
    soma = 0
    soma = np.sum(funcao(xMedio) * h)
    
    
    #plotar o gráfico 
    x = np.linspace(a, b, 500)
    y = funcao(x)
    plt.plot(x, y, 'b')
        
    for xm in xMedio:
        plt.bar(xm, funcao(xm), width=h, alpha=0.3, edgecolor='r', align='center')
        
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Soma de Riemann (ponto médio)')
    plt.show()
    
    return soma
