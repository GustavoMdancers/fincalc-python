import pytest
from fincalc import calcular_juros_compostos

def test_juros_compostos_valido():
    # Arrange & Act
    resultado = calcular_juros_compostos(1000.0, 5.0, 2)
    # Assert
    assert round(resultado, 2) == 1102.50

def test_juros_compostos_tempo_zero():
    # Arrange & Act
    resultado = calcular_juros_compostos(1000.0, 5.0, 0)
    # Assert
    assert round(resultado, 2) == 1000.00

def test_juros_compostos_capital_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_juros_compostos(-500.0, 5.0, 2)

def test_juros_compostos_tempo_negativo():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        calcular_juros_compostos(1000.0, 5.0, -1)
