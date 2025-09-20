import numpy as np
import pytest
from riemann import soma_de_Riemann 

tolerancia = 1e-3

# f(x) = cos(x^2) no intervalo [0, 1] ≈ 0.904524
def test_funcao_cos_x2():
    f = lambda x: np.cos(x**2)
    resultado = soma_de_Riemann(f, 0, 1, 20000)
    esperado = 0.9045242379
    assert np.isclose(resultado, esperado, atol=tolerancia)

# f(x) = ln(x+1) no intervalo [0, 1] = (2*ln(2) - 1) ≈ 0.386294
def test_funcao_log():
    f = lambda x: np.log(x+1)
    resultado = soma_de_Riemann(f, 0, 1, 20000)
    esperado = 2*np.log(2) - 1
    assert np.isclose(resultado, esperado, atol=tolerancia)

# f(x) = sqrt(1 - x^2) no intervalo [0, 1] π/4 ≈ 0.785398
def test_funcao_semicirculo():
    f = lambda x: np.sqrt(1 - x**2)
    resultado = soma_de_Riemann(f, 0, 1, 20000)
    esperado = np.pi / 4
    assert np.isclose(resultado, esperado, atol=tolerancia)

# f(x) = 1/(1+x^2) no intervalo [0, 1] = π/4 ≈ 0.785398
def test_funcao_racional():
    f = lambda x: 1/(1 + x**2)
    resultado = soma_de_Riemann(f, 0, 1, 20000)
    esperado = np.pi / 4
    assert np.isclose(resultado, esperado, atol=tolerancia)

# f(x) = e^(-x^2) no intervalo [0, 1] ≈ 0.746824
def test_funcao_gaussiana():
    f = lambda x: np.exp(-x**2)
    resultado = soma_de_Riemann(f, 0, 1, 20000)
    esperado = 0.7468241328
    assert np.isclose(resultado, esperado, atol=tolerancia)
