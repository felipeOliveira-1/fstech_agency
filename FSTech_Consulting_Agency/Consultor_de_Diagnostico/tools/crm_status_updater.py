# Ferramenta: Atualizador de Status do CRM (ClickUp)

# Importar utilitário ClickUp
from FSTech_Consulting_Agency.utils.clickup_client import update_task_status, STATUS_MAP

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def update_crm_task_status(crm_task_id: str, status_key: str) -> str:
    """Atualiza o status de uma tarefa específica na lista de CRM do ClickUp.

    Use esta ferramenta para mover um lead/oportunidade através das etapas do funil
    de vendas no CRM ClickUp (ex: de 'Contato Realizado' para 'Reunião Agendada').

    Args:
        crm_task_id: O ID da tarefa na lista de CRM do ClickUp.
        status_key: A chave do novo status desejado conforme o fluxo definido (ex: 'contato_realizado', 'reuniao_agendada', 'proposta_enviada', 'venda_realizada', etc.).

    Returns:
        Uma string confirmando a atualização do status ou uma mensagem de erro.
    """
    if not crm_task_id:
        return "Erro: ID da tarefa do CRM (crm_task_id) é obrigatório."
    if not status_key:
        return "Erro: Chave do novo status (status_key) é obrigatória."

    # Validar chave de status usando o mapeamento do utilitário
    if status_key.lower() not in STATUS_MAP:
        valid_keys = [k for k in STATUS_MAP.keys() if k not in ["pendente", "em_andamento", "bloqueada", "concluida"]] # Excluir status genéricos de tarefa
        return f"Erro: Chave de status CRM inválida {status_key}. Chaves válidas para CRM: {', '.join(valid_keys)}."

    print(f"Executando atualização de status CRM para tarefa {crm_task_id} para 	{status_key}	...")

    try:
        # Chamar a função utilitária para atualizar
        success = update_task_status(crm_task_id, status_key)
        
        if success:
            target_status_name = STATUS_MAP.get(status_key.lower())
            return f"Status da tarefa CRM {crm_task_id} atualizado com sucesso para 	{target_status_name}	 no ClickUp."
        else:
            return f"Falha ao tentar atualizar o status da tarefa CRM {crm_task_id} no ClickUp."

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
            print(f"--- Atualizar Status CRM ({TEST_CRM_TASK_ID}) para Reunião Agendada ---")
            print(update_crm_task_status(crm_task_id=TEST_CRM_TASK_ID, status_key="reuniao_agendada"))

            print(f"\n--- Atualizar Status CRM ({TEST_CRM_TASK_ID}) para Proposta Enviada ---")
            print(update_crm_task_status(crm_task_id=TEST_CRM_TASK_ID, status_key="proposta_enviada"))
            
            print(f"\n--- Tentar Atualizar Status CRM Inválido ({TEST_CRM_TASK_ID}) ---")
            print(update_crm_task_status(crm_task_id=TEST_CRM_TASK_ID, status_key="ganhou_o_projeto")) # Chave inválida

        except (ValueError, ConnectionError) as e:
             print(f"\nErro durante o teste (configuração ou conexão): {e}")
        except Exception as e:
             print(f"\nOcorreu um erro inesperado durante os testes: {e}")

