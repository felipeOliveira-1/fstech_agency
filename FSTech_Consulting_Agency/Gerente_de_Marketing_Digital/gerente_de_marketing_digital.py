# Agente: Gerente de Marketing Digital

import json
import datetime

# Importar ferramentas refatoradas
from .tools import (
    content_calendar_manager, 
    social_media_post_generator, 
    ad_campaign_launcher, 
    seo_optimizer,
    crm_lead_creator # Ferramenta de integração ClickUp adicionada
)

# --- Definição do Agente (Estilo OpenAI SDK) ---

# Carregar instruções do arquivo .md (ou definir diretamente)
GERENTE_MARKETING_INSTRUCTIONS = """
Você é o Gerente de Marketing Digital da FSTech Consulting Agency. Sua principal responsabilidade é atrair e qualificar leads para a agência, utilizando estratégias de marketing digital (conteúdo, SEO, PPC, redes sociais). Ao identificar um lead qualificado, registre-o no CRM (ClickUp).

Responsabilidades Principais:
*   Geração de Leads: Implementar e gerenciar estratégias de atração.
*   Marketing de Conteúdo: Planejar, criar e distribuir conteúdo relevante.
*   SEO: Otimizar site e conteúdo para motores de busca.
*   Campanhas de Anúncios: Criar, gerenciar e otimizar campanhas pagas.
*   Gestão de Redes Sociais: Gerenciar presença online e interação.
*   Email Marketing: Desenvolver e executar campanhas de email.
*   Análise de Métricas: Monitorar e analisar desempenho.
*   Qualificação de Leads: Realizar triagem inicial.
*   Registro de Leads no CRM: Criar tarefa para lead qualificado no ClickUp.

Diretrizes Gerais:
*   Foque em leads alinhados com o público-alvo da FSTech.
*   Utilize dados para tomar decisões.
*   Mantenha a consistência da marca.
*   Colabore com outros agentes.

Use as ferramentas disponíveis para cumprir suas responsabilidades.
"""

# Lista de ferramentas disponíveis para este agente
GERENTE_MARKETING_TOOLS = [
    content_calendar_manager.manage_content_calendar,
    social_media_post_generator.generate_social_media_post,
    ad_campaign_launcher.launch_ad_campaign,
    seo_optimizer.optimize_seo,
    crm_lead_creator.create_crm_lead # Adicionada ferramenta ClickUp
]

# Função para criar a definição do agente
def create_gerente_marketing_agent_definition():
    """Retorna a definição do Agente Gerente de Marketing Digital."""
    return {
        "name": "Gerente de Marketing Digital Agent - FSTech",
        "instructions": GERENTE_MARKETING_INSTRUCTIONS,
        "tools": GERENTE_MARKETING_TOOLS
    }

# --- Lógica de Execução (Exemplo Simplificado - Sem LLM Real) ---

