# Ferramenta: Rastreador de Progresso (Integrado ao ClickUp)

import datetime
import random

# Importar utilitário ClickUp
from FSTech_Consulting_Agency.utils.clickup_client import get_clickup_client, update_task_status, STATUS_MAP

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# NOTA: A visualização de progresso do projeto (view_project_progress) 
# precisaria buscar *todas* as tarefas do projeto via API, 
# o que pode ser mais complexo e lento. 
# Vamos focar em visualizar e atualizar status de tarefas individuais por enquanto.

@function_tool
def track_task_progress(task_id: str, new_status_key: str = None) -> str:
    """Rastreia ou atualiza o status de uma tarefa específica no ClickUp.

    Use esta ferramenta para verificar o status atual de uma tarefa no ClickUp
    ou para atualizar seu status para um novo valor definido no fluxo de trabalho.

    Args:
        task_id: O ID da tarefa no ClickUp.
        new_status_key: (Opcional) A chave do novo status desejado (ex: 	concluida	, 	projeto_em_andamento	, 	bloqueada	). Se omitido, apenas visualiza o status atual.

    Returns:
        Uma string com o status atual da tarefa, confirmação de atualização ou uma mensagem de erro.
    """
    if not task_id:
        return "Erro: ID da tarefa (task_id) é obrigatório."

    client = None
    try:
        client = get_clickup_client()
    except (ValueError, ConnectionError) as e:
        return f"Erro ao conectar ao ClickUp: {e}"
    
    if not client:
        return "Erro: Falha ao obter cliente ClickUp."

    # Se new_status_key for fornecido, tenta atualizar
    if new_status_key:
        print(f"Executando ação de atualização de status para tarefa {task_id}...")
        # Validar chave de status
        if new_status_key.lower() not in STATUS_MAP:
             return f"Erro: Chave de status inválida {new_status_key}. Chaves válidas: {', '.join(STATUS_MAP.keys())}."
        
        # Chamar a função utilitária para atualizar
        success = update_task_status(task_id, new_status_key)
        if success:
            target_status_name = STATUS_MAP.get(new_status_key.lower())
            return f"Status da tarefa {task_id} atualizado com sucesso para 	{target_status_name}	 no ClickUp."
        else:
            return f"Falha ao tentar atualizar o status da tarefa {task_id} no ClickUp."
    
    # Se new_status_key não for fornecido, apenas visualiza
    else:
        print(f"Executando ação de visualização de status para tarefa {task_id}...")
        try:
            task = client.get_task(task_id)
            if task and task.status:
                # Acessar o nome do status dentro do objeto status
                current_status_name = task.status.status 
                return f"Status atual da Tarefa {task_id} (	{task.name[:30]}...	) no ClickUp: {current_status_name}"
            elif task:
                 return f"Tarefa {task_id} encontrada, mas sem informação de status clara na resposta: {task}"
            else:
                return f"Erro: Tarefa com ID {task_id} não encontrada no ClickUp."
        except Exception as e:
            return f"Erro ao buscar status da tarefa {task_id} no ClickUp: {e}"

# Exemplo de uso (requer .env configurado e ID de tarefa válido)
if __name__ == "__main__":
    # IMPORTANTE: Substitua por um ID de tarefa REAL do seu ClickUp para testar
    TEST_CLICKUP_TASK_ID = "EXISTING_TASK_ID_HERE" 

    if TEST_CLICKUP_TASK_ID == "EXISTING_TASK_ID_HERE":
        print("### ATENÇÃO: Configure a variável TEST_CLICKUP_TASK_ID com um ID de tarefa real do seu ClickUp para executar os testes. ###")
    else:
        try:
            print(f"--- Ver Status Tarefa ({TEST_CLICKUP_TASK_ID}) ---")
            print(track_task_progress(task_id=TEST_CLICKUP_TASK_ID))

            print(f"\n--- Atualizar Status Tarefa ({TEST_CLICKUP_TASK_ID}) para Em Andamento ---")
            # Use uma chave válida do STATUS_MAP em clickup_client.py
            print(track_task_progress(task_id=TEST_CLICKUP_TASK_ID, new_status_key="em_andamento")) 

            print(f"\n--- Ver Status Tarefa Atualizado ({TEST_CLICKUP_TASK_ID}) ---")
            print(track_task_progress(task_id=TEST_CLICKUP_TASK_ID))
            
            print(f"\n--- Tentar Atualizar Status Inválido ({TEST_CLICKUP_TASK_ID}) ---")
            print(track_task_progress(task_id=TEST_CLICKUP_TASK_ID, new_status_key="feito_errado"))

        except (ValueError, ConnectionError) as e:
             print(f"\nErro durante o teste (configuração ou conexão): {e}")
        except Exception as e:
             print(f"\nOcorreu um erro inesperado durante os testes: {e}")

