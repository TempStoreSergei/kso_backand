from fastapi import HTTPException, Response, Cookie

from jose import JWTError, jwt

from api.DTO.auth.refresh_dto import RefreshResponseDTO
from api.utils.auth.create_jwt import create_jwt_token, SECRET_KEY, ALGORITHM


async def refresh(
    response: Response,
    refresh_token: str | None = Cookie(default=None),
):
    if not refresh_token:
        raise HTTPException(status_code=401, detail="Refresh token missing")

    try:
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if not username:
            raise HTTPException(status_code=401, detail="Invalid refresh token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    new_access_token = create_jwt_token({"sub": username})
    response.set_cookie(
        key="access_token",
        value=new_access_token,
        httponly=True,
        secure=True,
        samesite="strict",
        max_age=60 * 15
    )

    return RefreshResponseDTO(detail="access token refreshed")
