# Agente: Consultor de Diagnóstico (Integrado com OpenAI Assistants API)

import os
import sys
import time
import json

# Adicionar o diretório raiz do projeto ao sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from dotenv import load_dotenv
from openai import OpenAI

# --- Carregar Configurações ---
load_dotenv(dotenv_path=os.path.join(project_root, ".env")) # Carrega do diretório raiz
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASSISTANT_NAME = "Consultor de Diagnóstico FSTech"
ASSISTANT_MODEL = "gpt-4o" # Ou outro modelo de sua preferência

# --- Importar Ferramentas ---
# (Agora os imports devem funcionar)
from Consultor_de_Diagnostico.tools.client_intake_form_generator import generate_client_intake_form
from Consultor_de_Diagnostico.tools.crm_status_updater import update_crm_task_status
from Consultor_de_Diagnostico.tools.pricing_calculator import calculate_proposal_price
from Consultor_de_Diagnostico.tools.proposal_builder import build_proposal_markdown
# Adicione aqui imports para tech_diagnostic_analyzer e roadmap_generator se/quando implementados

# Mapeamento de nomes de função para funções reais
AVAILABLE_FUNCTIONS = {
    "generate_client_intake_form": generate_client_intake_form,
    "update_crm_task_status": update_crm_task_status,
    "calculate_proposal_price": calculate_proposal_price,
    "build_proposal_markdown": build_proposal_markdown,
    # Adicione outras funções aqui
}

