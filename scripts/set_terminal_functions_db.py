from sqlalchemy import select

from api.configs.database import async_session_maker
from api.models.auth_models import TerminalFunctions
from api.configs.loggers import logger


async def set_terminal_functions_db():
    """Функция заполняет таблицу функций терминала в БД."""

    functions = [
        {
            'function_name': 'Изменить свой пароль',
            'endpoint_name': '/api/v1/auth/change_user_password',
        },
        {
            'function_name': 'Инициализировать наличную систему оплаты',
            'endpoint_name': '/api/v1/cash_system/init_system',
        },
        {
            'function_name': 'Получить статус наличной системы оплаты',
            'endpoint_name': '/api/v1/cash_system/status_system',
        },
        {
            'function_name': 'Тест приема купюр',
            'endpoint_name': '/api/v1/cash_system/status_system/bill_acceptor/test',
        },
        {
            'function_name': 'Тест выдачи купюр',
            'endpoint_name': '/api/v1/cash_system/status_system/bill_dispenser/test',
        },
    ]

    async with async_session_maker() as session:
        for func in functions:
            db_func = await session.scalar(
                select(TerminalFunctions).where(
                    (TerminalFunctions.function_name == func["function_name"])
                    | (TerminalFunctions.endpoint_name == func["endpoint_name"])
                )
            )
            if db_func:
                continue
            func_data = TerminalFunctions(**func)
            session.add(func_data)
            logger.info(f'Добавлена функция {func_data.function_name}')
        await session.commit()
