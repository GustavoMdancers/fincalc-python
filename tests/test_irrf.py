import pytest
from fincalc import calcular_irrf


# TC2.1 - Partição Válida (Faixa 2)
def test_irrf_faixa_dois():
    imposto = calcular_irrf(2500.00)
    assert round(imposto, 2) == 18.06


# TC2.2 - Análise de Valor Limite (Isenção)
def test_irrf_limite_isencao():
    imposto = calcular_irrf(2259.20)
    assert round(imposto, 2) == 0.0


# TC2.3 - Partição Inválida (Salário Negativo)
def test_irrf_salario_negativo():
    with pytest.raises(ValueError):
        calcular_irrf(-1000.00)
