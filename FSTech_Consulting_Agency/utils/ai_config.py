"""
Configurações centralizadas para modelos de IA usados no sistema FSTech.
Este arquivo define as configurações padrão para todos os modelos de IA usados pelos agentes.
"""

# Modelo padrão a ser usado por todos os agentes
DEFAULT_MODEL = "gpt-4.1"

# Configurações de temperatura para diferentes tipos de tarefas
TEMPERATURES = {
    "creative": 0.8,    # Para tarefas criativas como geração de conteúdo
    "balanced": 0.3,    # Para tarefas de equilíbrio entre criatividade e precisão
    "analytical": 0.13,  # Para tarefas analíticas, diagnóstico e extração
    "factual": 0.15      # Para tarefas que exigem máxima precisão e objetividade
}

# Configurações de token para diferentes contextos
MAX_TOKENS = {
    "short": 1000,      # Para respostas curtas e precisas
    "medium": 2000,     # Para análises e explicações moderadas
    "long": 3000,      # Para documentos e análises detalhadas
    "proposal": 5000   # Para propostas completas
}

def get_model_config(task_type="balanced"):
    """
    Retorna a configuração padrão para um tipo de tarefa específico.
    
    Args:
        task_type: Tipo de tarefa ('creative', 'balanced', 'analytical', 'factual')
        
    Returns:
        Dict com configurações do modelo
    """
    return {
        "model": DEFAULT_MODEL,
        "temperature": TEMPERATURES.get(task_type, 0.17)
    }
