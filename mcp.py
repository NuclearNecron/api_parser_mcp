from mcp.server.fastmcp import FastMCP
from schemas import EndpointSummary, SwaggerDoc
from parser import get_swagger_docs, parse_swagger_json

mcp = FastMCP("ApiSwaggerParser")


@mcp.tool()
async def generate_endpoint_summaries(endpoint:str) -> SwaggerDoc:
    """Получаем все информацию о каждом эндпоинте в SWAGGER"""
    swagger_json = await get_swagger_docs(endpoint)

    result = await parse_swagger_json(swagger_json)

    return SwaggerDoc(endpoints=result)


@mcp.tool()
async def manual_swager_upload(json_data:dict) -> SwaggerDoc:
    """Получаем все информацию о каждом эндпоинте в документе Json"""

    result = await parse_swagger_json(json_data)

    return SwaggerDoc(endpoints=result)


@mcp.tool()
async def get_endpoint_summary(path: str, method: str, endpoint:str) -> EndpointSummary:
    """Получает summary для конкретного эндпоинта"""
    endpoints_data = await generate_endpoint_summaries(endpoint)

    for endpoint in endpoints_data.endpoints:
        if endpoint.path == path and endpoint.method == method:
            return endpoint

    return "Эндпоинта не существует"


if __name__ == "__main__":
    mcp.run()
