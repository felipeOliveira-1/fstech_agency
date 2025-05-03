# Ferramenta: Gerenciador de Configuração de Plataforma

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def configure_platform(platform_name: str, configuration_details: dict) -> str:
    """Configura ou ajusta configurações em plataformas de software específicas.

    Use esta ferramenta para aplicar configurações específicas em plataformas como
    CRMs (Salesforce, HubSpot), ERPs, ou outras ferramentas de negócio, com base
    nos detalhes fornecidos.

    Args:
        platform_name: O nome da plataforma a ser configurada (ex: 	Salesforce	, 	HubSpot	, 	SAP	).
        configuration_details: Um dicionário com as configurações a serem aplicadas (ex: {"object": "Lead", "field": "Status", "new_value": "Qualified"}).

    Returns:
        Uma string confirmando a aplicação da configuração ou uma mensagem de erro.
    """
    # Validação básica
    if not platform_name or not configuration_details or not isinstance(configuration_details, dict):
        return "Erro: Nome da plataforma (platform_name) e detalhes da configuração (configuration_details como dict) são necessários."

    print(f"Aplicando configuração na plataforma {platform_name}...")
    print(f"Detalhes da Configuração: {configuration_details}")

    # Lógica simulada de configuração
    # Em um cenário real, isso envolveria chamadas de API específicas da plataforma
    # para modificar configurações, criar campos customizados, ajustar permissões, etc.

    # Exemplo: Extrair detalhes para simulação
    obj = configuration_details.get("object", "N/A")
    field = configuration_details.get("field", "N/A")
    value = configuration_details.get("new_value", "N/A")

    # Simulação de sucesso
    confirmation_message = f"Configuração aplicada com sucesso na plataforma {platform_name}. Detalhes: Objeto 	{obj}	, Campo 	{field}	, Novo Valor 	{value}	 (simulado)."

    print(confirmation_message)
    return confirmation_message

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    config1 = {
        "object": "Opportunity",
        "action": "add_custom_field",
        "field_name": "FSTech_Consulting_Phase__c",
        "field_type": "Picklist",
        "picklist_values": ["Diagnóstico", "Implementação", "Otimização"]
    }
    status1 = configure_platform(platform_name="Salesforce", configuration_details=config1)
    print(f"\nStatus Final 1: {status1}")

    config2 = {
        "object": "Contact",
        "workflow_rule": "Update Lead Score on Email Open",
        "action": "activate_rule"
    }
    status2 = configure_platform(platform_name="HubSpot", configuration_details=config2)
    print(f"\nStatus Final 2: {status2}")

