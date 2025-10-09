from pydantic import BaseModel, Field


class DeleteFileResponseDTO(BaseModel):
    detail: str
