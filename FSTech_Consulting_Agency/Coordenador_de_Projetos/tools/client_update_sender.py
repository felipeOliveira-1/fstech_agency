# Ferramenta: Enviador de Atualização para Cliente

import datetime
import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def send_client_update(client_id: str, project_id: str, update_summary: str, communication_channel: str = "Email") -> str:
    """Envia um resumo de atualização do progresso do projeto para o cliente.

    Use esta ferramenta para comunicar formalmente o status atual, próximos passos
    e quaisquer pontos de atenção relevantes para o cliente, através do canal especificado.

    Args:
        client_id: O ID do cliente para quem enviar a atualização.
        project_id: O ID do projeto ao qual a atualização se refere.
        update_summary: O texto do resumo da atualização a ser enviado.
        communication_channel: (Opcional) O canal de comunicação a ser usado (ex: 	Email	, 	Slack	, 	Portal do Cliente	). Default: 	Email	.

    Returns:
        Uma string confirmando o envio da atualização ou uma mensagem de erro.
    """
    # Validação básica
    if not client_id or not project_id or not update_summary:
        return "Erro: ID do cliente (client_id), ID do projeto (project_id) e resumo da atualização (update_summary) são obrigatórios."
    
    supported_channels = ["email", "slack", "portal do cliente"]
    if communication_channel.lower() not in supported_channels:
        print(f"Aviso: Canal {communication_channel} não é um canal padrão suportado ({', '.join(supported_channels)}). Tentando enviar mesmo assim.")
        # Poderia retornar erro se quisesse ser mais estrito

    print(f"Preparando para enviar atualização do projeto {project_id} para o cliente {client_id} via {communication_channel}...")
    print(f"Resumo: {update_summary[:100]}...")

    # Lógica simulada de envio
    # Em um cenário real, isso envolveria:
    # 1. Obter detalhes de contato do cliente (email, ID do Slack, etc.) com base no client_id.
    # 2. Formatar a mensagem adequadamente para o canal.
    # 3. Usar a API apropriada (Email API, Slack API, API do Portal) para enviar a mensagem.
    # 4. Registrar o envio da comunicação.

    # Simulação de sucesso
    timestamp = datetime.datetime.now().isoformat()
    confirmation_message = f"Atualização do projeto {project_id} enviada com sucesso para o cliente {client_id} via {communication_channel} em {timestamp}. Resumo: 	{update_summary[:50]}...	 (simulado)."

    print(confirmation_message)
    return confirmation_message

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    client = "VIP-BIGCORP"
    proj = "PROJ-AI-IMPL"
    summary = "Concluímos a Fase 2 (Implementação) do projeto. Os testes começarão na próxima semana. Nenhum bloqueio identificado no momento. Próxima reunião de status agendada para DD/MM."
    
    print("--- Enviar via Email (Padrão) ---")
    print(send_client_update(client_id=client, project_id=proj, update_summary=summary))

    print("\n--- Enviar via Slack ---")
    summary_slack = "Update rápido: Fase 2 concluída! Testes na próxima semana. Detalhes no portal."
    print(send_client_update(client_id=client, project_id=proj, update_summary=summary_slack, communication_channel="Slack"))

    print("\n--- Tentar Enviar via Canal Inválido ---")
    print(send_client_update(client_id=client, project_id=proj, update_summary="Teste canal inválido", communication_channel="WhatsApp"))

