import streamlit as st
import os
import sys
import time
import json
import pandas as pd
from datetime import datetime, timedelta

# Add project folder to system path
project_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_path)

# Import the orquestrador and other modules
from FSTech_Consulting_Agency.orquestrador_fstech import (
    fluxo_fstech, 
    consultor_agent, 
    suporte_agent, 
    gerente_marketing_agent, 
    coordenador_agent, 
    especialista_agent, 
    arquiteto_agent, 
    ceo_agent,
    analista_roi_agent,
    orquestrador
)

# Import ClickUp and Cal.com integrations
from FSTech_Consulting_Agency.utils.clickup_client import create_crm_task, update_task_status
from FSTech_Consulting_Agency.Suporte_Administrativo.tools.appointment_scheduler_manager import schedule_meeting_calcom

# Create cache for session state
if 'process_started' not in st.session_state:
    st.session_state.process_started = False
if 'current_step' not in st.session_state:
    st.session_state.current_step = 0
if 'client_name' not in st.session_state:
    st.session_state.client_name = ""
if 'client_company' not in st.session_state:
    st.session_state.client_company = ""
if 'client_email' not in st.session_state:
    st.session_state.client_email = ""
if 'briefing' not in st.session_state:
    st.session_state.briefing = ""
if 'lead_source' not in st.session_state:
    st.session_state.lead_source = ""
if 'objetivo_cliente' not in st.session_state:
    st.session_state.objetivo_cliente = ""
if 'logs' not in st.session_state:
    st.session_state.logs = []
if 'task_id' not in st.session_state:
    st.session_state.task_id = None
if 'client_message' not in st.session_state:
    st.session_state.client_message = ""
if 'proposal_content' not in st.session_state:
    st.session_state.proposal_content = ""
if 'arquitetura_proposta' not in st.session_state:
    st.session_state.arquitetura_proposta = ""
if 'roi_summary' not in st.session_state:
    st.session_state.roi_summary = ""
if 'meeting_id' not in st.session_state:
    st.session_state.meeting_id = None

# Helper functions
def add_log(message, agent="Sistema"):
    timestamp = datetime.now().strftime("%H:%M:%S")
    st.session_state.logs.append({
        "timestamp": timestamp,
        "agent": agent,
        "message": message
    })

def reset_session():
    st.session_state.process_started = False
    st.session_state.current_step = 0
    st.session_state.client_name = ""
    st.session_state.client_company = ""
    st.session_state.client_email = ""
    st.session_state.briefing = ""
    st.session_state.objetivo_cliente = ""
    st.session_state.lead_source = ""
    st.session_state.logs = []
    st.session_state.task_id = None
    st.session_state.client_message = ""
    st.session_state.proposal_content = ""
    st.session_state.arquitetura_proposta = ""
    st.session_state.roi_summary = ""
    st.session_state.meeting_id = None

