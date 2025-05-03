# Ferramenta: Construtor de Propostas Comerciais (Markdown)

import os
from datetime import datetime

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Template Markdown para a proposta
PROPOSAL_TEMPLATE = """
# Proposta Comercial - {client_company}

**Data:** {date}
**Para:** {client_name} ({client_company})
**De:** FSTech Consulting Agency

## 1. Entendimento do Desafio

Com base em nossa conversa e análise inicial, compreendemos que o principal desafio enfrentado por {client_company} é:

```
{problem_description}
```

## 2. Solução Proposta

Para endereçar este desafio, propomos a seguinte solução técnica:

**Componentes Principais:**
{architecture_sketch}

**Descrição da Solução:**

*(Detalhar aqui como os componentes se conectam e resolvem o problema do cliente)*

## 3. Escopo e Entregáveis

O escopo deste projeto inclui:

*   Desenvolvimento e implementação dos componentes descritos acima.
*   Testes e validação da solução.
*   Treinamento inicial (se aplicável).
*   Documentação técnica.

**Entregáveis:**

*   Sistema/Solução funcional conforme descrito.
*   Código fonte (se aplicável).
*   Documentação.

## 4. Cronograma Estimado

Estimamos que o projeto levará aproximadamente **{estimated_timeline}** para ser concluído, a partir da data de início acordada.

(Um cronograma mais detalhado pode ser fornecido após o início do projeto)

## 5. Investimento

O investimento total para a implementação desta solução é de **{price}**.

**Condições de Pagamento:**

*(Detalhar condições: ex: 50% na assinatura, 50% na entrega)*

## 6. Próximos Passos

Caso esta proposta seja aprovada, os próximos passos serão:

1.  Assinatura do contrato de prestação de serviços.
2.  Reunião de kickoff do projeto.
3.  Início do desenvolvimento.

Aguardamos seu retorno e ficamos à disposição para quaisquer esclarecimentos.

Atenciosamente,

Equipe FSTech Consulting Agency
"""

import re

@function_tool
def build_proposal_markdown(
    client_name: str,
    client_company: str,
    problem_description: str,
    architecture_sketch: str,
    price: str,
    estimated_timeline: str,
    output_dir: str = "/home/ubuntu/proposals"
) -> str:
    """Gera um documento de proposta comercial em formato Markdown.

    Utiliza um template padrão e preenche com as informações fornecidas sobre
    o cliente, problema, solução, arquitetura, preço e cronograma.

    Args:
        client_name: Nome do contato principal no cliente.
        client_company: Nome da empresa cliente.
        problem_description: Descrição do problema ou necessidade do cliente.
        architecture_sketch: Esboço da arquitetura sugerida (idealmente vindo do system_architecture_designer).
        price: O preço final calculado para a proposta (idealmente vindo do pricing_calculator).
        estimated_timeline: O prazo estimado para conclusão do projeto (ex: "4-6 semanas", "3 meses").
        output_dir: (Opcional) Diretório onde o arquivo .md será salvo (padrão: /home/ubuntu/proposals).

    Returns:
        O caminho absoluto para o arquivo Markdown da proposta gerada ou uma mensagem de erro.
    """
    if not all([client_name, client_company, problem_description, architecture_sketch, price, estimated_timeline]):
        return "Erro: Todos os parâmetros são obrigatórios para gerar a proposta."

    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Formatar data atual
    current_date = datetime.now().strftime("%d/%m/%Y")

    # Preencher o template
    proposal_content = PROPOSAL_TEMPLATE.format(
        client_name=client_name,
        client_company=client_company,
        date=current_date,
        problem_description=problem_description,
        architecture_sketch=architecture_sketch,
        price=price,
        estimated_timeline=estimated_timeline
    )

    # Definir nome do arquivo
    safe_company_name = re.sub(r'[^\w\-]+', '_', client_company.lower())
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"proposta_{safe_company_name}_{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)

    # Salvar o arquivo
    print(f"Gerando proposta para {client_company} em {file_path}...")

    # Escreve o arquivo de proposta
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(proposal_content)
        print(f"\u2705 Proposta salva com sucesso em: {file_path}")
    except Exception as e:
        print(f"\u274c Erro ao salvar a proposta: {str(e)}")
        return f"Erro ao salvar a proposta: {str(e)}"

    return f"Proposta para {client_company} salva com sucesso em: {file_path}"

# Exemplo de uso
if __name__ == "__main__":
    # Simular saídas das ferramentas anteriores
    simulated_arch = """
- API REST/GraphQL (Score: 2)
- Banco de Dados (SQL) (Score: 2)
- Frontend Web (Score: 2)
- Sistema de Autenticação (Score: 1)
    """
    simulated_price = "R$ 9.375,00"

    print("--- Gerando Proposta Exemplo ---")
    result = build_proposal_markdown(
        client_name="João Silva",
        client_company="Empresa Exemplo Ltda",
        problem_description="Dificuldade em gerenciar leads e acompanhar o funil de vendas de forma eficiente.",
        architecture_sketch=simulated_arch,
        price=simulated_price,
        estimated_timeline="6-8 semanas",
        output_dir="/home/ubuntu/test_proposals" # Usando diretório de teste
    )
    print(result)

    print("\n--- Teste de Erro (Parâmetro Faltando) ---")
    result_error = build_proposal_markdown(
        client_name="Maria Souza",
        client_company="Outra Empresa SA",
        problem_description="Necessidade de automatizar relatórios financeiros.",
        architecture_sketch="- Fluxo de Automação (Score: 1)\n- Geração de Relatórios (Score: 1)",
        price="R$ 5.000,00",
        estimated_timeline=None # Faltando
    )
    print(result_error)

