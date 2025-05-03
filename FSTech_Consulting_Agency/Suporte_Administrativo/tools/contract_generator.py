# Ferramenta: Gerador de Contrato de Prestação de Serviços (Markdown)

import os
import re
from datetime import datetime

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

# Template Markdown para o contrato
CONTRACT_TEMPLATE = """
# CONTRATO DE PRESTAÇÃO DE SERVIÇOS DE CONSULTORIA E DESENVOLVIMENTO

**CONTRATANTE:** {client_company}, inscrita no CNPJ sob o nº [CNPJ DO CLIENTE], com sede em [ENDEREÇO DO CLIENTE], neste ato representada na forma de seus atos constitutivos, doravante denominada simplesmente CONTRATANTE.

**CONTRATADA:** FSTech Consulting Agency (ou [SUA RAZÃO SOCIAL]), inscrita no CNPJ sob o nº [SEU CNPJ], com sede em [SEU ENDEREÇO], neste ato representada na forma de seus atos constitutivos, doravante denominada simplesmente CONTRATADA.

As partes acima identificadas têm, entre si, justo e contratado o presente Contrato de Prestação de Serviços, que se regerá pelas cláusulas seguintes e pelas condições descritas no presente.

## CLÁUSULA PRIMEIRA - DO OBJETO DO CONTRATO

O objeto do presente contrato é a prestação de serviços de consultoria e desenvolvimento pela CONTRATADA à CONTRATANTE, consistindo em:

```
{scope_description}
```

(Baseado na proposta comercial aceita em [DATA DA ACEITAÇÃO DA PROPOSTA])

## CLÁUSULA SEGUNDA - DAS OBRIGAÇÕES DA CONTRATADA

Constituem obrigações da CONTRATADA:

a) Prestar os serviços descritos na Cláusula Primeira com zelo, diligência e observância às melhores práticas de mercado.
b) Cumprir o cronograma estimado de **{estimated_timeline}**, ressalvados motivos de força maior ou atrasos decorrentes de ações ou omissões da CONTRATANTE.
c) Manter sigilo sobre todas as informações confidenciais da CONTRATANTE a que tiver acesso.
d) [Outras obrigações específicas]

## CLÁUSULA TERCEIRA - DAS OBRIGAÇÕES DA CONTRATANTE

Constituem obrigações da CONTRATANTE:

a) Fornecer à CONTRATADA todas as informações, acessos e recursos necessários para a boa execução dos serviços.
b) Efetuar o pagamento dos valores devidos nas datas e formas pactuadas.
c) Designar um representante para acompanhar a execução dos serviços e aprovar as entregas.
d) [Outras obrigações específicas]

## CLÁUSULA QUARTA - DO PREÇO E DAS CONDIÇÕES DE PAGAMENTO

Pelos serviços prestados, a CONTRATANTE pagará à CONTRATADA o valor total de **{price}**.

O pagamento será efetuado da seguinte forma:

```
{payment_terms}
```

## CLÁUSULA QUINTA - DA VIGÊNCIA

O presente contrato vigorará a partir da data de sua assinatura até a conclusão dos serviços e o cumprimento de todas as obrigações pelas partes, estimado em **{estimated_timeline}**.

## CLÁUSULA SEXTA - DA CONFIDENCIALIDADE

[Texto padrão sobre confidencialidade]

## CLÁUSULA SÉTIMA - DA PROPRIEDADE INTELECTUAL

[Texto padrão sobre propriedade intelectual dos entregáveis]

## CLÁUSULA OITAVA - DA RESCISÃO

[Texto padrão sobre condições de rescisão]

## CLÁUSULA NONA - DO FORO

Fica eleito o foro da comarca de [SUA CIDADE]/[SEU ESTADO] para dirimir quaisquer controvérsias oriundas do presente contrato.

E, por estarem assim justas e contratadas, as partes assinam o presente contrato em 2 (duas) vias de igual teor e forma.

[Local], {current_date}.


_________________________________________
**{client_company}**
(CONTRATANTE)


_________________________________________
**FSTech Consulting Agency (ou [SUA RAZÃO SOCIAL])**
(CONTRATADA)
"""

