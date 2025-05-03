# Ferramenta: Projeção de Benefícios Financeiros

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def project_benefits(business_problem: str, solution_description: str, industry: str = "Tecnologia", company_size: str = "Média") -> dict:
    """Projeta os benefícios financeiros esperados com base no problema de negócio e solução proposta.
    
    Args:
        business_problem: Descrição do problema de negócio que está sendo resolvido.
        solution_description: Descrição da solução técnica proposta.
        industry: Setor da indústria do cliente (ex: Tecnologia, Varejo, Saúde).
        company_size: Tamanho da empresa (Pequena, Média, Grande, Enterprise).
        
    Returns:
        Um dicionário com categorias de benefícios projetados e suas estimativas.
    """
    # Análise simplificada baseada em palavras-chave
    problem_lower = business_problem.lower()
    solution_lower = solution_description.lower()
    
    # Benefícios padrão por tipo
    benefits = {
        "cost_reduction": {
            "value": 0,
            "description": "",
            "confidence": "Média"
        },
        "productivity_gain": {
            "value": 0,
            "description": "",
            "confidence": "Média"
        },
        "revenue_increase": {
            "value": 0,
            "description": "",
            "confidence": "Baixa"
        },
        "risk_mitigation": {
            "value": 0,
            "description": "",
            "confidence": "Média"
        }
    }
    
    # Analisar problema de negócio para identificar oportunidades
    if any(word in problem_lower for word in ["ineficiência", "lento", "demorado", "manual"]):
        benefits["productivity_gain"]["value"] = 20
        benefits["productivity_gain"]["description"] = "Aumento de produtividade pela eliminação de tarefas manuais e processos ineficientes"
        benefits["productivity_gain"]["confidence"] = "Alta"
    
    if any(word in problem_lower for word in ["custo", "despesa", "recurso", "desperdício"]):
        benefits["cost_reduction"]["value"] = 15
        benefits["cost_reduction"]["description"] = "Redução de custos operacionais pela otimização de recursos"
        benefits["cost_reduction"]["confidence"] = "Alta"
    
    if any(word in problem_lower for word in ["venda", "cliente", "conversão", "receita"]):
        benefits["revenue_increase"]["value"] = 10
        benefits["revenue_increase"]["description"] = "Aumento de receita por melhor experiência do cliente ou eficiência de vendas"
        benefits["revenue_increase"]["confidence"] = "Média"
    
    if any(word in problem_lower for word in ["erro", "falha", "segurança", "compliance", "regulação"]):
        benefits["risk_mitigation"]["value"] = 12
        benefits["risk_mitigation"]["description"] = "Mitigação de riscos operacionais, regulatórios ou de segurança"
        benefits["risk_mitigation"]["confidence"] = "Alta"
    
    # Analisar solução técnica
    if any(word in solution_lower for word in ["automação", "automático", "workflow"]):
        benefits["productivity_gain"]["value"] += 10
        if benefits["productivity_gain"]["description"]:
            benefits["productivity_gain"]["description"] += " através de automação de processos"
        else:
            benefits["productivity_gain"]["description"] = "Ganhos de produtividade através de automação de processos"
    
    if any(word in solution_lower for word in ["inteligência artificial", "ia", "machine learning", "ml"]):
        benefits["productivity_gain"]["value"] += 15
        benefits["cost_reduction"]["value"] += 10
        if "ai_optimization" not in benefits:
            benefits["ai_optimization"] = {
                "value": 18,
                "description": "Otimização de processos através de inteligência artificial",
                "confidence": "Média"
            }
    
    if any(word in solution_lower for word in ["dashboard", "análise", "relatório", "indicador"]):
        benefits["decision_making"] = {
            "value": 15,
            "description": "Melhoria na tomada de decisão através de insights baseados em dados",
            "confidence": "Média"
        }
    
    # Ajustar com base na indústria
    industry_multipliers = {
        "Tecnologia": 1.0,
        "Finanças": 1.2,
        "Saúde": 1.1,
        "Varejo": 0.9,
        "Manufatura": 1.05,
        "Serviços": 0.95
    }
    
    multiplier = industry_multipliers.get(industry, 1.0)
    
    # Ajustar com base no tamanho da empresa
    size_scale = {
        "Pequena": 0.7,
        "Média": 1.0,
        "Grande": 1.5,
        "Enterprise": 2.5
    }
    
    scale = size_scale.get(company_size, 1.0)
    
    # Aplicar ajustes e converter percentuais em valores monetários estimados
    base_revenue = {
        "Pequena": 2000000,
        "Média": 10000000,
        "Grande": 50000000,
        "Enterprise": 200000000
    }.get(company_size, 10000000)
    
    # Calcular projeções monetizadas
    result = {
        "percentage_benefits": {},
        "monetary_benefits": {},
        "annual_projection": {},
        "benefits_summary": "",
        "highest_benefit_categories": []
    }
    
    # Ordenar benefícios por valor para identificar os mais significativos
    benefit_items = list(benefits.items())
    benefit_items.sort(key=lambda x: x[1]["value"], reverse=True)
    
    for category, details in benefit_items:
        # Ajustar percentual pela indústria e tamanho
        adjusted_percentage = details["value"] * multiplier / 100  # Converter para decimal
        
        if adjusted_percentage > 0:
            # Estimar valores monetários baseados no tamanho da empresa
            monetary_value = base_revenue * adjusted_percentage * scale
            
            # Armazenar no resultado
            result["percentage_benefits"][category] = f"{adjusted_percentage*100:.1f}%"
            result["monetary_benefits"][category] = f"R$ {monetary_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            
            # Projeção para 3 anos (crescente em cada ano)
            result["annual_projection"][category] = {
                "year_1": f"R$ {monetary_value:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                "year_2": f"R$ {monetary_value*1.2:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."),
                "year_3": f"R$ {monetary_value*1.3:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            }
    
    # Identificar as principais categorias de benefício
    result["highest_benefit_categories"] = [category for category, _ in benefit_items[:2]]
    
    # Gerar resumo dos benefícios
    top_categories = [f"{benefits[category]['description']}" for category in result["highest_benefit_categories"] if category in benefits]
    result["benefits_summary"] = "Principais benefícios financeiros projetados: " + "; ".join(top_categories) + "."
    
    # Calcular benefício total estimado em 3 anos
    total_benefit = 0
    for category, details in benefits.items():
        adjusted_percentage = details["value"] * multiplier / 100
        if adjusted_percentage > 0:
            monetary_value = base_revenue * adjusted_percentage * scale
            total_benefit += monetary_value * (1 + 1.2 + 1.3)  # Soma dos 3 anos
    
    # Formatar valor total
    result["total_projected_benefit_3_years"] = f"R$ {total_benefit:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    
    return result

# Exemplo de uso
if __name__ == "__main__":
    result = project_benefits(
        business_problem="Estamos gastando muito tempo com processos manuais de aprovação, o que causa atrasos e erros frequentes.",
        solution_description="Sistema automatizado de workflow com dashboard para acompanhamento e integração com nossos sistemas legados.",
        industry="Finanças",
        company_size="Grande"
    )
    
    print("=== Projeção de Benefícios ===")
    print(f"Resumo: {result['benefits_summary']}")
    print("\nPrincipais categorias de benefício:")
    for category in result["highest_benefit_categories"]:
        print(f"- {category}: {result['percentage_benefits'].get(category, '0%')}")
    
    print("\nProjeção anual (top categoria):")
    top_category = result["highest_benefit_categories"][0]
    for year, value in result["annual_projection"].get(top_category, {}).items():
        print(f"  {year}: {value}")
    
    print(f"\nBenefício total projetado (3 anos): {result['total_projected_benefit_3_years']}")
