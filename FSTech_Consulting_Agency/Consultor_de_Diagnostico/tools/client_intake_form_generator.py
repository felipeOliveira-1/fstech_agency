# Ferramenta: Gerador de Formulário de Intake de Cliente

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def generate_client_intake_form(industry: str, main_challenge: str) -> str:
    """Gera um formulário de intake personalizado para novos clientes.

    Use esta ferramenta no início do engajamento com um novo cliente para coletar
    informações essenciais sobre seu negócio, desafios e objetivos.

    Args:
        industry: O setor de atuação do cliente (ex: 	Varejo	, 	Saúde	, 	Finanças	).
        main_challenge: O principal desafio ou dor que o cliente busca resolver (ex: 	Baixa eficiência operacional	, 	Dificuldade em escalar	).

    Returns:
        Uma string contendo o formulário de intake formatado em Markdown ou uma mensagem de erro.
    """
    # Validação básica
    if not industry or not main_challenge:
        return "Erro: Setor (industry) e principal desafio (main_challenge) são necessários."

    print(f"Gerando formulário de intake para setor 	{industry}	 com desafio 	{main_challenge}	...")

    # Lógica simulada para gerar o formulário
    form_content = f"""# Formulário de Intake - FSTech Consulting Agency

**Cliente:** [Nome da Empresa do Cliente]
**Contato Principal:** [Nome e Cargo]
**Email:** [Email de Contato]
**Telefone:** [Telefone de Contato]

**Setor de Atuação:** {industry}

## Sobre o Negócio

1.  Descreva brevemente sua empresa e seus principais produtos/serviços.
2.  Qual o tamanho da sua empresa (número de funcionários, faturamento anual aproximado)?
3.  Quem são seus principais concorrentes?

## Desafios e Objetivos

4.  **Principal Desafio:** {main_challenge}
    *   Como este desafio impacta seu negócio atualmente?
    *   Quais tentativas já foram feitas para resolvê-lo?
5.  Quais são seus principais objetivos de negócio para os próximos 12 meses?
6.  Quais métricas você usa para medir o sucesso em relação a esses objetivos?

## Tecnologia e Processos Atuais (Foco em {industry})

7.  Quais são as principais ferramentas/softwares que vocês utilizam hoje?
8.  Como você descreveria seus processos internos relacionados a [Área relevante para o desafio]?
9.  Existem gargalos conhecidos ou áreas de ineficiência?

## Expectativas com a FSTech

10. O que você espera alcançar trabalhando conosco?
11. Qual o orçamento estimado para este projeto/consultoria?
12. Qual o cronograma ideal para implementação?

*Obrigado por preencher! Entraremos em contato em breve.*
"""

    # Em um cenário real, poderia salvar em arquivo ou enviar por email.
    return form_content

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    form = generate_client_intake_form(industry="Tecnologia SaaS", main_challenge="Aquisição de novos clientes B2B")
    print(form)

