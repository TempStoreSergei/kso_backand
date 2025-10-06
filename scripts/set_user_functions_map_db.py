# from sqlalchemy import select
#
# from api.configs.database import async_session_maker
# from api.models.auth_models import UserFunctionsMap, User, TerminalFunctions
# from api.configs.loggers import logger
#
#
# async def set_user_functions_map_db():
#     """Функция заполняет таблицу связей функций терминала и пользователей."""
#
#     # функции доступные оператору и самой кассе
#     common_funcs = [
#         'Изменить свой пароль',
#         'Получить функции пользователя',
#         'Получение файлов скринсейвера',
#         'Получение настроек скринсейвера',
#         'Инициализировать наличную систему оплаты',
#         'Получить статус наличной системы оплаты',
#         'Запустить процесс оплаты наличными',
#         'Остановить/прервать процесс оплаты наличными',
#         'Тест приема купюр',
#         'Сброс кол-ва купюр в купюроприемнике (инкасация)',
#         'Тест выдачи купюр',
#         'Добавление купюр в bill_dispenser',
#         'Тест приема монет',
#         'Тест выдачи монет',
#         'Добавление монет',
#         'Инкасация coin_system',
#         'Сброс кол-ва монет',
#         'Проверка соединения с аппаратом эквайринга',
#         'Открыть технологическое меню',
#         'Получить сверку итогов',
#         'Начать безналичную оплату',
#         'Отмена платежа по карте',
#         'Возврат платежа по карте',
#         'Ввод со сканера',
#         'Проверка соединения с ФР',
#         'Открыть смену',
#         'Закрыть смену',
#         'Получить статус ФН',
#         'Получить статус ФР',
#         'Создать чек оплаты',
#         'Печать последнего чека',
#         'Получение последнего фискального документа',
#         'Печать слип чека',
#         'Получить X-отчет',
#
#         'Добавление файла скринсейвера',
#         'Удаление файла скринсейвера',
#         'Обновление настроек скринсейвера',
#         'Обновление файла скринсейвера',
#         'Получить фискальный документ',
#         'Сбросить состояние ФР',
#         'Отменить открытый чек',
#     ]
#     user_functions_map = {
#         # функции доступные только администратору
#         'admin': [
#             'Изменить пароль пользователя',
#             'Установить доступные устройства наличной системы оплаты',
#             'Установка максимального кол-ва купюр в купюроприемнике',
#             'Настройка номиналов купюр в bill_dispenser',
#             'Сброс кол-ва купюр в bill_dispenser',
#             'Создать чек возврата',
#         ] + common_funcs,
#         'operator': common_funcs,
#     }
#
#     async with async_session_maker() as session:
#         # админ
#         query = select(User).where(User.user_name == 'admin')
#         result = await session.execute(query)
#         admin_user = result.scalar_one_or_none()
#
#         if admin_user:
#             for func_name in user_functions_map['admin']:
#                 query = select(TerminalFunctions).where(TerminalFunctions.function_name == func_name)
#                 result = await session.execute(query)
#                 func = result.scalar_one_or_none()
#
#                 if func:
#                     # проверка на существование
#                     check_query = select(UserFunctionsMap).where(
#                         UserFunctionsMap.user_id == admin_user.id,
#                         UserFunctionsMap.terminal_function_id == func.id,
#                     )
#                     check_result = await session.execute(check_query)
#                     exists = check_result.scalar_one_or_none()
#
#                     if not exists:
#                         rule = UserFunctionsMap(
#                             terminal_function=func,
#                             user=admin_user,
#                         )
#                         session.add(rule)
#                         logger.info(f'Пользователю admin добавлена функция {func_name}')
#
#         # оператор
#         query = select(User).where(User.user_name == 'operator')
#         result = await session.execute(query)
#         operator_user = result.scalar_one_or_none()
#
#         if operator_user:
#             for func_name in user_functions_map['operator']:
#                 query = select(TerminalFunctions).where(TerminalFunctions.function_name == func_name)
#                 result = await session.execute(query)
#                 func = result.scalar_one_or_none()
#
#                 if func:
#                     check_query = select(UserFunctionsMap).where(
#                         UserFunctionsMap.user_id == operator_user.id,
#                         UserFunctionsMap.terminal_function_id == func.id,
#                     )
#                     check_result = await session.execute(check_query)
#                     exists = check_result.scalar_one_or_none()
#
#                     if not exists:
#                         rule = UserFunctionsMap(
#                             terminal_function=func,
#                             user=operator_user,
#                         )
#                         session.add(rule)
#                         logger.info(f'Пользователю operator добавлена функция {func_name}')
#
#         await session.commit()