def run_gerente_marketing_task(task_description: str, context: dict = None):
    """Simula a execução de uma tarefa pelo Agente de Marketing (sem LLM real)."""
    agent_def = create_gerente_marketing_agent_definition()
    context = context or {}
    print(f"--- Executando Tarefa com Agente: {agent_def[	name	]} ---")
    print(f"Tarefa: {task_description}")
    print(f"Contexto: {context}")
    print(f"Instruções do Agente: {agent_def[	instructions	][:100]}...")
    print("Ferramentas Disponíveis:")
    for tool_func in agent_def[	tools	]:
        print(f"- {tool_func.__name__}")

    # Simulação MUITO simplificada da seleção de ferramenta
    selected_tool = None
    args = {}
    task_lower = task_description.lower()

    # Adicionar lógica para selecionar a nova ferramenta crm_lead_creator
    if "criar lead" in task_lower or "registrar lead" in task_lower or "novo lead crm" in task_lower:
        selected_tool = crm_lead_creator.create_crm_lead
        args = {
            "lead_name": context.get("lead_name", "Lead Desconhecido"),
            "description": context.get("description"),
            "assignee_email": context.get("assignee_email") # Email do Consultor, por exemplo
        }
    elif "calendário" in task_lower or "agendar conteúdo" in task_lower:
        selected_tool = content_calendar_manager.manage_content_calendar
        args = {
            "action": context.get("action", "add_item"),
            "date": context.get("date", datetime.date.today().strftime("%Y-%m-%d")),
            "topic": context.get("topic", "Tópico Padrão"),
            "channel": context.get("channel", "Blog"),
            "content_id": context.get("content_id")
        }
    elif "post" in task_lower or "mídia social" in task_lower or "social media" in task_lower:
        selected_tool = social_media_post_generator.generate_social_media_post
        args = {
            "topic": context.get("topic", "Tópico Genérico"),
            "channel": context.get("channel", "LinkedIn"),
            "target_audience": context.get("audience", "Geral"),
            "tone": context.get("tone", "Informativo")
        }
    elif "campanha" in task_lower or "anúncio" in task_lower or "ads" in task_lower:
        selected_tool = ad_campaign_launcher.launch_ad_campaign
        args = {
            "platform": context.get("platform", "Google Ads"),
            "campaign_name": context.get("campaign_name", "Campanha Padrão"),
            "budget": context.get("budget", 100.0),
            "target_audience_criteria": context.get("audience_criteria", {}),
            "ad_creative_details": context.get("creative_details", {})
        }
    elif "seo" in task_lower or "otimizar" in task_lower:
        selected_tool = seo_optimizer.optimize_seo
        args = {
            "content_url": context.get("url", "http://example.com"),
            "target_keywords": context.get("keywords", ["tecnologia"])
        }

    if selected_tool:
        print(f"\n>>> LLM (Simulado) decidiu usar a ferramenta: {selected_tool.__name__}")
        try:
            result = selected_tool(**args)
            print("\n--- Resultado da Ferramenta ---")
            print(result)
            print("---------------------------")
            return result, context
        except Exception as e:
            error_message = f"Erro ao executar ferramenta {selected_tool.__name__}: {e}"
            print(error_message)
            return error_message, context
    else:
        no_tool_message = "Nenhuma ferramenta de marketing apropriada encontrada (simulado). Tarefa pode exigir análise manual ou mais detalhes."
        print(f"\n{no_tool_message}")
        return no_tool_message, context

# Exemplo de execução de tarefa
if __name__ == "__main__":
    # Exemplo de criação de lead
    contexto_lead = {"lead_name": "Empresa Exemplo Lead", "description": "Solicitou demonstração via site."}
    run_gerente_marketing_task("Criar lead no CRM para Empresa Exemplo", contexto_lead)
    print("\n=========================================\n")
    
    contexto_cal = {"action": "add_item", "date": "2025-05-20", "topic": "Webinar sobre IA Generativa", "channel": "LinkedIn Event"}
    run_gerente_marketing_task("Agendar divulgação de webinar no calendário", contexto_cal)
    print("\n=========================================\n")

    contexto_post = {"topic": "5 Dicas de SEO para E-commerce", "channel": "Blog", "audience": "Lojistas Online"}
    run_gerente_marketing_task("Gerar rascunho de post para blog sobre SEO", contexto_post)
    print("\n=========================================\n")

    contexto_ads = {
        "platform": "Facebook Ads",
        "campaign_name": "Lead Gen - Ebook Automação",
        "budget": 500.0,
        "audience_criteria": {"interests": ["Marketing Digital", "Automação"], "age_range": "25-55"},
        "creative_details": {"headline": "Baixe nosso Ebook Grátis!", "image_url": "..."}
    }
    run_gerente_marketing_task("Lançar campanha no Facebook para ebook", contexto_ads)
    print("\n=========================================\n")

    contexto_seo = {"url": "https://fstech.example.com/servicos/consultoria-ia", "keywords": ["consultoria ia", "inteligência artificial para empresas"]}
    run_gerente_marketing_task("Otimizar página de serviço de IA para SEO", contexto_seo)