# Streamlit UI
st.set_page_config(
    page_title="FSTech Consulting Agency",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem !important;
        color: #0066cc;
    }
    .sub-header {
        font-size: 1.5rem !important;
        color: #4d4d4d;
    }
    .agent-card {
        border: 1px solid #e6e6e6;
        border-radius: 5px;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: #f9f9f9;
    }
    .agent-title {
        color: #0066cc;
        font-weight: bold;
    }
    .highlight {
        background-color: #ffd700;
        padding: 0.2rem;
        border-radius: 3px;
    }
    .footer {
        text-align: center;
        color: #888888;
        font-size: 0.8rem;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.markdown("<h1 class='main-header'>FSTech Agency</h1>", unsafe_allow_html=True)
st.sidebar.markdown("---")

# Display available agents in sidebar
st.sidebar.markdown("<h2 class='sub-header'>Agentes Disponíveis</h2>", unsafe_allow_html=True)
agents = {
    "Consultor de Diagnóstico": consultor_agent,
    "Suporte Administrativo": suporte_agent,
    "Gerente de Marketing Digital": gerente_marketing_agent,
    "Coordenador de Projetos": coordenador_agent,
    "Especialista Técnico": especialista_agent,
    "Arquiteto de Software": arquiteto_agent,
    "CEO": ceo_agent,
    "Analista de ROI": analista_roi_agent
}

selected_agent = st.sidebar.selectbox("Visualizar detalhes do agente:", list(agents.keys()))
with st.sidebar.expander(f"Detalhes: {selected_agent}", expanded=False):
    agent = agents[selected_agent]
    st.write(f"**Nome:** {agent.name}")
    
    # Get tools from the agent
    tools_list = []
    for tool in agent.tools:
        if hasattr(tool, "__name__"):
            tools_list.append(tool.__name__)
        elif hasattr(tool, "__func__"):
            tools_list.append(tool.__func__.__name__)
        else:
            tools_list.append(str(tool))
    
    st.write("**Ferramentas:**")
    for tool in tools_list:
        st.write(f"- {tool}")

# Main content
st.markdown("<h1 class='main-header'>FSTech Consulting Agency</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Sistema de Automação de Fluxo de Vendas</h2>", unsafe_allow_html=True)

# Criação das abas
tab_fluxo, tab_interacao, tab_logs, tab_sobre = st.tabs(["Fluxo Operacional", "Interação Livre", "Visualização de Logs", "Sobre"])

# Tab 1: Fluxo Operacional
with tab_fluxo:
    if not st.session_state.process_started:
        st.markdown("### Iniciar Novo Fluxo de Venda")
        st.markdown("Preencha as informações abaixo para iniciar o processo de venda automatizado.")
        
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.client_name = st.text_input("Nome do Cliente", st.session_state.client_name)
            st.session_state.client_company = st.text_input("Empresa do Cliente", st.session_state.client_company)
            st.session_state.client_email = st.text_input("Email do Cliente", st.session_state.client_email)
            st.session_state.lead_source = st.selectbox(
                "Origem do Lead", 
                ["LinkedIn", "Indicação", "Website", "Email Marketing", "Outro"],
                index=0 if not st.session_state.lead_source else ["LinkedIn", "Indicação", "Website", "Email Marketing", "Outro"].index(st.session_state.lead_source)
            )
        
        with col2:
            st.session_state.briefing = st.text_area(
                "Briefing Inicial", 
                st.session_state.briefing,
                height=120,
                placeholder="Descreva brevemente o projeto e necessidades do cliente..."
            )
            
            st.session_state.objetivo_cliente = st.text_area(
                "Objetivo Principal do Cliente", 
                st.session_state.objetivo_cliente,
                height=80,
                placeholder="Qual o principal objetivo do cliente com este projeto?"
            )
        
        if st.button("Iniciar Fluxo Operacional", type="primary"):
            if not st.session_state.client_name or not st.session_state.briefing:
                st.error("Por favor, preencha pelo menos o Nome do Cliente e o Briefing Inicial.")
            else:
                # Create ClickUp task for the new lead
                with st.spinner("Criando registro no CRM..."):
                    try:
                        task_name = f"Lead - {st.session_state.client_company or st.session_state.client_name}"
                        description = f"**Cliente:** {st.session_state.client_name}\n\n**Empresa:** {st.session_state.client_company}\n\n**Email:** {st.session_state.client_email}\n\n**Origem:** {st.session_state.lead_source}\n\n**Briefing:**\n{st.session_state.briefing}"
                        
                        task_id = create_crm_task(task_name, description)
                        if task_id:
                            st.session_state.task_id = task_id
                            add_log(f"Lead criado no CRM ClickUp com ID: {task_id}", "CRM")
                        else:
                            add_log("Não foi possível criar o registro no CRM. Continuando sem integração.", "Sistema")
                    except Exception as e:
                        add_log(f"Erro ao criar lead no CRM: {str(e)}", "Sistema")
                
                st.session_state.process_started = True
                st.session_state.current_step = 1
                add_log(f"Iniciando fluxo para cliente: {st.session_state.client_name} da empresa {st.session_state.client_company}")
                st.rerun()
    
    else:
        # Display current process steps
        steps = [
            "Briefing Inicial", 
            "Análise de Oportunidade", 
            "Agendamento de Reunião",
            "Análise Técnica", 
            "Pesquisa de Mercado", 
            "Geração de Proposta",
            "Envio e Negociação"
        ]
        
        step_progress = st.progress(st.session_state.current_step / len(steps))
        st.markdown(f"**Etapa Atual: {steps[st.session_state.current_step-1]}**")
        
        # Display client info
        st.markdown("### Informações do Cliente")
        col1, col2, col3 = st.columns(3)
        col1.markdown(f"**Cliente:** {st.session_state.client_name}")
        col2.markdown(f"**Empresa:** {st.session_state.client_company}")
        col3.markdown(f"**Origem do Lead:** {st.session_state.lead_source}")
        
        st.markdown("**Briefing:**")
        st.markdown(f"```{st.session_state.briefing}```")
        
        # Current step processing
        if st.session_state.current_step == 1:
            st.markdown("### Briefing Inicial")
            
            # Mostrar o briefing recebido
            with st.expander("Ver Briefing Recebido", expanded=True):
                st.markdown(f"**Cliente:** {st.session_state.client_name}")
                st.markdown(f"**Empresa:** {st.session_state.client_company}")
                st.markdown(f"**Email:** {st.session_state.client_email}")
                st.markdown("**Briefing:**")
                st.markdown(f"```{st.session_state.briefing}```")
            
            # Se a mensagem ainda não foi gerada, mostrar botão para análise
            if st.session_state.client_message == "":
                st.markdown("### Análise do Briefing")
                st.markdown("O consultor de diagnóstico irá analisar o briefing e criar uma mensagem personalizada para envio ao cliente.")
                
                if st.button("Analisar Briefing e Criar Mensagem", type="primary"):
                    with st.spinner("Analisando briefing e gerando mensagem de abordagem..."):
                        # Generate client message based on briefing - foco em marcar reunião
                        client_message = f"""Olá {st.session_state.client_name},

Muito obrigado por compartilhar seu projeto com a FSTech Consulting Agency!

Baseado no briefing inicial que você nos forneceu, identificamos oportunidades interessantes para auxiliar a {st.session_state.client_company} a alcançar seus objetivos tecnológicos.

Para que possamos compreender melhor as necessidades do seu projeto e apresentar uma solução personalizada, gostaríamos de agendar uma reunião de diagnóstico. 

Durante esta conversa, poderemos:
- Entender em detalhes os requisitos do projeto
- Esclarecer dúvidas técnicas
- Discutir timelines e expectativas
- Apresentar nossa abordagem para resolver seus desafios

Você teria disponibilidade para uma reunião esta semana? Caso positivo, indique alguns horários que sejam convenientes para você.

Estamos entusiasmados com a possibilidade de trabalhar juntos neste projeto!

Atenciosamente,
Equipe FSTech Consulting Agency"""
                        
                        # Save client message to session state
                        st.session_state.client_message = client_message
                        
                        add_log("Briefing analisado. Mensagem de abordagem criada.", "Consultor de Diagnóstico")
                        time.sleep(1)  # Pequena pausa para feedback visual
                        st.rerun()
            
            # Se a mensagem já foi gerada, apresentá-la para avaliação e possibilitar envio manual
            if st.session_state.client_message:
                st.markdown("### Mensagem para Envio ao Cliente")
                st.markdown("Revise a mensagem gerada pelo Consultor de Diagnóstico. Você pode editá-la conforme necessário.")
                
                message_box = st.text_area("Mensagem para o cliente", 
                                        st.session_state.client_message, 
                                        height=300)
                st.session_state.client_message = message_box
                
                # Facilitar a cópia da mensagem
                if st.button("Copiar Mensagem"):
                    st.code(st.session_state.client_message, language="")
                    st.success("⬆️ Copie a mensagem acima e envie ao cliente manualmente via email ou seu canal preferido.")
                
                # Solicitar confirmação de que a mensagem foi enviada
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Confirmar Envio da Mensagem", type="primary"):
                        # Atualizar status no ClickUp para Contato Realizado
                        if st.session_state.task_id:
                            try:
                                update_task_status(st.session_state.task_id, "contato_realizado")
                                add_log("Status atualizado no CRM para 'Contato Realizado'", "CRM")
                            except Exception as e:
                                add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                        
                        add_log("Mensagem de abordagem enviada ao cliente", "Consultor de Diagnóstico")
                        st.success("Mensagem enviada! Status atualizado no CRM. Aguarde a resposta do cliente para agendar a reunião.")
                
                # Se a reunião já foi agendada em resposta à mensagem
                st.markdown("### A reunião foi agendada?")
                st.markdown("Após o envio da mensagem, o cliente respondeu sobre a reunião?")
            
                # Solicitar informações de data e hora antes de confirmar agendamento
                if 'pre_agendamento' not in st.session_state:
                    st.session_state.pre_agendamento = False
                
                if not st.session_state.pre_agendamento:
                    st.markdown("#### Informações de Agendamento")
                    st.markdown("Por favor, informe a data e horário proposto pelo cliente para a reunião:")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        st.session_state.data_proposta = st.date_input("Data da Reunião Proposta")
                    with col2:
                        st.session_state.hora_proposta = st.time_input("Horário Proposto")
                    
                    st.session_state.local_reuniao = st.radio(
                        "Local da Reunião",
                        options=["Videoconferência", "Presencial", "Telefone"],
                        index=0
                    )
                    
                    if st.session_state.local_reuniao == "Presencial":
                        st.session_state.endereco_reuniao = st.text_input("Endereço da Reunião")
                    
                    if st.button("Salvar Informações de Agendamento", type="primary"):
                        data_hora = f"{st.session_state.data_proposta.strftime('%d/%m/%Y')} às {st.session_state.hora_proposta.strftime('%H:%M')}"
                        local = st.session_state.local_reuniao
                        if local == "Presencial" and st.session_state.endereco_reuniao:
                            local += f" - {st.session_state.endereco_reuniao}"
                        
                        st.session_state.info_reuniao = f"Reunião marcada para {data_hora}. Local: {local}"
                        add_log(f"Informações de agendamento registradas: {st.session_state.info_reuniao}", "Consultor de Diagnóstico")
                        st.session_state.pre_agendamento = True
                        st.rerun()
                
                # Exibir informações de agendamento e solicitar confirmação
                if st.session_state.pre_agendamento:
                    st.info(f"Informações de Agendamento: {st.session_state.info_reuniao}")
                    st.markdown("#### Confirmar Agendamento")
                    st.markdown("A reunião foi confirmada com estas informações?")
                    
                    col1, col2 = st.columns(2)
                    with col1:
                        if st.button("Sim, Reunião Confirmada✅", type="primary"):
                            # Update ClickUp task status
                            if st.session_state.task_id:
                                try:
                                    update_task_status(st.session_state.task_id, "reuniao_agendada")
                                    add_log("Status atualizado no CRM para 'Reunião Agendada'", "CRM")
                                except Exception as e:
                                    add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                            
                            # Salvar as informações de data e hora para reutilizar na etapa formal
                            st.session_state.data_reuniao_salva = st.session_state.data_proposta
                            st.session_state.hora_reuniao_salva = st.session_state.hora_proposta
                            st.session_state.local_reuniao_salvo = st.session_state.local_reuniao
                            if 'endereco_reuniao' in st.session_state:
                                st.session_state.endereco_reuniao_salvo = st.session_state.endereco_reuniao
                            
                            add_log(f"Reunião com o cliente confirmada: {st.session_state.info_reuniao}", "Consultor de Diagnóstico")
                            st.success("Reunião confirmada! Prosseguindo para o agendamento formal no sistema.")
                            time.sleep(1)  # Pequena pausa para feedback visual
                            st.session_state.current_step = 3  # Pula diretamente para o passo 3 (agendamento da reunião)
                            st.rerun()
                    
                    with col2:
                        col2a, col2b = st.columns(2)
                        with col2a:
                            if st.button("Editar Informações"):
                                st.session_state.pre_agendamento = False
                                st.rerun()
                        
                        with col2b:
                            if st.button("Não, Ainda Aguardando"):
                                add_log("Aguardando resposta do cliente para confirmação da reunião", "Sistema")
                                st.info("Continue acompanhando. Você pode retornar mais tarde para atualizar o status.")
        
        elif st.session_state.current_step == 2:
            st.markdown("### Análise de Oportunidade")
            st.markdown("O CEO está avaliando o potencial da oportunidade...")
            
            complexidade = st.select_slider(
                "Nível de Complexidade",
                options=["baixa", "média", "alta"],
                value="média"
            )
            
            if st.button("Analisar Oportunidade"):
                with st.spinner("Analisando..."):
                    time.sleep(2)  # Simulação de processamento
                    add_log(f"Oportunidade analisada. Complexidade: {complexidade}", "CEO")
                    st.session_state.current_step = 3
                    st.rerun()
        elif st.session_state.current_step == 3:
            st.markdown("### Agendamento de Reunião")
            st.markdown("O suporte administrativo está configurando a reunião...")
            
            # Verificar se já temos informações de agendamento salvas da etapa anterior
            if 'data_reuniao_salva' in st.session_state and 'hora_reuniao_salva' in st.session_state:
                st.success("Dados de agendamento recuperados da etapa anterior")
                st.info(f"Data e hora já confirmados: {st.session_state.data_reuniao_salva.strftime('%d/%m/%Y')} às {st.session_state.hora_reuniao_salva.strftime('%H:%M')}")
                if 'local_reuniao_salvo' in st.session_state:
                    st.info(f"Local: {st.session_state.local_reuniao_salvo}")
                    if st.session_state.local_reuniao_salvo == "Presencial" and 'endereco_reuniao_salvo' in st.session_state:
                        st.info(f"Endereço: {st.session_state.endereco_reuniao_salvo}")
            
            # Form for scheduling - já preenchido com dados anteriores quando disponíveis
            col1, col2 = st.columns(2)
            with col1:
                data_reuniao = st.date_input("Data da Reunião", 
                                          value=st.session_state.get("data_reuniao_salva", datetime.now().date()))
                duracao = st.selectbox("Duração", ["30 minutos", "1 hora", "1 hora e 30 minutos", "2 horas"], index=1)
                # Usando o ID fixo do Cal.com (1585329)
                event_type_id = 1585329
                st.info(f"Usando ID de Evento do Cal.com: {event_type_id}")
            with col2:
                hora_reuniao = st.time_input("Hora da Reunião", 
                                           value=st.session_state.get("hora_reuniao_salva", datetime.now().time()))
                titulo_reuniao = st.text_input("Título da Reunião", 
                                              value=f"Reunião de Diagnóstico - {st.session_state.client_company or st.session_state.client_name}")
                descricao_base = f"Discussão dos requisitos do projeto com {st.session_state.client_name}\n\nPauta:\n1. Apresentação da equipe\n2. Detalhamento do briefing\n3. Levantamento de requisitos adicionais\n4. Próximos passos"
                
                # Adicionar informações de local se disponíveis
                if 'local_reuniao_salvo' in st.session_state:
                    local_info = f"\n\nLocal: {st.session_state.local_reuniao_salvo}"
                    if st.session_state.local_reuniao_salvo == "Presencial" and 'endereco_reuniao_salvo' in st.session_state:
                        local_info += f"\nEndereço: {st.session_state.endereco_reuniao_salvo}"
                    descricao_base += local_info
                
                descricao_reuniao = st.text_area("Descrição/Pauta", 
                                               value=descricao_base, 
                                               height=150)
            
            # Convert duration string to minutes
            duration_map = {
                "30 minutos": 30,
                "1 hora": 60,
                "1 hora e 30 minutos": 90,
                "2 horas": 120
            }
            duration_minutes = duration_map.get(duracao, 60)
            
            # Campo para forçar entrada do email, caso não esteja no state
            if not st.session_state.get("client_email", "").strip():
                client_email = st.text_input("Email do cliente (obrigatório para agendamento)",
                                           value=st.session_state.get("client_email", ""),
                                           key="email_input_agendamento")
                if client_email and "@" in client_email:
                    st.session_state.client_email = client_email.strip()
                    st.success(f"Email do cliente registrado: {client_email}")
            
            # Mostra o email atual, se existir
            if st.session_state.get("client_email", "").strip():
                st.success(f"Email do cliente: {st.session_state.client_email}")
            
            if st.button("Agendar Reunião no Cal.com"):
                if not st.session_state.get("client_email", "").strip():
                    st.error("Email do cliente é obrigatório para agendar no Cal.com")
                else:
                    with st.spinner("Agendando no Cal.com..."):
                        try:
                            # Format datetime for Cal.com API with correct timezone for São Paulo (UTC-3)
                            start_time = datetime.combine(data_reuniao, hora_reuniao)
                            end_time = start_time + timedelta(minutes=duration_minutes)
                            
                            # Format in ISO 8601 for Cal.com API - correct for São Paulo (UTC-3)
                            # Não adicionar 'Z' ao final, pois isso indica UTC/GMT
                            # Em vez disso, usamos o timezone explicitamente no formato ISO 8601
                            start_iso = start_time.isoformat() + "-03:00"
                            end_iso = end_time.isoformat() + "-03:00"
                            
                            # Validar o email novamente
                            email = st.session_state.client_email.strip()
                            if not "@" in email or not "." in email.split("@")[1]:
                                st.error(f"Email '{email}' parece inválido. Por favor, verifique o formato do email.")
                            else:
                                # Chamar a API do Cal.com
                                result = schedule_meeting_calcom(
                                    event_type_id=int(event_type_id),
                                    start_time=start_iso,
                                    end_time=end_iso,
                                    attendee_name=st.session_state.client_name,
                                    attendee_email=email,
                                    title=titulo_reuniao,
                                    description=descricao_reuniao
                                )
                                
                                # Processar o resultado
                                try:
                                    # Tentativa de converter a string de resposta para JSON
                                    if isinstance(result, str) and '{' in result:
                                        result_json = json.loads(result.replace("'", "\""))
                                    elif isinstance(result, dict):
                                        result_json = result
                                    else:
                                        result_json = None
                                        
                                    # Se temos um objeto JSON e ele tem status de sucesso, extrair ID
                                    if result_json and result_json.get('status') == 'success' and 'data' in result_json:
                                        booking_data = result_json['data']
                                        meeting_id = str(booking_data.get('id'))
                                        meeting_url = None
                                        
                                        # Try to get video call URL if available
                                        if 'videoCallUrl' in booking_data:
                                            meeting_url = booking_data['videoCallUrl']
                                        elif 'references' in booking_data:
                                            for ref in booking_data['references']:
                                                if ref.get('type') == 'google_meet_video' and 'meetingUrl' in ref:
                                                    meeting_url = ref['meetingUrl']
                                                    break
                                        
                                        st.session_state.meeting_id = meeting_id
                                        success_message = f"Reunião agendada no Cal.com! ID: {meeting_id}"
                                        if meeting_url:
                                            success_message += f" | Link da videoconferência: {meeting_url}"
                                        
                                        add_log(success_message, "Suporte Administrativo")
                                    # Caso o resultado contenha "sucesso" no formato texto (para compatibilidade)
                                    elif "sucesso" in str(result).lower() and "ID:" in str(result):
                                        meeting_id = str(result).split("ID:")[-1].strip()
                                        st.session_state.meeting_id = meeting_id
                                        add_log(f"Reunião agendada no Cal.com! ID: {meeting_id}", "Suporte Administrativo")
                                    else:
                                        # Vamos considerar sucesso mesmo se o parsing falhar mas o agendamento for criado
                                        st.session_state.meeting_id = "unknown_id"
                                        add_log("Reunião possivelmente agendada no Cal.com, mas não foi possível confirmar o ID", "Suporte Administrativo")
                                except Exception as parse_error:
                                    st.warning(f"Erro ao processar resposta do Cal.com: {parse_error}")
                                    # Assumimos que o agendamento foi feito
                                    st.session_state.meeting_id = "parsing_failed"
                                    add_log(f"Reunião possivelmente agendada no Cal.com, erro ao processar resposta", "Suporte Administrativo")
                                
                                # Update ClickUp task status
                                if st.session_state.task_id:
                                    try:
                                        update_task_status(st.session_state.task_id, "reuniao_agendada")
                                        add_log("Status atualizado no CRM para 'Reunião Agendada'", "CRM")
                                    except Exception as e:
                                        add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                                
                                st.success(f"Reunião agendada com sucesso para {data_reuniao} às {hora_reuniao}")
                                st.session_state.current_step = 4
                                time.sleep(1)  # Pequena pausa para feedback visual
                                st.rerun()
                        except Exception as e:
                            # Log error but allow manual scheduling
                            st.error(f"Erro ao integrar com Cal.com: {str(e)}")
                            add_log(f"Erro ao agendar no Cal.com: {str(e)}", "Sistema")
            
            # Manual scheduling option as fallback
            with st.expander("Agendar Manualmente (sem integração)"):
                st.info("Use esta opção se a integração com Cal.com não estiver disponível.")
                if st.button("Confirmar Agendamento Manual"):
                    data_hora = f"{data_reuniao} às {hora_reuniao}"
                    add_log(f"Reunião agendada manualmente para {data_hora}", "Suporte Administrativo")
                    
                    # Update ClickUp task status even for manual scheduling
                    if st.session_state.task_id:
                        try:
                            update_task_status(st.session_state.task_id, "reuniao_agendada")
                            add_log("Status atualizado no CRM para 'Reunião Agendada'", "CRM")
                        except Exception as e:
                            add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                            
                    st.success(f"Reunião agendada manualmente para {data_hora}")
                    st.session_state.current_step = 4
                    time.sleep(1)  # Pequena pausa para feedback visual
                    st.rerun()
        
        # Etapas 4 a 7 seguem o mesmo padrão...
        elif st.session_state.current_step == 4:
            st.markdown("### Análise Técnica")
            st.markdown("O arquiteto de software está analisando os requisitos técnicos...")
            
            if st.button("Realizar Análise Técnica"):
                with st.spinner("Analisando..."):
                    time.sleep(3)
                    add_log("Análise técnica concluída. Solução viável.", "Arquiteto de Software")
                    st.session_state.current_step = 5
                    st.rerun()
                    
        elif st.session_state.current_step == 5:
            st.markdown("### Pesquisa de Mercado")
            st.markdown("O analista de ROI está realizando pesquisa de mercado e cálculo de ROI...")
            
            if st.button("Realizar Pesquisa de Mercado"):
                with st.spinner("Pesquisando..."):
                    time.sleep(3)
                    add_log("Pesquisa de mercado concluída. ROI estimado em 240%.", "Analista de ROI")
                    st.session_state.current_step = 6
                    st.rerun()
                    
        elif st.session_state.current_step == 6:
            st.markdown("### Geração de Proposta")
            
            # Verificar se a reunião já foi marcada como realizada no ClickUp
            if 'reuniao_realizada' not in st.session_state or not st.session_state.reuniao_realizada:
                st.info("Antes de gerar a proposta, é necessário confirmar que a reunião foi realizada.")
                
                st.markdown("#### A reunião com o cliente foi realizada?")
                col1, col2 = st.columns(2)
                with col1:
                    if st.button("Sim, Reunião Realizada", type="primary"):
                        # Update ClickUp task status to "Reunião Realizada"
                        if st.session_state.task_id:
                            try:
                                update_task_status(st.session_state.task_id, "reuniao_realizada")
                                add_log("Status atualizado no CRM para 'Reunião Realizada'", "CRM")
                                st.success("Status atualizado com sucesso. Prosseguindo para geração da proposta.")
                                st.session_state.reuniao_realizada = True
                                time.sleep(1.5)  # Pausa para feedback visual
                                st.rerun()
                            except Exception as e:
                                add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                                st.error(f"Erro ao atualizar status: {str(e)}")
                with col2:
                    if st.button("Reagendar Reunião", type="secondary"):
                        st.session_state.current_step = 3  # Voltar para a etapa de agendamento
                        add_log("Reunião precisou ser reagendada", "Consultor de Diagnóstico")
                        st.rerun()
            
            # Se a reunião foi confirmada como realizada, mostrar a interface de geração de proposta
            if 'reuniao_realizada' in st.session_state and st.session_state.reuniao_realizada:
                st.markdown("O consultor está gerando a proposta comercial...")
                
                # Technical analysis summary displayed from previous step
                if st.session_state.arquitetura_proposta:
                    with st.expander("Análise Técnica do Arquiteto", expanded=False):
                        st.markdown(st.session_state.arquitetura_proposta)
            
            if 'reuniao_realizada' in st.session_state and st.session_state.reuniao_realizada:
                # ROI Analysis summary displayed from previous step
                if st.session_state.roi_summary:
                    with st.expander("Análise de ROI", expanded=False):
                        st.markdown(st.session_state.roi_summary)
                
                # Proposal parameters
                col1, col2 = st.columns(2)
                with col1:
                    valor_proposta = st.number_input("Valor da Proposta (R$)", min_value=1000, max_value=500000, value=15000, step=1000)
                    nivel_complexidade = st.selectbox("Nível de Complexidade", ["baixa", "média", "alta"], index=1)
                
                with col2:
                    horas_estimadas = st.number_input("Horas Estimadas", min_value=10, max_value=1000, value=80, step=10)
                    timeline_map = {
                        "baixa": "2-3 semanas",
                        "média": "4-6 semanas",
                        "alta": "8-12 semanas"
                    }
                    timeline = timeline_map.get(nivel_complexidade, "4-8 semanas")
                    st.markdown(f"**Timeline Estimado:** {timeline}")
                
                # Generate proposal when button is clicked
                if st.session_state.proposal_content == "" and st.button("Gerar Proposta"):
                    with st.spinner("Gerando proposta comercial completa..."):
                        # If architecture or ROI analysis don't exist, create placeholders
                        if not st.session_state.arquitetura_proposta:
                            st.session_state.arquitetura_proposta = f"Nossa equipe analisou os requisitos do projeto e propomos uma arquitetura escalável e segura que atenderá às necessidades da {st.session_state.client_company}.\n\nA solução incluirá: análise de requisitos, design de interface, desenvolvimento de APIs, integração com sistemas existentes, testes e implementação."
                        
                        if not st.session_state.roi_summary:
                            st.session_state.roi_summary = f"Baseado em nossa análise, estimamos um ROI de 240% para este projeto em um período de 12 meses.\n\nBenefícios esperados:\n- Aumento de eficiência operacional em 35%\n- Redução de custos operacionais em 25%\n- Melhoria na experiência do cliente\n- Tempo de retorno do investimento: 5 meses"
                        
                        # Generate markdown proposal
                        proposta = f"""# Proposta Comercial - {st.session_state.client_company}

## 1. Objetivos
De acordo com as informações compartilhadas durante nossa reunião com {st.session_state.client_name}, entendemos que o principal objetivo é {st.session_state.objetivo_cliente or 'desenvolver uma solução tecnológica que atenda às necessidades do negócio'}.

Briefing inicial:
> {st.session_state.briefing}

## 2. Solução Proposta
{st.session_state.arquitetura_proposta}

Complexidade estimada: **{nivel_complexidade.title()}**

## 3. Investimento

| Item | Detalhe | Valor |
| ---- | ------- | ----- |
| Desenvolvimento | {horas_estimadas} horas | R$ {valor_proposta:.2f} |
| Complexidade | {nivel_complexidade.upper()} | |
| Timeline estimado | {timeline} | |

## 4. Condições Comerciais

- **Prazo de Validade:** Esta proposta é válida por 15 dias a partir da data de emissão.
- **Forma de Pagamento:** 40% no início do projeto, 30% na entrega parcial e 30% na entrega final.
- **Suporte:** 3 meses de suporte técnico inclusos após a entrega final.

## 5. Próximos Passos

1. Aceite da proposta
2. Assinatura de contrato
3. Reunião de kick-off
4. Início do desenvolvimento

---

Agradecemos a oportunidade e estamos à disposição para quaisquer esclarecimentos adicionais.

**FSTech Consulting Agency**  
www.fstechagency.com  
contato@fstechagency.com  
+55 11 9999-9999
"""
                    
                    # Save proposal to session state
                    st.session_state.proposal_content = proposta
                    
                    # Update ClickUp task status
                    if st.session_state.task_id:
                        try:
                            update_task_status(st.session_state.task_id, "proposta_enviada")
                            add_log("Status atualizado no CRM para 'Proposta Enviada'", "CRM")
                        except Exception as e:
                            add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                    
                    add_log(f"Proposta gerada no valor de R$ {valor_proposta:.2f}", "Consultor de Diagnóstico")
                    time.sleep(1)  # Pequena pausa para feedback visual
            
            # Display proposal if generated
            if st.session_state.proposal_content:
                tabs = st.tabs(["Preview da Proposta", "Código Markdown"])
                
                with tabs[0]:
                    st.markdown(st.session_state.proposal_content)
                
                with tabs[1]:
                    st.code(st.session_state.proposal_content, language="markdown")
                    if st.button("Copiar Código Markdown"):
                        st.success("Código Markdown copiado! Cole em seu editor preferido ou envie diretamente.")
                
                # Botão para confirmar que a proposta está pronta 
                if st.button("Proposta Finalizada - Pronta para Envio"):
                    add_log("Proposta finalizada e pronta para envio", "Consultor de Diagnóstico")
                    st.session_state.current_step = 7
                    st.rerun()
                    
        elif st.session_state.current_step == 7:
            st.markdown("### Envio e Negociação da Proposta")
            
            # Show the proposal again for reference
            if st.session_state.proposal_content:
                with st.expander("Visualizar Proposta", expanded=False):
                    st.markdown(st.session_state.proposal_content)
            
            # Primeiro, perguntar se a proposta foi enviada
            st.markdown("#### 1. Confirmação de Envio da Proposta")
            st.info("Para continuar o fluxo, confirme se a proposta foi enviada ao cliente.")
            
            col1, col2 = st.columns(2)
            with col1:
                proposta_enviada = st.button("Sim, Proposta Enviada ao Cliente", type="primary")
                if proposta_enviada:
                    # Update ClickUp task status to Proposta Enviada
                    if st.session_state.task_id:
                        try:
                            update_task_status(st.session_state.task_id, "proposta_enviada")
                            add_log("Status atualizado no CRM para 'Proposta Enviada'", "CRM")
                            
                            # Após confirmar o envio, automaticamente atualizar para Aguardando Resposta
                            time.sleep(1) # Pequena pausa
                            update_task_status(st.session_state.task_id, "aguardando_resposta")
                            add_log("Status atualizado no CRM para 'Aguardando Resposta'", "CRM")
                        except Exception as e:
                            add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                    
                    add_log("Proposta enviada ao cliente. Aguardando resposta.", "Consultor de Diagnóstico")
                    st.success("Status atualizado: Proposta enviada e aguardando resposta do cliente.")
                    st.session_state.proposta_enviada = True
                    st.rerun()
            
            with col2:
                if st.button("Não, Ainda Não Enviada"):
                    st.warning("Envie a proposta ao cliente antes de continuar.")
                    st.session_state.proposta_enviada = False
            
            # Se a proposta já foi enviada, mostrar a etapa de confirmação de aceite
            if 'proposta_enviada' in st.session_state and st.session_state.proposta_enviada:
                st.markdown("---")
                st.markdown("#### 2. Resposta do Cliente")
                st.info("A proposta foi enviada e está aguardando resposta do cliente. O cliente já respondeu?")
                
                col1, col2 = st.columns(2)
                with col1:
                    proposta_aceita = st.button("Sim, Proposta Foi Aceita", type="primary")
                    if proposta_aceita:
                        # Update ClickUp status to Proposta Aceita
                        if st.session_state.task_id:
                            try:
                                update_task_status(st.session_state.task_id, "proposta_aceita")
                                add_log("Status atualizado no CRM para 'Proposta Aceita'", "CRM")
                            except Exception as e:
                                add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                        
                        add_log("🎉 Proposta aceita pelo cliente!", "Sistema")
                        st.success("Proposta aceita pelo cliente! Prosseguindo para confirmação de pagamento.")
                        st.session_state.proposta_aceita = True
                        st.balloons()
                        st.rerun()
                
                with col2:
                    proposta_recusada = st.button("Não, Proposta Foi Recusada", type="secondary")
                    if proposta_recusada:
                        # Get feedback for rejection
                        motivo_recusa = st.text_area("Motivo da recusa", 
                                                    placeholder="Registre aqui o feedback do cliente sobre a recusa...")
                        if motivo_recusa:
                            add_log(f"Feedback de recusa: {motivo_recusa}", "Sistema")
                        
                        st.warning("Proposta recusada. Considere enviar uma nova proposta ajustada.")
                        
                        # Opção para reiniciar processo
                        if st.button("Iniciar Novo Fluxo", key="novo_fluxo_recusado"):
                            reset_session()
                            st.rerun()
                        
                    ainda_aguardando = st.button("Ainda Aguardando Resposta")
                    if ainda_aguardando:
                        st.info("Continue acompanhando. Retorne quando o cliente responder.")
            
            # Se a proposta foi aceita, mostrar a etapa de confirmação de pagamento
            if 'proposta_aceita' in st.session_state and st.session_state.proposta_aceita:
                st.markdown("---")
                st.markdown("#### 3. Confirmação de Pagamento")
                st.info("A proposta foi aceita pelo cliente. O pagamento inicial já foi realizado?")
                
                col1, col2 = st.columns(2)
                with col1:
                    pagamento_realizado = st.button("Sim, Pagamento Realizado", type="primary")
                    if pagamento_realizado:
                        # Update ClickUp status to Venda Realizada
                        if st.session_state.task_id:
                            try:
                                update_task_status(st.session_state.task_id, "venda_realizada")
                                add_log("Status atualizado no CRM para 'Venda Realizada'", "CRM")
                            except Exception as e:
                                add_log(f"Erro ao atualizar status no CRM: {str(e)}", "Sistema")
                        
                        add_log("💰 Pagamento recebido! Venda concluída com sucesso.", "Sistema")
                        st.success("Pagamento confirmado! A venda foi realizada com sucesso.")
                        st.markdown("""
                        ### Próximos Passos:
                        1. Iniciar o projeto
                        2. Configurar equipe de execução
                        3. Agendar reunião de kick-off
                        """)
                        
                        # Opção para reiniciar o processo
                        if st.button("Iniciar Novo Fluxo de Venda", type="primary"):
                            reset_session()
                            st.rerun()
                
                with col2:
                    aguardando_pagamento = st.button("Não, Aguardando Pagamento")
                    if aguardando_pagamento:
                        st.info("Continue acompanhando. Retorne quando o pagamento for confirmado.")
                        add_log("Aguardando confirmação de pagamento.", "Sistema")
        
        # Botão para reiniciar fluxo a qualquer momento
        if st.button("Cancelar Fluxo", type="secondary"):
            if st.button("Confirmar Cancelamento"):
                reset_session()
                st.rerun()

# Tab 2: Interação Livre
with tab_interacao:
    st.markdown("### Interagir Diretamente com o Orquestrador")
    st.markdown("Digite sua pergunta ou comando para interagir diretamente com o sistema.")
    
    user_input = st.text_area("Sua solicitação:", height=100)
    
    if st.button("Enviar Solicitação"):
        if user_input:
            with st.spinner("Processando..."):
                # Na versão completa, chamaríamos diretamente o orquestrador
                # Aqui, simulamos uma resposta para evitar execução real
                st.markdown("**Resposta do Orquestrador:**")
                time.sleep(2)
                response = f"Sua solicitação '{user_input}' foi processada. O orquestrador está trabalhando nisso."
                st.success(response)
                add_log(f"Solicitação enviada: {user_input}", "Usuário")
                add_log(response, "Orquestrador")
        else:
            st.error("Por favor, digite uma solicitação.")

# Tab 3: Visualização de Logs
with tab_logs:
    st.markdown("### Histórico de Ações")
    
    if not st.session_state.logs:
        st.info("Nenhuma ação registrada ainda.")
    else:
        logs_df = pd.DataFrame(st.session_state.logs)
        st.dataframe(
            logs_df,
            column_config={
                "timestamp": "Horário",
                "agent": "Agente",
                "message": "Mensagem"
            },
            hide_index=True
        )
        
        if st.button("Limpar Histórico"):
            st.session_state.logs = []
            st.rerun()

# Tab 4: Sobre
with tab_sobre:
    st.markdown("### Sobre o FSTech Consulting Agency")
    st.markdown("""
    O **FSTech Consulting Agency** é um sistema de automação de fluxo de vendas para serviços de consultoria tecnológica.
    
    O sistema é estruturado em múltiplos agentes especializados:
    
    * **Consultor de Diagnóstico**: responsável por intake de clientes, diagnóstico inicial
    * **Suporte Administrativo**: gestão de agendamento e contato com clientes
    * **Gerente de Marketing Digital**: geração de conteúdo e estratégias de marketing
    * **Coordenador de Projetos**: acompanhamento de timelines e entregáveis
    * **Especialista Técnico**: implementação técnica das soluções
    * **Arquiteto de Software**: desenho de arquitetura e soluções técnicas
    * **CEO**: aprovação de estratégias e análise de oportunidades
    * **Analista de ROI**: cálculo de retorno sobre investimento
    
    O fluxo operacional inclui: intake de briefing, análise de oportunidade, agendamento de reunião, análise técnica pelo arquiteto, pesquisa de mercado, geração de proposta, envio e negociação.
    """)
    
    st.markdown("### Tecnologias Utilizadas")
    st.markdown("""
    * Python
    * OpenAI GPT-4.1
    * Streamlit
    * ClickUp (CRM)
    * Cal.com (agendamento)
    """)

st.markdown("<div class='footer'>© 2025 FSTech Consulting Agency | Todos os direitos reservados</div>", unsafe_allow_html=True)
