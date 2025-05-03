# FSTech Consulting Agency

## Visão Geral

A **FSTech Consulting Agency** é uma plataforma de consultoria tecnológica que automatiza e orquestra todo o ciclo de atendimento a pequenas e médias empresas (PMEs), solopreneurs e profissionais em transição digital. O objetivo é simplificar processos, otimizar operações e impulsionar o crescimento sustentável dos clientes, unindo tecnologia, consultoria personalizada e automação de ponta a ponta.

**Tagline:** Tecnologia simplificada para o seu crescimento.

## Propósito, Missão e Visão

- **Propósito:** Tornar a tecnologia acessível, prática e personalizada para empresas e profissionais, facilitando a adoção de soluções inovadoras e eficientes.
- **Missão:** Capacitar clientes com ferramentas e conhecimento tecnológico, entregando diagnóstico preciso, soluções sob medida e suporte contínuo.
- **Visão:** Ser referência em consultoria tecnológica para PMEs e profissionais em adaptação digital.

---

## Estrutura do Projeto

O projeto está organizado de forma modular, com cada diretório representando um agente ou função dentro da agência. Cada agente possui ferramentas próprias para executar tarefas específicas.

```
FSTech_Consulting_Agency/
├── CEO/
├── Consultor_de_Diagnostico/
├── Especialista_Tecnico/
├── Arquiteto_de_Software/
├── Suporte_Administrativo/
├── Gerente_de_Marketing_Digital/
├── Coordenador_de_Projetos/
├── utils/
├── tests/
├── agency.py
├── agency_manifesto.md
├── communication_flows.md
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── MANUAL.md
```

