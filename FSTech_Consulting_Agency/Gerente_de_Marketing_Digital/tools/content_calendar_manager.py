# Ferramenta: Gerenciador de Calendário de Conteúdo

import datetime
import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Simulação de um calendário de conteúdo (em memória)
CONTENT_CALENDAR = {}

@function_tool
def manage_content_calendar(action: str, date: str = None, topic: str = None, channel: str = None, content_id: str = None) -> str:
    """Gerencia o calendário de conteúdo de marketing (adicionar, visualizar, atualizar).

    Use esta ferramenta para agendar novos posts, visualizar o calendário para uma data
    ou período, ou atualizar o status de um item de conteúdo existente.

    Args:
        action: A ação a ser realizada (	add_item	, 	view_date	, 	update_status	).
        date: (Obrigatório para 	add_item	 e 	view_date	) A data no formato AAAA-MM-DD.
        topic: (Obrigatório para 	add_item	) O tópico ou título do conteúdo.
        channel: (Obrigatório para 	add_item	) O canal de publicação (ex: 	Blog	, 	LinkedIn	, 	Twitter	).
        content_id: (Obrigatório para 	update_status	) O ID do item de conteúdo a ser atualizado.
        # status: (Implícito para update_status, poderia ser um arg) Novo status (ex: 	Draft	, 	Scheduled	, 	Published	)

    Returns:
        Uma string com a confirmação da ação, a lista de itens para a data, ou uma mensagem de erro.
    """
    # Validação básica
    if not action in ["add_item", "view_date", "update_status"]:
        return "Erro: Ação inválida. Use 	add_item	, 	view_date	 ou 	update_status	."

    if (action == "add_item" or action == "view_date") and not date:
        return f"Erro: Para {action}, a data (date no formato AAAA-MM-DD) é obrigatória."
    
    if action == "add_item" and (not topic or not channel):
        return "Erro: Para 	add_item	, tópico (topic) e canal (channel) são obrigatórios."

    if action == "update_status" and not content_id:
        return "Erro: Para 	update_status	, o ID do conteúdo (content_id) é obrigatório."

    try:
        if date:
            date_obj = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        return "Erro: Formato inválido para data. Use AAAA-MM-DD."

    print(f"Executando ação no calendário de conteúdo: {action}...")

    if action == "add_item":
        new_content_id = f"content-{random.randint(1000, 9999)}"
        item = {
            "id": new_content_id,
            "topic": topic,
            "channel": channel,
            "status": "Draft", # Status inicial
            "scheduled_date": date
        }
        if date not in CONTENT_CALENDAR:
            CONTENT_CALENDAR[date] = []
        CONTENT_CALENDAR[date].append(item)
        confirmation = f"Item de conteúdo adicionado ao calendário para {date}:\nID: {new_content_id}\nTópico: {topic}\nCanal: {channel}\nStatus: Draft"
        print(confirmation)
        return confirmation

    elif action == "view_date":
        items_on_date = CONTENT_CALENDAR.get(date, [])
        if items_on_date:
            response = f"Itens de conteúdo agendados para {date}:\n"
            for item in items_on_date:
                response += f"- ID: {item[	 id	]}, Tópico: {item[	 topic	]}, Canal: {item[	 channel	]}, Status: {item[	 status	]}\n"
            return response
        else:
            return f"Nenhum item de conteúdo encontrado para {date}."

    elif action == "update_status":
        # Simulação: Atualizar status (requer encontrar o item pelo ID)
        found = False
        new_status = "Published" # Simular atualização para Publicado
        for d, items in CONTENT_CALENDAR.items():
            for item in items:
                if item["id"] == content_id:
                    old_status = item["status"]
                    item["status"] = new_status
                    found = True
                    confirmation = f"Status do item de conteúdo {content_id} atualizado de 	{old_status}	 para 	{new_status}	."
                    print(confirmation)
                    return confirmation
        if not found:
            return f"Erro: Item de conteúdo com ID {content_id} não encontrado."

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    print("--- Adicionar Item 1 ---")
    print(manage_content_calendar(action="add_item", date="2025-05-10", topic="Benefícios da IA para PMEs", channel="Blog"))
    print("\n--- Adicionar Item 2 ---")
    item2_resp = manage_content_calendar(action="add_item", date="2025-05-10", topic="Dica rápida de automação", channel="LinkedIn")
    print(item2_resp)
    # Extrair ID simulado para teste de update
    item2_id = None
    if "ID:" in item2_resp:
        try:
            item2_id = item2_resp.split("ID:")[1].split("\n")[0].strip()
        except:
            pass

    print("\n--- Ver Calendário ---")
    print(manage_content_calendar(action="view_date", date="2025-05-10"))
    print("\n--- Ver Calendário (Vazio) ---")
    print(manage_content_calendar(action="view_date", date="2025-05-11"))

    if item2_id:
        print("\n--- Atualizar Status Item 2 ---")
        print(manage_content_calendar(action="update_status", content_id=item2_id))
        print("\n--- Ver Calendário Atualizado ---")
        print(manage_content_calendar(action="view_date", date="2025-05-10"))
    else:
        print("\n--- Teste de Atualização Ignorado (ID não extraído) ---")

    print("\n--- Calendário Completo Simulado ---")
    import json
    print(json.dumps(CONTENT_CALENDAR, indent=2))

