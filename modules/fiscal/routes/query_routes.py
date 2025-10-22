from fastapi import status

from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.endpoints.query_endpoints import *


QUERY_ROUTES = [
    # БАЗОВЫЕ ЗАПРОСЫ СТАТУСА
    RouteDTO(
        path="/status",
        endpoint=get_status,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Полный статус ККТ",
        description="Запрос полной информации и статуса ККТ: модель, серийный номер, состояние смены, крышка, наличие бумаги и многое другое",
        responses={
            status.HTTP_200_OK: {
                "description": "Статус успешно получен",
            },
        },
    ),
    RouteDTO(
        path="/short-status",
        endpoint=get_short_status,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Короткий статус ККТ",
        description="Короткий запрос статуса: денежный ящик, бумага, крышка",
        responses={
            status.HTTP_200_OK: {
                "description": "Короткий статус получен",
            },
        },
    ),
    RouteDTO(
        path="/cash-sum",
        endpoint=get_cash_sum,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сумма наличных",
        description="Запрос суммы наличных в денежном ящике",
        responses={
            status.HTTP_200_OK: {
                "description": "Сумма наличных получена",
            },
        },
    ),
    RouteDTO(
        path="/shift-state",
        endpoint=get_shift_state,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Состояние смены",
        description="Запрос состояния смены: состояние (закрыта/открыта/истекла), номер смены, дата истечения",
        responses={
            status.HTTP_200_OK: {
                "description": "Состояние смены получено",
            },
        },
    ),
    RouteDTO(
        path="/receipt-state",
        endpoint=get_receipt_state,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Состояние чека",
        description="Запрос состояния чека: тип, сумма, номер, неоплаченный остаток, сдача",
        responses={
            status.HTTP_200_OK: {
                "description": "Состояние чека получено",
            },
        },
    ),
    RouteDTO(
        path="/datetime",
        endpoint=get_datetime,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Дата и время",
        description="Запрос текущих даты и времени в ККТ",
        responses={
            status.HTTP_200_OK: {
                "description": "Дата и время получены",
            },
        },
    ),
    RouteDTO(
        path="/serial-number",
        endpoint=get_serial_number,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Заводской номер",
        description="Запрос заводского номера ККТ",
        responses={
            status.HTTP_200_OK: {
                "description": "Заводской номер получен",
            },
        },
    ),
    RouteDTO(
        path="/model-info",
        endpoint=get_model_info,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Информация о модели",
        description="Запрос информации о модели ККТ: номер модели, название, версия ПО",
        responses={
            status.HTTP_200_OK: {
                "description": "Информация о модели получена",
            },
        },
    ),
    RouteDTO(
        path="/receipt-line-length",
        endpoint=get_receipt_line_length,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Ширина чековой ленты",
        description="Запрос ширины чековой ленты в символах и пикселях",
        responses={
            status.HTTP_200_OK: {
                "description": "Ширина чековой ленты получена",
            },
        },
    ),

    # ЗАПРОСЫ ВЕРСИЙ МОДУЛЕЙ
    RouteDTO(
        path="/unit-version",
        endpoint=get_unit_version,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Версия модуля",
        description="Запрос версии модуля ККТ (прошивка, конфигурация, шаблоны, блок управления, загрузчик)",
        responses={
            status.HTTP_200_OK: {
                "description": "Версия модуля получена",
            },
        },
    ),

    # СЧЕТЧИКИ И СУММЫ
    RouteDTO(
        path="/payment-sum",
        endpoint=get_payment_sum,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сумма платежей",
        description="Запрос суммы платежей за смену по типу оплаты и типу чека",
        responses={
            status.HTTP_200_OK: {
                "description": "Сумма платежей получена",
            },
        },
    ),
    RouteDTO(
        path="/cashin-sum",
        endpoint=get_cashin_sum,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сумма внесений",
        description="Запрос суммы внесений за смену",
        responses={
            status.HTTP_200_OK: {
                "description": "Сумма внесений получена",
            },
        },
    ),
    RouteDTO(
        path="/cashout-sum",
        endpoint=get_cashout_sum,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Сумма выплат",
        description="Запрос суммы выплат за смену",
        responses={
            status.HTTP_200_OK: {
                "description": "Сумма выплат получена",
            },
        },
    ),
    RouteDTO(
        path="/receipt-count",
        endpoint=get_receipt_count,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Количество чеков",
        description="Запрос количества чеков за смену по типу",
        responses={
            status.HTTP_200_OK: {
                "description": "Количество чеков получено",
            },
        },
    ),
    RouteDTO(
        path="/non-nullable-sum",
        endpoint=get_non_nullable_sum,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Необнуляемая сумма",
        description="Запрос необнуляемой суммы (накопительный итог с момента фискализации) по типу чека",
        responses={
            status.HTTP_200_OK: {
                "description": "Необнуляемая сумма получена",
            },
        },
    ),

    # ПИТАНИЕ И ТЕМПЕРАТУРА
    RouteDTO(
        path="/power-source-state",
        endpoint=get_power_source_state,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Состояние питания",
        description="Запрос состояния источника питания: заряд, напряжение, работа от аккумулятора, зарядка",
        responses={
            status.HTTP_200_OK: {
                "description": "Состояние питания получено",
            },
        },
    ),
    RouteDTO(
        path="/printer-temperature",
        endpoint=get_printer_temperature,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Температура печатающей головки",
        description="Запрос температуры термопечатающей головки (ТПГ) в градусах Цельсия",
        responses={
            status.HTTP_200_OK: {
                "description": "Температура получена",
            },
        },
    ),

    # ДИАГНОСТИКА И ОШИБКИ
    RouteDTO(
        path="/fatal-status",
        endpoint=get_fatal_status,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Фатальные ошибки",
        description="Запрос фатальных ошибок ККТ: сбои оборудования, памяти, ФН и другие критические ошибки",
        responses={
            status.HTTP_200_OK: {
                "description": "Информация о фатальных ошибках получена",
            },
        },
    ),

    # СЕТЕВЫЕ ИНТЕРФЕЙСЫ
    RouteDTO(
        path="/mac-address",
        endpoint=get_mac_address,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="MAC-адрес",
        description="Запрос MAC-адреса Ethernet интерфейса",
        responses={
            status.HTTP_200_OK: {
                "description": "MAC-адрес получен",
            },
        },
    ),
    RouteDTO(
        path="/ethernet-info",
        endpoint=get_ethernet_info,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Конфигурация Ethernet",
        description="Запрос текущей конфигурации Ethernet: IP, маска, шлюз, DNS, порт (только для ККТ версий 5.X)",
        responses={
            status.HTTP_200_OK: {
                "description": "Конфигурация Ethernet получена",
            },
        },
    ),
    RouteDTO(
        path="/wifi-info",
        endpoint=get_wifi_info,
        response_model=BaseResponseDTO,
        methods=["GET"],
        status_code=status.HTTP_200_OK,
        summary="Конфигурация Wi-Fi",
        description="Запрос текущей конфигурации Wi-Fi: IP, маска, шлюз, порт (только для ККТ версий 5.X)",
        responses={
            status.HTTP_200_OK: {
                "description": "Конфигурация Wi-Fi получена",
            },
        },
    ),
]
