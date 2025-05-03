# Ferramenta: Estimador de Redução de Custos

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def estimate_cost_reduction(current_costs: dict, solution_impact: dict, time_horizon_months: int = 12) -> dict:
    """Estima a redução de custos potencial proporcionada pela solução proposta.
    
    Args:
        current_costs: Dicionário com as categorias de custos atuais e seus valores mensais.
        solution_impact: Dicionário com o impacto percentual da solução em cada categoria de custo.
        time_horizon_months: Horizonte de tempo em meses para a projeção.
        
    Returns:
        Um dicionário com análise detalhada da economia de custos projetada.
    """
    if not current_costs:
        # Fornecer um template com categorias comuns se não fornecido
        current_costs = {
            "personal": 0,  # Custos com pessoal
            "infrastructure": 0,  # Infraestrutura de TI/operações
            "licenses": 0,  # Licenças de software
            "maintenance": 0,  # Manutenção de sistemas
            "operational": 0,  # Custos operacionais diversos
            "errors": 0,  # Custo de erros e retrabalho
            "compliance": 0  # Custos de conformidade regulatória
        }
    
    if not solution_impact:
        # Estimativas conservadoras de impacto se não fornecido
        solution_impact = {
            "personal": 0.10,  # 10% redução em custos de pessoal
            "infrastructure": 0.15,  # 15% redução em infraestrutura
            "licenses": 0.05,  # 5% redução em licenças
            "maintenance": 0.20,  # 20% redução em manutenção
            "operational": 0.10,  # 10% redução em custos operacionais
            "errors": 0.25,  # 25% redução em custos de erros
            "compliance": 0.15  # 15% redução em custos de compliance
        }
    
    # Iniciar cálculos
    savings_monthly = {}
    total_current_monthly = 0
    total_savings_monthly = 0
    
    # Calcular economia por categoria
    for category, monthly_cost in current_costs.items():
        impact_percentage = solution_impact.get(category, 0)
        savings = monthly_cost * impact_percentage
        
        savings_monthly[category] = {
            "current_cost": monthly_cost,
            "impact_percentage": impact_percentage * 100,  # Converter para exibição percentual
            "monthly_savings": savings,
            "annual_savings": savings * 12
        }
        
        total_current_monthly += monthly_cost
        total_savings_monthly += savings
    
    # Calcular projeção ao longo do tempo
    monthly_projection = []
    cumulative_savings = 0
    
    for month in range(1, time_horizon_months + 1):
        # Simular aumento gradual da economia (ramp-up period)
        ramp_up_factor = min(1.0, month / 3)  # Atingir 100% de economia após 3 meses
        month_savings = total_savings_monthly * ramp_up_factor
        cumulative_savings += month_savings
        
        monthly_projection.append({
            "month": month,
            "savings": month_savings,
            "cumulative_savings": cumulative_savings
        })
    
    # Formar resultado
    result = {
        "total_current_monthly_cost": total_current_monthly,
        "total_monthly_savings": total_savings_monthly,
        "total_annual_savings": total_savings_monthly * 12,
        "savings_percentage": (total_savings_monthly / total_current_monthly * 100) if total_current_monthly > 0 else 0,
        "detailed_savings": savings_monthly,
        "monthly_projection": monthly_projection,
        "cumulative_savings_total": cumulative_savings,
        "top_savings_categories": []
    }
    
    # Identificar categorias com maior economia
    sorted_categories = sorted(
        [(category, details["monthly_savings"]) for category, details in savings_monthly.items()],
        key=lambda x: x[1],
        reverse=True
    )
    
    result["top_savings_categories"] = [category for category, _ in sorted_categories[:3] if _ > 0]
    
    # Formatar valores monetários para exibição
    def format_currency(value):
        return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    result["formatted"] = {
        "total_current_monthly_cost": format_currency(total_current_monthly),
        "total_monthly_savings": format_currency(total_savings_monthly),
        "total_annual_savings": format_currency(total_savings_monthly * 12),
        "cumulative_savings_total": format_currency(cumulative_savings)
    }
    
    # Adicionar resumo textual
    result["summary"] = f"A solução proposta pode gerar uma economia mensal de {result['formatted']['total_monthly_savings']} " \
                        f"({result['savings_percentage']:.1f}% dos custos atuais), " \
                        f"totalizando {result['formatted']['total_annual_savings']} por ano. " \
                        f"Em {time_horizon_months} meses, a economia acumulada será de {result['formatted']['cumulative_savings_total']}."
    
    return result

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo: Projeto de automação de processos
    current_costs_example = {
        "personal": 100000,  # R$ 100.000/mês em pessoal
        "infrastructure": 20000,  # R$ 20.000/mês em infraestrutura
        "licenses": 15000,  # R$ 15.000/mês em licenças de software
        "maintenance": 25000,  # R$ 25.000/mês em manutenção
        "operational": 30000,  # R$ 30.000/mês em custos operacionais
        "errors": 10000,  # R$ 10.000/mês em correção de erros
        "compliance": 5000   # R$ 5.000/mês em compliance
    }
    
    solution_impact_example = {
        "personal": 0.20,  # Redução de 20% em custos de pessoal
        "infrastructure": 0.15,  # Redução de 15% em infraestrutura
        "licenses": 0.05,  # Redução de 5% em licenças
        "maintenance": 0.25,  # Redução de 25% em manutenção
        "operational": 0.10,  # Redução de 10% em custos operacionais
        "errors": 0.30,  # Redução de 30% em custos de erros
        "compliance": 0.20   # Redução de 20% em custos de compliance
    }
    
    result = estimate_cost_reduction(
        current_costs=current_costs_example,
        solution_impact=solution_impact_example,
        time_horizon_months=24
    )
    
    print("=== Análise de Redução de Custos ===")
    print(result["summary"])
    print("\nTop 3 categorias com maior economia:")
    
    for category in result["top_savings_categories"]:
        monthly_savings = result["detailed_savings"][category]["monthly_savings"]
        impact = result["detailed_savings"][category]["impact_percentage"]
        print(f"- {category.capitalize()}: {format_currency(monthly_savings)}/mês ({impact:.1f}% de redução)")
    
    print("\nProjeção de economia (primeiros 6 meses):")
    for month in result["monthly_projection"][:6]:
        print(f"Mês {month['month']}: {format_currency(month['cumulative_savings'])} acumulado")

def format_currency(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
