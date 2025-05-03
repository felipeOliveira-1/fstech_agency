# Ferramenta: Designer de Arquitetura de Sistema e Avaliador de Complexidade

import re

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Palavras-chave associadas a componentes comuns e sua pontuação de complexidade
COMPONENT_KEYWORDS = {
    "api": {"name": "API REST/GraphQL", "score": 2},
    "banco de dados": {"name": "Banco de Dados (SQL/NoSQL)", "score": 2},
    "database": {"name": "Banco de Dados (SQL/NoSQL)", "score": 2},
    "sql": {"name": "Banco de Dados (SQL)", "score": 2},
    "nosql": {"name": "Banco de Dados (NoSQL)", "score": 2},
    "frontend": {"name": "Frontend Web (React/Vue/Angular)", "score": 2},
    "interface web": {"name": "Frontend Web", "score": 2},
    "site": {"name": "Frontend Web", "score": 1},
    "aplicativo móvel": {"name": "Aplicativo Móvel (iOS/Android)", "score": 3},
    "mobile app": {"name": "Aplicativo Móvel (iOS/Android)", "score": 3},
    "inteligência artificial": {"name": "Componente de IA/ML", "score": 3},
    "machine learning": {"name": "Componente de IA/ML", "score": 3},
    "modelo de ia": {"name": "Componente de IA/ML", "score": 3},
    "llm": {"name": "Integração com LLM", "score": 2},
    "gpt": {"name": "Integração com LLM (GPT)", "score": 2},
    "integração": {"name": "Integração com Sistema Externo", "score": 2},
    "webhook": {"name": "Integração via Webhook", "score": 1},
    "automação": {"name": "Fluxo de Automação", "score": 1},
    "pagamento": {"name": "Integração de Pagamento", "score": 2},
    "login": {"name": "Sistema de Autenticação", "score": 1},
    "autenticação": {"name": "Sistema de Autenticação", "score": 1},
    "dashboard": {"name": "Painel de Controle/Dashboard", "score": 1},
    "relatórios": {"name": "Geração de Relatórios", "score": 1}
}

# Limites de pontuação para níveis de complexidade
COMPLEXITY_THRESHOLDS = {
    "baixa": 4,
    "media": 8,
    "alta": float("inf") # Qualquer coisa acima de 8
}

@function_tool
def design_architecture_and_assess_complexity(requirements_text: str) -> str:
    """Analisa um texto de requisitos técnicos, sugere componentes de arquitetura
    e estima a complexidade geral (baixa, media, alta).

    Args:
        requirements_text: O texto descrevendo os requisitos técnicos do projeto.

    Returns:
        Uma string contendo o esboço da arquitetura sugerida e o nível de complexidade estimado.
    """
    if not requirements_text:
        return "Erro: O texto de requisitos não pode estar vazio."

    detected_components = set()
    total_score = 0
    architecture_sketch = []

    # Normalizar texto para minúsculas para busca case-insensitive
    normalized_text = requirements_text.lower()

    # Buscar palavras-chave no texto
    for keyword, data in COMPONENT_KEYWORDS.items():
        # Usar regex para encontrar palavras inteiras
        if re.search(r"\b" + re.escape(keyword) + r"\b", normalized_text):
            component_name = data["name"]
            if component_name not in detected_components:
                detected_components.add(component_name)
                total_score += data["score"]
                architecture_sketch.append(f"- {component_name} (Score: {data['score']})")

    # Determinar nível de complexidade
    complexity_level = "baixa" # Padrão
    if total_score > COMPLEXITY_THRESHOLDS["media"]:
        complexity_level = "alta"
    elif total_score > COMPLEXITY_THRESHOLDS["baixa"]:
        complexity_level = "media"

    # Montar resultado
    if not architecture_sketch:
        result_summary = "Nenhum componente técnico chave identificado claramente nos requisitos. "
    else:
        result_summary = "Esboço da Arquitetura Sugerida:\n" + "\n".join(architecture_sketch) + "\n\n"

    result_summary += f"Pontuação Total de Complexidade: {total_score}\n"
    result_summary += f"Nível de Complexidade Estimado: {complexity_level.upper()}"

    print(f"Análise de Arquitetura: Score={total_score}, Complexidade={complexity_level.upper()}")
    print(f"Componentes Detectados: {', '.join(detected_components) if detected_components else 'Nenhum'}")

    return result_summary

# Exemplo de uso
if __name__ == "__main__":
    req1 = """
    Precisamos de um sistema web com login de usuários, um dashboard para visualizar dados
    e uma API para integração com um aplicativo móvel futuro. O sistema deve usar um banco de dados SQL.
    Também queremos uma automação simples para enviar emails.
    """
    print("--- Análise Requisito 1 ---")
    print(design_architecture_and_assess_complexity(req1))

    req2 = """
    Desenvolver um aplicativo móvel que se conecta a uma API existente.
    Deve incluir funcionalidade de pagamento.
    """
    print("\n--- Análise Requisito 2 ---")
    print(design_architecture_and_assess_complexity(req2))

    req3 = """
    Criar um modelo de machine learning para previsão de vendas, com um frontend web simples
    para input de dados e visualização dos resultados. Usar um banco de dados NoSQL.
    Integrar com nosso CRM via webhook.
    """
    print("\n--- Análise Requisito 3 ---")
    print(design_architecture_and_assess_complexity(req3))

    req4 = "Apenas um site institucional simples."
    print("\n--- Análise Requisito 4 ---")
    print(design_architecture_and_assess_complexity(req4))

    req5 = ""
    print("\n--- Teste de Erro (Vazio) ---")
    print(design_architecture_and_assess_complexity(req5))

