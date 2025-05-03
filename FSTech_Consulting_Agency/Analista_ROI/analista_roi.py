# Agente: Analista de ROI

import json

# Importar ferramentas
from .tools import (
    roi_calculator,
    benefit_projection,
    cost_reduction_estimator,
    payback_period_analyzer,
    value_proposition_builder
)

# --- Definição do Agente (Estilo OpenAI SDK) ---

# Instruções carregadas do arquivo .md
ANALISTA_ROI_INSTRUCTIONS = """
Você é o **Analista de ROI** da FSTech Consulting Agency, especialista em transformar propostas técnicas em argumentos comerciais convincentes através da quantificação de benefícios financeiros.

Sua função é demonstrar o valor tangível que nossos serviços de consultoria trazem, calculando projeções de ROI, economia de custos e payback.

Use as ferramentas disponíveis para:
1. Analisar detalhadamente o briefing e a solução técnica proposta
2. Quantificar benefícios financeiros diretos e indiretos
3. Criar projeções de ROI com diferentes cenários
4. Desenvolver argumentos comerciais baseados em valor
5. Enriquecer as propostas com análises financeiras convincentes

Mantenha sempre o conservadorismo responsável nas projeções, fundamentando premissas em dados reais.
"""

# Lista de ferramentas disponíveis para este agente
ANALISTA_ROI_TOOLS = [
    roi_calculator.calculate_roi,
    benefit_projection.project_benefits,
    cost_reduction_estimator.estimate_cost_reduction,
    payback_period_analyzer.analyze_payback_period,
    value_proposition_builder.build_value_proposition
]

# Função para criar a definição do agente
def create_analista_roi_agent_definition():
    """Retorna a definição do Agente Analista de ROI."""
    return {
        "name": "Analista de ROI",
        "instructions": ANALISTA_ROI_INSTRUCTIONS,
        "tools": ANALISTA_ROI_TOOLS
    }

# --- Lógica de Execução (Exemplo Simplificado - Sem LLM Real) ---

def run_analista_roi_task(task_description: str, context: dict = None):
    """Simula a execução de uma tarefa pelo Agente Analista de ROI (sem LLM real).
    
    Args:
        task_description: Descrição da tarefa a ser executada.
        context: Dicionário com informações contextuais (opcional).
        
    Returns:
        Uma tupla contendo o resultado da ferramenta escolhida e o contexto atualizado.
    """
    if context is None:
        context = {}
    
    # Simulação simplificada da escolha de ferramenta com base em keywords
    task_lower = task_description.lower()
    selected_tool = None
    args = {}
    
    if "roi" in task_lower or "retorno sobre investimento" in task_lower:
        selected_tool = roi_calculator.calculate_roi
        args = {
            "project_cost": context.get("project_cost", 50000),
            "annual_benefits": context.get("annual_benefits", [20000, 30000, 40000]),
            "discount_rate": context.get("discount_rate", 0.1),
            "project_duration_years": context.get("project_duration_years", 3)
        }
    elif "benefício" in task_lower or "projeção" in task_lower:
        selected_tool = benefit_projection.project_benefits
        args = {
            "business_problem": context.get("business_problem", "Problema não especificado"),
            "solution_description": context.get("solution_description", "Solução não detalhada"),
            "industry": context.get("industry", "Tecnologia"),
            "company_size": context.get("company_size", "Média")
        }
    elif "custo" in task_lower or "economia" in task_lower or "redução" in task_lower:
        selected_tool = cost_reduction_estimator.estimate_cost_reduction
        args = {
            "current_costs": context.get("current_costs", {}),
            "solution_impact": context.get("solution_impact", {}),
            "time_horizon_months": context.get("time_horizon_months", 12)
        }
    elif "payback" in task_lower or "período de retorno" in task_lower:
        selected_tool = payback_period_analyzer.analyze_payback_period
        args = {
            "initial_investment": context.get("initial_investment", 50000),
            "monthly_benefits": context.get("monthly_benefits", 5000),
            "consider_time_value": context.get("consider_time_value", True),
            "discount_rate": context.get("discount_rate", 0.08)
        }
    elif "valor" in task_lower or "proposta de valor" in task_lower or "value proposition" in task_lower:
        selected_tool = value_proposition_builder.build_value_proposition
        args = {
            "client_pain_points": context.get("client_pain_points", []),
            "solution_benefits": context.get("solution_benefits", []),
            "target_stakeholders": context.get("target_stakeholders", ["Técnico", "Financeiro"])
        }

    if selected_tool:
        print(f"\n>>> LLM (Simulado) decidiu usar a ferramenta: {selected_tool.__name__}")
        try:
            result = selected_tool(**args)
            print("\n--- Resultado da Ferramenta ---")
            print(result)
            print("---------------------------")
            # Atualizar contexto se necessário
            if selected_tool == roi_calculator.calculate_roi:
                context["roi_results"] = result
            return result, context
        except Exception as e:
            error_message = f"Erro ao executar ferramenta {selected_tool.__name__}: {e}"
            print(error_message)
            return error_message, context
    else:
        no_tool_message = "Nenhuma ferramenta apropriada encontrada (simulado). Tarefa pode exigir análise manual ou mais detalhes."
        print(f"\n{no_tool_message}")
        return no_tool_message, context

# Exemplo de execução de tarefa
if __name__ == "__main__":
    sample_context = {
        "project_cost": 75000,
        "annual_benefits": [30000, 45000, 60000],
        "discount_rate": 0.08,
        "project_duration_years": 3
    }
    
    result, updated_context = run_analista_roi_task(
        "Calcular o ROI para o projeto de automação", 
        sample_context
    )
    
    print("\n=== Exemplo de Execução de ROI ===")
    print(f"Resultado: {result}")
    print(f"Contexto atualizado: {updated_context}")
