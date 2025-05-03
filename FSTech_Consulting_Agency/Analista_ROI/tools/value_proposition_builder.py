# Ferramenta: Construtor de Proposta de Valor

from datetime import datetime

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def build_value_proposition(client_pain_points: list, solution_benefits: list, target_stakeholders: list = ["Técnico", "Financeiro", "Executivo"]) -> dict:
    """Constrói uma proposta de valor persuasiva baseada nos pontos de dor do cliente e benefícios da solução.
    
    Args:
        client_pain_points: Lista de pontos de dor/problemas do cliente.
        solution_benefits: Lista de benefícios/vantagens da solução proposta.
        target_stakeholders: Tipos de stakeholders a considerar (Técnico, Financeiro, Executivo).
        
    Returns:
        Um dicionário contendo propostas de valor adaptadas para diferentes stakeholders.
    """
    if not client_pain_points:
        client_pain_points = [
            "Processo manual ineficiente",
            "Altos custos operacionais",
            "Dificuldade em escalar operações",
            "Falta de visibilidade em tempo real"
        ]
    
    if not solution_benefits:
        solution_benefits = [
            "Automação de processos manuais",
            "Redução de custos operacionais",
            "Escalabilidade da solução",
            "Dashboards em tempo real",
            "Melhoria na experiência do cliente"
        ]
    
    # Dicionário de mensagens específicas por tipo de stakeholder
    stakeholder_focus = {
        "Técnico": {
            "value_themes": ["eficiência", "precisão", "robustez", "escalabilidade", "integração", "manutenção"],
            "key_metrics": ["tempo de processamento", "taxa de erro", "disponibilidade do sistema", "capacidade de resposta"],
            "pain_amplifiers": ["complexidade técnica", "falhas recorrentes", "dívida técnica", "limitações de sistemas"],
            "benefit_enhancers": ["arquitetura moderna", "tecnologia avançada", "código limpo", "automação de testes"],
            "value_statement_template": "Nossa solução {key_benefit} através de {key_technology}, eliminando {main_pain} e permitindo {future_advantage}."
        },
        "Financeiro": {
            "value_themes": ["ROI", "economia", "eficiência de custos", "controle orçamentário", "previsibilidade financeira"],
            "key_metrics": ["payback", "economia mensal", "redução de despesas", "margem de contribuição"],
            "pain_amplifiers": ["custos crescentes", "desperdício de recursos", "ineficiência orçamentária", "imprevisibilidade"],
            "benefit_enhancers": ["economia clara", "payback rápido", "custos previsíveis", "redução de overhead"],
            "value_statement_template": "Nosso sistema oferece {key_benefit} com um retorno claro do investimento, reduzindo {main_pain} em até {impact_percentage} e permitindo {financial_improvement}."
        },
        "Executivo": {
            "value_themes": ["vantagem competitiva", "crescimento", "inovação", "visão estratégica", "posicionamento no mercado"],
            "key_metrics": ["market share", "satisfação do cliente", "agilidade nos negócios", "tempo de lançamento"],
            "pain_amplifiers": ["pressão competitiva", "oportunidades perdidas", "limitações de crescimento", "desalinhamento estratégico"],
            "benefit_enhancers": ["vantagem no mercado", "capacidade de inovação", "escalabilidade do negócio", "alinhamento estratégico"],
            "value_statement_template": "Nossa solução proporciona {key_benefit} para sua organização, transformando {main_pain} em {strategic_advantage}, posicionando sua empresa à frente da concorrência."
        }
    }
    
    # Construir propostas de valor por stakeholder
    value_propositions = {}
    
    for stakeholder in target_stakeholders:
        if stakeholder not in stakeholder_focus:
            continue
        
        focus = stakeholder_focus[stakeholder]
        
        # Selecionar os pontos de dor mais relevantes para este stakeholder
        relevant_pains = []
        for pain in client_pain_points:
            pain_lower = pain.lower()
            if any(theme in pain_lower for theme in focus["value_themes"]) or \
               any(metric in pain_lower for metric in focus["key_metrics"]):
                relevant_pains.append(pain)
        
        if not relevant_pains and client_pain_points:
            relevant_pains = [client_pain_points[0]]  # Usar pelo menos um se nenhum for altamente relevante
        
        # Selecionar os benefícios mais relevantes para este stakeholder
        relevant_benefits = []
        for benefit in solution_benefits:
            benefit_lower = benefit.lower()
            if any(theme in benefit_lower for theme in focus["value_themes"]) or \
               any(metric in benefit_lower for metric in focus["key_metrics"]):
                relevant_benefits.append(benefit)
        
        if not relevant_benefits and solution_benefits:
            relevant_benefits = [solution_benefits[0]]  # Usar pelo menos um se nenhum for altamente relevante
        
        # Construir proposta de valor com template
        main_pain = relevant_pains[0] if relevant_pains else "desafios atuais"
        key_benefit = relevant_benefits[0] if relevant_benefits else "benefícios significativos"
        
        if stakeholder == "Técnico":
            value_statement = focus["value_statement_template"].format(
                key_benefit=key_benefit.lower(),
                key_technology="tecnologias modernas e práticas de engenharia robustas",
                main_pain=main_pain.lower(),
                future_advantage="maior escalabilidade e manutenibilidade do sistema"
            )
        elif stakeholder == "Financeiro":
            value_statement = focus["value_statement_template"].format(
                key_benefit=key_benefit.lower(),
                main_pain=main_pain.lower(),
                impact_percentage="30%",
                financial_improvement="maior controle orçamentário e previsibilidade financeira"
            )
        elif stakeholder == "Executivo":
            value_statement = focus["value_statement_template"].format(
                key_benefit=key_benefit.lower(),
                main_pain=main_pain.lower(),
                strategic_advantage="vantagem competitiva sustentável"
            )
        else:
            value_statement = f"Nossa solução resolve {main_pain.lower()} através de {key_benefit.lower()}."
        
        # Adicionar detalhes adicionais
        bullet_points = []
        for i, benefit in enumerate(relevant_benefits[:3]):
            if i < len(relevant_pains):
                bullet = f"Transforma \"{relevant_pains[i]}\" em \"{benefit}\""
            else:
                bullet = f"Proporciona \"{benefit}\""
            bullet_points.append(bullet)
        
        # Montar proposta completa
        value_propositions[stakeholder] = {
            "headline": value_statement,
            "key_points": bullet_points,
            "relevant_pain_points": relevant_pains,
            "relevant_benefits": relevant_benefits
        }
    
    # Criar proposta de valor consolidada
    all_pain_points = []
    all_benefits = []
    
    for stakeholder, proposition in value_propositions.items():
        all_pain_points.extend(proposition["relevant_pain_points"])
        all_benefits.extend(proposition["relevant_benefits"])
    
    # Remover duplicados
    all_pain_points = list(dict.fromkeys(all_pain_points))
    all_benefits = list(dict.fromkeys(all_benefits))
    
    # Construir a proposta de valor principal
    main_value_proposition = f"Nossa solução resolve {all_pain_points[0].lower() if all_pain_points else 'seus principais desafios'} " \
                            f"proporcionando {all_benefits[0].lower() if all_benefits else 'benefícios concretos'}, " \
                            f"resultando em retorno de investimento significativo e vantagem competitiva."
    
    # Criar resultado final
    result = {
        "main_value_proposition": main_value_proposition,
        "stakeholder_propositions": value_propositions,
        "consolidated_pain_points": all_pain_points,
        "consolidated_benefits": all_benefits,
        "target_stakeholders": target_stakeholders,
        "created_at": datetime.now().strftime("%d/%m/%Y")
    }
    
    return result

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo de pontos de dor e benefícios para um sistema de automação
    pains = [
        "Processos manuais demorados e sujeitos a erros",
        "Altos custos operacionais com tarefas repetitivas",
        "Falta de visibilidade em tempo real do status das operações",
        "Dificuldade de escalar operações com o crescimento da empresa",
        "Dificuldade em cumprir prazos regulatórios"
    ]
    
    benefits = [
        "Automação completa de processos manuais recorrentes",
        "Redução de 35% nos custos operacionais",
        "Dashboard em tempo real com KPIs estratégicos",
        "Arquitetura escalável que cresce com seu negócio",
        "Sistema de alertas automáticos para deadlines regulatórios",
        "Integração com sistemas legados existentes"
    ]
    
    result = build_value_proposition(
        client_pain_points=pains,
        solution_benefits=benefits,
        target_stakeholders=["Técnico", "Financeiro", "Executivo"]
    )
    
    print("=== Proposta de Valor Principal ===")
    print(result["main_value_proposition"])
    
    print("\n=== Propostas Específicas por Stakeholder ===")
    for stakeholder, proposition in result["stakeholder_propositions"].items():
        print(f"\n## Para stakeholder {stakeholder}:")
        print(proposition["headline"])
        print("\nPontos-chave:")
        for point in proposition["key_points"]:
            print(f"- {point}")
