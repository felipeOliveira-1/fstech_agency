# FSTech Consulting Agency

**Plataforma de consultoria tecnológica automatizada para PMEs e profissionais em transição digital.**

## Visão Geral

A FSTech Consulting Agency automatiza o ciclo completo de consultoria tecnológica, desde o contato inicial até a entrega do projeto, combinando agentes especializados de IA com integrações com ferramentas externas.

**Tagline:** Tecnologia simplificada para o seu crescimento.

## Funcionalidades Principais

- **Agentes Especializados:** Consultor, Arquiteto, Especialista Técnico, Analista ROI, Suporte, Marketing
- **Fluxo Automatizado:** Briefing → Reunião → Análise Técnica → Proposta → Negociação → Execução
- **Integrações:** ClickUp (CRM), Cal.com (Agendamento), OpenAI API (Conteúdo e Análise)
- **Interface:** Aplicação Streamlit para operação visual e intuitiva

## Instalação Rápida

```bash
# Clone e configure
git clone https://github.com/seu-usuario/FSTech_Consulting_Agency_openai_integrated.git
cd FSTech_Consulting_Agency_openai_integrated

# Ambiente e dependências
python -m venv venv
source venv/bin/activate  # Linux/Mac ou venv\Scripts\activate (Windows)
pip install -r requirements.txt

# Configure suas APIs (.env)
cp .env.example .env
# Edite o arquivo .env com suas chaves API

# Execute
streamlit run app.py
```

## Como Usar

1. Acesse http://localhost:8501
2. Preencha os dados do cliente e briefing
3. Siga o fluxo guiado para análise e proposta
4. Acompanhe o status no ClickUp automaticamente

## Estrutura do Projeto

```
FSTech_Consulting_Agency/
├── Agentes (CEO/, Consultor_de_Diagnostico/, etc.)
├── utils/ (Ferramentas compartilhadas)
├── tests/ (Testes automatizados)
├── app.py (Interface Streamlit)
├── orquestrador_fstech.py (Coordenação)
└── requirements.txt
```

## Próximas Funcionalidades (2025.2)

- Dashboard analítico com KPIs de vendas e projetos
- Integração com WhatsApp Business API
- Agente de Qualidade e Compliance
- Expansão do fluxo de pós-venda automatizado
- Sistema multi-organização com white-labeling

## Contribuindo

Interessado em contribuir? Áreas prioritárias:
- Novos agentes especializados
- Integrações adicionais (WhatsApp, ERPs, etc.)
- Melhorias de interface e visualização
- Testes e documentação

Siga PEP8, adicione testes e abra um Pull Request.

## Contato

Dúvidas ou sugestões? Abra uma issue ou envie email para contato@fstechagency.com