- **app.py**: Interface principal (Streamlit), orquestra todo o fluxo operacional.
- **orquestrador_fstech.py**: Hub central de lógica, coordena agentes e integrações.
- **requirements.txt**: Lista de dependências do projeto.
- **tests/**: Testes automatizados.
- **agency_manifesto.md**: Propósito, missão, visão e valores.
- **communication_flows.md**: Descreve fluxos de comunicação internos e externos.

---

## Como Funciona: Fluxo Operacional

O sistema guia o usuário (consultor) por todas as etapas do ciclo de vendas e atendimento, de forma automatizada e interativa:

1. **Início do Processo**
   - Usuário preenche dados do cliente (nome, empresa, briefing, objetivo).
   - Criação automática de lead no CRM (ClickUp).

2. **Briefing e Diagnóstico**
   - Exibição e análise do briefing.
   - Geração automática de mensagem para o cliente.

3. **Análise de Oportunidade**
   - Avaliação do potencial do projeto.
   - Registro de observações.

4. **Agendamento de Reunião**
   - Proposta de datas/horários.
   - Integração com Cal.com para agendamento automático.

5. **Análise Técnica**
   - Avaliação do arquiteto de software.
   - Sugestão de arquitetura e análise de complexidade.

6. **Pesquisa de Mercado**
   - Consultor pode realizar pesquisas e coletar dados para embasar a proposta.

7. **Geração de Proposta**
   - Coleta de parâmetros (valor, horas, cronograma).
   - Geração automatizada de proposta em Markdown.
   - Preview e exportação da proposta.

8. **Envio e Negociação**
   - Confirmação de envio da proposta.
   - Acompanhamento de status (aceita, recusada, aguardando).
   - Registro de feedbacks e reinício de fluxo, se necessário.

9. **Fechamento e Pós-venda**
   - Orientação sobre próximos passos (contrato, kick-off).
   - Atualização de status no CRM.

---

## Principais Funcionalidades e Agentes

- **Consultor de Diagnóstico:** Intake, diagnóstico, roadmap, propostas, integração com ClickUp.
- **Especialista Técnico:** Implementação técnica das soluções.
- **Arquiteto de Software:** Design de arquitetura, análise técnica.
- **Analista de ROI:** Análise de retorno sobre investimento.
- **Gerente de Marketing Digital:** Geração de leads, criação de campanhas e leads no CRM.
- **Coordenador de Projetos:** Orquestração, acompanhamento de projetos e tarefas.
- **Suporte Administrativo:** Pós-venda, agendamento (Cal.com), suporte não-técnico.
- **CEO:** Estratégia, expansão e relacionamento VIP.

Cada agente possui scripts e ferramentas próprias, localizados em seus respectivos diretórios.

---

## Integrações e Tecnologias

- **Python** (com Streamlit para interface)
- **OpenAI API** (para geração de conteúdo e automação de propostas)
- **ClickUp API** (CRM: criação e atualização de tarefas, funil de vendas)
- **Cal.com API** (agendamento de reuniões)
- **Pandas** (tratamento de dados)
- **Ambiente virtual** (venv)

---

## Instalação e Configuração

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/FSTech_Consulting_Agency_openai_integrated.git
   cd FSTech_Consulting_Agency_openai_integrated
   ```

2. **Crie e ative um ambiente virtual:**
   ```bash
   python -m venv venv
   # Ative o ambiente (Windows):
   venv\Scripts\activate
   # Ou (Linux/Mac):
   source venv/bin/activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure as variáveis de ambiente:**
   - Copie `.env.example` para `.env` e preencha com suas chaves:
     ```env
     CLICKUP_API_KEY=SUA_CHAVE_API_CLICKUP_AQUI
     CALCOM_API_KEY=SUA_CHAVE_API_CALCOM_AQUI
     OPENAI_API_KEY=SUA_CHAVE_API_OPENAI_AQUI
     ```

5. **Execute a aplicação principal:**
   ```bash
   streamlit run app.py
   ```

---

## Como Usar

- Acesse a interface web do Streamlit (geralmente em http://localhost:8501).
- Siga as etapas do fluxo operacional, preenchendo os dados conforme solicitado.
- Utilize as abas para acompanhar logs, interagir com agentes e acessar informações sobre o sistema.
- Propostas, diagnósticos e registros são gerados automaticamente e podem ser exportados ou enviados ao cliente.

---

## Testes Automatizados

O projeto inclui testes automatizados para garantir a qualidade e estabilidade do código, especialmente para o fluxo de processamento de transcrições de reuniões:

### Estrutura de Testes

```
tests/
├── Arquiteto_de_Software/
├── CEO/
├── Consultor_de_Diagnostico/
├── Coordenador_de_Projetos/
├── Especialista_Tecnico/
├── Gerente_de_Marketing_Digital/
├── Suporte_Administrativo/
├── Analista_ROI/
│   └── test_analista_roi.py     # Testes para o Analista de ROI
├── integration_test_fluxo.py     # Testes de integração para fluxos completos
└── __init__.py
```

### Tipos de Testes

1. **Testes Unitários**: Verificam se cada agente funciona corretamente individualmente.
   - Exemplo: `test_analista_roi.py` testa o processamento de transcrições da reunião pelo Analista de ROI.

2. **Testes de Integração**: Verificam se todo o fluxo funciona corretamente.
   - Exemplo: `integration_test_fluxo.py` testa o fluxo completo desde a entrada da transcrição até sua análise pelos agentes Arquiteto e Analista de ROI.

### Executando os Testes

Para rodar todos os testes:
```bash
python -m pytest
```

Para rodar testes específicos:
```bash
# Testes do Analista de ROI
python -m pytest FSTech_Consulting_Agency/tests/Analista_ROI/

# Testes de integração
python -m pytest FSTech_Consulting_Agency/tests/integration_test_fluxo.py
```

> **Importante**: Execute os testes a partir da raiz do projeto para garantir que todos os imports funcionem corretamente.

## Contribuindo com o Projeto

1. **Fork este repositório** e crie uma branch para sua feature ou correção.
2. **Siga o padrão de código** (PEP8 para Python) e documente suas funções.
3. **Adicione testes** na pasta `tests/` sempre que possível.
4. **Abra um Pull Request** detalhando sua contribuição.
5. Sugestões de melhorias, novos fluxos e integrações são bem-vindos!

---

## Roadmap e Próximos Passos

- Refino da interface e experiência do usuário.
- Expansão dos fluxos pós-venda e gestão de projetos.
- Novas integrações (ex: ERPs, WhatsApp, automações adicionais).
- Maior cobertura de testes automatizados.
- Internacionalização e documentação multilíngue.

---

## Suporte e Contato

- Dúvidas, sugestões ou problemas: abra uma issue ou envie email para contato@fstechagency.com
- Mais detalhes sobre missão, visão e valores: consulte `agency_manifesto.md`
- Para detalhes técnicos de cada agente, consulte os diretórios correspondentes e o `MANUAL.md`

---

**FSTech Consulting Agency — Tecnologia simplificada para o seu crescimento.**

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
