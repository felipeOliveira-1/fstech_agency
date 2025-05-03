# FSTech Consulting Agency - Estrutura do Projeto

## Visão Geral

Este repositório contém a estrutura base para a **FSTech Consulting Agency**, uma agência de consultoria focada em auxiliar pequenas e médias empresas (PMEs), solopreneurs e adultos em adaptação tecnológica a adotar soluções de IA e automação de forma acessível e personalizada.

O objetivo principal é simplificar processos, automatizar tarefas e impulsionar o crescimento dos clientes através de consultoria, implementação e suporte tecnológico especializado, seguindo as diretrizes de desenvolvimento de agentes da OpenAI.

**Tagline:** Tecnologia simplificada para o seu crescimento.

## Estrutura do Projeto

O projeto está organizado em diretórios, cada um representando um agente (função) dentro da agência, com ferramentas específicas e instruções claras:

```
FSTech_Consulting_Agency/
├── CEO/
│   ├── __init__.py
│   ├── ceo.py
│   ├── instructions.md
│   └── tools/
│       ├── business_strategy_builder.py
│       ├── client_relationship_manager.py
│       ├── kpi_dashboard_manager.py
│       └── risk_assessment_tool.py
├── Consultor_de_Diagnostico/
│   ├── ...
│   └── tools/
│       ├── client_intake_form_generator.py
│       ├── crm_status_updater.py  # Integrado com ClickUp
│       ├── proposal_builder.py
│       ├── roadmap_generator.py
│       └── tech_diagnostic_analyzer.py
├── Especialista_Tecnico/
│   └── ...
├── Arquiteto_de_Software/
│   └── ...
├── Suporte_Administrativo/
│   └── tools/
│       ├── appointment_scheduler_manager.py # Integrado com Cal.com
│       ├── client_support_bot.py
│       ├── feedback_collector.py
│       └── subscription_tracker.py
├── Gerente_de_Marketing_Digital/
│   └── tools/
│       ├── ad_campaign_launcher.py
│       ├── content_calendar_manager.py
│       ├── crm_lead_creator.py      # Integrado com ClickUp
│       ├── seo_optimizer.py
│       └── social_media_post_generator.py
├── Coordenador_de_Projetos/
│   └── tools/
│       ├── client_update_sender.py
│       ├── crm_project_status_updater.py # Integrado com ClickUp
│       ├── progress_tracker.py         # Integrado com ClickUp
│       ├── project_timeline_manager.py
│       └── task_assignment_manager.py
├── utils/
│   ├── __init__.py
│   └── clickup_client.py       # Utilitário para API ClickUp
├── tests/                      # Estrutura para testes futuros
├── agency.py                 # Arquivo principal da agência (placeholder)
├── agency_manifesto.md       # Define propósito, visão, missão e valores
├── communication_flows.md    # Descreve a comunicação interna e externa
├── requirements.txt          # Dependências Python (inclui openai, clickup-python, requests, python-dotenv)
├── .env.example              # Exemplo de variáveis de ambiente (CLICKUP_API_KEY, CALCOM_API_KEY, OPENAI_API_KEY)
├── .gitignore                # Arquivos a serem ignorados pelo Git
├── README.md                 # Este arquivo
└── MANUAL.md                 # Guia de uso e entendimento da estrutura
```

## Agentes e Funcionalidades Chave

A agência é composta por agentes especializados:

1.  **CEO:** Estratégia, supervisão, relacionamento VIP. **(Com acesso web para pesquisa)**
2.  **Consultor de Diagnóstico:** Diagnóstico, roadmap, propostas, atualização de status no CRM (ClickUp). **(Com acesso web para pesquisa)**
3.  **Especialista Técnico:** Implementação técnica.
4.  **Arquiteto de Software:** Design de arquitetura.
5.  **Suporte Administrativo:** Pós-venda, agendamentos (Cal.com), suporte não-técnico.
6.  **Gerente de Marketing Digital:** Geração de leads, criação de leads no CRM (ClickUp).
7.  **Coordenador de Projetos:** Orquestração de projetos, atualização de status de projeto/tarefas no CRM (ClickUp).

**Integrações Implementadas:**

*   **ClickUp:** Agentes atualizam e criam tarefas na lista de CRM (ID `901311371093`) e Contatos (ID `901311372158`) usando a API v2 via `utils/clickup_client.py`.
*   **Cal.com:** O `Suporte Administrativo` pode agendar reuniões usando a API v2 via `appointment_scheduler_manager.py`.
*   **Acesso Web:** Os agentes `Consultor` e `CEO` possuem instruções para usar ferramentas de pesquisa web para análise de mercado e precificação.

## Como Funciona (Visão Geral)

1.  **Setup:** Configure suas chaves de API para ClickUp e Cal.com no arquivo `.env` (criado a partir do `.env.example`). Instale as dependências com `pip install -r requirements.txt`.
2.  **Fluxo:** O fluxo comercial (descrito no `MANUAL.md` e refinado nas interações) guia a colaboração entre os agentes. Por exemplo:
    *   Uma nova oportunidade aciona o `Gerente de Marketing` para criar um lead no ClickUp.
    *   O `Consultor` interage com o lead, e o `Suporte` agenda a reunião via Cal.com.
    *   O `Consultor` atualiza o status no ClickUp.
    *   Para a proposta, o `Consultor` colabora com `Arquiteto` e `Especialista` (usando ferramentas futuras) e usa pesquisa web para precificação.
    *   Após a venda, o `Coordenador` atualiza o status do projeto no ClickUp e gerencia as tarefas.
