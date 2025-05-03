# Ferramenta: Assistente de Engenharia de Prompt

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def optimize_prompt(original_prompt: str, task_type: str, target_model: str = "geral") -> str:
    """Otimiza um prompt existente para melhorar o desempenho do LLM.

    Use esta ferramenta para refinar prompts, tornando-os mais claros, concisos
    e eficazes para uma tarefa específica e, opcionalmente, para um modelo alvo.

    Args:
        original_prompt: O prompt original que precisa ser otimizado.
        task_type: O tipo de tarefa que o prompt visa realizar (ex: 	Geração de Texto	, 	Extração de Informação	, 	Classificação	, 	Tradução	).
        target_model: (Opcional) O modelo LLM específico para o qual otimizar (ex: 	GPT-4	, 	Claude 3	). Default é 	geral	.

    Returns:
        Uma string contendo o prompt otimizado ou uma mensagem de erro.
    """
    # Validação básica
    if not original_prompt or not task_type:
        return "Erro: Prompt original (original_prompt) e tipo de tarefa (task_type) são necessários."

    print(f"Otimizando prompt para tarefa 	{task_type}	 (Modelo alvo: {target_model})...")
    print(f"Prompt Original: {original_prompt[:100]}...")

    # Lógica simulada de otimização de prompt
    # Em um cenário real, isso poderia envolver:
    # 1. Usar um LLM para analisar e reescrever o prompt.
    # 2. Aplicar heurísticas de engenharia de prompt (clareza, contexto, persona, formato de saída).
    # 3. Adicionar exemplos (few-shot prompting).

    optimized_prompt = f"""## Prompt Otimizado (Simulado) ##

**Contexto:** Você é um assistente especialista em {task_type}.
**Tarefa:** [Reformulação da tarefa baseada no prompt original]
**Instruções Claras:**
1.  [Instrução 1 derivada do original]
2.  [Instrução 2 derivada do original]
3.  Considere o modelo alvo: {target_model}.
**Formato de Saída Esperado:** [Descrição do formato]

**Prompt Original (para referência):**
{original_prompt}
"""

    # Adicionar uma sugestão simulada
    if "geração" in task_type.lower():
        optimized_prompt += "\n**Sugestão:** Adicione exemplos de saída desejada para melhorar a consistência."
    elif "extração" in task_type.lower():
         optimized_prompt += "\n**Sugestão:** Especifique claramente as entidades a serem extraídas e o formato JSON desejado."

    print("Prompt otimizado (simulado) gerado.")
    return optimized_prompt

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    prompt_original = "Me diga sobre inteligência artificial."
    optimized = optimize_prompt(original_prompt=prompt_original, task_type="Geração de Texto Explicativo", target_model="GPT-4o")
    print(optimized)

    print("\n--------------------\n")

    prompt_extracao = "Extraia o nome da empresa e o valor da fatura do seguinte texto: A fatura #123 da Acme Corp é de $500."
    optimized_ext = optimize_prompt(original_prompt=prompt_extracao, task_type="Extração de Informação")
    print(optimized_ext)

