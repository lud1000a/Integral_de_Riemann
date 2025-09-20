import numpy as np
import riemann

funcoes = [
    (lambda x: x**3 - 2*x + 1, 0, 2),             # Polinômio
    (np.sin, 0, np.pi),                           # Seno
    (np.cos, 0, np.pi/2),                         # Cosseno
    (np.tan, 0, np.pi/4),                         # Tangente
    (np.exp, 0, 2),                               # Exponencial
    (np.log, 1, 10),                              # Logaritmo natural
    (np.sqrt, 0, 4),                              # Raiz quadrada
    (lambda x: x**2 + np.sin(x), 0, 2),          # Soma
    (lambda x: np.exp(x) - np.sqrt(x), 0, 4),    # Diferença
    (lambda x: x * np.log(x), 1, 3),             # Produto
    (lambda x: np.sin(x)/x, 0.1, 2),             # Quociente (evitando x=0)
    (lambda x: np.log(1 + x**2), 0, 2),          # Composição 1
    (lambda x: np.sqrt(np.exp(x) - 1), 0, 2)     # Composição 2
]

for f, a, b in funcoes:
    print(riemann.soma_de_Riemann(f, a, b, 50))


