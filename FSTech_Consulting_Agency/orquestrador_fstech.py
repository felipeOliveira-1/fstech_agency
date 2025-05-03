from agents import Agent, Runner
import os
import re

# Função utilitária para carregar instruções de arquivo markdown

def load_instructions(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

# Diretórios dos agentes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
AGENTS_DIR = BASE_DIR

# Importar ferramentas de cada agente
from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.client_intake_form_generator import generate_client_intake_form
from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.crm_status_updater import update_crm_task_status
from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.pricing_calculator import calculate_proposal_price
from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.proposal_builder import build_proposal_markdown

from FSTech_Consulting_Agency.Suporte_Administrativo.tools import (
    client_support_bot, appointment_scheduler_manager, subscription_tracker, feedback_collector
)
from FSTech_Consulting_Agency.Gerente_de_Marketing_Digital.tools import (
    content_calendar_manager, social_media_post_generator, ad_campaign_launcher, seo_optimizer, crm_lead_creator
)
from FSTech_Consulting_Agency.Coordenador_de_Projetos.tools import (
    project_timeline_manager, task_assignment_manager, progress_tracker, client_update_sender, crm_project_status_updater
)
from FSTech_Consulting_Agency.Especialista_Tecnico.tools import (
    automation_setup_wizard, llm_fine_tuner, prompt_engineering_assistant, api_integrator, platform_configuration_manager
)
from FSTech_Consulting_Agency.Arquiteto_de_Software.tools import (
    system_architecture_designer, api_blueprint_generator, scalability_tester, security_audit_assistant
)
from FSTech_Consulting_Agency.CEO.tools import (
    business_strategy_builder, client_relationship_manager, kpi_dashboard_manager, risk_assessment_tool
)

# Importar ferramentas do Analista de ROI
from FSTech_Consulting_Agency.Analista_ROI.tools import (
    roi_calculator, benefit_projection, cost_reduction_estimator, 
    payback_period_analyzer, value_proposition_builder
)

# Carregar instruções de cada agente
consultor_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Consultor_de_Diagnostico', 'instructions.md'))
suporte_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Suporte_Administrativo', 'instructions.md'))
gerente_marketing_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Gerente_de_Marketing_Digital', 'instructions.md'))
coordenador_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Coordenador_de_Projetos', 'instructions.md'))
especialista_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Especialista_Tecnico', 'instructions.md'))
arquiteto_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Arquiteto_de_Software', 'instructions.md'))
ceo_instructions = load_instructions(os.path.join(AGENTS_DIR, 'CEO', 'instructions.md'))
analista_roi_instructions = load_instructions(os.path.join(AGENTS_DIR, 'Analista_ROI', 'instructions.md'))

# Instanciar cada agente
consultor_agent = Agent(
    name="Consultor de Diagnóstico",
    instructions=consultor_instructions,
    tools=[generate_client_intake_form, update_crm_task_status, calculate_proposal_price, build_proposal_markdown]
)

suporte_agent = Agent(
    name="Suporte Administrativo",
    instructions=suporte_instructions,
    tools=[
        client_support_bot.handle_client_support_query,
        appointment_scheduler_manager.schedule_meeting_calcom,
        subscription_tracker.track_subscription,
        feedback_collector.collect_feedback
    ]
)

gerente_marketing_agent = Agent(
    name="Gerente de Marketing Digital",
    instructions=gerente_marketing_instructions,
    tools=[
        content_calendar_manager.manage_content_calendar,
        social_media_post_generator.generate_social_media_post,
        ad_campaign_launcher.launch_ad_campaign,
        seo_optimizer.optimize_seo,
        crm_lead_creator.create_crm_lead
    ]
)

coordenador_agent = Agent(
    name="Coordenador de Projetos",
    instructions=coordenador_instructions,
    tools=[
        project_timeline_manager.manage_project_timeline,
        task_assignment_manager.manage_task_assignment,
        progress_tracker.track_task_progress,
        client_update_sender.send_client_update,
        crm_project_status_updater.update_crm_project_status
    ]
)

especialista_agent = Agent(
    name="Especialista Técnico",
    instructions=especialista_instructions,
    tools=[
        automation_setup_wizard.setup_automation,
        llm_fine_tuner.fine_tune_llm,
        prompt_engineering_assistant.optimize_prompt,
        api_integrator.integrate_api,
        platform_configuration_manager.configure_platform
    ]
)

arquiteto_agent = Agent(
    name="Arquiteto de Software",
    instructions=arquiteto_instructions,
    tools=[
        system_architecture_designer.design_architecture_and_assess_complexity,
        api_blueprint_generator.generate_api_blueprint,
        scalability_tester.test_scalability,
        security_audit_assistant.perform_security_audit
    ]
)

ceo_agent = Agent(
    name="CEO",
    instructions=ceo_instructions,
    tools=[
        business_strategy_builder.build_strategy,
        client_relationship_manager.manage_client_vip,
        kpi_dashboard_manager.manage_kpi_dashboard,
        risk_assessment_tool.assess_risk
    ]
)

# Instanciar agente Analista de ROI
analista_roi_agent = Agent(
    name="Analista de ROI",
    instructions=analista_roi_instructions,
    tools=[
        roi_calculator.calculate_roi,
        benefit_projection.project_benefits,
        cost_reduction_estimator.estimate_cost_reduction,
        payback_period_analyzer.analyze_payback_period,
        value_proposition_builder.build_value_proposition
    ]
)

# Orquestrador central
orquestrador = Agent(
    name="Orquestrador FSTech",
    instructions="Você é o orquestrador da FSTech. Use as ferramentas/agentes disponíveis para delegar tarefas conforme o fluxo operacional.",
    tools=[
        consultor_agent.as_tool(tool_name="consultor", tool_description="Ferramentas do Consultor de Diagnóstico: intake de clientes, cálculo de preço, propostas."),
        suporte_agent.as_tool(tool_name="suporte", tool_description="Ferramentas do Suporte: agendamento, feedback, suporte ao cliente."),
        gerente_marketing_agent.as_tool(tool_name="marketing", tool_description="Ferramentas de Marketing: conteúdo, social media, SEO, campanhas."),
        coordenador_agent.as_tool(tool_name="coordenador", tool_description="Ferramentas do Coordenador de Projetos: cronograma, tarefas, progresso."),
        especialista_agent.as_tool(tool_name="especialista", tool_description="Ferramentas do Especialista Técnico: automação, APIs, plataformas, fine-tuning."),
        arquiteto_agent.as_tool(tool_name="arquiteto", tool_description="Ferramentas do Arquiteto: arquitetura, APIs, segurança, escalabilidade."),
        ceo_agent.as_tool(tool_name="ceo", tool_description="Ferramentas do CEO: estratégia, clientes VIP, KPIs, riscos."),
        analista_roi_agent.as_tool(tool_name="analista_roi", tool_description="Ferramentas do Analista de ROI: cálculo de ROI, projeção de benefícios, análise de payback, proposta de valor.")
    ]
)

def fluxo_fstech():
    print("\n=== FLUXO OPERACIONAL FSTech (SIMPLIFICADO) ===\n")

    # 1. Obtenção da oportunidade e briefing reduzido via arquivo
    input("👤 Carregue o arquivo briefing_inicial.txt e pressione ENTER para continuar.")
    with open("briefing_inicial.txt", "r", encoding="utf-8") as f:
        briefing = f.read().strip()

    # --- EXTRAÇÃO E LANÇAMENTO NO CLICKUP IMEDIATO ---
    titulo = briefing.strip().split(".")[0][:80] if "." in briefing else briefing.strip()[:80]
    breve_descricao = briefing[:150] + ("..." if len(briefing) > 150 else "")
    responsavel_nome = "Felipe Silva"
    prioridade = "normal"
    assignee_id = None
    try:
        from FSTech_Consulting_Agency.utils.clickup_client import create_crm_task, update_task_status
        task_id = create_crm_task(titulo, breve_descricao, assignee_id=assignee_id)
        if task_id:
            print(f"\nLead CRM criada no ClickUp com sucesso!")
            update_task_status(task_id, "oportunidade_identificada")
        else:
            print("\n[ERRO] Não foi possível criar lead no ClickUp.")
    except Exception:
        print("\n[ERRO] Falha ao criar tarefa no ClickUp.")

    try:
        from FSTech_Consulting_Agency.utils.openai_extractor import extract_industry_and_challenge
        industry, main_challenge = extract_industry_and_challenge(briefing)
        print(f"🤖 Sugerido pelo assistente:\nSetor: {industry}\nDesafio: {main_challenge}")
    except Exception as e:
        print(f" Erro ao usar IA para extrair setor/desafio: {e}")
        industry = ""
        main_challenge = ""
    # Confirmação ou ajuste pelo usuário
    industry = input(f"👤 Confirme ou ajuste o setor de atuação [{industry}]: ") or industry
    main_challenge = input(f"👤 Confirme ou ajuste o principal desafio/dor [{main_challenge}]: ") or main_challenge
    
    # Extrair nome e email do cliente do briefing
    import re
    nome_cliente = ""
    email_cliente = ""
    nome_match = re.search(r"Contratante:\s*([^\n]+)", briefing)
    if nome_match:
        nome_cliente = nome_match.group(1).strip()
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", briefing)
    if email_match:
        email_cliente = email_match.group(0).strip()
    if not nome_cliente:
        nome_cliente = input("👤 Nome do cliente: ")
    if not email_cliente:
        email_cliente = input("👤 E-mail do cliente: ")

    # 2. Entrar em contato com cliente solicitando agendamento de reunião
    # Limitar o tamanho do briefing exibido para a mensagem de contato
    max_briefing_len = 220
    briefing_resumido = (briefing[:max_briefing_len] + '...') if len(briefing) > max_briefing_len else briefing
    contato_msg = (
        f"Olá, tudo bem?\n\n"
        f"Recebemos sua demanda: \n---\n{briefing_resumido}\n---\n\n"
        "Gostaríamos de agendar uma reunião de diagnóstico para entender melhor suas necessidades e propor a melhor solução. "
        "Por favor, indique sua disponibilidade para conversarmos.\n\nAbraços,\nEquipe FSTech"
    )
    print("\n🤖 Sugestão de mensagem para contato:\n" + "="*35)
    print(contato_msg)
    print("="*35)
    input("👤 Revise e envie a mensagem ao cliente. Pressione ENTER para registrar o contato realizado no ClickUp.")
    # Atualizar status para 'contato_realizado' no ClickUp
    from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.crm_status_updater import update_crm_task_status
    status_contato = update_crm_task_status(task_id, 'contato_realizado')
    print(status_contato)
    input("Pressione ENTER quando o cliente responder...")

    # 3. Cliente responde e agenda reunião
    # Novo formato amigável para entrada de data/hora
    from datetime import datetime, timedelta
    import re
    while True:
        data_input = input("👤 Informe a data da reunião (ex: 09-05-2025): ")
        hora_input = input("👤 Informe o horário da reunião (ex: 14:00, 24h): ")
        try:
            import pytz
            # Converter para datetime
            data_hora_str = f"{data_input.strip()} {hora_input.strip()}"
            local_tz = pytz.timezone("America/Sao_Paulo")
            start_dt_local = local_tz.localize(datetime.strptime(data_hora_str, "%d-%m-%Y %H:%M"))
            start_dt_utc = start_dt_local.astimezone(pytz.utc)
            data_reuniao = start_dt_utc.strftime("%Y-%m-%dT%H:%M:00.000Z")
            end_dt_local = start_dt_local + timedelta(hours=1)
            end_dt_utc = end_dt_local.astimezone(pytz.utc)
            end_time = end_dt_utc.strftime("%Y-%m-%dT%H:%M:00.000Z")
            break
        except Exception as e:
            print(f"⚠️ Formato inválido. Tente novamente. Erro: {e}")
    # Limpeza extra de sufixos comuns em nome e e-mail
    for sufixo in ["Email", "Telefone", "E-mail", "Contato", "email", "telefone"]:
        nome_cliente = nome_cliente.replace(sufixo, "").strip()
        email_cliente = email_cliente.replace(sufixo, "").strip()
    # Sanitização do e-mail (garante que só o endereço será enviado)
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", email_cliente)
    if email_match:
        email_cliente = email_match.group(0).strip()
    else:
        while True:
            email_cliente = input(" E-mail do cliente (apenas o endereço): ").strip()
            email_match = re.search(r"[\w\.-]+@[\w\.-]+", email_cliente)
            if email_match:
                email_cliente = email_match.group(0).strip()
                break
            else:
                print(" E-mail inválido. Tente novamente.")
    try:
        resposta_agendamento = appointment_scheduler_manager.schedule_meeting_calcom(
            event_type_id=1585329,
            start_time=data_reuniao,
            end_time=end_time,
            attendee_name=nome_cliente,
            attendee_email=email_cliente,
            timezone="America/Sao_Paulo",
            title=titulo,
            description=breve_descricao
        )
        print(f"🤖 Reunião agendada com sucesso!")
    except Exception as e:
        print(f"❌ [ERRO] Falha ao agendar reunião no Cal.com: {e}")
        resposta_agendamento = None
    # Atualizar status no ClickUp após agendamento
    if task_id:
        try:
            update_task_status(task_id, "reuniao_agendada")
        except Exception as e:
            print(f"⚠️ Não foi possível atualizar status no ClickUp: {e}")

    # 4. Análise da ata pelo Arquiteto de Software
    print("\n📃 Encaminhando ata de reunião para análise do Arquiteto de Software...")
    input("👤 Carregue o arquivo ata_reuniao.txt e pressione ENTER para continuar.")
    with open("ata_reuniao.txt", "r", encoding="utf-8") as f:
        ata_reuniao = f.read().strip()
        
    print("📚 Arquiteto de Software analisando requisitos técnicos da ata...")
    esboco_solucao = system_architecture_designer.design_architecture_and_assess_complexity(ata_reuniao)
    print(f"🤖 Arquiteto sugeriu a seguinte solução técnica: {esboco_solucao}")
    
    # Extrair nível de complexidade para usar na pesquisa de mercado
    nivel_complexidade = "media"
    if "ALTA" in esboco_solucao:
        nivel_complexidade = "alta"
    elif "BAIXA" in esboco_solucao:
        nivel_complexidade = "baixa"
        
    # Realizar pesquisa de mercado para preços e prazos
    print("💰 Arquiteto realizando pesquisa de mercado para estimativa de preços e prazos...")
    from FSTech_Consulting_Agency.Arquiteto_de_Software.tools.market_research_tool import research_market_prices
    
    # Criar um contexto de descrição com combinação do briefing e análise
    contexto_projeto = f"Briefing: {briefing}\n\nAta da Reunião: {ata_reuniao}\n\nSolução Proposta: {esboco_solucao}"
    
    # Executar a pesquisa de mercado
    try:
        resultado_pesquisa = research_market_prices(project_description=contexto_projeto, complexity_level=nivel_complexidade)
        print(f"📊 Resultado da pesquisa de mercado: {resultado_pesquisa}")
        
        # Extrair dados para uso na proposta
        faixa_preco = resultado_pesquisa.get("price_range", "R$ 8.000,00 - R$ 15.000,00")
        prazo_estimado = resultado_pesquisa.get("timeline", "4-8 semanas")
        fatores_mercado = resultado_pesquisa.get("market_factors", [])
        
        # Exibir informações para o usuário
        print(f"💵 Faixa de preço recomendada: {faixa_preco}")
        print(f"⏱️ Prazo estimado: {prazo_estimado}")
        print(f"📈 Fatores de mercado considerados:")
        for fator in fatores_mercado:
            print(f"  • {fator}")
    except Exception as e:
        print(f"⚠️ Não foi possível realizar pesquisa de mercado completa: {e}")
        faixa_preco = "R$ 8.000,00 - R$ 15.000,00"  # Valores padrão
        prazo_estimado = "4-8 semanas"
        fatores_mercado = ["Estimativa baseada em projetos similares"]

    
    # Solicitar uma descrição mais detalhada da solução ao Arquiteto
    print("📝 Arquiteto preparando descrição detalhada da solução proposta...")
    
    # Com base na ata e na análise inicial, criar uma descrição detalhada da solução
    from FSTech_Consulting_Agency.utils.openai_extractor import extract_industry_and_challenge
    
    try:
        # Primeiro, gerar um entendimento refinado do desafio pelo Arquiteto
        print("💼 Arquiteto sintetizando o entendimento técnico do desafio...")
        
        # Combinar informações do briefing e da ata para um entendimento mais rico
        desafios_pontos_chave = """
Com base na análise dos requisitos, identificamos o seguinte desafio central:

O cliente necessita de uma ferramenta automatizada em Python para monitoramento e auditoria de conteúdo web com as seguintes capacidades essenciais:

1. **Monitoramento automático** de páginas web selecionadas com agendamento personalizável
2. **Detecção inteligente** de atualizações de conteúdo e mudanças estruturais (HTML/CSS)
3. **Captura e arquivamento** de versões das páginas para comparação histórica
4. **Geração de relatórios** detalhados em formatos estruturados (Excel/PDF)

A solução precisa operar de forma completamente offline, sem dependências de serviços externos pagos, e deve implementar práticas avançadas de web scraping respeitando boas práticas da web.
"""

        # Extrair palavras-chave e componentes do esboço
        componentes = [linha.strip() for linha in esboco_solucao.split('\n') 
                      if linha.strip().startswith('-')]
        
        if not componentes or "Nenhum componente técnico" in esboco_solucao:
            # Analisar a ata para extrair informações relevantes se não houver componentes detectados
            descricao_solucao = f"""
Propomos uma solução modular e escalável desenvolvida em Python:

1. **Camada de Captura de Dados**: Interface para leitura e processamento dos arquivos/sites alvo
2. **Processamento Central**: Lógica de negócio para análise e transformação dos dados coletados
3. **Visualização & Relatórios**: Exportação em formatos estruturados conforme requisitos

A arquitetura seguirá o padrão MVC para facilitar manutenção e expansões futuras.
"""
        else:
            # Construir descrição com base nos componentes detectados
            descritor_componentes = "\n".join(componentes)
            descricao_solucao = f"""
Com base na análise técnica detalhada da sua necessidade, propomos uma solução composta pelos seguintes componentes:

{descritor_componentes}

Estes componentes serão integrados em uma arquitetura modular que permite:

1. **Flexibilidade**: Adaptação às mudanças de requisitos ou tecnologias
2. **Escalonamento**: Capacidade de crescer conforme o volume de dados/usuários aumenta
3. **Manutenção Simplificada**: Separação lógica que facilita atualizações e correções

Vamos implementar usando as melhores práticas atuais de desenvolvimento, com documentação completa e înfase na segurança e confiabilidade.
"""
    except Exception as e:
        # Se houver erro na extração detalhada, usar uma descrição genérica
        desafios_pontos_chave = "Com base em nossa análise, identificamos a necessidade de uma solução de monitoramento web automatizado com geração de relatórios e operação offline."
        descricao_solucao = "A solução será desenvolvida usando tecnologias modernas e robustas, priorizando escalabilidade, desempenho e facilidade de uso conforme os requisitos discutidos."

    # Atualizar status para 'reuniao_realizada' no ClickUp
    status_reuniao = update_crm_task_status(task_id, 'reuniao_realizada')
    print(status_reuniao)

    # Extração dos detalhes técnicos para a proposta a partir do esboço sugerido
    if not esboco_solucao or "Nenhum componente técnico" in esboco_solucao:
        # Solucao padrão se o esboço não tem detalhes suficientes
        arquitetura_proposta = "Solução web modular baseada em Python, com exportação de relatórios em formatos padronizados."
    else:
        # Usar o esboço do arquiteto para a proposta
        arquitetura_proposta = esboco_solucao.split("Pontuação Total")[0].strip()
    
    print("\n📝 Gerando proposta comercial com base na arquitetura sugerida e descrição detalhada...")
    
    # Modificar o template da proposta para incluir a descrição detalhada da solução
    from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.proposal_builder import PROPOSAL_TEMPLATE
    
    # Obter o template original
    template_original = PROPOSAL_TEMPLATE
    
    # Primeiro, substituir o entendimento do desafio pelo refinado do arquiteto
    template_modificado = template_original.replace(
        "Com base em nossa conversa e análise inicial, compreendemos que o principal desafio enfrentado por {client_company} é:\n\n```\n{problem_description}\n```",
        desafios_pontos_chave if 'desafios_pontos_chave' in locals() else "Com base em nossa conversa e análise inicial, compreendemos que o principal desafio enfrentado por {client_company} é:\n\n```\n{problem_description}\n```"
    )
    
    # Depois, substituir o marcador genérico pela descrição detalhada do arquiteto
    template_modificado = template_modificado.replace(
        "*(Detalhar aqui como os componentes se conectam e resolvem o problema do cliente)*", 
        descricao_solucao if 'descricao_solucao' in locals() else "A solução será implementada conforme arquitetura definida acima."
    )
    
    # Armazenamos o template original
    from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.proposal_builder import build_proposal_markdown as orig_build_proposal
    
    # Definimos uma função wrapper que usa o template modificado
    def custom_build_proposal(**kwargs):
        # Import necessário dentro da função
        import inspect
        from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools import proposal_builder
        
        # Guarda o template original
        original_template = proposal_builder.PROPOSAL_TEMPLATE
        
        try:
            # Substitui pelo template modificado
            proposal_builder.PROPOSAL_TEMPLATE = template_modificado
            # Chama a função original
            result = orig_build_proposal(**kwargs)
        finally:
            # Restaura o template original no módulo
            proposal_builder.PROPOSAL_TEMPLATE = original_template
            
        return result
    
    # Extrair nome da empresa cliente do briefing ou solicitar ao usuário
    if 'nome_empresa' not in locals() or not nome_empresa:
        nome_empresa = input("👤 Nome da empresa do cliente: ")
    
    # Extração padrão de nível de complexidade (necessário em todos os cenários)
    nivel_complexidade = "media"
    if esboco_solucao:
        if "ALTA" in esboco_solucao:
            nivel_complexidade = "alta"
        elif "BAIXA" in esboco_solucao:
            nivel_complexidade = "baixa"
    
    # Definição de horas estimadas (usado em ambos os caminhos)
    horas_estimadas = {
        "baixa": 40,
        "media": 100,
        "alta": 180
    }.get(nivel_complexidade, 80)
    
    # Calcular preço com base na pesquisa de mercado
    if 'research_result' in locals() and research_result and 'price_range' in research_result:
        print("🤖 Utilizando dados da pesquisa de mercado para precificação...")
        
        # Extrair dados da pesquisa
        price_range = research_result.get('price_range', '')
        prazo_estimado = research_result.get('timeline', '')
        market_factors = research_result.get('market_factors', [])
        
        # Extrair valores da faixa de preço (formato esperado: "R$ X - R$ Y")
        if ' - ' in price_range:
            valores = price_range.split(' - ')
            valor_minimo = valores[0].replace('R$ ', '').replace('.', '').replace(',', '.')
            valor_maximo = valores[1].replace('R$ ', '').replace('.', '').replace(',', '.')
            try:
                valor_minimo = float(valor_minimo)
                valor_maximo = float(valor_maximo)
                preco = f"R$ {((valor_minimo + valor_maximo) / 2):,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')
                print(f"🤖 Valor com base em pesquisa de mercado: {preco}")
            except ValueError:
                # Fallback para cálculo tradicional se houver erro na conversão
                preco = None
        else:
            preco = None
            
        # Solicitar análise de ROI após a pesquisa de mercado
        print("\n🔍 Analisando retorno sobre investimento para o cliente...")
        global roi_summary
        
        # Converter valor médio da faixa de preço para um número para cálculo do ROI
        try:
            investimento_inicial = (valor_minimo + valor_maximo) / 2
        except UnboundLocalError:
            # Valor fallback se não conseguir extrair da pesquisa
            investimento_inicial = horas_estimadas * 150 * (1 + 25/100)  # Usando valor padrão
            
        # Estimar benefícios mensais (simplificação para exemplo)
        monthly_benefits = investimento_inicial * 0.15  # 15% do investimento inicial como benefício mensal
        
        # Solicitar análise de ROI e payback
        roi_analysis = payback_period_analyzer.analyze_payback_period(
            initial_investment=investimento_inicial,
            monthly_benefits=monthly_benefits,
            consider_time_value=True,
            discount_rate=0.08  # Taxa de desconto anual padrão
        )
        
        # Incluir problema e solução para projeção de benefícios
        benefits_analysis = benefit_projection.project_benefits(
            business_problem=briefing,
            solution_description=arquitetura_proposta,
            industry="Tecnologia",  # Valor padrão, idealmente seria identificado do briefing
            company_size="Média"    # Valor padrão, idealmente seria identificado do briefing
        )
        
        # Construir proposta de valor
        pain_points = ["Processos manuais e ineficientes", "Custos operacionais elevados", 
                      "Falta de escalabilidade" if "escala" in nivel_complexidade else "Limitações técnicas atuais"]
        
        solution_benefits = ["Automatização de processos críticos", 
                           f"Redução de custos operacionais", 
                           f"Retorno de investimento em {roi_analysis.get('effective_payback_months', 12)} meses",
                           "Arquitetura tecnológica moderna e escalável"]
        
        value_proposition = value_proposition_builder.build_value_proposition(
            client_pain_points=pain_points,
            solution_benefits=solution_benefits,
            target_stakeholders=["Técnico", "Financeiro", "Executivo"]
        )
        
        # Obter argumentos de negócios da proposta de valor
        roi_summary = f"\n## Análise de Retorno sobre Investimento\n\n"
        roi_summary += f"* **Período de retorno estimado (payback):** {roi_analysis.get('effective_payback_months', 'N/A')} meses\n"
        roi_summary += f"* **ROI anualizado:** {roi_analysis.get('irr_percentage_estimate', 'N/A')}%\n"
        roi_summary += f"* **Avaliação de retorno:** {roi_analysis.get('payback_assessment', 'N/A')}\n\n"
        
        roi_summary += f"**Proposta de Valor Principal:** {value_proposition.get('main_value_proposition', '')}\n\n"
        
        # Adicionar projeção de benefícios se disponível
        if benefits_analysis and 'benefits_summary' in benefits_analysis:
            roi_summary += f"**Benefícios Projetados:** {benefits_analysis.get('benefits_summary', '')}\n"
            roi_summary += f"**Benefício total projetado (3 anos):** {benefits_analysis.get('total_projected_benefit_3_years', '')}\n\n"
        
        # Proposta para cada stakeholder (opcional, pode ser adaptado ao template da proposta)
        for stakeholder, prop in value_proposition.get('stakeholder_propositions', {}).items():
            roi_summary += f"**Para {stakeholder}:** {prop.get('headline', '')}\n"
        
        print(f"🤖 Análise de ROI concluída com sucesso!")
    else:
        # Cálculo de preço fallback se não houver dados da pesquisa de mercado
        
        # Definir margem de lucro baseada na complexidade
        margem_lucro = {
            "baixa": 20,
            "media": 30,
            "alta": 35
        }.get(nivel_complexidade, 25)
        
        # Importar calculadora de preço
        from FSTech_Consulting_Agency.Consultor_de_Diagnostico.tools.pricing_calculator import calculate_proposal_price
        
        # Calcular preço
        resultado_preco = calculate_proposal_price(
            estimated_effort_hours=horas_estimadas,
            complexity_level=nivel_complexidade,
            desired_margin_percentage=margem_lucro
        )
        
        # Extrair apenas o valor formatado
        if "preço calculado para a proposta é" in resultado_preco:
            preco = resultado_preco.split("preço calculado para a proposta é")[1].strip()
        else:
            preco = "R$ " + str(horas_estimadas * 150 * (1 + margem_lucro/100)).replace(".", ",") + ",00" 
    
    # Usar o prazo da pesquisa de mercado ou definir com base na complexidade
    if 'prazo_estimado' in locals() and prazo_estimado:
        timeline = prazo_estimado
    else:
        # Timeline fallback
        timeline = {
            "baixa": "2-3 semanas",
            "media": "4-6 semanas",
            "alta": "8-12 semanas"
        }.get(nivel_complexidade, "4-8 semanas")
    
    print(f"🤖 Complexidade: {nivel_complexidade.upper()} | Esforço: {horas_estimadas}h | Preço: {preco} | Timeline: {timeline}")
    
    # Verificar se temos análise de ROI para incorporar na proposta
    if 'roi_summary' in locals():
        # Adicionar análise de ROI ao esboço de arquitetura
        arquitetura_proposta_completa = arquitetura_proposta + "\n\n" + roi_summary
        print("🤖 Análise de ROI incorporada à proposta.")
    else:
        arquitetura_proposta_completa = arquitetura_proposta
        print("⚠️ Análise de ROI não disponível para incorporação.")
    
    # Garantir que todos os parâmetros necessários estejam definidos
    client_name = nome_cliente if 'nome_cliente' in locals() else 'Cliente'
    client_company = nome_empresa if 'nome_empresa' in locals() and nome_empresa else 'Empresa'
    problem_desc = briefing if briefing else 'Briefing não disponível'
    arch_sketch = arquitetura_proposta_completa if arquitetura_proposta_completa else 'Descrição da solução não disponível'
    price_value = preco if 'preco' in locals() and preco else 'Preço a definir'
    timeline_value = timeline if 'timeline' in locals() and timeline else '4-8 semanas'
            
    # Definir diretório para salvar as propostas geradas
    output_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'documentos_gerados')
    
    # Gerar proposta incorporando a análise e descrição detalhada do arquiteto
    print("\n📝 Gerando proposta final...")
    proposta = custom_build_proposal(
        client_name=client_name,
        client_company=client_company,
        problem_description=problem_desc,
        architecture_sketch=arch_sketch,
        price=price_value,
        estimated_timeline=timeline_value,
        output_dir=output_dir
    )
    print(proposta)

    # 5. Encerrar ou seguir fluxo conforme desejado
    print("\nFluxo concluído. Volte ao menu inicial para nova operação ou finalize o sistema.")
    input("👤 Revise e envie a proposta ao cliente. Pressione ENTER para continuar após envio.")
    if task_id:
        update_task_status(task_id, "proposta_enviada")

    # 7. Negócio fechado
    resultado_negociacao = input("👤 Negociação concluída? (sim/não): ")
    if resultado_negociacao.lower() == "sim" and task_id:
        update_task_status(task_id, "proposta_aceita")
        print("🤖 Status atualizado para 'Proposta Aceita'.")
        
        # 8. Verificação de pagamento
        pagamento_realizado = input("👤 Pagamento inicial realizado? (sim/não): ")
        if pagamento_realizado.lower() == "sim" and task_id:
            update_task_status(task_id, "venda_realizada")
            print("🤖 Status atualizado para 'Venda Realizada'.")
            print("🎉 Venda concluída com sucesso! Agora é hora de iniciar o projeto.")
        else:
            print("Aguardando pagamento para concluir o processo de venda.")
    else:
        print("Fluxo encerrado sem fechamento de negócio.")
        return
        
    print("\n=== FIM DO FLUXO FSTECH ===\n")

if __name__ == "__main__":
    print("\n=== ORQUESTRADOR FSTECH INICIADO ===\n")
    while True:
        print("\nEscolha uma opção:")
        print("1. Executar fluxo operacional simplificado FSTech")
        print("2. Interagir livremente com o orquestrador (prompt)")
        print("0. Sair")
        escolha = input("Opção: ")
        if escolha == "1":
            fluxo_fstech()
        elif escolha == "2":
            user_input = input("Digite sua solicitação para a agência: ")
            result = orquestrador.run(user_input)
            print("\n=== RESPOSTA DA AGÊNCIA ===\n")
            print(result)
            print("\n==========================\n")
        elif escolha == "0":
            break
        else:
            print("Opção inválida.")
