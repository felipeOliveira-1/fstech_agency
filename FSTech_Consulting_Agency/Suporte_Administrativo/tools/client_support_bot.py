# Ferramenta: Bot de Suporte ao Cliente

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def handle_client_support_query(query: str, client_id: str = None) -> str:
    """Responde a perguntas frequentes de clientes ou encaminha para o agente apropriado.

    Use esta ferramenta para lidar com consultas básicas de suporte ao cliente,
    como perguntas sobre faturamento, status do projeto ou problemas técnicos simples.
    Se a consulta for complexa, ela pode sugerir encaminhamento.

    Args:
        query: A pergunta ou solicitação do cliente.
        client_id: (Opcional) O ID do cliente, se conhecido, para buscar contexto.

    Returns:
        Uma string com a resposta para o cliente ou uma sugestão de encaminhamento.
    """
    # Validação básica
    if not query:
        return "Erro: A consulta do cliente (query) é necessária."

    print(f"Processando consulta de suporte: 	{query}	 (Cliente: {client_id or 	N/A	})...")

    # Lógica simulada de resposta/triagem
    query_lower = query.lower()
    response = ""

    if "fatura" in query_lower or "pagamento" in query_lower or "cobrança" in query_lower:
        response = "Para questões sobre faturamento, por favor, verifique a seção 	Minha Conta	 em nosso portal ou entre em contato com financeiro@fstech.example.com."
        if client_id:
            response += f" Posso verificar o status da sua última fatura, {client_id}? (Simulado)"
            # Simular busca: response += " Sua última fatura foi enviada em DD/MM/AAAA e está com status PAGO." 
    elif "status" in query_lower and ("projeto" in query_lower or "entrega" in query_lower):
        response = "Para obter o status mais recente do seu projeto, por favor, consulte o portal do cliente ou entre em contato com seu Coordenador de Projetos dedicado."
        if client_id:
            response += f" Posso pedir uma atualização ao Coordenador sobre o projeto de {client_id}? (Simulado)"
            # Simular encaminhamento interno
    elif "problema técnico" in query_lower or "erro" in query_lower or "não funciona" in query_lower:
        response = "Lamento ouvir sobre o problema técnico. Por favor, forneça mais detalhes (qual sistema, o que você tentou fazer, mensagens de erro) para que eu possa encaminhar ao Especialista Técnico."
    elif "agendar" in query_lower or "reunião" in query_lower:
        response = "Para agendar uma reunião, por favor, use nossa ferramenta de agendamento online [link simulado] ou me diga sua disponibilidade e o motivo da reunião para que eu possa verificar com a equipe."
    else:
        response = "Obrigado por sua consulta. Entendi que você perguntou sobre: 	" + query[:50] + "...	. Vou verificar a melhor forma de ajudar ou encaminhar para o especialista correto."

    print(f"Resposta gerada (simulada): {response}")
    return response

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    print(handle_client_support_query(query="Qual o status do meu projeto?", client_id="VIP-BIGCORP"))
    print("\n--------------------\n")
    print(handle_client_support_query(query="Recebi uma cobrança inesperada na minha fatura."))
    print("\n--------------------\n")
    print(handle_client_support_query(query="Estou tendo um erro ao acessar o portal."))
    print("\n--------------------\n")
    print(handle_client_support_query(query="Gostaria de agendar uma call para discutir novas ideias."))

