import streamlit as st
import time
from datetime import datetime, timedelta
from FSTech_Consulting_Agency.utils.app_helpers import add_log
from FSTech_Consulting_Agency.Suporte_Administrativo.tools.appointment_scheduler_manager import schedule_meeting_calcom

def process_transcription_upload(file_upload, session_state):
    """
    Processa o upload de um arquivo de transcrição/resumo de reunião.
    
    Args:
        file_upload: Objeto UploadedFile do Streamlit
        session_state: Objeto session_state do Streamlit
        
    Returns:
        bool: Indica se o upload foi bem-sucedido
    """
    if file_upload is not None:
        try:
            # Ler conteúdo do arquivo
            content = file_upload.read().decode("utf-8")
            
            # Verificar se o conteúdo é válido
            if len(content.strip()) < 10:
                return False, "O arquivo de transcrição parece estar vazio ou conter muito pouco texto."
            
            # Salvar a transcrição no session_state
            session_state.reuniao_transcricao = content
            
            add_log(session_state, f"Transcrição da reunião recebida ({len(content)} caracteres)", "Sistema")
            return True, "Transcrição recebida com sucesso!"
            
        except Exception as e:
            return False, f"Erro ao processar arquivo: {str(e)}"
    
    return False, "Nenhum arquivo fornecido."

def schedule_client_meeting(client_name, client_email, briefing, session_state):
    """
    Agenda uma reunião com o cliente utilizando o Cal.com.
    
    Args:
        client_name: Nome do cliente
        client_email: Email do cliente
        briefing: Briefing inicial do cliente
        session_state: Objeto session_state do Streamlit
        
    Returns:
        tuple: (success_bool, message, meeting_data)
    """
    try:
        # Configurar parâmetros da reunião
        meeting_title = f"FSTech Agency - Reunião com {client_name}"
        meeting_description = f"Briefing: {briefing[:200]}..."
        
        # Data e hora proposta (1 dia útil a partir de agora)
        proposed_date = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")
        proposed_time = "14:00:00"  # 14h (horário comercial)
        
        # Chamar a API do Cal.com para agendar
        meeting_data = schedule_meeting_calcom(
            attendee_name=client_name,
            attendee_email=client_email,
            title=meeting_title,
            description=meeting_description,
            date=proposed_date,
            time=proposed_time
        )
        
        if meeting_data and 'id' in meeting_data:
            # Salvar ID da reunião no session_state
            session_state.meeting_id = meeting_data['id']
            
            # Adicionar log
            add_log(
                session_state, 
                f"Reunião agendada com {client_name} para {proposed_date} às {proposed_time}", 
                "Suporte Administrativo"
            )
            
            return True, "Reunião agendada com sucesso!", meeting_data
        else:
            return False, "Erro ao agendar reunião. API não retornou ID.", None
            
    except Exception as e:
        return False, f"Erro ao agendar reunião: {str(e)}", None

def generate_client_message(client_name):
    """
    Gera uma mensagem inicial para o cliente após receber o briefing.
    
    Args:
        client_name: Nome do cliente
        
    Returns:
        str: Mensagem formatada para o cliente
    """
    client_message = f"""Olá {client_name},

Muito obrigado por compartilhar seu projeto com a FSTech Consulting Agency!

Analisamos seu briefing inicial e estamos entusiasmados com as possibilidades. Para entendermos melhor suas necessidades e garantir que nossa proposta atenda perfeitamente suas expectativas, gostaríamos de agendar uma reunião para discutir mais detalhes.

Você teria disponibilidade para uma reunião esta semana? Caso positivo, indique alguns horários que sejam convenientes para você.

Estamos entusiasmados com a possibilidade de trabalhar juntos neste projeto!

Atenciosamente,
Equipe FSTech Consulting Agency"""

    return client_message
