import pytest
from fincalc import calcular_parcela_price

def test_price_financiamento_padrao():
    parcela = calcular_parcela_price(10000.0, 1.5, 12)
    assert round(parcela, 2) == 916.80

def test_price_taxa_zero():
    parcela = calcular_parcela_price(12000.0, 0.0, 12)
    assert round(parcela, 2) == 1000.00

def test_price_emprestimo_negativo():
    with pytest.raises(ValueError):
        calcular_parcela_price(-5000.0, 1.5, 12)