3.  **Execução (Simulada):** Os arquivos `[agent_name].py` contêm uma lógica *simulada* de como um LLM poderia orquestrar as ferramentas com base em uma descrição de tarefa. Os exemplos `if __name__ == "__main__":` nas ferramentas permitem testar as integrações com ClickUp e Cal.com diretamente (após configurar o `.env` e IDs de teste).

## Funcionalidades Implementadas

### Orquestrador FSTech

O projeto agora conta com um orquestrador central (`orquestrador_fstech.py`) que implementa um fluxo operacional completo, integrando todas as etapas do processo de vendas:

1. **Leitura de briefing inicial:** Sistema lê automaticamente do arquivo `briefing_inicial.txt`
2. **Criação de lead no ClickUp:** Gera automaticamente uma tarefa no CRM com as informações do cliente
3. **Análise de desafio e setor:** Extrai e confirma as informações-chave do briefing
4. **Agendamento no Cal.com:** Interface com API do Cal.com para agendar reuniões com clientes
5. **Leitura da ata da reunião:** Sistema lê automaticamente do arquivo `ata_reuniao.txt`
6. **Geração de proposta técnica:** Constrói proposta personalizada com base nos dados coletados
7. **Atualização de status no ClickUp:** Gerencia o funil de vendas automaticamente (Oportunidade → Reunião Agendada → Reunião Realizada → Proposta Enviada → Proposta Aceita → Venda Realizada)

### Integrações Funcionais

* **ClickUp:** Implementação completa para criação e atualização de tarefas no CRM usando a API v2
* **Cal.com:** Agendamento funcional de reuniões com validação de disponibilidade
* **Entrada de dados via arquivos:** Suporte para carregar briefing e ata de arquivos externos

## Estado Atual do Projeto

O sistema está operacional com um fluxo completo de vendas que vai desde a identificação de oportunidade até a finalização da venda. As ferramentas principais foram implementadas e estão funcionando, incluindo:

* **proposal_builder:** Geração de propostas técnicas funcionais
* **system_architecture_designer:** Análise de complexidade e sugestão de arquitetura
* **clickup_client:** Cliente completo para interação com ClickUp
* **appointment_scheduler_manager:** Interface completa com Cal.com

## Próximos Passos

* **Refinar interface do usuário:** Adicionar interface gráfica para facilitar o uso
* **Expandir fluxos de trabalho:** Implementar fluxos adicionais para gerenciamento de projetos após a venda
* **Melhorar tratamento de erros:** Tornar o sistema mais resiliente a falhas de API
* **Desenvolver Testes:** Criar testes unitários e de integração na pasta `tests/`

Consulte o `MANUAL.md` para mais detalhes sobre a estrutura e use `python -m FSTech_Consulting_Agency.orquestrador_fstech` para executar o fluxo completo.


## Sistema Integrado de Vendas e CRM

O sistema FSTech agora integra múltiplos componentes em um fluxo coeso para o processo de vendas e gestão de clientes:

### Orquestrador Principal

O arquivo `orquestrador_fstech.py` funciona como o hub central do sistema, coordenando todos os agentes e ferramentas. Ele oferece:

* **Menu de opções interativo** para navegação do sistema
* **Fluxo operacional simplificado** que guia o usuário passo a passo
* **Integração com todas as ferramentas** da agência

### Como Funciona:

1. O orquestrador inicia e apresenta as opções ao usuário
2. Ao selecionar o fluxo operacional, o sistema:
   * Lê o briefing inicial do arquivo `briefing_inicial.txt`
   * Cria automaticamente uma tarefa no ClickUp usando a API
   * Extrai e analisa informações relevantes do briefing
   * Gerencia o agendamento de reuniões via Cal.com
   * Lê a ata da reunião do arquivo `ata_reuniao.txt`
   * Gera uma proposta técnica personalizada
   * Atualiza o status no ClickUp conforme o progresso
   * Finaliza o processo após a venda ser realizada

### Integrações e APIs

O sistema está totalmente funcional com:

* **ClickUp API:** Para gerenciamento de CRM e tarefas
* **Cal.com API:** Para agendamento de reuniões
* **System Designer:** Para análise de requisitos técnicos
* **Proposal Builder:** Para geração de propostas comerciais

**Configuração:**

1.  **Chave API OpenAI:** Obtenha sua chave de API no site da OpenAI.
2.  **Arquivo `.env`:** Crie um arquivo `.env` na raiz do projeto (copiando `.env.example`) e adicione sua chave na variável `OPENAI_API_KEY`.
    ```
    CLICKUP_API_KEY=SUA_CHAVE_API_CLICKUP_AQUI
    CALCOM_API_KEY=SUA_CHAVE_API_CALCOM_AQUI
    OPENAI_API_KEY=SUA_CHAVE_API_OPENAI_AQUI
    ```
3.  **Dependências:** Certifique-se de ter instalado as dependências com `pip install -r requirements.txt`.

**Execução (Exemplo com Consultor):**

*   Navegue até o diretório raiz do projeto (`/home/ubuntu/FSTech_Consulting_Agency`).
*   Execute o script do agente usando `python3` (a versão padrão com as dependências instaladas):
    ```bash
    python3 Consultor_de_Diagnostico/consultor_de_diagnostico.py
    ```
*   O script usará o prompt de exemplo definido no bloco `if __name__ == "__main__":`. Você pode modificar este prompt para testar diferentes cenários.

**Observação:** A execução real e as chamadas de API só funcionarão se você fornecer uma chave de API OpenAI válida no arquivo `.env`.
