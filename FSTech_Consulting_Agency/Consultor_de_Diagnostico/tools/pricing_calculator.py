# Ferramenta: Calculadora de Precificação de Proposta

import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env (se houver taxas base ou configurações)
# load_dotenv(dotenv_path="/home/ubuntu/FSTech_Consulting_Agency/.env")

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Fatores de complexidade (exemplo, pode ser ajustado)
COMPLEXITY_MULTIPLIERS = {
    "baixa": 1.0,
    "media": 1.5,
    "alta": 2.0
}

# Taxa horária base (exemplo, pode vir do .env ou ser parâmetro)
BASE_HOURLY_RATE_BRL = 150.00

@function_tool
def calculate_proposal_price(estimated_effort_hours: float, complexity_level: str, desired_margin_percentage: float, base_hourly_rate: float = BASE_HOURLY_RATE_BRL) -> str:
    """Calcula o preço de uma proposta com base no esforço, complexidade e margem.

    Utiliza o esforço estimado (em horas), um nível de complexidade (baixa, media, alta)
    que ajusta o custo base, e a margem de lucro desejada para determinar o preço final.

    Args:
        estimated_effort_hours: O número total de horas estimadas para o projeto.
        complexity_level: O nível de complexidade do projeto ("baixa", "media", "alta").
        desired_margin_percentage: A margem de lucro desejada como porcentagem (ex: 20 para 20%).
        base_hourly_rate: (Opcional) A taxa horária base em BRL (padrão: 150.00).

    Returns:
        Uma string com o preço calculado formatado em BRL ou uma mensagem de erro.
    """
    if not all([estimated_effort_hours, complexity_level, desired_margin_percentage is not None]):
        return "Erro: Os parâmetros estimated_effort_hours, complexity_level e desired_margin_percentage são obrigatórios."
    if estimated_effort_hours <= 0:
        return "Erro: O esforço estimado em horas deve ser maior que zero."
    if desired_margin_percentage < 0:
        return "Erro: A margem desejada não pode ser negativa."
    if base_hourly_rate <= 0:
        return "Erro: A taxa horária base deve ser maior que zero."

    complexity_key = complexity_level.lower()
    if complexity_key not in COMPLEXITY_MULTIPLIERS:
        valid_levels = ", ".join(COMPLEXITY_MULTIPLIERS.keys())
        return f"Erro: Nível de complexidade inválido 	{complexity_level}	. Use um dos seguintes: {valid_levels}."

    complexity_multiplier = COMPLEXITY_MULTIPLIERS[complexity_key]

    # Calcular custo base
    base_cost = estimated_effort_hours * base_hourly_rate

    # Ajustar custo pela complexidade
    adjusted_cost = base_cost * complexity_multiplier

    # Calcular preço final com margem
    final_price = adjusted_cost * (1 + (desired_margin_percentage / 100.0))

    # Formatar como moeda brasileira
    formatted_price = f"R$ {final_price:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    print(f"Cálculo de Preço: Esforço={estimated_effort_hours}h, Complexidade={complexity_level} (x{complexity_multiplier}), Margem={desired_margin_percentage}%, TaxaBase=R${base_hourly_rate:.2f} -> Preço Final={formatted_price}")

    return f"O preço calculado para a proposta é {formatted_price}."

# Exemplo de uso
if __name__ == "__main__":
    print("--- Calculando Preço Exemplo 1 (Médio) ---")
    print(calculate_proposal_price(estimated_effort_hours=50, complexity_level="Media", desired_margin_percentage=25))

    print("\n--- Calculando Preço Exemplo 2 (Alto) ---")
    print(calculate_proposal_price(estimated_effort_hours=120, complexity_level="Alta", desired_margin_percentage=30))

    print("\n--- Calculando Preço Exemplo 3 (Baixo, Taxa Customizada) ---")
    print(calculate_proposal_price(estimated_effort_hours=20, complexity_level="Baixa", desired_margin_percentage=15, base_hourly_rate=200.00))

    print("\n--- Teste de Erro (Complexidade Inválida) ---")
    print(calculate_proposal_price(estimated_effort_hours=30, complexity_level="Muito Alta", desired_margin_percentage=20))

    print("\n--- Teste de Erro (Esforço Zero) ---")
    print(calculate_proposal_price(estimated_effort_hours=0, complexity_level="Media", desired_margin_percentage=20))

