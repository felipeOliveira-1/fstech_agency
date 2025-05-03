# Ferramenta: Gerenciador de Agendamentos (Cal.com)

import os
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv(dotenv_path="/home/ubuntu/FSTech_Consulting_Agency/.env")

# Constantes da API Cal.com
CALCOM_API_URL = "https://api.cal.com/v2"
CALCOM_API_KEY = os.getenv("CALCOM_API_KEY")

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def schedule_meeting_calcom(event_type_id: int, start_time: str, end_time: str, attendee_name: str, attendee_email: str, timezone: str = "America/Sao_Paulo", title: str = None, description: str = None) -> str:
    """Agenda uma nova reunião (booking) no Cal.com usando a API v2.

    Use esta ferramenta para criar um agendamento diretamente no Cal.com após
    o cliente confirmar a data/hora.

    Args:
        event_type_id: O ID numérico do tipo de evento no Cal.com (ex: reunião de diagnóstico).
        start_time: Data e hora de início no formato ISO 8601 (ex: "2025-05-10T14:00:00.000Z").
        end_time: Data e hora de término no formato ISO 8601 (ex: "2025-05-10T15:00:00.000Z").
        attendee_name: Nome completo do participante (cliente).
        attendee_email: Email do participante (cliente).
        timezone: (Opcional) Fuso horário da reunião (padrão: "America/Sao_Paulo").
        title: (Opcional) Título personalizado para o agendamento.
        description: (Opcional) Descrição ou notas adicionais para o agendamento.

    Returns:
        Uma string confirmando o agendamento com o ID ou uma mensagem de erro.
    """
    if not CALCOM_API_KEY:
        return "Erro: Chave da API do Cal.com (CALCOM_API_KEY) não configurada no arquivo .env."
    if not all([event_type_id, start_time, end_time, attendee_name, attendee_email]):
        return "Erro: Os parâmetros event_type_id, start_time, end_time, attendee_name e attendee_email são obrigatórios."

    headers = {
        "Authorization": f"Bearer {CALCOM_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "eventTypeId": event_type_id,
        "start": start_time,
        "end": end_time,
        "responses": {
            "name": attendee_name,
            "email": attendee_email
        },
        "timeZone": timezone,
        "language": "en",
        "status": "ACCEPTED",
        "metadata": {"source": "api"}
    }
    # Adicionar título e descrição se fornecidos
    if title:
        payload["title"] = title
    if description:
        payload["description"] = description

    endpoint = f"{CALCOM_API_URL}/bookings"

    print(f"Executando agendamento no Cal.com para {attendee_email} no evento {event_type_id}...")

    try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status() # Lança exceção para erros HTTP (4xx ou 5xx)

        booking_data = response.json()
        booking_id = booking_data.get("booking", {}).get("id")
        booking_uid = booking_data.get("booking", {}).get("uid")

        if booking_id or booking_uid:
            return f"Agendamento criado com sucesso no Cal.com! ID: {booking_id or booking_uid}"
        else:
            return f"Agendamento pode ter sido criado, mas ID não encontrado na resposta: {booking_data}"

    except requests.exceptions.RequestException as e:
        if e.response is not None:
            print("[DEBUG] Corpo da resposta de erro da Cal.com:")
            print(e.response.text)
            error_details = e.response.text
        else:
            error_details = str(e)
        return f"Erro de comunicação com a API do Cal.com: {error_details}"
    except Exception as e:
        return f"Erro inesperado ao agendar no Cal.com: {e}"

# Exemplo de uso (requer .env configurado e ID de tipo de evento válido)
if __name__ == "__main__":
    # IMPORTANTE: Substitua por um ID de Tipo de Evento REAL do seu Cal.com
    TEST_EVENT_TYPE_ID = 12345 # Substitua!
    # Datas e horas de exemplo (ajuste conforme necessário)
    start_iso = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0).isoformat() + "Z"
    end_iso = datetime.now().replace(hour=11, minute=0, second=0, microsecond=0).isoformat() + "Z"

    if TEST_EVENT_TYPE_ID == 12345:
        print("### ATENÇÃO: Configure a variável TEST_EVENT_TYPE_ID com um ID de tipo de evento real do seu Cal.com para executar os testes. ###")
    elif not CALCOM_API_KEY or CALCOM_API_KEY == "SUA_CHAVE_API_CALCOM_AQUI":
        print("### ATENÇÃO: Configure a variável CALCOM_API_KEY no arquivo .env com sua chave real do Cal.com para executar os testes. ###")
    else:
        try:
            print(f"--- Agendando reunião de teste no Cal.com (Evento ID: {TEST_EVENT_TYPE_ID}) ---")
            result = schedule_meeting_calcom(
                event_type_id=TEST_EVENT_TYPE_ID,
                start_time=start_iso,
                end_time=end_iso,
                attendee_name="Cliente Teste",
                attendee_email="cliente.teste@example.com",
                title="Reunião Diagnóstico FSTech (Teste API)"
            )
            print(result)
        except Exception as e:
            print(f"\nOcorreu um erro inesperado durante os testes: {e}")

