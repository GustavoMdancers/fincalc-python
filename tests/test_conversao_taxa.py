import pytest
from fincalc import converter_taxa_anual_para_mensal


def test_conversao_taxa_positiva():
    # Arrange & Act
    taxa_m = converter_taxa_anual_para_mensal(12.6825)
    # Assert
    assert round(taxa_m, 4) == 1.0000


def test_conversao_taxa_nula():
    # Arrange & Act
    taxa_m = converter_taxa_anual_para_mensal(0.0)
    # Assert
    assert round(taxa_m, 4) == 0.0


def test_conversao_taxa_abaixo_menos_cem():
    # Arrange, Act & Assert
    with pytest.raises(ValueError):
        converter_taxa_anual_para_mensal(-150.0)
