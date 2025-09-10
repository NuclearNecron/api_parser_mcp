from pydantic import BaseModel


class EndpointSummary(BaseModel):
    path: str
    method: str
    summary: str
    description: str
    parameters: list
    responses: dict


class SwaggerDoc(BaseModel):
    endpoints: list[EndpointSummary]