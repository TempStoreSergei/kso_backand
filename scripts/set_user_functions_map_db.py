from sqlalchemy import select

from api.configs.database import async_session_maker
from api.models.auth_models import UserFunctionsMap, User, TerminalFunctions
from api.configs.loggers import logger


async def set_user_functions_map_db():
    """Функция заполняет таблицу связей функций терминала и пользователей."""

    user_functions_map = {
        'admin': [
            'Изменить свой пароль',
            'Инициализировать наличную систему оплаты',
            'Получить статус наличной системы оплаты',
            'Тест приема купюр',
            'Тест выдачи купюр',
        ],
        'operator': [
            'Изменить свой пароль',
            'Инициализировать наличную систему оплаты',
            'Получить статус наличной системы оплаты',
            'Тест приема купюр',
            'Тест выдачи купюр',
        ],
    }

    async with async_session_maker() as session:
        # админ
        query = select(User).where(User.user_name == 'admin')
        result = await session.execute(query)
        admin_user = result.scalar_one_or_none()

        if admin_user:
            for func_name in user_functions_map['admin']:
                query = select(TerminalFunctions).where(TerminalFunctions.function_name == func_name)
                result = await session.execute(query)
                func = result.scalar_one_or_none()

                if func:
                    # проверка на существование
                    check_query = select(UserFunctionsMap).where(
                        UserFunctionsMap.user_id == admin_user.id,
                        UserFunctionsMap.terminal_function_id == func.id,
                    )
                    check_result = await session.execute(check_query)
                    exists = check_result.scalar_one_or_none()

                    if not exists:
                        rule = UserFunctionsMap(
                            terminal_function=func,
                            user=admin_user,
                        )
                        session.add(rule)
                        logger.info(f'Пользователю admin добавлена функция {func_name}')

        # оператор
        query = select(User).where(User.user_name == 'operator')
        result = await session.execute(query)
        operator_user = result.scalar_one_or_none()

        if operator_user:
            for func_name in user_functions_map['operator']:
                query = select(TerminalFunctions).where(TerminalFunctions.function_name == func_name)
                result = await session.execute(query)
                func = result.scalar_one_or_none()

                if func:
                    check_query = select(UserFunctionsMap).where(
                        UserFunctionsMap.user_id == operator_user.id,
                        UserFunctionsMap.terminal_function_id == func.id,
                    )
                    check_result = await session.execute(check_query)
                    exists = check_result.scalar_one_or_none()

                    if not exists:
                        rule = UserFunctionsMap(
                            terminal_function=func,
                            user=operator_user,
                        )
                        session.add(rule)
                        logger.info(f'Пользователю operator добавлена функция {func_name}')

        await session.commit()
