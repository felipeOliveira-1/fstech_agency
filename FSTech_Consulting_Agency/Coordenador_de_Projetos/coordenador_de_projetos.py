# Agente: Coordenador de Projetos

import json
import datetime

# Importar ferramentas refatoradas
from .tools import (
    project_timeline_manager, 
    task_assignment_manager, 
    progress_tracker, # Refatorado para ClickUp
    client_update_sender,
    crm_project_status_updater # Nova ferramenta adicionada
)

# --- Definição do Agente (Estilo OpenAI SDK) ---

# Carregar instruções do arquivo .md (ou definir diretamente)
COORDENADOR_INSTRUCTIONS = """
Você é o Coordenador de Projetos da FSTech Consulting Agency. Sua função é orquestrar a execução dos projetos, desde o handover do Consultor até a entrega final. Você define cronogramas, atribui tarefas, monitora progresso, gerencia recursos, facilita comunicação e mantém o cliente informado. Você também atualiza o status principal do projeto no CRM (ClickUp) para 	Projeto em Andamento	 ou 	Projeto Concluído	.

Responsabilidades Principais:
*   Planejamento do Projeto: Criar plano detalhado (cronograma, marcos, recursos).
*   Gestão de Tarefas: Quebrar projeto em tarefas e atribuir aos agentes (pode ser em lista de projeto separada no ClickUp).
*   Monitoramento de Progresso: Acompanhar andamento de tarefas individuais no ClickUp, identificar desvios, tomar ações.
*   Atualização Status CRM: Marcar a tarefa principal do projeto no CRM como 	Projeto em Andamento	 ou 	Projeto Concluído	.
*   Gerenciamento de Riscos: Identificar e mitigar riscos.
*   Comunicação: Facilitar comunicação entre stakeholders, ser ponto de contato do cliente.
*   Gestão de Recursos: Garantir alocação eficiente.
*   Relatórios de Status: Preparar e enviar atualizações regulares.
*   Controle de Qualidade: Colaborar para garantir qualidade das entregas.
*   Encerramento do Projeto: Formalizar conclusão e handover para Suporte.

Diretrizes Gerais:
*   Comunicação clara e proativa.
*   Organização e detalhismo.
*   Antecipar problemas, buscar soluções colaborativas.
*   Gerenciar escopo, prazo e orçamento.

Use as ferramentas disponíveis para cumprir suas responsabilidades.
"""

# Lista de ferramentas disponíveis para este agente
COORDENADOR_TOOLS = [
    project_timeline_manager.manage_project_timeline, # Pode precisar integrar com ClickUp também
    task_assignment_manager.manage_task_assignment, # Pode precisar integrar com ClickUp também
    progress_tracker.track_task_progress, # Integrado com ClickUp
    client_update_sender.send_client_update,
    crm_project_status_updater.update_crm_project_status # Integrado com ClickUp
]

# Função para criar a definição do agente
def create_coordenador_agent_definition():
    """Retorna a definição do Agente Coordenador de Projetos."""
    return {
        "name": "Coordenador de Projetos Agent - FSTech",
        "instructions": COORDENADOR_INSTRUCTIONS,
        "tools": COORDENADOR_TOOLS
    }

# --- Lógica de Execução (Exemplo Simplificado - Sem LLM Real) ---

def run_coordenador_task(task_description: str, context: dict = None):
    """Simula a execução de uma tarefa pelo Coordenador (sem LLM real)."""
    agent_def = create_coordenador_agent_definition()
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

    # Adicionar lógica para selecionar a nova ferramenta crm_project_status_updater
    if "atualizar status projeto crm" in task_lower or "marcar projeto como" in task_lower:
        selected_tool = crm_project_status_updater.update_crm_project_status
        args = {
            "crm_task_id": context.get("crm_task_id", "UNKNOWN_CRM_TASK"),
            "status_key": context.get("status_key") # Ex: "projeto_em_andamento" ou "projeto_concluido"
        }
    elif "cronograma" in task_lower or "linha do tempo" in task_lower or "marco" in task_lower:
        selected_tool = project_timeline_manager.manage_project_timeline
        args = {
            "action": context.get("action", "view_timeline"),
            "project_id": context.get("project_id", "UNKNOWN_PROJ"),
            "milestone_name": context.get("milestone_name"),
            "new_date": context.get("new_date"),
            "new_status": context.get("new_status")
        }
    elif "tarefa" in task_lower and "atribuir" in task_lower or "criar task" in task_lower:
        # Nota: Esta ferramenta ainda não está integrada ao ClickUp
        selected_tool = task_assignment_manager.manage_task_assignment
        args = {
            "action": context.get("action", "view_project_tasks"),
            "project_id": context.get("project_id"),
            "task_id": context.get("task_id"),
            "description": context.get("description"),
            "assignee_email": context.get("assignee_email"),
            "due_date": context.get("due_date")
        }
    elif ("progresso" in task_lower or "status" in task_lower) and "tarefa" in task_lower:
        # Esta ferramenta foi refatorada para ClickUp
        selected_tool = progress_tracker.track_task_progress
        args = {
            "task_id": context.get("task_id", "UNKNOWN_TASK"),
            "new_status_key": context.get("status_key") # Ex: "concluida", "bloqueada"
        }
    elif "atualização" in task_lower or "update" in task_lower or "informar cliente" in task_lower:
        selected_tool = client_update_sender.send_client_update
        args = {
            "client_id": context.get("client_id", "UNKNOWN_CLIENT"),
            "project_id": context.get("project_id", "UNKNOWN_PROJ"),
            "update_summary": context.get("summary", "Atualização padrão."),
            "communication_channel": context.get("channel", "Email")
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
        no_tool_message = "Nenhuma ferramenta de coordenação apropriada encontrada (simulado). Tarefa pode exigir análise manual ou mais detalhes."
        print(f"\n{no_tool_message}")
        return no_tool_message, context

# Exemplo de execução de tarefa
if __name__ == "__main__":
    # IMPORTANTE: Substitua por IDs REAIS do seu ClickUp para testar
    TEST_CRM_TASK_ID = "EXISTING_CRM_TASK_ID_HERE" 
    TEST_REGULAR_TASK_ID = "EXISTING_REGULAR_TASK_ID_HERE"

    if TEST_CRM_TASK_ID != "EXISTING_CRM_TASK_ID_HERE":
        contexto_crm_proj_start = {"crm_task_id": TEST_CRM_TASK_ID, "status_key": "projeto_em_andamento"}
        run_coordenador_task("Marcar projeto CRM como iniciado", contexto_crm_proj_start)
        print("\n=========================================\n")
    else:
        print("### ATENÇÃO: Configure TEST_CRM_TASK_ID para testar atualização de status de projeto CRM. ###\n")

    if TEST_REGULAR_TASK_ID != "EXISTING_REGULAR_TASK_ID_HERE":
        contexto_task_progress = {"task_id": TEST_REGULAR_TASK_ID, "status_key": "concluida"}
        run_coordenador_task("Atualizar status da tarefa X para concluída no ClickUp", contexto_task_progress)
        print("\n=========================================\n")
    else:
        print("### ATENÇÃO: Configure TEST_REGULAR_TASK_ID para testar atualização de status de tarefa regular. ###\n")

    # Exemplo de ferramenta não integrada (ainda simulada)
    contexto_assign = {"action": "assign_task", "task_id": "task-sim-003", "assignee_email": "arquiteto@fstech.example.com", "due_date": "2025-06-05"}
    run_coordenador_task("Atribuir tarefa de API ao arquiteto (simulado)", contexto_assign)
    print("\n=========================================\n")

