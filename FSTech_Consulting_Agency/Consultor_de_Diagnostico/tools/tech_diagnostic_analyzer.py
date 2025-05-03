# Ferramenta: Analisador de Diagnóstico Tecnológico

import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def analyze_tech_diagnostic(client_data: dict, focus_area: str) -> str:
    """Analisa os dados do cliente para diagnosticar problemas tecnológicos e oportunidades.

    Use esta ferramenta após coletar informações iniciais (intake) para analisar
    a situação tecnológica atual do cliente em uma área específica e identificar
    pontos de melhoria ou problemas.

    Args:
        client_data: Um dicionário contendo informações coletadas sobre o cliente (ex: do formulário de intake).
        focus_area: A área tecnológica específica a ser analisada (ex: 	Infraestrutura de TI	, 	Processos de Vendas	, 	Marketing Digital	).

    Returns:
        Uma string formatada em Markdown com o sumário do diagnóstico ou uma mensagem de erro.
    """
    # Validação básica
    if not client_data or not isinstance(client_data, dict) or not focus_area:
        return "Erro: Dados do cliente (client_data como dict) e área de foco (focus_area) são necessários."

    client_name = client_data.get("name", "Cliente Desconhecido")
    print(f"Analisando diagnóstico tecnológico para {client_name} com foco em {focus_area}...")

    # Lógica simulada para análise de diagnóstico
    strengths = []
    weaknesses = []
    opportunities = []

    # Simulação baseada na área de foco
    if "infraestrutura" in focus_area.lower():
        weaknesses.append("Hardware obsoleto identificado em alguns setores.")
        weaknesses.append("Processo de backup manual e propenso a erros.")
        opportunities.append("Migração para infraestrutura em nuvem para escalabilidade.")
        opportunities.append("Implementação de solução de backup automatizado.")
        strengths.append("Equipe de TI interna dedicada (embora pequena).")
    elif "vendas" in focus_area.lower():
        weaknesses.append("CRM subutilizado, dados de clientes descentralizados.")
        weaknesses.append("Falta de automação no follow-up de leads.")
        opportunities.append("Implementação de funil de vendas automatizado no CRM.")
        opportunities.append("Treinamento da equipe de vendas para uso eficaz do CRM.")
        strengths.append("Produto/serviço com boa aceitação no mercado.")
    elif "marketing" in focus_area.lower():
        weaknesses.append("Presença online limitada, SEO básico.")
        weaknesses.append("Campanhas de email marketing genéricas.")
        opportunities.append("Desenvolvimento de estratégia de conteúdo e SEO.")
        opportunities.append("Segmentação de público e personalização de campanhas de email.")
        strengths.append("Marca com boa reputação offline.")
    else:
        weaknesses.append("Área de foco não mapeada para análise detalhada simulada.")
        opportunities.append("Realizar análise mais aprofundada específica para esta área.")
        strengths.append("Disposição do cliente em investir em melhorias.")

    diagnostic_summary = f"""# Sumário do Diagnóstico Tecnológico - {client_name}

**Área de Foco:** {focus_area}

## Pontos Fortes Identificados (Simulado):
"""
    for strength in strengths:
        diagnostic_summary += f"- {strength}\n"

    diagnostic_summary += "\n## Pontos Fracos / Desafios Identificados (Simulado):\n"
    for weakness in weaknesses:
        diagnostic_summary += f"- {weakness}\n"

    diagnostic_summary += "\n## Oportunidades de Melhoria Identificadas (Simulado):\n"
    for opportunity in opportunities:
        diagnostic_summary += f"- {opportunity}\n"

    diagnostic_summary += "\n*Nota: Este é um diagnóstico simulado baseado em dados limitados.*"

    return diagnostic_summary

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    simulated_client_data = {
        "name": "Exemplo Corp",
        "industry": "Manufatura",
        "main_challenge": "Processos manuais lentos",
        "tech_stack": ["ERP antigo", "Planilhas Excel", "Email"]
    }
    print("--- Diagnóstico: Infraestrutura ---")
    print(analyze_tech_diagnostic(client_data=simulated_client_data, focus_area="Infraestrutura de TI"))
    print("\n--- Diagnóstico: Vendas ---")
    print(analyze_tech_diagnostic(client_data=simulated_client_data, focus_area="Processos de Vendas"))

