# Manual de Uso - Estrutura FSTech Consulting Agency

## 1. Introdução

Este manual fornece um guia detalhado sobre como entender e utilizar a estrutura de projeto da FSTech Consulting Agency. Ele complementa o `README.md` com informações mais aprofundadas sobre cada componente.

O objetivo desta estrutura é servir como uma base organizada para o desenvolvimento de um sistema multiagente que simula as operações da FSTech Consulting Agency.

## 2. Entendendo a Estrutura de Diretórios

A estrutura principal está organizada por agentes, facilitando a modularidade e a manutenção:

```
FSTech_Consulting_Agency/
├── [Nome_do_Agente]/        # Diretório para cada agente (CEO, Consultor, etc.)
│   ├── __init__.py         # Identifica como pacote Python
│   ├── [nome_agente].py    # Lógica principal do agente (placeholder)
│   ├── instructions.md     # Descrição detalhada do papel do agente
│   └── tools/              # Ferramentas específicas do agente
│       ├── __init__.py     # (Opcional, mas boa prática)
│       └── tool_name.py    # Script Python para cada ferramenta (placeholder)
├── agency.py             # Ponto de entrada ou orquestrador da agência (placeholder)
├── agency_manifesto.md   # Visão, missão e valores da agência
├── communication_flows.md # Mapeamento da comunicação interna/externa
├── requirements.txt      # Dependências Python (a definir)
├── .env                  # Variáveis de ambiente (ex: chaves de API)
├── .gitignore            # Arquivos ignorados pelo Git
├── README.md             # Visão geral do projeto
└── MANUAL.md             # Este manual
```

## 3. Detalhes dos Componentes

### 3.1. Diretórios dos Agentes (`[Nome_do_Agente]/`)

Cada agente possui seu próprio diretório encapsulando sua lógica e ferramentas.

*   **`instructions.md`**: Este é um arquivo crucial para entender o que cada agente faz. Ele detalha:
    *   O papel do agente na agência.
    *   Suas responsabilidades principais.
    *   As ferramentas que ele utiliza.
    *   Com quem ele se comunica (fluxo de entrada e saída de informações).
    *   Diretrizes gerais de operação.
    *   **Como usar:** Leia este arquivo primeiro ao tentar entender um agente específico.

*   **`[nome_agente].py`**: Este arquivo Python está destinado a conter a lógica principal do agente. Atualmente, são placeholders vazios. No desenvolvimento futuro, ele poderia:
    *   Importar e utilizar as ferramentas do diretório `tools/`.
    *   Gerenciar o estado do agente.
    *   Interagir com outros agentes (baseado nos `communication_flows.md`).
    *   Processar entradas e gerar saídas.

*   **`tools/`**: Contém os scripts Python que representam as ferramentas disponíveis para o agente.
    *   **`tool_name.py`**: Cada arquivo implementa uma ferramenta específica mencionada no `instructions.md` do agente.
    *   **Placeholders Atuais:** Os scripts atuais contêm funções Python com a assinatura esperada (argumentos e tipo de retorno) e lógica simulada (`print` statements, retornos de strings formatadas, simulação de tempo com `time.sleep`). Eles **não** realizam as operações reais.
    *   **Bloco `if __name__ == "__main__":`**: Muitos scripts de ferramentas incluem este bloco. Ele permite executar o script diretamente do terminal (`python nome_da_ferramenta.py`) para ver um exemplo de uso e a saída simulada da função principal da ferramenta. Isso é útil para testes básicos e entendimento inicial.
    *   **Como usar:** Analise o código da função para entender os inputs e outputs esperados. Execute o script diretamente (se tiver o bloco `if __name__ == "__main__":`) para ver um exemplo.

### 3.2. Arquivos na Raiz

*   **`agency.py`**: Placeholder para o script principal que poderia orquestrar a interação entre os agentes ou iniciar a aplicação.
*   **`agency_manifesto.md`**: Contém a declaração de propósito, visão, missão e valores da FSTech. Fundamental para alinhar o desenvolvimento com os objetivos da agência.
*   **`communication_flows.md`**: Documenta como a informação flui entre os agentes e entre a agência e os clientes. Essencial para implementar a lógica de interação.
*   **`requirements.txt`**: Arquivo padrão Python para listar as dependências do projeto (ex: `requests`, `flask`, bibliotecas de IA/ML, etc.). Atualmente vazio, precisa ser preenchido conforme as ferramentas reais forem implementadas.
*   **`.env`**: Arquivo para armazenar variáveis de ambiente sensíveis, como chaves de API, senhas de banco de dados, etc. **Não deve ser commitado no Git** (está no `.gitignore`).
*   **`.gitignore`**: Especifica arquivos e diretórios que o Git deve ignorar (ex: `venv`, `__pycache__`, `.env`).
*   **`README.md`**: Fornece uma visão geral rápida do projeto.
*   **`MANUAL.md`**: Este arquivo.

## 4. Como Desenvolver a Partir Desta Estrutura

1.  **Configurar Ambiente:**
    *   Crie um ambiente virtual: `python -m venv venv`
    *   Ative o ambiente: `source venv/bin/activate` (Linux/macOS) ou `venv\Scripts\activate` (Windows).
    *   Instale as dependências (quando definidas): `pip install -r requirements.txt`.

2.  **Implementar Ferramentas:**
    *   Substitua a lógica simulada nos arquivos `tools/*.py` pela implementação real.
    *   Isso pode envolver chamadas a APIs externas, manipulação de dados, uso de bibliotecas específicas, etc.
    *   Adicione as bibliotecas necessárias ao `requirements.txt`.

3.  **Implementar Lógica dos Agentes:**
    *   Desenvolva a lógica nos arquivos `[nome_agente].py` para que eles possam chamar suas ferramentas e interagir com base nos fluxos de comunicação.

4.  **Desenvolver Orquestração (`agency.py`):**
    *   Implemente a lógica em `agency.py` para gerenciar o ciclo de vida dos agentes e o fluxo geral de trabalho da agência.

5.  **Integrações:**
    *   Configure as integrações mencionadas (ClickUp, canais de comunicação) usando as APIs correspondentes. Armazene chaves e segredos no arquivo `.env`.

6.  **Testes:**
    *   Crie testes unitários para as ferramentas e a lógica dos agentes.
    *   Crie testes de integração para verificar os fluxos de trabalho completos.

## 5. Executando Placeholders

Como mencionado, você pode executar os scripts de ferramentas que possuem um bloco `if __name__ == "__main__":` diretamente para ver a saída simulada.

**Exemplo:**

```bash
# Navegue até o diretório da ferramenta
cd /path/to/FSTech_Consulting_Agency/CEO/tools

# Execute o script
python business_strategy_builder.py
```

Isso executará o código dentro do bloco `if __name__ == "__main__":` no final do arquivo, mostrando um exemplo de como a função `build_strategy` (neste caso) seria chamada e qual seria sua saída simulada.

---
