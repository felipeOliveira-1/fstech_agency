# Ferramenta: Gerenciador de Atribuição de Tarefas

import datetime
import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Simulação de uma base de dados de tarefas e atribuições (em memória)
TASKS_DB = {
    "task-001": {"project_id": "PROJ-AI-IMPL", "description": "Configurar ambiente de desenvolvimento", "assignee": "especialista@fstech.example.com", "due_date": "2025-04-10", "status": "Concluída"},
    "task-002": {"project_id": "PROJ-AI-IMPL", "description": "Implementar módulo de ingestão de dados", "assignee": "especialista@fstech.example.com", "due_date": "2025-05-15", "status": "Em Andamento"},
    "task-003": {"project_id": "PROJ-AI-IMPL", "description": "Desenvolver API de previsão", "assignee": None, "due_date": "2025-06-01", "status": "Pendente"}
}

# Simulação de membros da equipe
TEAM_MEMBERS = ["especialista@fstech.example.com", "arquiteto@fstech.example.com", "suporte@fstech.example.com"]

@function_tool
def manage_task_assignment(action: str, project_id: str = None, task_id: str = None, description: str = None, assignee_email: str = None, due_date: str = None) -> str:
    """Gerencia tarefas de projeto (criar, atribuir, visualizar).

    Use esta ferramenta para criar novas tarefas dentro de um projeto, atribuir tarefas
    a membros da equipe, ou visualizar tarefas existentes (por projeto ou por responsável).

    Args:
        action: A ação a ser realizada (	create_task	, 	assign_task	, 	view_project_tasks	, 	view_assignee_tasks	).
        project_id: (Obrigatório para 	create_task	 e 	view_project_tasks	) O ID do projeto.
        task_id: (Obrigatório para 	assign_task	) O ID da tarefa.
        description: (Obrigatório para 	create_task	) A descrição da nova tarefa.
        assignee_email: (Obrigatório para 	assign_task	 e 	view_assignee_tasks	) O email do membro da equipe.
        due_date: (Opcional para 	create_task	, 	assign_task	) A data de vencimento da tarefa (AAAA-MM-DD).

    Returns:
        Uma string com a confirmação da ação, a lista de tarefas ou uma mensagem de erro.
    """
    # Validação básica
    if not action in ["create_task", "assign_task", "view_project_tasks", "view_assignee_tasks"]:
        return "Erro: Ação inválida. Use 	create_task	, 	assign_task	, 	view_project_tasks	 ou 	view_assignee_tasks	."
    
    if (action == "create_task" or action == "view_project_tasks") and not project_id:
        return f"Erro: Para {action}, ID do projeto (project_id) é obrigatório."
    if action == "create_task" and not description:
        return "Erro: Para 	create_task	, descrição (description) é obrigatória."
    if action == "assign_task" and not task_id:
        return "Erro: Para 	assign_task	, ID da tarefa (task_id) é obrigatório."
    if (action == "assign_task" or action == "view_assignee_tasks") and not assignee_email:
         return f"Erro: Para {action}, email do responsável (assignee_email) é obrigatório."
    if assignee_email and assignee_email not in TEAM_MEMBERS:
        # Em um cenário real, poderia verificar contra uma lista de usuários válida
        print(f"Aviso: Email {assignee_email} não encontrado na lista de membros da equipe simulada.")
        # return f"Erro: Email {assignee_email} não é um membro válido da equipe."

    if due_date:
        try:
            datetime.datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            return "Erro: Formato inválido para due_date. Use AAAA-MM-DD."

    print(f"Executando ação de gerenciamento de tarefas: {action}...")

    if action == "create_task":
        new_task_id = f"task-{random.randint(100, 999)}"
        while new_task_id in TASKS_DB:
            new_task_id = f"task-{random.randint(100, 999)}"
        
        TASKS_DB[new_task_id] = {
            "project_id": project_id,
            "description": description,
            "assignee": None,
            "due_date": due_date,
            "status": "Pendente"
        }
        confirmation = f"Tarefa 	{new_task_id}	 criada com sucesso no projeto {project_id}: 	{description}	." + (f" Data de Vencimento: {due_date}" if due_date else "")
        print(confirmation)
        return confirmation

    elif action == "assign_task":
        if task_id in TASKS_DB:
            TASKS_DB[task_id]["assignee"] = assignee_email
            if due_date: # Permitir atualizar data ao atribuir
                TASKS_DB[task_id]["due_date"] = due_date
            confirmation = f"Tarefa {task_id} atribuída a {assignee_email}." + (f" Nova Data de Vencimento: {due_date}" if due_date else "")
            print(confirmation)
            # Em um cenário real, notificaria o assignee.
            return confirmation
        else:
            return f"Erro: Tarefa com ID {task_id} não encontrada."

    elif action == "view_project_tasks":
        project_tasks = []
        for task_id_key, task_details in TASKS_DB.items():
            if task_details["project_id"] == project_id:
                assignee = task_details["assignee"] or "Não atribuída"
                due = task_details["due_date"] or "N/A"
                project_tasks.append(f"- ID: {task_id_key}, Desc: {task_details[	 description	][:30]}..., Resp: {assignee}, Venc: {due}, Status: {task_details[	 status	]}")
        if project_tasks:
            return f"Tarefas encontradas para o projeto {project_id}:\n" + "\n".join(project_tasks)
        else:
            return f"Nenhuma tarefa encontrada para o projeto {project_id}."

    elif action == "view_assignee_tasks":
        assignee_tasks = []
        for task_id_key, task_details in TASKS_DB.items():
            if task_details["assignee"] == assignee_email:
                due = task_details["due_date"] or "N/A"
                assignee_tasks.append(f"- ID: {task_id_key}, Proj: {task_details[	 project_id	]}, Desc: {task_details[	 description	][:30]}..., Venc: {due}, Status: {task_details[	 status	]}")
        if assignee_tasks:
            return f"Tarefas encontradas para {assignee_email}:\n" + "\n".join(assignee_tasks)
        else:
            return f"Nenhuma tarefa encontrada para {assignee_email}."

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    proj_id = "PROJ-AI-IMPL"
    assignee = "especialista@fstech.example.com"

    print(f"--- Ver Tarefas Projeto ({proj_id}) ---")
    print(manage_task_assignment(action="view_project_tasks", project_id=proj_id))

    print(f"\n--- Ver Tarefas Responsável ({assignee}) ---")
    print(manage_task_assignment(action="view_assignee_tasks", assignee_email=assignee))

    print(f"\n--- Criar Nova Tarefa ({proj_id}) ---")
    print(manage_task_assignment(action="create_task", project_id=proj_id, description="Documentar arquitetura da API", due_date="2025-06-15"))

    print(f"\n--- Atribuir Tarefa task-003 ---")
    print(manage_task_assignment(action="assign_task", task_id="task-003", assignee_email="arquiteto@fstech.example.com"))

    print(f"\n--- Ver Tarefas Projeto Atualizado ({proj_id}) ---")
    print(manage_task_assignment(action="view_project_tasks", project_id=proj_id))

    print("\n--- Base de Tarefas Simulada Completa ---")
    import json
    print(json.dumps(TASKS_DB, indent=2))

