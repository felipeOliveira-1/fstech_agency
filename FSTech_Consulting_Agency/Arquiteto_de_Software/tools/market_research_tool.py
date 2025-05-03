# Ferramenta: Pesquisa de Mercado para Precificação e Estimativa de Prazos

import os
import re
from dotenv import load_dotenv
from openai import OpenAI

# Carregar variáveis de ambiente
load_dotenv()

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def research_market_prices(project_description: str, complexity_level: str) -> dict:
    """
    Realiza uma pesquisa de mercado para determinar preços e prazos adequados 
    para um projeto com base em sua descrição e nível de complexidade.
    
    Args:
        project_description: Descrição detalhada do projeto tecnológico.
        complexity_level: Nível de complexidade (baixa, media, alta).
        
    Returns:
        Um dicionário contendo informações sobre preço estimado, prazo estimado e fatores 
        relevantes do mercado.
    """
    try:
        # Verificar API key
        openai_api_key = os.getenv("OPENAI_API_KEY")
        if not openai_api_key:
            return {
                "status": "error",
                "message": "OPENAI_API_KEY não encontrada nas variáveis de ambiente.",
                "price_range": "R$ 8.000,00 - R$ 15.000,00",  # Valor fallback
                "timeline": "4-8 semanas",                   # Timeline fallback
                "market_factors": ["Valor baseado em estimativa padrão sem pesquisa de mercado"]
            }
        
        client = OpenAI(api_key=openai_api_key)
        
        # Criar prompt que simula uma pesquisa de mercado detalhada
        prompt = f"""
        Você é um especialista em pesquisa de mercado para projetos de tecnologia no Brasil.
        Faça uma análise detalhada para definir o preço e prazo de um projeto com as seguintes características:
        
        Descrição do Projeto: {project_description}
        Nível de Complexidade: {complexity_level}
        
        Com base em sua experiência e conhecimento do mercado brasileiro atual:
        
        1. Qual seria a faixa de preço adequada para este projeto em Reais (BRL)?
        2. Qual seria um prazo realista para entrega (em semanas)?
        3. Quais fatores do mercado atual influenciam esta precificação?
        
        Forneça sua análise no formato JSON exato:
        {{
          "price_range": "R$ X - R$ Y",
          "timeline": "A-B semanas",
          "market_factors": ["fator 1", "fator 2", "fator 3"]
        }}
        """
        
        # Realizar a "pesquisa" (consulta ao modelo)
        completion = client.chat.completions.create(
            model="gpt-4.1",
            messages=[
                {"role": "system", "content": "Você é um especialista em pesquisa de mercado para projetos de tecnologia no Brasil, com amplo conhecimento sobre preços e prazos atuais."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.4
        )
        
        # Extrair o conteúdo JSON da resposta
        json_str = completion.choices[0].message.content
        
        # Usar regex para extrair apenas o JSON (caso haja texto antes ou depois)
        json_match = re.search(r'({.*})', json_str, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        
        # Avaliar o JSON como um dicionário Python
        result = eval(json_str.replace('null', 'None').replace('true', 'True').replace('false', 'False'))
        
        # Adicionar status de sucesso
        result["status"] = "success"
        
        print(f"Pesquisa de mercado concluída: {result}")
        return result
    
    except Exception as e:
        print(f"Erro ao realizar pesquisa de mercado: {e}")
        return {
            "status": "error",
            "message": f"Erro ao realizar pesquisa: {str(e)}",
            "price_range": "R$ 8.000,00 - R$ 15.000,00",  # Valor fallback
            "timeline": "4-8 semanas",                   # Timeline fallback
            "market_factors": ["Valor baseado em estimativa padrão devido a erro na pesquisa"]
        }

# Exemplo de uso
if __name__ == "__main__":
    test_description = "Sistema web para gestão de inventário com dashboard de análise e integração com sistemas de pagamento. Inclui APIs REST e autenticação de usuários."
    
    print("--- Realizando Pesquisa de Mercado (Complexidade Média) ---")
    result_medium = research_market_prices(test_description, "media")
    print(f"Resultado: {result_medium}")
    
    print("\n--- Realizando Pesquisa de Mercado (Complexidade Alta) ---")
    result_high = research_market_prices(test_description + " Também inclui um sistema de machine learning para previsão de estoque e recomendações automatizadas.", "alta")
    print(f"Resultado: {result_high}")
