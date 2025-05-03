# Agente: Especialista Técnico

import json

# Importar ferramentas refatoradas
from .tools import (
    automation_setup_wizard, 
    llm_fine_tuner, 
    prompt_engineering_assistant, 
    api_integrator, 
    platform_configuration_manager
)

# --- Definição do Agente (Estilo OpenAI SDK) ---

# Carregar instruções do arquivo .md (ou definir diretamente)
ESPECIALISTA_INSTRUCTIONS = """
Você é o Especialista Técnico da FSTech Consulting Agency. Sua principal responsabilidade é a execução prática e a implementação das soluções tecnológicas definidas no roadmap do cliente. Você trabalha na configuração de plataformas, automação de processos, integração de APIs, e pode envolver tarefas como fine-tuning de LLMs e engenharia de prompts, garantindo que as soluções sejam entregues com qualidade e eficiência.

Responsabilidades Principais:
*   Implementação Técnica: Executar as tarefas técnicas descritas no roadmap e no plano de projeto.
*   Configuração de Plataformas: Configurar softwares, CRMs, ferramentas de automação, etc.
*   Automação de Processos: Desenvolver e implementar fluxos de trabalho automatizados.
*   Integração de APIs: Conectar diferentes sistemas e serviços usando APIs.
*   Fine-tuning de LLMs (quando aplicável): Ajustar modelos de linguagem para tarefas específicas.
*   Engenharia de Prompts (quando aplicável): Criar e otimizar prompts para LLMs.
*   Testes e Validação: Garantir que as soluções funcionem corretamente.
*   Documentação Técnica: Documentar as implementações.
*   Colaboração: Trabalhar com Arquiteto de Software e Coordenador de Projetos.

Diretrizes Gerais:
*   Siga as especificações técnicas e a arquitetura definida.
*   Priorize a qualidade e a robustez.
*   Documente seu trabalho.
*   Comunique desafios proativamente.

Use as ferramentas disponíveis para cumprir suas responsabilidades.
"""

# Lista de ferramentas disponíveis para este agente
ESPECIALISTA_TOOLS = [
    automation_setup_wizard.setup_automation,
    llm_fine_tuner.fine_tune_llm,
    prompt_engineering_assistant.optimize_prompt,
    api_integrator.integrate_api,
    platform_configuration_manager.configure_platform
]

# Função para criar a definição do agente
def create_especialista_agent_definition():
    """Retorna a definição do Agente Especialista Técnico."""
    return {
        "name": "Especialista Técnico Agent - FSTech",
        "instructions": ESPECIALISTA_INSTRUCTIONS,
        "tools": ESPECIALISTA_TOOLS
    }

# --- Lógica de Execução (Exemplo Simplificado - Sem LLM Real) ---

def run_especialista_task(task_description: str, context: dict = None):
    """Simula a execução de uma tarefa pelo Agente Especialista (sem LLM real)."""
    agent_def = create_especialista_agent_definition()
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

    if "automação" in task_lower or "automatizar" in task_lower:
        selected_tool = automation_setup_wizard.setup_automation
        args = {
            "platform": context.get("platform", "Zapier"), 
            "task_description": context.get("automation_task", task_description),
            "credentials": context.get("credentials")
        }
    elif "fine-tuning" in task_lower or "fine tune" in task_lower:
        selected_tool = llm_fine_tuner.fine_tune_llm
        args = {
            "base_model": context.get("base_model", "openai/gpt-3.5-turbo"),
            "dataset_path": context.get("dataset_path", "/path/to/default_dataset.jsonl"),
            "hyperparameters": context.get("hyperparameters")
        }
    elif "prompt" in task_lower or "otimizar prompt" in task_lower:
        selected_tool = prompt_engineering_assistant.optimize_prompt
        args = {
            "original_prompt": context.get("original_prompt", task_description),
            "task_type": context.get("task_type", "Geral"),
            "target_model": context.get("target_model", "geral")
        }
    elif "integrar api" in task_lower or "integração" in task_lower:
        selected_tool = api_integrator.integrate_api
        args = {
            "source_api_details": context.get("source_api", {}),
            "target_system_details": context.get("target_system", {}),
            "data_mapping": context.get("mapping", {})
        }
    elif "configurar plataforma" in task_lower or "configuração" in task_lower:
        selected_tool = platform_configuration_manager.configure_platform
        args = {
            "platform_name": context.get("platform_name", "Salesforce"),
            "configuration_details": context.get("config_details", {})
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
        no_tool_message = "Nenhuma ferramenta apropriada encontrada (simulado). Tarefa pode exigir análise manual ou mais detalhes."
        print(f"\n{no_tool_message}")
        return no_tool_message, context

# Exemplo de execução de tarefa
if __name__ == "__main__":
    contexto_automacao = {
        "platform": "Make.com",
        "automation_task": "Quando novo item adicionado ao Airtable, criar card no Trello."
    }
    run_especialista_task("Configurar automação entre Airtable e Trello", contexto_automacao)
    print("\n=========================================\n")

    contexto_finetune = {
        "base_model": "meta-llama/Llama-2-7b-chat-hf",
        "dataset_path": "/home/ubuntu/datasets/faq_fstech.jsonl"
    }
    run_especialista_task("Realizar fine-tuning do Llama 2 com nosso FAQ", contexto_finetune)
    print("\n=========================================\n")

    contexto_prompt = {
        "original_prompt": "Resuma este longo relatório financeiro.",
        "task_type": "Sumarização",
        "target_model": "Claude 3 Opus"
    }
    run_especialista_task("Otimizar prompt de sumarização", contexto_prompt)
    print("\n=========================================\n")

    contexto_integracao = {
        "source_api": {"name": "Stripe API", "endpoint": "/v1/charges"},
        "target_system": {"name": "QuickBooks API", "endpoint": "/v3/company/.../invoice"},
        "mapping": {"amount": "TotalAmt", "customer": "CustomerRef"}
    }
    run_especialista_task("Integrar API do Stripe com QuickBooks", contexto_integracao)
    print("\n=========================================\n")

    contexto_config = {
        "platform_name": "HubSpot",
        "config_details": {"object": "Deal", "action": "create_pipeline_stage", "stage_name": "Proposta Enviada"}
    }
    run_especialista_task("Configurar novo estágio no pipeline de Vendas do HubSpot", contexto_config)

