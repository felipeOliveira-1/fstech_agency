# Ferramenta: Calculadora de ROI

import numpy as np
from datetime import datetime

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def calculate_roi(project_cost: float, annual_benefits: list, discount_rate: float = 0.1, project_duration_years: int = 3) -> dict:
    """Calcula o ROI (Retorno sobre Investimento) e outros indicadores financeiros.
    
    Args:
        project_cost: Custo total do projeto (valor presente).
        annual_benefits: Lista de benefícios anuais projetados (ano 1, 2, 3, etc.).
        discount_rate: Taxa de desconto anual para cálculo do valor presente líquido.
        project_duration_years: Duração do projeto em anos para análise.
        
    Returns:
        Um dicionário contendo o ROI percentual, VPL, TIR e outros indicadores relevantes.
    """
    try:
        # Validar inputs
        if project_cost <= 0:
            return {"error": "O custo do projeto deve ser maior que zero."}
        
        if not annual_benefits or len(annual_benefits) == 0:
            return {"error": "É necessário fornecer ao menos um valor de benefício anual."}
        
        # Ajustar lista de benefícios para a duração do projeto
        if len(annual_benefits) < project_duration_years:
            # Repetir o último valor se faltarem anos
            last_value = annual_benefits[-1]
            annual_benefits.extend([last_value] * (project_duration_years - len(annual_benefits)))
        elif len(annual_benefits) > project_duration_years:
            # Truncar se houver mais anos que o necessário
            annual_benefits = annual_benefits[:project_duration_years]
        
        # Calcular valor presente líquido (VPL)
        npv = -project_cost  # Investimento inicial é negativo
        cumulative_benefits = 0
        discounted_benefits = []
        
        for year, benefit in enumerate(annual_benefits, start=1):
            present_value = benefit / ((1 + discount_rate) ** year)
            discounted_benefits.append(present_value)
            npv += present_value
            cumulative_benefits += benefit
        
        # Calcular ROI (simples e ajustado ao valor do dinheiro no tempo)
        roi_simple = (cumulative_benefits - project_cost) / project_cost * 100
        roi_npv = npv / project_cost * 100
        
        # Calcular payback simples (em anos)
        cumulative = 0
        payback_simple = project_duration_years
        
        for year, benefit in enumerate(annual_benefits, start=1):
            cumulative += benefit
            if cumulative >= project_cost:
                # Interpolação linear para precisão
                prev_cumulative = cumulative - benefit
                fraction = (project_cost - prev_cumulative) / benefit
                payback_simple = year - 1 + fraction
                break
        
        # Calcular TIR (simulação simplificada)
        # Na implementação real, usaríamos numpy.irr ou similar
        irr_estimate = (cumulative_benefits / project_duration_years) / project_cost * 100
        
        # Formar resultado
        result = {
            "roi_percentage": round(roi_simple, 2),
            "roi_npv_percentage": round(roi_npv, 2),
            "npv": round(npv, 2),
            "payback_years": round(payback_simple, 2),
            "irr_percentage_estimate": round(irr_estimate, 2),
            "total_benefits": round(cumulative_benefits, 2),
            "discounted_benefits": [round(b, 2) for b in discounted_benefits],
            "analysis_date": datetime.now().strftime("%d/%m/%Y"),
            "analysis_summary": ""
        }
        
        # Adicionar análise qualitativa
        if npv > 0:
            if roi_npv > 50:
                result["analysis_summary"] = "Projeto altamente recomendado. ROI excepcional."
            elif roi_npv > 25:
                result["analysis_summary"] = "Projeto recomendado. ROI forte."
            else:
                result["analysis_summary"] = "Projeto viável. ROI positivo."
        else:
            result["analysis_summary"] = "Projeto não recomendado financeiramente. ROI negativo."
        
        return result
        
    except Exception as e:
        return {
            "error": f"Erro ao calcular ROI: {str(e)}",
            "roi_percentage": 0,
            "npv": 0,
            "payback_years": 0,
            "analysis_summary": "Não foi possível realizar a análise de ROI."
        }

# Exemplo de uso
if __name__ == "__main__":
    # Exemplo 1: Projeto de automação de processos
    result1 = calculate_roi(
        project_cost=100000,
        annual_benefits=[40000, 60000, 80000],
        discount_rate=0.08,
        project_duration_years=3
    )
    print("=== Análise de ROI: Projeto de Automação ===")
    for key, value in result1.items():
        print(f"{key}: {value}")
    
    # Exemplo 2: Projeto de transformação digital
    result2 = calculate_roi(
        project_cost=500000,
        annual_benefits=[150000, 250000, 350000, 350000, 350000],
        discount_rate=0.1,
        project_duration_years=5
    )
    print("\n=== Análise de ROI: Projeto de Transformação Digital ===")
    for key, value in result2.items():
        print(f"{key}: {value}")