@function_tool
def generate_contract_markdown(
    client_company: str,
    scope_description: str,
    price: str,
    payment_terms: str,
    estimated_timeline: str,
    output_dir: str = "/home/ubuntu/contracts"
) -> str:
    """Gera um documento de contrato de prestação de serviços em formato Markdown.

    Utiliza um template padrão e preenche com as informações fornecidas sobre
    o cliente, escopo, preço, condições de pagamento e cronograma.
    Inclui placeholders para informações legais que devem ser preenchidas manualmente.

    Args:
        client_company: Nome da empresa cliente.
        scope_description: Descrição detalhada do escopo dos serviços (pode vir da proposta).
        price: O preço total acordado (ex: "R$ 10.000,00").
        payment_terms: As condições de pagamento acordadas (ex: "50% na assinatura, 50% na entrega final").
        estimated_timeline: O prazo estimado para conclusão do projeto (ex: "6-8 semanas").
        output_dir: (Opcional) Diretório onde o arquivo .md será salvo (padrão: /home/ubuntu/contracts).

    Returns:
        O caminho absoluto para o arquivo Markdown do contrato gerado ou uma mensagem de erro.
    """
    if not all([client_company, scope_description, price, payment_terms, estimated_timeline]):
        return "Erro: Todos os parâmetros são obrigatórios para gerar o contrato."

    # Criar diretório de saída se não existir
    os.makedirs(output_dir, exist_ok=True)

    # Formatar data atual
    current_date = datetime.now().strftime("%d de %B de %Y") # Formato por extenso

    # Preencher o template
    contract_content = CONTRACT_TEMPLATE.format(
        client_company=client_company,
        scope_description=scope_description,
        price=price,
        payment_terms=payment_terms,
        estimated_timeline=estimated_timeline,
        current_date=current_date
    )

    # Definir nome do arquivo
    safe_company_name = re.sub(r'[^\w\-]+', '_', client_company.lower())
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = f"contrato_{safe_company_name}_{timestamp}.md"
    file_path = os.path.join(output_dir, file_name)

    # Salvar o arquivo (usaremos file_write na próxima etapa, aqui simulamos o retorno do path)
    print(f"Gerando contrato para {client_company} em {file_path}...")

    # Simulação: Em um cenário real com LLM, chamaríamos a ferramenta file_write aqui.
    # Por enquanto, apenas retornamos o caminho onde o arquivo DEVERIA ser salvo.
    # Para testes locais, você pode descomentar a linha abaixo:
    # with open(file_path, 'w', encoding='utf-8') as f:
    #     f.write(contract_content)

    return f"Arquivo do contrato pronto para ser salvo em: {file_path}\nConteúdo:\n---\n{contract_content}\n---"

# Exemplo de uso
if __name__ == "__main__":
    simulated_scope = """
- Desenvolvimento de API REST para gerenciamento de produtos.
- Criação de Frontend Web para interação com a API.
- Implementação de sistema de autenticação de usuários.
- Configuração de Banco de Dados SQL.
    """
    simulated_price = "R$ 15.000,00"
    simulated_payment = "50% na assinatura do contrato.\n50% após a entrega final e aprovação."
    simulated_timeline = "8-10 semanas"

    print("--- Gerando Contrato Exemplo ---")
    result = generate_contract_markdown(
        client_company="Empresa Teste S.A.",
        scope_description=simulated_scope,
        price=simulated_price,
        payment_terms=simulated_payment,
        estimated_timeline=simulated_timeline,
        output_dir="/home/ubuntu/test_contracts" # Usando diretório de teste
    )
    print(result)

    print("\n--- Teste de Erro (Parâmetro Faltando) ---")
    result_error = generate_contract_markdown(
        client_company="Companhia Beta",
        scope_description="Consultoria em SEO.",
        price="R$ 3.000,00",
        payment_terms="Pagamento único adiantado.",
        estimated_timeline=None # Faltando
    )
    print(result_error)

