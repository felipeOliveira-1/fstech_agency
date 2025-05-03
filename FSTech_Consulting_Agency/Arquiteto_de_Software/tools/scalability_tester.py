# Ferramenta: Testador de Escalabilidade

import random
import time

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def test_scalability(target_endpoint: str, concurrent_users: int, duration_minutes: int) -> str:
    """Realiza um teste de carga simulado para avaliar a escalabilidade de um endpoint.

    Use esta ferramenta para simular o acesso de múltiplos usuários concorrentes a um
    endpoint específico da aplicação e medir seu desempenho sob carga.

    Args:
        target_endpoint: A URL completa do endpoint a ser testado.
        concurrent_users: O número de usuários virtuais simultâneos a simular.
        duration_minutes: A duração do teste em minutos.

    Returns:
        Uma string formatada em Markdown com o resumo dos resultados do teste de carga ou uma mensagem de erro.
    """
    # Validação básica
    if not target_endpoint or not concurrent_users or not duration_minutes:
        return "Erro: Endpoint (target_endpoint), número de usuários (concurrent_users) e duração (duration_minutes) são necessários."
    if not target_endpoint.startswith("http"): # Validação simples de URL
        return "Erro: target_endpoint deve ser uma URL válida (iniciando com http ou https)."
    if not isinstance(concurrent_users, int) or concurrent_users <= 0:
        return "Erro: concurrent_users deve ser um inteiro positivo."
    if not isinstance(duration_minutes, int) or duration_minutes <= 0:
        return "Erro: duration_minutes deve ser um inteiro positivo."

    print(f"Iniciando teste de escalabilidade no endpoint: {target_endpoint}")
    print(f"Configuração: {concurrent_users} usuários concorrentes por {duration_minutes} minutos...")

    # Lógica simulada de teste de carga
    # Em um cenário real, usaria ferramentas como k6, Locust, JMeter via linha de comando
    start_time = time.time()
    total_requests = 0
    successful_requests = 0
    failed_requests = 0
    response_times = []

    # Simular execução do teste
    print("Teste em andamento (simulado)...")
    time.sleep(min(duration_minutes * 2, 5)) # Simular duração (limitado a 5s para não bloquear)

    # Gerar resultados simulados
    total_requests = concurrent_users * duration_minutes * random.randint(30, 60) # Req/min simulado
    failed_requests = int(total_requests * random.uniform(0.0, 0.05)) # Taxa de erro simulada < 5%
    successful_requests = total_requests - failed_requests
    avg_response_time = random.uniform(50, 500) # ms
    p95_response_time = avg_response_time * random.uniform(1.5, 2.5)
    throughput = successful_requests / (duration_minutes * 60) # Req/seg

    end_time = time.time()
    actual_duration_seconds = end_time - start_time

    results_summary = f"""# Resumo do Teste de Escalabilidade (Simulado)

**Endpoint Testado:** {target_endpoint}
**Configuração:** {concurrent_users} usuários concorrentes
**Duração Real (Simulada):** {actual_duration_seconds:.2f} segundos (Configurado para {duration_minutes} min)

## Métricas Principais:
- **Total de Requisições:** {total_requests}
- **Requisições Bem-sucedidas:** {successful_requests}
- **Requisições Falhas:** {failed_requests} ({ (failed_requests / total_requests * 100) if total_requests > 0 else 0 :.2f}%)
- **Taxa de Transferência (Throughput):** {throughput:.2f} reqs/seg
- **Tempo Médio de Resposta:** {avg_response_time:.2f} ms
- **Percentil 95 (P95) Tempo de Resposta:** {p95_response_time:.2f} ms

## Conclusão (Simulada):
- [Avaliação simulada: Ex: O sistema demonstrou boa performance sob a carga testada, ou, O sistema apresentou degradação X...]

*Nota: Este é um resultado de teste simulado.*
"""

    print("Teste de escalabilidade concluído (simulado).")
    return results_summary

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    endpoint = "https://api.fstech.example.com/v1/process"
    results = test_scalability(target_endpoint=endpoint, concurrent_users=100, duration_minutes=5)
    print(results)

