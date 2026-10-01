# FinCalc - Sistema de Cálculos Financeiros em Python


def calcular_juros_simples(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros simples."""
    if capital < 0 or anos < 0:
        raise ValueError("Capital e anos devem ser não-negativos.")
    juros = capital * (taxa_anual / 100) * anos
    return capital + juros


def calcular_aposentadoria(
    patrimonio_atual: float, aporte_mensal: float, anos: int, taxa_anual: float
) -> float:
    """Calcula o patrimônio acumulado para aposentadoria."""
    if patrimonio_atual < 0 or aporte_mensal < 0 or anos < 0:
        raise ValueError("Patrimônio, aporte e anos devem ser não-negativos.")
    meses = anos * 12
    taxa_mensal = (taxa_anual / 100) / 12
    saldo = patrimonio_atual
    for _ in range(meses):
        saldo = (saldo + aporte_mensal) * (1 + taxa_mensal)
    return saldo


def calcular_juros_compostos(capital: float, taxa_anual: float, anos: int) -> float:
    """Calcula o montante final obtido por juros compostos."""
    montante = capital * ((1 + (taxa_anual / 100)) ** anos)
    return montante


# Implementação da Feature Cálculo de IRRF - Mateus Mendes Mattos
def calcular_irrf(salario_bruto: float) -> float:
    if salario_bruto <= 2259.20:
        return 0.0
    elif salario_bruto <= 2826.65:
        return (salario_bruto * 0.075) - 169.44
    elif salario_bruto <= 3751.05:
        return (salario_bruto * 0.15) - 381.44
    else:
        return (salario_bruto * 0.225) - 662.77


# Implementação da Feature Cálculo de Valor Futuro - João Paulo Leal Silveira
def calcular_valor_futuro(
    aporte_mensal: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor futuro acumulado com aportes mensais recorrentes."""
    if aporte_mensal < 0 or meses < 0:
        raise ValueError("Aporte mensal e meses não podem ser negativos.")
    if meses == 0:
        return 0.0

    i = taxa_mensal / 100
    if i == 0:
        return aporte_mensal * meses

    vf = aporte_mensal * (((1 + i) ** meses - 1) / i)
    return vf


if __name__ == "__main__":
    print("Iniciando o sistema FinCalc...")
    montante = calcular_juros_simples(1000.0, 5.0, 2)
    print(f"Juros Simples: R$ {montante:.2f}")
    montante_comp = calcular_juros_compostos(1000.0, 5.0, 2)
    print(f"Juros Compostos: R$ {montante_comp:.2f}")
    patrimonio = calcular_aposentadoria(10000.0, 500.0, 20, 6.0)
    print(f"Patrimônio Estimado para Aposentadoria: R$ {patrimonio:.2f}")

    irrf = calcular_irrf(3000.00)
    print(
        "Cálculo da alíquota simplificada de Imposto de Renda Retido na Fonte: "
        f"R$ {irrf:.2f}"
    )

    print("\n--- Teste de Valor Futuro (João Paulo) ---")
    vf = calcular_valor_futuro(500.0, 1.0, 3)
    print(f"Valor Futuro acumulado (R$ 500/mês a 1% por 3 meses): R$ {vf:.2f}")


# Implementação de features de cálculo de Lucro Líquido e Margem e
# Rendimento Real Ajustado - Júlia Suriani
def calcular_lucro_liquido(receita_total, custos_totais, impostos_despesas):
    """Calcula o Lucro Líquido e a Margem Operacional."""
    lucro_liquido = receita_total - custos_totais - impostos_despesas
    margem_operacional = (
        (lucro_liquido / receita_total) * 100 if receita_total > 0 else 0
    )
    return lucro_liquido, margem_operacional


def calcular_rendimento_real(rendimento_nominal_pct, inflacao_pct):
    """Calcula o Rendimento Real Ajustado pela Inflação (Fórmula de Fisher)."""
    i = rendimento_nominal_pct / 100
    j = inflacao_pct / 100
    rendimento_real_pct = ((1 + i) / (1 + j) - 1) * 100
    return rendimento_real_pct


if __name__ == "__main__":
    print("--- Teste de Lucro Líquido e Margem Operacional ---")
    lucro, margem = calcular_lucro_liquido(100000, 60000, 15000)
    print(f"Lucro Líquido: R$ {lucro:.2f}")
    print(f"Margem Operacional: {margem:.2f}%")

    print("\n--- Teste de Rendimento Real Ajustado pela Inflação ---")
    rend_real = calcular_rendimento_real(10.0, 4.5)
    print(f"Rendimento Real Ajustado: {rend_real:.2f}%")


# Implementação da Feature Cálculo de Amortização Price - Func 03 (Luca)
def calcular_parcela_price(
    valor_emprestimo: float, taxa_mensal: float, meses: int
) -> float:
    """Calcula o valor da parcela fixa em um financiamento pela Tabela Price."""
    if valor_emprestimo < 0:
        raise ValueError("O empréstimo não pode ser negativo.")

    if taxa_mensal == 0:
        return valor_emprestimo / meses

    i = taxa_mensal / 100
    numerador = i * ((1 + i) ** meses)
    denominador = ((1 + i) ** meses) - 1
    return valor_emprestimo * (numerador / denominador)


# Implementação da Feature Cálculo de Depreciação Linear - Func 05 (Luca)
def calcular_depreciacao_linear(
    valor_inicial: float, valor_residual: float, vida_util_anos: int
) -> float:
    """Calcula o valor de depreciação anual de um ativo corporativo."""
    if vida_util_anos <= 0:
        raise ValueError("A vida útil não pode ser zero ou negativa.")

    if valor_residual > valor_inicial:
        raise ValueError("O valor residual não pode ser maior que o inicial.")

    return (valor_inicial - valor_residual) / vida_util_anos


# Bloco para testar manualmente as suas funções
if __name__ == "__main__":
    print("\n--- Teste Tabela Price (Func 03) ---")
    parcela_price = calcular_parcela_price(10000.0, 1.5, 12)
    print(f"Parcela Tabela Price: R$ {parcela_price:.2f}")

    print("\n--- Teste Depreciação Linear (Func 05) ---")
    depreciacao = calcular_depreciacao_linear(50000.0, 5000.0, 5)
    print(f"Depreciação Linear Anual: R$ {depreciacao:.2f}")
