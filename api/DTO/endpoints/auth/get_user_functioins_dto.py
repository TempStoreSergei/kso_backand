from pydantic import BaseModel


class GetUserFunctionsResponseDTO(BaseModel):
    functions: list[str]
