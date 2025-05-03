# Ferramenta: Assistente de Configuração de Automação

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def setup_automation(platform: str, task_description: str, credentials: dict = None) -> str:
    """Configura automações em plataformas como Zapier, Make.com ou n8n.

    Use esta ferramenta para criar ou configurar fluxos de trabalho automatizados
    baseados na descrição da tarefa fornecida pelo cliente ou coordenador.

    Args:
        platform: A plataforma de automação a ser usada (ex: 	Zapier	, 	Make.com	, 	N8N	).
        task_description: Uma descrição clara da automação desejada (ex: 	Quando um novo lead chegar no CRM, enviar notificação no Slack e criar tarefa no ClickUp	).
        credentials: (Opcional) Dicionário com credenciais necessárias (em um cenário real, usar gerenciamento seguro de segredos).

    Returns:
        Uma string confirmando a configuração da automação ou uma mensagem de erro.
    """
    # Validação básica
    if not platform or not task_description:
        return "Erro: Plataforma (platform) e descrição da tarefa (task_description) são necessários."

    supported_platforms = ["zapier", "make.com", "n8n"]
    if platform.lower() not in supported_platforms:
        return f"Erro: Plataforma 	{platform}	 não suportada. Use uma de: {', '.join(supported_platforms)}"

    print(f"Configurando automação na plataforma {platform} para a tarefa: 	{task_description}	...")

    # Lógica simulada de configuração
    # Em um cenário real, isso envolveria chamadas de API para a plataforma
    # ou interação via UI (se usando RPA/modelos de uso de computador)
    if credentials:
        print("Usando credenciais fornecidas (simulado).")
        # Exemplo: api_key = credentials.get("api_key")

    automation_id = f"{platform.lower()}-{hash(task_description) % 10000}"
    confirmation_message = f"Automação configurada com sucesso na plataforma {platform}. ID da Automação (simulado): {automation_id}. Tarefa: 	{task_description}	."

    print(confirmation_message)
    return confirmation_message

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    task = "Quando um email com assunto 	Fatura	 chegar, salvar anexo no Google Drive."
    creds = {"google_api_key": "SIMULATED_KEY"}
    result = setup_automation(platform="Zapier", task_description=task, credentials=creds)
    print(result)

    print("\n--- Plataforma Inválida ---")
    result_invalid = setup_automation(platform="InvalidPlatform", task_description=task)
    print(result_invalid)

