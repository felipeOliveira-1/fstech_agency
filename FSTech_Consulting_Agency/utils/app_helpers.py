from datetime import datetime

def add_log(session_state, message, agent="Sistema"):
    """
    Adiciona um log ao histórico de ações com timestamp atual.
    
    Args:
        session_state: Objeto session_state do Streamlit
        message: Mensagem para registrar no log
        agent: Nome do agente ou origem da mensagem
    """
    timestamp = datetime.now().strftime("%H:%M:%S")
    session_state.logs.append({
        "timestamp": timestamp,
        "agent": agent,
        "message": message
    })

def reset_session(session_state):
    """
    Reseta todas as variáveis da sessão para seus valores padrão.
    
    Args:
        session_state: Objeto session_state do Streamlit
    """
    session_state.process_started = False
    session_state.current_step = 0
    session_state.client_name = ""
    session_state.client_company = ""
    session_state.client_email = ""
    session_state.briefing = ""
    session_state.objetivo_cliente = ""
    session_state.lead_source = ""
    session_state.logs = []
    session_state.task_id = None
    session_state.client_message = ""
    session_state.proposal_content = ""
    session_state.arquitetura_proposta = ""
    session_state.roi_summary = ""
    session_state.meeting_id = None
    session_state.reuniao_transcricao = ""

def initialize_session_state(session_state):
    """
    Inicializa as variáveis da sessão caso ainda não existam.
    
    Args:
        session_state: Objeto session_state do Streamlit
    """
    if 'process_started' not in session_state:
        session_state.process_started = False
    if 'current_step' not in session_state:
        session_state.current_step = 0
    if 'client_name' not in session_state:
        session_state.client_name = ""
    if 'client_company' not in session_state:
        session_state.client_company = ""
    if 'client_email' not in session_state:
        session_state.client_email = ""
    if 'briefing' not in session_state:
        session_state.briefing = ""
    if 'lead_source' not in session_state:
        session_state.lead_source = ""
    if 'objetivo_cliente' not in session_state:
        session_state.objetivo_cliente = ""
    if 'logs' not in session_state:
        session_state.logs = []
    if 'task_id' not in session_state:
        session_state.task_id = None
    if 'client_message' not in session_state:
        session_state.client_message = ""
    if 'proposal_content' not in session_state:
        session_state.proposal_content = ""
    if 'arquitetura_proposta' not in session_state:
        session_state.arquitetura_proposta = ""
    if 'roi_summary' not in session_state:
        session_state.roi_summary = ""
    if 'meeting_id' not in session_state:
        session_state.meeting_id = None
    if 'reuniao_transcricao' not in session_state:
        session_state.reuniao_transcricao = ""
