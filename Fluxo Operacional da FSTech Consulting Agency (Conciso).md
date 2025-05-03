# Fluxo Operacional da FSTech Consulting Agency (Conciso)

Este documento descreve o fluxo de trabalho padrão da agência, desde a identificação da oportunidade até a conclusão do projeto, indicando as etapas manuais e as ações realizadas pelos agentes de IA.

**Legenda:**
*   👤 **Usuário:** Ação manual realizada por você.
*   🤖 **Agente:** Ação realizada por um agente de IA (com ferramentas específicas).

---

1.  👤 **Usuário:** Identifica e fornece os detalhes da nova oportunidade (ex: da plataforma Asimov, email, etc.).

2.  🤖 **Agente (Gerente Mkt/Consultor):**
    *   Recebe os detalhes da oportunidade.
    *   *(Opcional/Futuro)* Usa `crm_lead_creator` para registrar o lead no ClickUp (Status: "Oportunidade Identificada").
    *   Passa a informação para o `Consultor de Diagnóstico`.

3.  🤖 **Agente (Consultor):**
    *   Usa o LLM (OpenAI Assistant) para analisar os detalhes da oportunidade.
    *   Gera uma **sugestão** de mensagem de contato inicial (Email/WhatsApp) para agendar a reunião de diagnóstico.

4.  👤 **Usuário:**
    *   Revisa a sugestão de mensagem.
    *   Envia a mensagem ao contato principal da oportunidade.

5.  👤 **Usuário:**
    *   Recebe a confirmação e a data/hora da reunião.
    *   Informa a data/hora agendada aos agentes.

6.  🤖 **Agente (Suporte/Consultor):**
    *   Usa `appointment_scheduler_manager` para agendar a reunião no Cal.com (ou outro calendário integrado).

7.  🤖 **Agente (Consultor):**
    *   Usa `crm_status_updater` para atualizar o status no ClickUp para "Contato Realizado" e depois "Reunião Agendada".

8.  👤 **Usuário:**
    *   Conduz a reunião de diagnóstico com o cliente.
    *   Faz anotações detalhadas ou grava a reunião.

9.  🤖 **Agente (Consultor):**
    *   Usa `crm_status_updater` para atualizar o status no ClickUp para "Reunião Realizada".

10. 👤 **Usuário:**
    *   Fornece as anotações/transcrição da reunião aos agentes (via prompt ou upload de arquivo, se implementado).

11. 🤖 **Agente (Consultor - Líder da Fase):**
    *   Recebe as anotações/transcrição.
    *   Usa o LLM para iniciar e coordenar a fase de elaboração da proposta, interagindo com outros agentes conforme necessário.

12. 🤖 **Agente (Consultor -> Arquiteto):**
    *   `Consultor` envia requisitos técnicos.
    *   `Arquiteto` usa `system_architecture_designer` para analisar viabilidade, esboçar arquitetura e estimar complexidade.
    *   `Arquiteto` retorna a análise para o `Consultor`.

13. 🤖 **Agente (Consultor -> Especialista):**
    *   `Consultor` envia esboço da arquitetura.
    *   `Especialista` usa `effort_estimator` (ferramenta futura) para estimar o esforço de implementação.
    *   `Especialista` retorna a estimativa para o `Consultor`.

14. 🤖 **Agente (Consultor/CEO):**
    *   Usa `pricing_calculator` (com inputs de complexidade, esforço, margem) para calcular o preço.
    *   *(Opcional)* Pode usar ferramentas de pesquisa web para embasar a precificação.

15. 🤖 **Agente (Consultor):**
    *   Consolida todas as informações (escopo, arquitetura, esforço, preço, prazo estimado).
    *   Usa `proposal_builder` para gerar o documento da proposta em formato Markdown (`.md`).

16. 👤 **Usuário:**
    *   Revisa cuidadosamente a proposta gerada pelo agente.
    *   Faz ajustes finais, se necessário.
    *   Envia a proposta ao cliente.

17. 🤖 **Agente (Consultor):**
    *   Usa `crm_status_updater` para atualizar o status no ClickUp para "Proposta Enviada" e, posteriormente, "Aguardando Resposta".

18. 👤 **Usuário:**
    *   Conduz a negociação com o cliente.
    *   Informa o resultado (aceite ou recusa) aos agentes.

19. 🤖 **Agente (Consultor):**
    *   Se aceita, usa `crm_status_updater` para atualizar o status no ClickUp para "Proposta Aceita".

20. 🤖 **Agente (Suporte/Legal):**
    *   Recebe os detalhes da proposta aceita.
    *   Usa `contract_generator` para gerar um rascunho do contrato em formato Markdown (`.md`).

21. 👤 **Usuário:**
    *   Revisa cuidadosamente o contrato gerado.
    *   Faz ajustes legais/finais, se necessário (idealmente com apoio jurídico).
    *   Envia o contrato ao cliente para assinatura.

22. 🤖 **Agente (Consultor):**
    *   Após assinatura, usa `crm_status_updater` para atualizar o status no ClickUp para "Venda Realizada".

23. 🤖 **Agente (Consultor -> Coordenador):**
    *   `Consultor` faz o handover formal do projeto (documentação, proposta, contrato, etc.) para o `Coordenador de Projetos`.

24. 🤖 **Agente (Coordenador):**
    *   Usa `crm_project_status_updater` para atualizar o status da tarefa principal no CRM para "Projeto em Andamento".
    *   Inicia o planejamento detalhado do projeto (usando `project_timeline_manager`, `task_assignment_manager` - ferramentas futuras ou integrações com ClickUp).

25. 🤖 **Agente (Coordenador):**
    *   Durante a execução, usa `progress_tracker` (integrado ao ClickUp) para monitorar o andamento.
    *   Usa `client_update_sender` (ferramenta futura) para enviar atualizações periódicas ao cliente.

26. 🤖 **Agente (Coordenador):**
    *   Após a conclusão e entrega, usa `crm_project_status_updater` para atualizar o status no ClickUp para "Projeto Concluído".

---

**Observações:**

*   Este fluxo assume a utilização das ferramentas e integrações que implementamos (OpenAI Assistants, ClickUp, Cal.com) e algumas que ainda são placeholders.
*   As etapas manuais (👤 Usuário) são cruciais para revisão, contato direto com o cliente e decisões finais.
*   A comunicação entre agentes é atualmente simulada através de prompts sequenciais ou coordenação manual, mas pode ser automatizada com uma camada de orquestração mais avançada no futuro.
