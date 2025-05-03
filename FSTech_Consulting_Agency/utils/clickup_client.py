# Utilitário para interação com a API do ClickUp

import os
from dotenv import load_dotenv
import requests

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

CLICKUP_API_KEY = os.getenv("CLICKUP_API_KEY")

# IDs das Listas (fornecidos pelo usuário)
CRM_LIST_ID = "901311371093"
CONTACTS_LIST_ID = "901311372158"

# Mapeamento de Status (conforme fornecido pelo usuário)
STATUS_MAP = {
    "oportunidade_identificada": "Oportunidade Identificada",
    "contato_realizado": "Contato Realizado",
    "aguardando_futuro_contato": "Aguardando Futuro Contato",
    "reuniao_agendada": "Reunião Agendada",
    "reuniao_realizada": "Reunião Realizada",
    "proposta_enviada": "Proposta Enviada",
    "aguardando_resposta": "Aguardando Resposta",
    "proposta_aceita": "Proposta Aceita",
    "venda_realizada": "Venda Realizada",
    "projeto_em_andamento": "Projeto em Andamento",
    "projeto_concluido": "Projeto Concluído",
    "concluida": "Concluída"
}

def clickup_request(method, endpoint, **kwargs):
    """
    Helper to send requests to the ClickUp API.
    """
    if not CLICKUP_API_KEY:
        raise ValueError("Chave da API do ClickUp (CLICKUP_API_KEY) não encontrada no ambiente.")
    url = f"https://api.clickup.com/api/v2/{endpoint.lstrip('/')}"
    headers = kwargs.pop("headers", {})
    headers["Authorization"] = CLICKUP_API_KEY
    response = requests.request(method, url, headers=headers, **kwargs)
    try:
        response.raise_for_status()
    except Exception:
        raise
    return response.json()

def get_clickup_client():
    """Retorna uma instância inicializada do cliente ClickUp."""
    if not CLICKUP_API_KEY:
        raise ValueError("Chave da API do ClickUp (CLICKUP_API_KEY) não encontrada no ambiente.")
    try:
        response = clickup_request("GET", "team")
        return True
    except Exception as e:
        raise ConnectionError(f"Falha ao conectar ao ClickUp: {e}")

def update_task_status(task_id: str, status_key: str) -> bool:
    """Atualiza o status de uma tarefa no ClickUp.

    Args:
        task_id: O ID da tarefa no ClickUp.
        status_key: A chave do status desejado (ex: 'proposta_enviada', 'concluida').

    Returns:
        True se a atualização foi bem-sucedida, False caso contrário.
    """
    target_status_name = STATUS_MAP.get(status_key.lower())
    if not target_status_name:
        return False
    try:
        payload = {"status": target_status_name}
        response = clickup_request("PUT", f"task/{task_id}", json=payload)
        if response and isinstance(response, dict) and response.get('id') == task_id:
            return True
        else:
            return False
    except Exception:
        return False


def create_crm_task(task_name: str, description: str = None, assignee_id: int = None) -> str | None:
    """Cria uma nova tarefa na lista de CRM com status inicial.

    Args:
        task_name: O nome da nova tarefa (ex: Lead - Nome da Empresa).
        description: (Opcional) Descrição detalhada da tarefa.
        assignee_id: (Opcional) ID numérico do usuário do ClickUp a ser atribuído.

    Returns:
        O ID da tarefa criada ou None em caso de erro.
    """
    initial_status = STATUS_MAP.get("oportunidade_identificada")
    if not initial_status:
        return None
    payload = {
        "name": task_name,
        "status": initial_status,
    }
    if description:
        payload["description"] = description
    if assignee_id:
        payload["assignees"] = [assignee_id]
    try:
        task = clickup_request("POST", f"list/{CRM_LIST_ID}/task", json=payload)
        if task and isinstance(task, dict) and task.get('id'):
            return task['id']
        else:
            return None
    except Exception:
        return None


# Adicionar mais funções utilitárias conforme necessário (ex: get_task, find_contact, etc.)

# Exemplo de teste (requer .env configurado)
if __name__ == "__main__":
    try:
        # Teste 1: Criar uma tarefa de teste
        print("--- Teste: Criar Tarefa CRM ---")
        test_task_id = create_crm_task("Teste Lead - Empresa XYZ", "Lead de teste via API", assignee_id=None) # Coloque um ID de usuário válido se quiser testar atribuição
        
        if test_task_id:
            print(f"ID da tarefa de teste criada: {test_task_id}")
            
            # Teste 2: Atualizar status da tarefa criada
            print("\n--- Teste: Atualizar Status para Contato Realizado ---")
            success = update_task_status(test_task_id, "contato_realizado")
            print(f"Atualização de status bem-sucedida: {success}")

            # Teste 3: Atualizar para status inválido
            print("\n--- Teste: Atualizar para Status Inválido ---")
            success_invalid = update_task_status(test_task_id, "status_que_nao_existe")
            print(f"Atualização de status (inválido) bem-sucedida: {success_invalid}")
            
            # Limpeza (Opcional - deletar a tarefa de teste)
            # print("\n--- Limpeza: Deletando tarefa de teste ---")
            # try:
            #     client = get_clickup_client()
            #     if client:
            #         client.delete_task(test_task_id)
            #         print(f"Tarefa {test_task_id} deletada.")
            # except Exception as del_e:
            #     print(f"Erro ao deletar tarefa de teste: {del_e}")
        else:
            print("Não foi possível criar a tarefa de teste para prosseguir.")
            
    except ValueError as ve:
        print(f"Erro de configuração: {ve}")
    except ConnectionError as ce:
        print(f"Erro de conexão: {ce}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado durante os testes: {e}")

