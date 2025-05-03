# Ferramenta: Gerador de Post para Mídia Social

import random

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def generate_social_media_post(topic: str, channel: str, target_audience: str = "Geral", tone: str = "Informativo") -> str:
    """Gera um rascunho de post para mídias sociais sobre um tópico específico.

    Use esta ferramenta para criar rapidamente rascunhos de posts para canais como
    LinkedIn, Twitter, Instagram, etc., adaptados ao público e tom desejados.

    Args:
        topic: O tópico principal do post.
        channel: O canal de mídia social alvo (ex: 	LinkedIn	, 	Twitter	, 	Instagram	).
        target_audience: (Opcional) O público-alvo do post (ex: 	PMEs	, 	Desenvolvedores	, 	Executivos C-Level	). Default: 	Geral	.
        tone: (Opcional) O tom desejado para o post (ex: 	Informativo	, 	Engajador	, 	Promocional	, 	Humorístico	). Default: 	Informativo	.

    Returns:
        Uma string contendo o rascunho do post ou uma mensagem de erro.
    """
    # Validação básica
    if not topic or not channel:
        return "Erro: Tópico (topic) e canal (channel) são obrigatórios."

    print(f"Gerando rascunho de post para {channel} sobre 	{topic}	...")
    print(f"Público: {target_audience}, Tom: {tone}")

    # Lógica simulada de geração de post (poderia usar LLM)
    hashtags = [f"#{word.capitalize()}" for word in topic.split()[:3]] # Hashtags simples
    hashtags.append("#FSTech")
    if "ia" in topic.lower(): hashtags.append("#InteligenciaArtificial")
    if "automação" in topic.lower(): hashtags.append("#Automacao")

    post_body = f"[Rascunho Simulado - Tom: {tone}] Descubra como {topic} pode impactar {target_audience}! Na FSTech, ajudamos você a [verbo relacionado ao tópico, ex: implementar, otimizar, entender]. Saiba mais em nosso site!"

    # Ajuste simulado para canal
    if channel.lower() == "twitter":
        post_body = post_body[:260] + "..." # Limitar tamanho simulado
        post_body += " #ShortTweet" 
    elif channel.lower() == "linkedin":
        post_body += "\n\n#Tech #Consulting #Inovacao" # Hashtags mais profissionais
    elif channel.lower() == "instagram":
        post_body = f"Imagem: [Sugestão de imagem relacionada a {topic}]\n\nLegenda: {post_body} #InstaTech #BusinessGrowth"

    draft_post = f"""**Canal:** {channel}
**Público:** {target_audience}
**Tom:** {tone}

**Rascunho do Post:**
{post_body}

**Hashtags Sugeridas:** {' '.join(hashtags)}

*Nota: Este é um rascunho simulado. Revise e adapte antes de publicar.*
"""

    print("Rascunho de post gerado.")
    return draft_post

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    print("--- Post LinkedIn ---")
    print(generate_social_media_post(topic="Otimização de Processos com IA", channel="LinkedIn", target_audience="Gerentes de Operações", tone="Profissional"))

    print("\n--- Post Twitter ---")
    print(generate_social_media_post(topic="Novas funcionalidades de automação na FSTech", channel="Twitter", tone="Engajador"))

    print("\n--- Post Instagram ---")
    print(generate_social_media_post(topic="Case de Sucesso Cliente X", channel="Instagram", target_audience="Empreendedores", tone="Inspirador"))

