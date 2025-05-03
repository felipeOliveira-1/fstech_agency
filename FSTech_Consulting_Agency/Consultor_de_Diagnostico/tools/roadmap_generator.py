# Ferramenta: Gerador de Roadmap

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def generate_roadmap(diagnostic_summary: str, client_objectives: list[str]) -> str:
    """Cria um roadmap de alto nível baseado no diagnóstico e nos objetivos do cliente.

    Use esta ferramenta após a análise do diagnóstico para propor um plano de ação
    inicial com fases e marcos principais para atingir os objetivos do cliente,
    abordando os problemas identificados.

    Args:
        diagnostic_summary: O sumário do diagnóstico tecnológico (gerado pela ferramenta analyze_tech_diagnostic).
        client_objectives: Uma lista dos principais objetivos de negócio do cliente (ex: [	Aumentar eficiência em 20%	, 	Melhorar experiência do cliente	]).

    Returns:
        Uma string formatada em Markdown contendo o roadmap proposto ou uma mensagem de erro.
    """
    # Validação básica
    if not diagnostic_summary or not client_objectives or not isinstance(client_objectives, list):
        return "Erro: Sumário do diagnóstico (diagnostic_summary) e lista de objetivos do cliente (client_objectives) são necessários."

    print(f"Gerando roadmap baseado no diagnóstico e objetivos: {client_objectives}...")

    # Lógica simulada para gerar o roadmap (extraindo oportunidades do sumário)
    # Idealmente, um LLM analisaria o diagnostic_summary para identificar ações
    opportunities = []
    if "oportunidades de melhoria" in diagnostic_summary.lower():
        lines = diagnostic_summary.split("\n")
        in_opportunities_section = False
        for line in lines:
            if "oportunidades de melhoria" in line.lower():
                in_opportunities_section = True
                continue
            if in_opportunities_section and line.strip().startswith("-"):
                opportunities.append(line.strip()[2:]) # Extrai o texto após "- "
            elif in_opportunities_section and not line.strip(): # Fim da seção
                break

    if not opportunities:
        opportunities = ["Implementar solução X", "Otimizar processo Y", "Treinar equipe Z"] # Fallback simulado

    roadmap_content = f"""# Roadmap Proposto - FSTech Consulting Agency

**Baseado em:** Diagnóstico Tecnológico e Objetivos do Cliente
**Objetivos Principais:** { "; ".join(client_objectives) }

## Fase 1: Fundação e Planejamento (Próximos 1-2 meses)

*   **Marco 1.1:** Validação detalhada dos requisitos.
*   **Marco 1.2:** Definição da arquitetura da solução (se aplicável).
*   **Ação:** {opportunities[0] if opportunities else "[Ação Chave 1]"}

## Fase 2: Implementação Inicial (Meses 2-4)

*   **Marco 2.1:** Desenvolvimento/Configuração do Módulo A.
*   **Marco 2.2:** Testes iniciais e feedback.
*   **Ação:** {opportunities[1] if len(opportunities) > 1 else "[Ação Chave 2]"}

## Fase 3: Expansão e Otimização (Meses 4-6+)

*   **Marco 3.1:** Implementação do Módulo B / Rollout completo.
*   **Marco 3.2:** Treinamento de usuários e Go-live.
*   **Marco 3.3:** Monitoramento e otimização contínua.
*   **Ação:** {opportunities[2] if len(opportunities) > 2 else "[Ação Chave 3]"}

**Próximos Passos:** Apresentar e validar este roadmap com o cliente.

*Nota: Este é um roadmap de alto nível e simulado. As fases e ações serão detalhadas.*
"""

    return roadmap_content

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    simulated_diag_summary = """# Sumário do Diagnóstico...

## Oportunidades de Melhoria Identificadas (Simulado):
- Migração para infraestrutura em nuvem para escalabilidade.
- Implementação de solução de backup automatizado.
- Revisão de processos internos.
"""
    simulated_objectives = ["Reduzir custos de TI em 15%", "Aumentar a segurança dos dados"]

    roadmap = generate_roadmap(diagnostic_summary=simulated_diag_summary, client_objectives=simulated_objectives)
    print(roadmap)

