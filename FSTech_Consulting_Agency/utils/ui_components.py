import streamlit as st
import pandas as pd
from datetime import datetime

def display_logs(logs_list):
    """
    Exibe os logs da aplicação em formato tabular.
    
    Args:
        logs_list: Lista de logs a serem exibidos
    """
    if not logs_list:
        st.info("Nenhuma ação registrada ainda.")
    else:
        logs_df = pd.DataFrame(logs_list)
        st.dataframe(
            logs_df,
            column_config={
                "timestamp": "Horário",
                "agent": "Agente",
                "message": "Mensagem"
            },
            hide_index=True
        )

def display_client_info(session_state):
    """
    Exibe as informações do cliente atual.
    
    Args:
        session_state: Objeto session_state do Streamlit
    """
    col1, col2, col3 = st.columns(3)
    col1.markdown(f"**Cliente:** {session_state.client_name}")
    col2.markdown(f"**Empresa:** {session_state.client_company}")
    col3.markdown(f"**Origem do Lead:** {session_state.lead_source}")
    
    st.markdown("**Briefing:**")
    st.markdown(f"```{session_state.briefing}```")
    
    if hasattr(session_state, 'objetivo_cliente') and session_state.objetivo_cliente:
        st.markdown(f"**Objetivo Principal:** {session_state.objetivo_cliente}")

def display_proposal(proposal_content):
    """
    Exibe a proposta comercial formatada.
    
    Args:
        proposal_content: Conteúdo da proposta em markdown
    """
    st.markdown(proposal_content)
    
    # Opções de exportação (podem ser expandidas)
    st.download_button(
        label="Baixar Proposta (Markdown)",
        data=proposal_content,
        file_name=f"proposta_comercial_{datetime.now().strftime('%Y%m%d')}.md",
        mime="text/markdown"
    )

def display_progress_steps(steps, current_step):
    """
    Exibe a barra de progresso com os passos do fluxo.
    
    Args:
        steps: Lista de nomes dos passos
        current_step: Índice do passo atual (1-based)
    """
    # Calcular progresso
    progress_value = current_step / len(steps)
    
    # Exibir barra de progresso
    st.progress(progress_value)
    
    # Exibir steps como bullets
    steps_html = ""
    for i, step in enumerate(steps):
        if i+1 < current_step:
            # Passo concluído
            steps_html += f"✅ {step} → "
        elif i+1 == current_step:
            # Passo atual
            steps_html += f"🔵 **{step}** → "
        else:
            # Passo futuro
            steps_html += f"⚪ {step} → "
    
    # Remover a última seta
    steps_html = steps_html.rstrip(" → ")
    
    # Exibir passos
    st.markdown(steps_html)

def form_client_input():
    """
    Exibe o formulário de entrada de dados do cliente.
    
    Returns:
        tuple: (client_name, client_company, client_email, briefing, lead_source, objetivo_cliente)
    """
    col1, col2 = st.columns(2)
    
    with col1:
        client_name = st.text_input(
            "Nome do Cliente", 
            st.session_state.client_name,
            placeholder="Ex: João Silva"
        )
        
        client_company = st.text_input(
            "Empresa", 
            st.session_state.client_company,
            placeholder="Ex: Empresa XYZ Ltda."
        )
        
        client_email = st.text_input(
            "Email do Cliente", 
            st.session_state.client_email,
            placeholder="Ex: joao.silva@empresa.com"
        )
        
        lead_source = st.selectbox(
            "Origem do Lead",
            ["LinkedIn", "Indicação", "Website", "Email Marketing", "Outro"],
            index=0 if not st.session_state.lead_source else ["LinkedIn", "Indicação", "Website", "Email Marketing", "Outro"].index(st.session_state.lead_source)
        )
    
    with col2:
        briefing = st.text_area(
            "Briefing Inicial", 
            st.session_state.briefing,
            height=120,
            placeholder="Descreva a solicitação ou projeto do cliente..."
        )
        
        objetivo_cliente = st.text_area(
            "Objetivo Principal do Cliente", 
            st.session_state.objetivo_cliente,
            height=80,
            placeholder="Qual o principal objetivo do cliente com este projeto?"
        )
    
    return client_name, client_company, client_email, briefing, lead_source, objetivo_cliente
