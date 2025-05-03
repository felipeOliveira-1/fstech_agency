# Ferramenta: Gerador de Blueprint de API

# Simulação de um decorador para definir a ferramenta
def function_tool(func):
    """Decorador simulado para registrar metadados da ferramenta."""
    func._is_tool = True
    return func

@function_tool
def generate_api_blueprint(api_name: str, resources: list[dict], data_models: dict) -> str:
    """Gera uma especificação de API (blueprint) no formato OpenAPI (Swagger).

    Use esta ferramenta para criar a documentação e definição formal de uma API
    com base nos recursos, endpoints e modelos de dados definidos.

    Args:
        api_name: O nome da API (ex: 	API de Clientes FSTech	).
        resources: Uma lista de dicionários descrevendo os recursos e endpoints (ex: [{	path	: 	/clientes	, 	methods	: [	GET	, 	POST	]}]).
        data_models: Um dicionário definindo os modelos de dados (schemas) usados pela API (ex: {	Cliente	: {	properties	: {	name	: {	"type"	: 	"string"	}}}}).

    Returns:
        Uma string contendo a especificação OpenAPI em formato YAML (simulado) ou uma mensagem de erro.
    """
    # Validação básica
    if not api_name or not resources or not data_models:
        return "Erro: Nome da API (api_name), lista de recursos (resources) e modelos de dados (data_models) são necessários."

    print(f"Gerando blueprint OpenAPI para a API: {api_name}...")

    # Lógica simulada para gerar OpenAPI YAML
    openapi_spec = f"""openapi: 3.0.0
info:
  title: {api_name}
  version: 1.0.0
  description: API para gerenciar {api_name.split(	 	)[-2] if len(api_name.split()) > 2 else 	Recursos	} na FSTech.

paths:"""

    for resource in resources:
        path = resource.get("path", "/unknown")
        methods = resource.get("methods", ["GET"])
        openapi_spec += f"\n  {path}:"
        for method in methods:
            method_lower = method.lower()
            summary = f"{method.capitalize()} {path.split('/')[-1] if path != '/' else 'root'}"
            operation_id = f"{method_lower}{path.replace('/', '_')}"
            openapi_spec += f"\n    {method_lower}:"
            openapi_spec += f"\n      summary: {summary}"
            openapi_spec += f"\n      operationId: {operation_id}"
            # Adicionar parâmetros e respostas simuladas básicas
            if method_lower == "get":
                openapi_spec += "\n      responses:\n        	200	:\n          description: Sucesso"
            elif method_lower == "post":
                 openapi_spec += "\n      requestBody:\n        content:\n          application/json:\n            schema:\n              $ref: 	#/components/schemas/{list(data_models.keys())[0] if data_models else 	DefaultModel	}	"
                 openapi_spec += "\n      responses:\n        	201	:\n          description: Criado"

    openapi_spec += "\n\ncomponents:\n  schemas:"
    for model_name, model_details in data_models.items():
        openapi_spec += f"\n    {model_name}:"
        # Simplificação extrema da conversão do modelo
        openapi_spec += f"\n      type: object"
        if "properties" in model_details:
            openapi_spec += "\n      properties:"
            for prop_name, prop_details in model_details["properties"].items():
                prop_type = prop_details.get("type", "string")
                openapi_spec += f"\n        {prop_name}:\n          type: {prop_type}"

    print("Blueprint OpenAPI (YAML simulado) gerado.")
    # Em um cenário real, salvaria em arquivo .yaml
    return openapi_spec

# Exemplo de uso (apenas para teste)
if __name__ == "__main__":
    res = [
        {"path": "/users", "methods": ["GET", "POST"]},
        {"path": "/users/{id}", "methods": ["GET", "PUT", "DELETE"]}
    ]
    models = {
        "User": {
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "email": {"type": "string", "format": "email"}
            }
        }
    }
    blueprint = generate_api_blueprint(api_name="API de Usuários Interna", resources=res, data_models=models)
    print(blueprint)

