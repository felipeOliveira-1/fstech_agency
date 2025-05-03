# Ferramenta: Analisador de Período de Payback

import numpy as np
from datetime import datetime

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def analyze_payback_period(initial_investment: float, monthly_benefits: float, consider_time_value: bool = True, discount_rate: float = 0.08) -> dict:
    """Analisa o período de payback (tempo de retorno do investimento) de um projeto.
    
    Args:
        initial_investment: Investimento inicial do projeto.
        monthly_benefits: Benefícios financeiros mensais estimados.
        consider_time_value: Se deve considerar o valor do dinheiro no tempo.
        discount_rate: Taxa de desconto anual (se consider_time_value=True).
        
    Returns:
        Um dicionário com análise detalhada do período de payback e fluxo de caixa.
    """
    if initial_investment <= 0:
        return {"error": "O investimento inicial deve ser maior que zero."}
    
    if monthly_benefits <= 0:
        return {"error": "Os benefícios mensais devem ser maiores que zero."}
    
    # Converter taxa anual para mensal
    monthly_discount_rate = (1 + discount_rate) ** (1/12) - 1 if consider_time_value else 0
    
    # Calcular payback simples (sem valor do dinheiro no tempo)
    simple_payback_months = initial_investment / monthly_benefits
    simple_payback_years = simple_payback_months / 12
    
    # Calcular payback descontado (com valor do dinheiro no tempo)
    if consider_time_value:
        cumulative_present_value = 0
        discounted_payback_months = 0
        
        # Calcular até atingir o valor do investimento inicial
        while cumulative_present_value < initial_investment:
            discounted_payback_months += 1
            month_present_value = monthly_benefits / ((1 + monthly_discount_rate) ** discounted_payback_months)
            cumulative_present_value += month_present_value
            
            # Limite de segurança para evitar loop infinito
            if discounted_payback_months > 1000:
                discounted_payback_months = float('inf')
                break
        
        discounted_payback_years = discounted_payback_months / 12
    else:
        discounted_payback_months = simple_payback_months
        discounted_payback_years = simple_payback_years
    
    # Gerar fluxo de caixa para visualização
    cash_flow = []
    cumulative_cash = -initial_investment
    cumulative_discounted = -initial_investment
    
    # Estender por pelo menos 6 meses além do período de payback
    analysis_months = max(36, int(discounted_payback_months) + 6)
    
    for month in range(1, analysis_months + 1):
        if consider_time_value:
            month_present_value = monthly_benefits / ((1 + monthly_discount_rate) ** month)
        else:
            month_present_value = monthly_benefits
        
        cumulative_cash += monthly_benefits
        cumulative_discounted += month_present_value
        
        cash_flow.append({
            "month": month,
            "nominal_benefit": monthly_benefits,
            "discounted_benefit": month_present_value,
            "cumulative_nominal": cumulative_cash,
            "cumulative_discounted": cumulative_discounted
        })
    
    # Formar resultado
    effective_payback = discounted_payback_months if consider_time_value else simple_payback_months
    effective_payback_years = effective_payback / 12
    
    # Avaliar a qualidade do período de payback
    payback_assessment = ""
    if effective_payback_years < 1:
        payback_assessment = "Excelente"
    elif effective_payback_years < 2:
        payback_assessment = "Muito bom"
    elif effective_payback_years < 3:
        payback_assessment = "Bom"
    elif effective_payback_years < 5:
        payback_assessment = "Razoável"
    else:
        payback_assessment = "Longo prazo"
    
    result = {
        "simple_payback_months": round(simple_payback_months, 1),
        "simple_payback_years": round(simple_payback_years, 2),
        "discounted_payback_months": round(discounted_payback_months, 1) if discounted_payback_months != float('inf') else "N/A",
        "discounted_payback_years": round(discounted_payback_years, 2) if discounted_payback_years != float('inf') else "N/A",
        "effective_payback_months": round(effective_payback, 1) if effective_payback != float('inf') else "N/A",
        "effective_payback_years": round(effective_payback_years, 2) if effective_payback_years != float('inf') else "N/A",
        "payback_assessment": payback_assessment,
        "considered_time_value": consider_time_value,
        "annual_discount_rate": discount_rate if consider_time_value else 0,
        "monthly_discount_rate": monthly_discount_rate,
        "cash_flow": cash_flow[:12],  # Limitar para os primeiros 12 meses no resultado
        "analysis_date": datetime.now().strftime("%d/%m/%Y")
    }
    
    # Formatar alguns valores para exibição
    def format_currency(value):
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    # Adicionar valores formatados
    result["formatted"] = {
        "initial_investment": format_currency(initial_investment),
        "monthly_benefits": format_currency(monthly_benefits),
        "annual_benefits": format_currency(monthly_benefits * 12),
    }
    
    # Adicionar resumo textual
    result["summary"] = f"Com um investimento inicial de {result['formatted']['initial_investment']} e benefícios mensais de " \
                       f"{result['formatted']['monthly_benefits']}, o período de payback é de aproximadamente " \
                       f"{result['effective_payback_months']} meses ({result['effective_payback_years']} anos). " \
                       f"Esta é uma taxa de retorno {result['payback_assessment'].lower()}."
    
    return result

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Projeto com payback rápido
    result1 = analyze_payback_period(
        initial_investment=100000,
        monthly_benefits=15000,
        consider_time_value=True,
        discount_rate=0.08
    )
    
    print("=== Análise de Payback: Projeto 1 ===")
    print(result1["summary"])
    print(f"Payback simples: {result1['simple_payback_months']} meses")
    print(f"Payback descontado: {result1['discounted_payback_months']} meses")
    print(f"Avaliação: {result1['payback_assessment']}")
    
    # Exemplo 2: Projeto com payback mais longo
    result2 = analyze_payback_period(
        initial_investment=500000,
        monthly_benefits=12000,
        consider_time_value=True,
        discount_rate=0.1
    )
    
    print("\n=== Análise de Payback: Projeto 2 ===")
    print(result2["summary"])
    print(f"Payback simples: {result2['simple_payback_months']} meses")
    print(f"Payback descontado: {result2['discounted_payback_months']} meses")
    print(f"Avaliação: {result2['payback_assessment']}")
