# Ferramenta: Gerenciador de Linha do Tempo do Projeto

import datetime
import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Simulação de dados de projetos (em memória)
PROJECT_TIMELINES = {
    "PROJ-AI-IMPL": {
        "name": "Implementação IA Cliente VIP-BIGCORP",
        "start_date": "2025-04-01",
        "end_date": "2025-07-31",
        "milestones": [
            {"name": "Kick-off", "date": "2025-04-05", "status": "Concluído"},
            {"name": "Fase 1 - Diagnóstico", "date": "2025-04-30", "status": "Concluído"},
            {"name": "Fase 2 - Implementação", "date": "2025-06-15", "status": "Em Andamento"},
            {"name": "Fase 3 - Testes", "date": "2025-07-15", "status": "Pendente"},
            {"name": "Go-live", "date": "2025-07-30", "status": "Pendente"}
        ]
    }
}

@function_tool
def manage_project_timeline(action: str, project_id: str, milestone_name: str = None, new_date: str = None, new_status: str = None) -> str:
    """Gerencia a linha do tempo de um projeto (visualizar, adicionar marco, atualizar marco).

    Use esta ferramenta para visualizar a linha do tempo de um projeto, adicionar novos
    marcos, ou atualizar a data ou status de marcos existentes.

    Args:
        action: A ação a ser realizada (	view_timeline	, 	add_milestone	, 	update_milestone	).
        project_id: O ID do projeto a ser gerenciado.
        milestone_name: (Obrigatório para 	add_milestone	 e 	update_milestone	) O nome do marco.
        new_date: (Obrigatório para 	add_milestone	, opcional para 	update_milestone	) A data do marco (AAAA-MM-DD).
        new_status: (Opcional para 	update_milestone	) O novo status do marco (ex: 	Pendente	, 	Em Andamento	, 	Concluído	, 	Atrasado	).

    Returns:
        Uma string com a linha do tempo, confirmação da ação ou uma mensagem de erro.
    """
    # Validação básica
    if not action in ["view_timeline", "add_milestone", "update_milestone"]:
        return "Erro: Ação inválida. Use 	view_timeline	, 	add_milestone	 ou 	update_milestone	."
    if not project_id:
        return "Erro: ID do projeto (project_id) é obrigatório."
    if (action == "add_milestone" or action == "update_milestone") and not milestone_name:
        return f"Erro: Para {action}, nome do marco (milestone_name) é obrigatório."
    if action == "add_milestone" and not new_date:
        return "Erro: Para 	add_milestone	, nova data (new_date) é obrigatória."
    if new_date:
        try:
            datetime.datetime.strptime(new_date, "%Y-%m-%d")
        except ValueError:
            return "Erro: Formato inválido para new_date. Use AAAA-MM-DD."

    print(f"Executando ação na linha do tempo do projeto {project_id}: {action}...")

    if project_id not in PROJECT_TIMELINES:
        return f"Erro: Projeto com ID {project_id} não encontrado."

    timeline = PROJECT_TIMELINES[project_id]

    if action == "view_timeline":
        response = f"Linha do Tempo do Projeto: {timeline[	name	]} ({project_id})\n"
        response += f"Início: {timeline[	start_date	]}, Fim: {timeline[	 end_date	]}\n\nMarcos:\n"
        for ms in timeline["milestones"]:
            response += f"- {ms[	name	]} (Data: {ms[	date	]}, Status: {ms[	status	]})\n"
        return response

    elif action == "add_milestone":
        # Verificar se marco já existe
        if any(ms["name"] == milestone_name for ms in timeline["milestones"]):
            return f"Erro: Marco 	{milestone_name}	 já existe no projeto {project_id}. Use 	update_milestone	 para modificar."
        
        new_milestone = {"name": milestone_name, "date": new_date, "status": "Pendente"} # Status inicial
        timeline["milestones"].append(new_milestone)
        # Ordenar marcos por data (simulado)
        timeline["milestones"].sort(key=lambda x: x["date"])
        confirmation = f"Marco 	{milestone_name}	 adicionado ao projeto {project_id} com data {new_date}."
        print(confirmation)
        return confirmation

    elif action == "update_milestone":
        found = False
        for ms in timeline["milestones"]:
            if ms["name"] == milestone_name:
                updated_fields = []
                if new_date:
                    ms["date"] = new_date
                    updated_fields.append(f"data para {new_date}")
                if new_status:
                    ms["status"] = new_status
                    updated_fields.append(f"status para {new_status}")
                
                if not updated_fields:
                     return f"Erro: Para 	update_milestone	, forneça 	new_date	 ou 	new_status	 para atualizar."

                # Reordenar se data mudou
                if new_date:
                     timeline["milestones"].sort(key=lambda x: x["date"])

                confirmation = f"Marco 	{milestone_name}	 no projeto {project_id} atualizado: { 	 e 	.join(updated_fields) }."
                print(confirmation)
                found = True
                return confirmation
        
        if not found:
            return f"Erro: Marco 	{milestone_name}	 não encontrado no projeto {project_id}."

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    proj_id = "PROJ-AI-IMPL"
    print(f"--- Ver Linha do Tempo ({proj_id}) ---")
    print(manage_project_timeline(action="view_timeline", project_id=proj_id))

    print(f"\n--- Adicionar Marco ({proj_id}) ---")
    print(manage_project_timeline(action="add_milestone", project_id=proj_id, milestone_name="Revisão Intermediária", new_date="2025-05-20"))

    print(f"\n--- Atualizar Marco ({proj_id}) ---")
    print(manage_project_timeline(action="update_milestone", project_id=proj_id, milestone_name="Fase 2 - Implementação", new_status="Concluído", new_date="2025-06-10"))

    print(f"\n--- Ver Linha do Tempo Atualizada ({proj_id}) ---")
    print(manage_project_timeline(action="view_timeline", project_id=proj_id))

    print("\n--- Tentar Adicionar Marco Existente ---")
    print(manage_project_timeline(action="add_milestone", project_id=proj_id, milestone_name="Kick-off", new_date="2025-04-06"))

    print("\n--- Tentar Atualizar Marco Inexistente ---")
    print(manage_project_timeline(action="update_milestone", project_id=proj_id, milestone_name="Marco Fantasma", new_status="Feito"))

