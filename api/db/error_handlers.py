import re
from functools import wraps

from fastapi import HTTPException
from sqlalchemy.exc import IntegrityError, SQLAlchemyError


def handle_db_error(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except ConnectionError:
            raise HTTPException(status_code=500, detail='Ошибка соединения с базой данных')
        except IntegrityError as e:
            error_text = str(e.orig)
            if "UniqueViolationError" in error_text:
                field = extract_unique_violation_field(error_text)
                raise HTTPException(
                    status_code=409,
                    detail=f'Значение поля "{field}" должно быть уникальным'
                )

            elif "ForeignKeyViolationError" in error_text:
                field = extract_foreign_key_field(error_text)
                raise HTTPException(
                    status_code=400,
                    detail=f'Поле "{field}" ссылается на несуществующую запись'
                )
            raise HTTPException(
                status_code=400,
                detail=f'Ошибка ограничения целостности данных: {e}'
            )
        except SQLAlchemyError as e:
            raise HTTPException(
                status_code=500,
                detail=(500, f'Неизвестная ошибка БД: {str(e)}'),
            )
    return wrapper


def extract_foreign_key_field(error_text: str):
    """
    Извлекает имя поля из строки ошибки вида: "author_id)=(0) is not present"
    """
    match = re.search(r'(\w+)\)=\([^)]+\) is not present', error_text)
    if match:
        return match.group(1)
    return 'неизвестное поле'


def extract_unique_violation_field(error_text: str):
    """
    Извлекает имя поля из строки ошибки вида:
    'Key (name)=(value) already exists.'
    """
    match = re.search(r'Key \((\w+)\)=\([^)]+\) already exists', error_text)
    if match:
        return match.group(1)
    return 'неизвестное поле'
