from typing import Callable, Type, List

from pydantic import BaseModel


class RouteDTO(BaseModel):
    path: str
    endpoint: Callable
    response_model: Type[BaseModel] | None
    methods: List[str]
    status_code: int
    summary: str
    description: str
    responses: dict[int, dict]
