from fastapi import Response

from api.DTO.auth.login_dto import LoginResponseDTO


async def logout(
    response: Response,
):
    response.delete_cookie(key="access_token", path="/")
    response.delete_cookie(key="refresh_token", path="/")

    return LoginResponseDTO(detail="logged in")
