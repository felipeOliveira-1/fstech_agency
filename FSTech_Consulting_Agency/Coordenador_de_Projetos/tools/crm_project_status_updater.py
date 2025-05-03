# Ferramenta: Atualizador de Status do Projeto no CRM (ClickUp)

# Importar utilitário ClickUp
from FSTech_Consulting_Agency.utils.clickup_client import update_task_status, STATUS_MAP

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def update_crm_project_status(crm_task_id: str, status_key: str) -> str:
    """Atualiza o status da tarefa principal do projeto na lista de CRM do ClickUp.

    Use esta ferramenta para indicar o início ou a conclusão de um projeto,
    atualizando a tarefa correspondente no CRM ClickUp para 	Projeto em Andamento	
    ou 	Projeto Concluído	.

    Args:
        crm_task_id: O ID da tarefa na lista de CRM do ClickUp que representa o projeto.
        status_key: A chave do novo status desejado (	projeto_em_andamento	 ou 	projeto_concluido	).

    Returns:
        Uma string confirmando a atualização do status ou uma mensagem de erro.
    """
    if not crm_task_id:
        return "Erro: ID da tarefa do CRM (crm_task_id) é obrigatório."
    if not status_key:
        return "Erro: Chave do novo status (status_key) é obrigatória."

    # Validar chave de status - permitir apenas as relevantes para o Coordenador
    allowed_keys = ["projeto_em_andamento", "projeto_concluido"]
    if status_key.lower() not in allowed_keys:
        return f"Erro: Chave de status inválida 	{status_key}	 para esta ferramenta. Use 	projeto_em_andamento	 ou 	projeto_concluido	."
    
    # Verificar se a chave existe no mapeamento geral (deve existir)
    if status_key.lower() not in STATUS_MAP:
        return f"Erro: Chave de status 	{status_key}	 não encontrada no mapeamento global STATUS_MAP."

    print(f"Executando atualização de status de projeto CRM para tarefa {crm_task_id} para 	{status_key}	...")

    try:
        # Chamar a função utilitária para atualizar
        success = update_task_status(crm_task_id, status_key)
        
        if success:
            target_status_name = STATUS_MAP.get(status_key.lower())
            return f"Status da tarefa principal do projeto (CRM ID: {crm_task_id}) atualizado com sucesso para 	{target_status_name}	 no ClickUp."
        else:
            return f"Falha ao tentar atualizar o status da tarefa principal do projeto (CRM ID: {crm_task_id}) no ClickUp."

    except (ValueError, ConnectionError) as e:
        return f"Erro de configuração ou conexão ao atualizar status no ClickUp: {e}"
    except Exception as e:
        return f"Erro inesperado ao atualizar status no ClickUp: {e}"

# Exemplo de uso (requer .env configurado e ID de tarefa CRM válido)
if __name__ == "__main__":
    # IMPORTANTE: Substitua por um ID de tarefa REAL da sua lista de CRM no ClickUp
    TEST_CRM_TASK_ID = "EXISTING_CRM_TASK_ID_HERE"

    if TEST_CRM_TASK_ID == "EXISTING_CRM_TASK_ID_HERE":
        print("### ATENÇÃO: Configure a variável TEST_CRM_TASK_ID com um ID de tarefa real da sua lista de CRM no ClickUp para executar os testes. ###")
    else:
        try:
            print(f"--- Atualizar Status Projeto CRM ({TEST_CRM_TASK_ID}) para Em Andamento ---")
            print(update_crm_project_status(crm_task_id=TEST_CRM_TASK_ID, status_key="projeto_em_andamento"))

            print(f"\n--- Atualizar Status Projeto CRM ({TEST_CRM_TASK_ID}) para Concluído ---")
            print(update_crm_project_status(crm_task_id=TEST_CRM_TASK_ID, status_key="projeto_concluido"))
            
            print(f"\n--- Tentar Atualizar Status Projeto CRM Inválido ({TEST_CRM_TASK_ID}) ---")
            print(update_crm_project_status(crm_task_id=TEST_CRM_TASK_ID, status_key="proposta_enviada")) # Chave inválida para esta ferramenta

        except (ValueError, ConnectionError) as e:
             print(f"\nErro durante o teste (configuração ou conexão): {e}")
        except Exception as e:
             print(f"\nOcorreu um erro inesperado durante os testes: {e}")

