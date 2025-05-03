import os
from openai import OpenAI

def extract_industry_and_challenge(briefing, model="gpt-4.1"):
    """
    Usa o modelo OpenAI para extrair setor e principal desafio a partir de um briefing.
    Retorna (industry, main_challenge)
    """
    openai_api_key = os.getenv("OPENAI_API_KEY")
    if not openai_api_key:
        raise ValueError("OPENAI_API_KEY não encontrado nas variáveis de ambiente.")
    client = OpenAI(api_key=openai_api_key)

    prompt = f"""
A seguir está um briefing de uma demanda de cliente. Extraia:
1. O setor de atuação (ex: Esportes, Tecnologia, Saúde, etc.)
2. O principal desafio/dor do cliente (frase curta)
Briefing: {briefing}
Responda no formato:
Setor: <setor>
Desafio: <desafio>
"""
    
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "Você é um assistente especialista em negócios e análise de demandas."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2100,
        temperature=0.13
    )
    content = completion.choices[0].message.content
    # Parse simples
    industry = ""
    main_challenge = ""
    for line in content.split("\n"):
        if line.lower().startswith("setor:"):
            industry = line.split(":", 1)[1].strip()
        elif line.lower().startswith("desafio:"):
            main_challenge = line.split(":", 1)[1].strip()
    return industry, main_challenge
