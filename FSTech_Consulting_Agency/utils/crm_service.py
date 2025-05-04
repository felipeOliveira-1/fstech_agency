from FSTech_Consulting_Agency.utils.clickup_client import create_crm_task, update_task_status
from FSTech_Consulting_Agency.utils.app_helpers import add_log

def create_lead_in_crm(session_state, task_name, description):
    """
    Cria um novo lead no CRM (ClickUp) e retorna o ID da tarefa criada.
    
    Args:
        session_state: Objeto session_state do Streamlit
        task_name: Nome da tarefa/oportunidade
        description: Descrição detalhada da tarefa
        
    Returns:
        str: ID da tarefa criada no CRM ou None em caso de erro
    """
    try:
        task_id = create_crm_task(task_name, description)
        if task_id:
            add_log(session_state, f"Lead criado no CRM ClickUp com ID: {task_id}", "CRM")
            return task_id
        else:
            add_log(session_state, "Não foi possível criar o registro no CRM. Continuando sem integração.", "Sistema")
            return None
    except Exception as e:
        add_log(session_state, f"Erro ao criar lead no CRM: {str(e)}", "Sistema")
        return None

def update_crm_status(session_state, task_id, status):
    """
    Atualiza o status de uma tarefa no CRM (ClickUp).
    
    Args:
        session_state: Objeto session_state do Streamlit
        task_id: ID da tarefa no CRM
        status: Novo status a ser definido
        
    Returns:
        bool: True se o status foi atualizado com sucesso, False caso contrário
    """
    if not task_id:
        return False
        
    try:
        update_task_status(task_id, status)
        add_log(session_state, f"Status atualizado no CRM para '{status}'", "CRM")
        return True
    except Exception as e:
        add_log(session_state, f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
        return False