# --- Definição das Ferramentas para OpenAI ---
# (Baseado nas docstrings e argumentos das funções importadas)
OPENAI_TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "generate_client_intake_form",
            "description": "Gera um formulário de intake personalizado (em Markdown) para coletar informações essenciais de novos clientes.",
            "parameters": {
                "type": "object",
                "properties": {
                    "industry": {"type": "string", "description": "O setor de atuação do cliente (ex: Varejo, Saúde, Finanças)."},
                    "main_challenge": {"type": "string", "description": "O principal desafio ou dor que o cliente busca resolver (ex: Baixa eficiência operacional)."}
                },
                "required": ["industry", "main_challenge"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_crm_task_status",
            "description": "Atualiza o status de uma tarefa específica na lista de CRM do ClickUp.",
            "parameters": {
                "type": "object",
                "properties": {
                    "crm_task_id": {"type": "string", "description": "O ID da tarefa na lista de CRM do ClickUp."},
                    "status_key": {"type": "string", "description": "A chave do novo status desejado (ex: 'contato_realizado', 'reuniao_agendada', 'proposta_enviada'). Use as chaves definidas no STATUS_MAP."}
                },
                "required": ["crm_task_id", "status_key"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate_proposal_price",
            "description": "Calcula o preço de uma proposta com base no esforço estimado (horas), nível de complexidade (baixa, media, alta) e margem de lucro desejada (%).",
            "parameters": {
                "type": "object",
                "properties": {
                    "estimated_effort_hours": {"type": "number", "description": "O número total de horas estimadas para o projeto."},
                    "complexity_level": {"type": "string", "enum": ["baixa", "media", "alta"], "description": "O nível de complexidade do projeto ('baixa', 'media', 'alta')."},
                    "desired_margin_percentage": {"type": "number", "description": "A margem de lucro desejada como porcentagem (ex: 20 para 20%)."},
                    "base_hourly_rate": {"type": "number", "description": "(Opcional) A taxa horária base em BRL. Padrão é 150.00 se omitido."}
                },
                "required": ["estimated_effort_hours", "complexity_level", "desired_margin_percentage"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "build_proposal_markdown",
            "description": "Gera um documento de proposta comercial completo em formato Markdown, pronto para ser salvo ou enviado.",
            "parameters": {
                "type": "object",
                "properties": {
                    "client_name": {"type": "string", "description": "Nome do contato principal no cliente."},
                    "client_company": {"type": "string", "description": "Nome da empresa cliente."},
                    "problem_description": {"type": "string", "description": "Descrição detalhada do problema ou necessidade do cliente, conforme discutido.",},
                    "architecture_sketch": {"type": "string", "description": "Esboço da arquitetura ou solução técnica proposta (pode vir do Arquiteto ou ser resumido aqui)."},
                    "price": {"type": "string", "description": "O preço final formatado (ex: 'R$ 10.000,00'), idealmente vindo da ferramenta 'calculate_proposal_price'."},
                    "estimated_timeline": {"type": "string", "description": "O prazo estimado para conclusão do projeto (ex: '4-6 semanas', '3 meses')."},
                    "output_dir": {"type": "string", "description": "(Opcional) Diretório onde o arquivo .md será salvo. Padrão: /home/ubuntu/proposals."}
                },
                "required": ["client_name", "client_company", "problem_description", "architecture_sketch", "price", "estimated_timeline"]
            }
        }
    },
    # Adicionar definições para tech_diagnostic_analyzer e roadmap_generator aqui
    {
        "type": "code_interpreter" # Habilita o Code Interpreter para análises, gráficos, etc.
    },
    {
       "type": "file_search" # Habilita a pesquisa em arquivos fornecidos
    }
]

# --- Funções do Assistente ---

def load_instructions(file_path=os.path.join(project_root, "Consultor_de_Diagnostico/instructions.md")):
    """Carrega as instruções do agente de um arquivo Markdown."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo de instruções não encontrado em {file_path}")
        return "Você é um consultor de diagnóstico útil."

def create_assistant(client):
    """Cria um novo assistente OpenAI com as configurações definidas."""
    instructions = load_instructions()
    print("Criando assistente...")
    assistant = client.beta.assistants.create(
        name=ASSISTANT_NAME,
        instructions=instructions,
        tools=OPENAI_TOOLS,
        model=ASSISTANT_MODEL,
    )
    print(f"Assistente '{assistant.name}' criado com ID: {assistant.id}")
    return assistant

def get_or_create_assistant(client):
    """Busca um assistente existente pelo nome ou cria um novo."""
    try:
        assistants = client.beta.assistants.list(limit=100)
        for assistant in assistants.data:
            if assistant.name == ASSISTANT_NAME:
                print(f"Assistente '{ASSISTANT_NAME}' encontrado com ID: {assistant.id}")
                # Opcional: Atualizar o assistente se as instruções ou ferramentas mudaram
                # instructions = load_instructions()
                # assistant = client.beta.assistants.update(
                #     assistant.id,
                #     instructions=instructions,
                #     tools=OPENAI_TOOLS,
                #     model=ASSISTANT_MODEL,
                # )
                # print(f"Assistente '{assistant.name}' atualizado.")
                return assistant
    except Exception as e:
        print(f"Erro ao listar assistentes: {e}. Tentando criar um novo.")

    # Se não encontrou ou deu erro ao listar, cria um novo
    return create_assistant(client)

def run_assistant(client, assistant_id, user_message):
    """Executa o assistente com uma mensagem do usuário e lida com chamadas de função."""
    print(f"\n--- Iniciando conversa com o {ASSISTANT_NAME} --- ")
    print(f"Usuário: {user_message}")

    thread = client.beta.threads.create()
    print(f"Thread criada: {thread.id}")

    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=user_message,
    )

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant_id,
    )
    print(f"Run iniciado: {run.id}")

    while run.status in ["queued", "in_progress", "requires_action"]:
        if run.status == "requires_action":
            print("\nAssistente requer ação (chamada de ferramenta)...")
            tool_outputs = []
            for tool_call in run.required_action.submit_tool_outputs.tool_calls:
                function_name = tool_call.function.name
                arguments = json.loads(tool_call.function.arguments)
                print(f"  -> Chamando: {function_name}({arguments})")

                if function_name in AVAILABLE_FUNCTIONS:
                    function_to_call = AVAILABLE_FUNCTIONS[function_name]
                    try:
                        output = function_to_call(**arguments)
                        print(f"  <- Resultado: {output}")
                        tool_outputs.append({
                            "tool_call_id": tool_call.id,
                            "output": str(output), # Garante que a saída seja string
                        })
                    except Exception as e:
                        print(f"  <- Erro ao executar {function_name}: {e}")
                        tool_outputs.append({
                            "tool_call_id": tool_call.id,
                            "output": f"Erro ao executar a ferramenta: {e}",
                        })
                else:
                    print(f"  <- Erro: Função '{function_name}' não encontrada.")
                    tool_outputs.append({
                        "tool_call_id": tool_call.id,
                        "output": f"Erro: Função '{function_name}' não disponível.",
                    })

            # Submeter os resultados das ferramentas
            run = client.beta.threads.runs.submit_tool_outputs(
                thread_id=thread.id,
                run_id=run.id,
                tool_outputs=tool_outputs,
            )
            print("Resultados das ferramentas submetidos.")

        else:
            print(f"Aguardando conclusão do run... (Status: {run.status})")
            time.sleep(5) # Espera antes de verificar o status novamente

        # Atualizar o status do run
        run = client.beta.threads.runs.retrieve(thread_id=thread.id, run_id=run.id)

    # Processar a resposta final
    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        assistant_message = ""
        # A resposta mais recente do assistente estará no início da lista
        for msg in messages.data:
            if msg.role == "assistant":
                if msg.content and msg.content[0].type == "text":
                    assistant_message = msg.content[0].text.value
                    break # Pega a primeira resposta do assistente

        print(f"\nAssistente: {assistant_message}")
        print("--- Fim da conversa --- ")
        return assistant_message
    else:
        error_message = f"Run falhou ou foi cancelado. Status: {run.status}"
        if run.last_error:
             error_message += f" Erro: {run.last_error.message}"
        print(error_message)
        print("--- Fim da conversa --- ")
        return error_message

# --- Execução Principal ---
if __name__ == "__main__":
    if not OPENAI_API_KEY or "DUMMY" in OPENAI_API_KEY:
        print("Erro: Chave da API da OpenAI não encontrada ou é uma chave dummy. Defina OPENAI_API_KEY corretamente no arquivo .env")
    else:
        client = OpenAI(api_key=OPENAI_API_KEY)
        assistant = get_or_create_assistant(client)

        # Solicita ao usuário colar a oportunidade
        print("Cole abaixo o texto da oportunidade. Pressione Enter duas vezes para finalizar:")
        lines = []
        while True:
            line = input()
            if line == "":
                break
            lines.append(line)
        user_input = "\n".join(lines)
        prompt = f"""
Analise a oportunidade abaixo e, com base nela, gere:
1. Uma análise técnica e estratégica da oportunidade.
2. Uma sugestão de mensagem de contato para abordar o cliente, pronta para ser enviada. A mensagem deve:
   - Ser cordial, objetiva e personalizada;
   - Utilizar o nome Felipe Silva na apresentação;
   - Sempre incluir a seguinte assinatura ao final:
[Felipe Silva]
[11 972726492]
[website: fstech.digital]

Oportunidade:
{user_input}
"""
        resposta = run_assistant(client, assistant.id, prompt)
        print("\n=== RESPOSTA DO ASSISTENTE ===\n")
        print(resposta)
        print("\n=== FIM DA RESPOSTA ===\n")

