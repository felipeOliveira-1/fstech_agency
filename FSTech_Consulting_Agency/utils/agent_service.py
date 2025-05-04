import streamlit as st
from FSTech_Consulting_Agency.Arquiteto_de_Software.arquiteto_de_software import run_arquiteto_task
from FSTech_Consulting_Agency.Analista_ROI.analista_roi import run_analista_roi_task

def execute_arquitect_agent(briefing, objetivo_cliente, transcricao=None):
    """
    Executa o agente Arquiteto de Software e retorna os resultados.
    
    Args:
        briefing: Briefing inicial do cliente
        objetivo_cliente: Objetivo principal do cliente
        transcricao: Transcrição ou resumo da reunião (opcional)
        
    Returns:
        dict: Dicionário contendo os resultados da análise arquitetônica
    """
    context = {
        "briefing": briefing,
        "objetivo_cliente": objetivo_cliente
    }
    
    # Adicionar transcrição ao contexto, se disponível
    if transcricao:
        context["reuniao_transcricao"] = transcricao
    
    task_description = f"Analise o briefing '{briefing}' e desenhe uma arquitetura adequada para o objetivo: {objetivo_cliente}"
    
    # Executar o agente Arquiteto
    resultado = run_arquiteto_task(task_description, context)
    
    # Extrair informações relevantes
    nivel_complexidade = resultado.get('nivel_complexidade', 'médio')
    horas_estimadas = resultado.get('horas_estimadas', 120)
    arquitetura_proposta = resultado.get('arquitetura_proposta', '')
    
    return {
        "nivel_complexidade": nivel_complexidade,
        "horas_estimadas": horas_estimadas,
        "arquitetura_proposta": arquitetura_proposta,
        "resultado_completo": resultado
    }

def execute_roi_agent(briefing, objetivo_cliente, nivel_complexidade, horas_estimadas, transcricao=None):
    """
    Executa o agente Analista de ROI e retorna os resultados.
    
    Args:
        briefing: Briefing inicial do cliente
        objetivo_cliente: Objetivo principal do cliente
        nivel_complexidade: Nível de complexidade do projeto
        horas_estimadas: Estimativa de horas para o projeto
        transcricao: Transcrição ou resumo da reunião (opcional)
        
    Returns:
        dict: Dicionário contendo os resultados da análise de ROI
    """
    context = {
        "briefing": briefing,
        "objetivo_cliente": objetivo_cliente,
        "nivel_complexidade": nivel_complexidade,
        "horas_estimadas": horas_estimadas
    }
    
    # Adicionar transcrição ao contexto, se disponível
    if transcricao:
        context["reuniao_transcricao"] = transcricao
    
    task_description = f"Calcule o ROI e valor da proposta para um projeto de complexidade {nivel_complexidade} e {horas_estimadas} horas estimadas."
    
    # Executar o agente Analista de ROI
    resultado = run_analista_roi_task(task_description, context)
    
    # Extrair informações relevantes
    valor_proposta = resultado.get('valor_proposta', horas_estimadas * 150)  # Valor padrão caso não retorne
    roi_summary = resultado.get('roi_summary', '')
    
    return {
        "valor_proposta": valor_proposta,
        "roi_summary": roi_summary,
        "resultado_completo": resultado
    }

def run_agents_analysis(st_session_state):
    """
    Executa a análise completa usando os agentes Arquiteto e Analista de ROI.
    Atualiza o session_state com os resultados obtidos.
    
    Args:
        st_session_state: Objeto session_state do Streamlit
        
    Returns:
        dict: Resultados consolidados da análise
    """
    # Executa o Arquiteto de Software
    arquiteto_results = execute_arquitect_agent(
        st_session_state.briefing,
        st_session_state.objetivo_cliente,
        st_session_state.get('reuniao_transcricao', None)
    )
    
    # Atualiza o session_state com os resultados do Arquiteto
    st_session_state.arquitetura_proposta = arquiteto_results['arquitetura_proposta']
    nivel_complexidade = arquiteto_results['nivel_complexidade']
    horas_estimadas = arquiteto_results['horas_estimadas']
    
    # Executa o Analista de ROI
    roi_results = execute_roi_agent(
        st_session_state.briefing,
        st_session_state.objetivo_cliente,
        nivel_complexidade,
        horas_estimadas,
        st_session_state.get('reuniao_transcricao', None)
    )
    
    # Atualiza o session_state com os resultados do Analista de ROI
    st_session_state.roi_summary = roi_results['roi_summary']
    valor_proposta = roi_results['valor_proposta']
    
    # Determinar timeline com base na complexidade
    timeline = "4-6 semanas"
    if nivel_complexidade.lower() == "médio":
        timeline = "6-8 semanas"
    elif nivel_complexidade.lower() == "alto" or nivel_complexidade.lower() == "alta":
        timeline = "8-12 semanas"
    
    # Retorna os resultados consolidados
    return {
        "nivel_complexidade": nivel_complexidade,
        "horas_estimadas": horas_estimadas,
        "valor_proposta": valor_proposta,
        "timeline": timeline,
        "arquitetura_proposta": st_session_state.arquitetura_proposta,
        "roi_summary": st_session_state.roi_summary
    }
