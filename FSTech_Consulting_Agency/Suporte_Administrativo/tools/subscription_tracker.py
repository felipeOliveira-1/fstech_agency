# Ferramenta: Rastreador de Assinaturas

import datetime
import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Simulação de uma base de dados de assinaturas (em memória)
SUBSCRIPTIONS_DB = {
    "sub-123": {"client_id": "VIP-BIGCORP", "service": "Plano Premium IA", "status": "Ativa", "next_billing_date": "2025-06-01", "amount": 5000.00},
    "sub-456": {"client_id": "SMB-STARTUP", "service": "Automação Básica", "status": "Ativa", "next_billing_date": "2025-05-15", "amount": 500.00},
    "sub-789": {"client_id": "OLD-CLIENT", "service": "Consultoria Pontual", "status": "Cancelada", "next_billing_date": None, "amount": 1500.00}
}

@function_tool
def track_subscription(action: str, client_id: str = None, subscription_id: str = None, new_status: str = None) -> str:
    """Gerencia e rastreia assinaturas de serviços dos clientes.

    Use esta ferramenta para verificar o status de uma assinatura, listar assinaturas
    de um cliente, ou atualizar o status de uma assinatura (ex: ativar, cancelar).

    Args:
        action: A ação a ser realizada (	view_subscription	, 	list_client_subscriptions	, 	update_status	).
        client_id: (Obrigatório para 	list_client_subscriptions	) O ID do cliente.
        subscription_id: (Obrigatório para 	view_subscription	 e 	update_status	) O ID da assinatura.
        new_status: (Obrigatório para 	update_status	) O novo status da assinatura (ex: 	Ativa	, 	Cancelada	, 	Suspensa	).

    Returns:
        Uma string com os detalhes da assinatura, lista de assinaturas, confirmação de atualização ou uma mensagem de erro.
    """
    # Validação básica
    if not action in ["view_subscription", "list_client_subscriptions", "update_status"]:
        return "Erro: Ação inválida. Use 	view_subscription	, 	list_client_subscriptions	 ou 	update_status	."

    if action == "list_client_subscriptions" and not client_id:
        return "Erro: Para 	list_client_subscriptions	, 	client_id	 é obrigatório."
    
    if (action == "view_subscription" or action == "update_status") and not subscription_id:
         return f"Erro: Para {action}, 	 subscription_id	 é obrigatório."

    if action == "update_status" and not new_status:
        return "Erro: Para 	update_status	, 	new_status	 é obrigatório."

    print(f"Executando ação de assinatura: {action}...")

    if action == "view_subscription":
        subscription = SUBSCRIPTIONS_DB.get(subscription_id)
        if subscription:
            return f"Detalhes da Assinatura {subscription_id}:\nCliente: {subscription[	client_id	]}\nServiço: {subscription[	 service	]}\nStatus: {subscription[	status	]}\nPróx. Faturamento: {subscription[	next_billing_date	] or 	N/A	}\nValor: ${subscription[	amount	]:.2f}"
        else:
            return f"Erro: Assinatura com ID {subscription_id} não encontrada."

    elif action == "list_client_subscriptions":
        client_subs = []
        for sub_id, sub_details in SUBSCRIPTIONS_DB.items():
            if sub_details["client_id"] == client_id:
                client_subs.append(f"- ID: {sub_id}, Serviço: {sub_details[	 service	]}, Status: {sub_details[	status	]}")
        if client_subs:
            return f"Assinaturas encontradas para o cliente {client_id}:\n" + "\n".join(client_subs)
        else:
            return f"Nenhuma assinatura encontrada para o cliente {client_id}."

    elif action == "update_status":
        if subscription_id in SUBSCRIPTIONS_DB:
            old_status = SUBSCRIPTIONS_DB[subscription_id]["status"]
            SUBSCRIPTIONS_DB[subscription_id]["status"] = new_status
            # Em um cenário real, poderia ajustar a data de faturamento ou disparar outras ações
            if new_status.lower() == "cancelada":
                 SUBSCRIPTIONS_DB[subscription_id]["next_billing_date"] = None
            
            confirmation_message = f"Status da assinatura {subscription_id} atualizado de 	{old_status}	 para 	{new_status}	 com sucesso."
            print(confirmation_message)
            return confirmation_message
        else:
            return f"Erro: Assinatura com ID {subscription_id} não encontrada para atualização."

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    print("--- Ver Assinatura ---")
    print(track_subscription(action="view_subscription", subscription_id="sub-123"))
    print("\n--- Listar Assinaturas Cliente ---")
    print(track_subscription(action="list_client_subscriptions", client_id="VIP-BIGCORP"))
    print("\n--- Listar Assinaturas Cliente Inexistente ---")
    print(track_subscription(action="list_client_subscriptions", client_id="NON-EXISTENT"))
    print("\n--- Atualizar Status ---")
    print(track_subscription(action="update_status", subscription_id="sub-456", new_status="Suspensa"))
    print("\n--- Ver Assinatura Atualizada ---")
    print(track_subscription(action="view_subscription", subscription_id="sub-456"))

