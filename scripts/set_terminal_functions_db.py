# from sqlalchemy import select
#
# from api.configs.database import async_session_maker
# from api.models.auth_models import TerminalFunctions
# from api.configs.loggers import logger
#
#
# async def set_terminal_functions_db():
#     """Функция заполняет таблицу функций терминала в БД."""
#
#     functions = [
#         # Общее
#         {
#             'function_name': 'Изменить свой пароль',
#             'endpoint_name': '/api/v1/auth/change_password',
#             'module_name': 'main',
#         },
#         {
#             'function_name': 'Изменить пароль пользователя',
#             'endpoint_name': '/api/v1/auth/change_user_password',
#             'module_name': 'main',
#         },
#         {
#             'function_name': 'Получить функции пользователя',
#             'endpoint_name': '/api/v1/auth/get_user_functions',
#             'module_name': 'main',
#         },
#         # Заставка
#         {
#             'function_name': 'Добавление файла скринсейвера',
#             'endpoint_name': '/api/v1/screensaver/add_screensaver_file',
#             'module_name': 'screensaver',
#         },
#         {
#             'function_name': 'Удаление файла скринсейвера',
#             'endpoint_name': '/api/v1/screensaver/delete_screensaver_file',
#             'module_name': 'screensaver',
#         },
#         {
#             'function_name': 'Получение файлов скринсейвера',
#             'endpoint_name': '/api/v1/screensaver/get_screensaver_files',
#             'module_name': 'screensaver',
#         },
#         {
#             'function_name': 'Получение настроек скринсейвера',
#             'endpoint_name': '/api/v1/screensaver/get_screensaver_settings',
#             'module_name': 'screensaver',
#         },
#         {
#             'function_name': 'Обновление настроек скринсейвера',
#             'endpoint_name': '/api/v1/screensaver/update_screensaver_settings',
#             'module_name': 'screensaver',
#         },
#         {
#             'function_name': 'Обновление файла скринсейвера',
#             'endpoint_name': '/api/v1/screensaver/update_screensaver_file',
#             'module_name': 'screensaver',
#         },
#         # Наличка
#         {
#             'function_name': 'Инициализировать наличную систему оплаты',
#             'endpoint_name': '/api/v1/cash_system/init_system',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Получить статус наличной системы оплаты',
#             'endpoint_name': '/api/v1/cash_system/status_system',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Установить доступные устройства наличной системы оплаты',
#             'endpoint_name': '/api/v1/cash_system/set_available_devices',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Запустить процесс оплаты наличными',
#             'endpoint_name': '/api/v1/cash_system/start_accepting_payment',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Остановить/прервать процесс оплаты наличными',
#             'endpoint_name': '/api/v1/cash_system/stop_accepting_payment',
#             'module_name': 'cash_system',
#         },
#         # Bill acceptor
#         {
#             'function_name': 'Тест приема купюр',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_acceptor/test',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Сброс кол-ва купюр в купюроприемнике (инкасация)',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_acceptor/reset_bill_count',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Установка максимального кол-ва купюр в купюроприемнике',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_acceptor/set_max_bill_count',
#             'module_name': 'cash_system',
#         },
#         # Bill Dispenser
#         {
#             'function_name': 'Тест выдачи купюр',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_dispenser/test',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Настройка номиналов купюр в bill_dispenser',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_dispenser/set_nominal',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Добавление купюр в bill_dispenser',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_dispenser/add_bill_count',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Сброс кол-ва купюр в bill_dispenser',
#             'endpoint_name': '/api/v1/cash_system/status_system/bill_dispenser/reset_bill_count',
#             'module_name': 'cash_system',
#         },
#         # Coin
#         {
#             'function_name': 'Тест приема монет',
#             'endpoint_name': '/api/v1/cash_system/coin_system/test',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Тест выдачи монет',
#             'endpoint_name': '/api/v1/cash_system/coin_system/test',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Добавление монет',
#             'endpoint_name': '/api/v1/cash_system/coin_system/add_coin_count',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Инкасация coin_system',
#             'endpoint_name': '/api/v1/cash_system/coin_system/cash_collection',
#             'module_name': 'cash_system',
#         },
#         {
#             'function_name': 'Сброс кол-ва монет',
#             'endpoint_name': '/api/v1/cash_system/coin_system/reset_coin_count',
#             'module_name': 'cash_system',
#         },
#         # Acquiring
#         {
#             'function_name': 'Проверка соединения с аппаратом эквайринга',
#             'endpoint_name': '/api/v1/acquiring/test_connect',
#             'module_name': 'acquiring',
#         },
#         {
#             'function_name': 'Открыть технологическое меню',
#             'endpoint_name': '/api/v1/acquiring/open_menu',
#             'module_name': 'acquiring',
#         },
#         {
#             'function_name': 'Получить сверку итогов',
#             'endpoint_name': '/api/v1/acquiring/get_results',
#             'module_name': 'acquiring',
#         },
#         {
#             'function_name': 'Начать безналичную оплату',
#             'endpoint_name': '/api/v1/acquiring/start_payment',
#             'module_name': 'acquiring',
#         },
#         {
#             'function_name': 'Отмена платежа по карте',
#             'endpoint_name': '/api/v1/acquiring/cancel_payment',
#             'module_name': 'acquiring',
#         },
#         {
#             'function_name': 'Возврат платежа по карте',
#             'endpoint_name': '/api/v1/acquiring/refund_payment',
#             'module_name': 'acquiring',
#         },
#         # Scanner
#         {
#             'function_name': 'Ввод со сканера',
#             'endpoint_name': '/api/v1/scanner/input',
#             'module_name': 'scanner',
#         },
#         # Fiscal
#         {
#             'function_name': 'Проверка соединения с ФР',
#             'endpoint_name': '/api/v1/fiscal/check_connect',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Открыть смену',
#             'endpoint_name': '/api/v1/fiscal/open_shift',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Закрыть смену',
#             'endpoint_name': '/api/v1/fiscal/close_shift',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Получить фискальный документ',
#             'endpoint_name': '/api/v1/fiscal/get_fiscal_document',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Сбросить состояние ФР',
#             'endpoint_name': '/api/v1/fiscal/reset_ecr',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Отменить открытый чек',
#             'endpoint_name': '/api/v1/fiscal/cancel_open_check',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Получить статус ФН',
#             'endpoint_name': '/api/v1/fiscal/get_fn_status',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Получить статус ФР',
#             'endpoint_name': '/api/v1/fiscal/get_ecr_status',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Создать чек оплаты',
#             'endpoint_name': '/api/v1/fiscal/create_payment_check',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Создать чек возврата',
#             'endpoint_name': '/api/v1/fiscal/create_refund_check',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Печать последнего чека',
#             'endpoint_name': '/api/v1/fiscal/print_last_document',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Получение последнего фискального документа',
#             'endpoint_name': '/api/v1/fiscal/get_last_document',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Печать слип чека',
#             'endpoint_name': '/api/v1/fiscal/print_slip_sheck',
#             'module_name': 'fiscal',
#         },
#         {
#             'function_name': 'Получить X-отчет',
#             'endpoint_name': '/api/v1/fiscal/get_x_report',
#             'module_name': 'fiscal',
#         },
#     ]
#
#     async with async_session_maker() as session:
#         for func in functions:
#             db_func = await session.scalar(
#                 select(TerminalFunctions).where(
#                     (TerminalFunctions.function_name == func["function_name"])
#                     | (TerminalFunctions.endpoint_name == func["endpoint_name"])
#                 )
#             )
#             if db_func:
#                 continue
#             func_data = TerminalFunctions(**func)
#             session.add(func_data)
#             logger.info(f'Добавлена функция {func_data.function_name}')
#         await session.commit()
