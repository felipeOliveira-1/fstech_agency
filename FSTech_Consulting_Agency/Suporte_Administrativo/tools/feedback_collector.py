# Ferramenta: Coletor de Feedback

import datetime
import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Simulação de uma base de dados de feedback (em memória)
FEEDBACK_DB = []

@function_tool
def collect_feedback(client_id: str, project_id: str = None, feedback_text: str = None, rating: int = None) -> str:
    """Coleta e registra feedback dos clientes sobre projetos ou serviços.

    Use esta ferramenta para registrar feedback recebido de clientes, seja através
    de formulários, emails ou conversas. Pode incluir texto livre e/ou uma classificação.

    Args:
        client_id: O ID do cliente que forneceu o feedback.
        project_id: (Opcional) O ID do projeto específico relacionado ao feedback.
        feedback_text: (Opcional) O texto do feedback fornecido pelo cliente.
        rating: (Opcional) Uma classificação numérica (ex: 1 a 5 estrelas) fornecida pelo cliente.

    Returns:
        Uma string confirmando o registro do feedback ou uma mensagem de erro.
    """
    # Validação básica
    if not client_id:
        return "Erro: ID do cliente (client_id) é obrigatório."
    if not feedback_text and not rating:
        return "Erro: Pelo menos o texto do feedback (feedback_text) ou a classificação (rating) deve ser fornecido."
    if rating is not None and not isinstance(rating, int):
         return "Erro: Classificação (rating) deve ser um número inteiro."

    print(f"Registrando feedback do cliente {client_id} (Projeto: {project_id or 	N/A	})...")

    # Lógica simulada de registro de feedback
    feedback_entry = {
        "feedback_id": f"fb-{random.randint(10000, 99999)}",
        "client_id": client_id,
        "project_id": project_id,
        "timestamp": datetime.datetime.now().isoformat(),
        "feedback_text": feedback_text,
        "rating": rating
    }
    FEEDBACK_DB.append(feedback_entry)

    confirmation_message = f"Feedback do cliente {client_id} registrado com sucesso. ID do Feedback (simulado): {feedback_entry[	feedback_id	]}."
    print(confirmation_message)
    # Em um cenário real, poderia salvar em banco de dados, enviar notificação, etc.
    return confirmation_message

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    print("--- Registrar Feedback Texto ---")
    print(collect_feedback(client_id="VIP-BIGCORP", project_id="PROJ-AI-IMPL", feedback_text="A equipe foi muito prestativa durante a implementação."))

    print("\n--- Registrar Feedback Rating ---")
    print(collect_feedback(client_id="SMB-STARTUP", rating=5))

    print("\n--- Registrar Feedback Completo ---")
    print(collect_feedback(client_id="VIP-BIGCORP", project_id="PROJ-AI-IMPL", feedback_text="O resultado superou as expectativas!", rating=5))

    print("\n--- Ver Base de Feedback Simulada ---")
    import json
    print(json.dumps(FEEDBACK_DB, indent=2))

