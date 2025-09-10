import httpx
from schemas import EndpointSummary

async def get_swagger_docs(swagger_url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(swagger_url+"/openapi.json")
    response.raise_for_status()
    return response.json()


async def parse_swagger_json(
    swagger_json: dict,
):
    result = []

    paths = swagger_json.get("paths", {})
    for path, methods in paths.items():
        for method, details in methods.items():
            summary = details.get("summary", "")
            description = details.get("description", "")
            parameters = details.get("parameters", [])
            responses = details.get("responses", {})

            result.append(
                EndpointSummary(
                    path=path,
                    method=method,
                    summary=summary,
                    description=description,
                    parameters=parameters,
                    responses=responses,
                )
            )

    return result