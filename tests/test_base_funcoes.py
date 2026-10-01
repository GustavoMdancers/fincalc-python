import sys
from unittest.mock import patch
import pytest
import fincalc


def test_juros_simples_valido():
    assert round(fincalc.calcular_juros_simples(1000.0, 5.0, 2), 2) == 1100.00


def test_juros_simples_capital_negativo():
    with pytest.raises(ValueError):
        fincalc.calcular_juros_simples(-1000.0, 5.0, 2)


def test_juros_simples_anos_negativos():
    with pytest.raises(ValueError):
        fincalc.calcular_juros_simples(1000.0, 5.0, -2)


def test_aposentadoria_valida():
    res = fincalc.calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    assert round(res, 2) == 265277.59


def test_aposentadoria_aporte_negativo():
    with pytest.raises(ValueError):
        fincalc.calcular_aposentadoria(10000.0, -500.0, 20, 6.0)


def test_aposentadoria_patrimonio_negativo():
    with pytest.raises(ValueError):
        fincalc.calcular_aposentadoria(-10000.0, 500.0, 20, 6.0)


def test_aposentadoria_anos_negativos():
    with pytest.raises(ValueError):
        fincalc.calcular_aposentadoria(10000.0, 500.0, -20, 6.0)


def test_irrf_faixas():
    assert fincalc.calcular_irrf(2000.0) == 0.0
    assert round(fincalc.calcular_irrf(2500.0), 2) == 18.06
    assert round(fincalc.calcular_irrf(3000.0), 2) == 68.56
    assert round(fincalc.calcular_irrf(4000.0), 2) == 237.23


def test_lucro_liquido_e_rendimento_real():
    lucro, margem = fincalc.calcular_lucro_liquido(100000, 60000, 15000)
    assert lucro == 25000
    assert margem == 25.0

    _, margem_zero = fincalc.calcular_lucro_liquido(0, 0, 0)
    assert margem_zero == 0

    rend_real = fincalc.calcular_rendimento_real(10.0, 4.5)
    assert round(rend_real, 2) == 5.26


def test_cobertura_script_main():
    # Garante que o bloco __main__ do fincalc.py seja executado e medido pelo coverage
    with patch.object(sys, 'argv', ['fincalc.py']):
        with open("fincalc.py", "r", encoding="utf-8") as f:
            code = compile(f.read(), "fincalc.py", "exec")
            exec(code, {"__name__": "__main__"})
