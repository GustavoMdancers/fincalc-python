import pytest
from fincalc import calcular_valor_futuro


def test_valor_futuro_aportes_padrao():
    # Arrange & Act (500 + 500*1.01 + 500*1.01^2 = 1515.05)
    vf = calcular_valor_futuro(500.0, 1.0, 3)
    # Assert
    assert round(vf, 2) == 1515.05


def test_valor_futuro_zero_meses():
    # Arrange & Act
    vf = calcular_valor_futuro(500.0, 1.0, 0)
    # Assert
    assert round(vf, 2) == 0.0


def test_valor_futuro_taxa_zero():
    # Arrange & Act
    vf = calcular_valor_futuro(500.0, 0.0, 12)
    # Assert
    assert round(vf, 2) == 6000.00


def test_valor_futuro_aporte_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_valor_futuro(-200.0, 1.0, 12)


def test_valor_futuro_meses_negativos():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_valor_futuro(500.0, 1.0, -5)
