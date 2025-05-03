# Ferramenta: Criador de Lead no CRM (ClickUp)

import os

# Importar utilitário ClickUp
from FSTech_Consulting_Agency.utils.clickup_client import create_crm_task, get_clickup_client

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def create_crm_lead(lead_name: str, description: str = None, assignee_email: str = None) -> str:
    """Cria uma nova tarefa de lead na lista de CRM do ClickUp.

    Use esta ferramenta quando um novo lead qualificado for identificado pelo marketing,
    para registrá-lo no CRM (ClickUp) com o status inicial "Oportunidade Identificada".

    Args:
        lead_name: O nome do lead ou da oportunidade (será o nome da tarefa no ClickUp).
        description: (Opcional) Detalhes adicionais sobre o lead ou a oportunidade.
        assignee_email: (Opcional) Email do membro da equipe FSTech a ser atribuído inicialmente (ex: Consultor de Diagnóstico).

    Returns:
        Uma string com o ID da tarefa criada no ClickUp ou uma mensagem de erro.
    """
    if not lead_name:
        return "Erro: Nome do lead (lead_name) é obrigatório."

    assignee_id = None
    if assignee_email:
        # Tentar encontrar o ID do usuário no ClickUp a partir do email
        # Esta parte requer uma função adicional no clickup_client.py ou lógica aqui
        # Por enquanto, vamos simular ou exigir o ID numérico se necessário
        print(f"Aviso: A busca de ID de usuário por email ({assignee_email}) não está implementada. Atribuição pode falhar se a API exigir ID numérico.")
        # Em um cenário real, você buscaria o ID do usuário via API:
        # try:
        #     client = get_clickup_client()
        #     teams = client.get_teams() # Assume que o usuário está em alguma equipe acessível
        #     if teams:
        #         # Itera sobre times e membros para encontrar o ID
        #         # ... lógica de busca ...
        #         pass 
        # except Exception as e:
        #     print(f"Erro ao buscar ID do usuário para {assignee_email}: {e}")
        pass # Deixa assignee_id como None por enquanto

    try:
        # Chamar a função utilitária para criar a tarefa
        task_id = create_crm_task(task_name=lead_name, description=description, assignee_id=assignee_id)
        
        if task_id:
            return f"Lead 	{lead_name}	 criado com sucesso no CRM ClickUp. ID da Tarefa: {task_id}"
        else:
            return f"Falha ao criar lead 	{lead_name}	 no CRM ClickUp."
            
    except (ValueError, ConnectionError) as e:
        return f"Erro de configuração ou conexão ao criar lead no ClickUp: {e}"
    except Exception as e:
        return f"Erro inesperado ao criar lead no ClickUp: {e}"

# Exemplo de uso (requer .env configurado)
if __name__ == "__main__":
    try:
        print("--- Criar Lead 1 (Simples) ---")
        print(create_crm_lead(lead_name="Lead Teste Marketing 1"))

        print("\n--- Criar Lead 2 (Com Descrição) ---")
        print(create_crm_lead(lead_name="Lead Teste Marketing 2 - Empresa Grande", description="Contato via formulário do site, interessado em IA."))
        
        # print("\n--- Criar Lead 3 (Com Atribuição - Requer ID ou busca implementada) ---")
        # print(create_crm_lead(lead_name="Lead Teste Marketing 3 - Atribuído", assignee_email="consultor@fstech.example.com"))

    except (ValueError, ConnectionError) as e:
         print(f"\nErro durante o teste (configuração ou conexão): {e}")
    except Exception as e:
         print(f"\nOcorreu um erro inesperado durante os testes: {e}")

