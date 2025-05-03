# Agente: Suporte Administrativo

import json
import datetime

# Importar ferramentas refatoradas
from .tools import (
    client_support_bot, 
    appointment_scheduler_manager, 
    subscription_tracker, 
    feedback_collector
)

# --- Definição do Agente (Estilo OpenAI SDK) ---

# Carregar instruções do arquivo .md (ou definir diretamente)
SUPORTE_INSTRUCTIONS = """
Você é o Suporte Administrativo da FSTech Consulting Agency. Sua função é garantir a satisfação e retenção do cliente após a venda e implementação. Você gerencia o atendimento pós-venda, agenda check-ins, administra assinaturas, coleta feedback e fornece suporte geral para questões não-técnicas.

Responsabilidades Principais:
*   Atendimento ao Cliente: Ponto de contato para suporte pós-venda e administrativo.
*   Agendamento: Gerenciar agenda de check-ins periódicos.
*   Gestão de Assinaturas: Monitorar e gerenciar planos de assinatura.
*   Processamento de Pagamentos: Acompanhar faturas e pagamentos.
*   Coleta de Feedback: Enviar pesquisas e coletar feedback.
*   Gestão de Documentação: Organizar registros de clientes e contratos.
*   Suporte Interno: Auxiliar outros agentes com tarefas administrativas.

Diretrizes Gerais:
*   Seja proativo na comunicação.
*   Mantenha registros organizados.
*   Priorize a resolução rápida.
*   Busque melhorar a experiência do cliente.

Use as ferramentas disponíveis para cumprir suas responsabilidades.
"""

# Lista de ferramentas disponíveis para este agente
SUPORTE_TOOLS = [
    client_support_bot.handle_client_support_query,
    appointment_scheduler_manager.manage_appointment,
    subscription_tracker.track_subscription,
    feedback_collector.collect_feedback
]

# Função para criar a definição do agente
def create_suporte_agent_definition():
    """Retorna a definição do Agente Suporte Administrativo."""
    return {
        "name": "Suporte Administrativo Agent - FSTech",
        "instructions": SUPORTE_INSTRUCTIONS,
        "tools": SUPORTE_TOOLS
    }

# --- Lógica de Execução (Exemplo Simplificado - Sem LLM Real) ---

def run_suporte_task(task_description: str, context: dict = None):
    """Simula a execução de uma tarefa pelo Agente Suporte (sem LLM real)."""
    agent_def = create_suporte_agent_definition()
    context = context or {}
    print(f"--- Executando Tarefa com Agente: {agent_def[	name	]} ---")
    print(f"Tarefa: {task_description}")
    print(f"Contexto: {context}")
    print(f"Instruções do Agente: {agent_def[	instructions	][:100]}...")
    print("Ferramentas Disponíveis:")
    for tool_func in agent_def[	tools	]:
        print(f"- {tool_func.__name__}")

    # Simulação MUITO simplificada da seleção de ferramenta
    selected_tool = None
    args = {}
    task_lower = task_description.lower()

    if "suporte" in task_lower or "pergunta" in task_lower or "dúvida" in task_lower:
        selected_tool = client_support_bot.handle_client_support_query
        args = {
            "query": context.get("query", task_description),
            "client_id": context.get("client_id")
        }
    elif "agendar" in task_lower or "reunião" in task_lower or "marcar" in task_lower:
        selected_tool = appointment_scheduler_manager.manage_appointment
        args = {
            "action": context.get("action", "book_appointment"), # Default to booking
            "attendees": context.get("attendees", []),
            "subject": context.get("subject", "Reunião FSTech"),
            "date_preference": context.get("date_preference"),
            "duration_minutes": context.get("duration", 30)
        }
    elif "assinatura" in task_lower or "plano" in task_lower or "cobrança" in task_lower:
        selected_tool = subscription_tracker.track_subscription
        args = {
            "action": context.get("action", "view_subscription"), # Default to view
            "client_id": context.get("client_id"),
            "subscription_id": context.get("subscription_id"),
            "new_status": context.get("new_status")
        }
    elif "feedback" in task_lower or "opinião" in task_lower or "classificação" in task_lower:
        selected_tool = feedback_collector.collect_feedback
        args = {
            "client_id": context.get("client_id", "UNKNOWN"),
            "project_id": context.get("project_id"),
            "feedback_text": context.get("feedback_text", task_description),
            "rating": context.get("rating")
        }

    if selected_tool:
        print(f"\n>>> LLM (Simulado) decidiu usar a ferramenta: {selected_tool.__name__}")
        try:
            result = selected_tool(**args)
            print("\n--- Resultado da Ferramenta ---")
            print(result)
            print("---------------------------")
            return result, context
        except Exception as e:
            error_message = f"Erro ao executar ferramenta {selected_tool.__name__}: {e}"
            print(error_message)
            return error_message, context
    else:
        no_tool_message = "Nenhuma ferramenta administrativa apropriada encontrada (simulado). Tarefa pode exigir análise manual ou encaminhamento."
        print(f"\n{no_tool_message}")
        return no_tool_message, context

# Exemplo de execução de tarefa
if __name__ == "__main__":
    contexto_suporte = {"client_id": "SMB-STARTUP", "query": "Como atualizo meu cartão de crédito?"}
    run_suporte_task("Responder dúvida sobre pagamento", contexto_suporte)
    print("\n=========================================\n")

    contexto_agenda = {
        "action": "book_appointment",
        "attendees": ["cliente_feliz@example.com", "coordenador@fstech.example.com"],
        "subject": "Check-in Trimestral Projeto Y",
        "date_preference": "2025-06-10"
    }
    run_suporte_task("Agendar reunião de check-in", contexto_agenda)
    print("\n=========================================\n")

    contexto_assinatura = {"action": "view_subscription", "subscription_id": "sub-789"}
    run_suporte_task("Verificar detalhes da assinatura sub-789", contexto_assinatura)
    print("\n=========================================\n")

    contexto_feedback = {
        "client_id": "VIP-BIGCORP",
        "project_id": "PROJ-DATA-VIZ",
        "feedback_text": "A visualização de dados ficou excelente!",
        "rating": 5
    }
    run_suporte_task("Registrar feedback positivo do cliente VIP", contexto_feedback)

