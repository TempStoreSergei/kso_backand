"""Маршруты для операций чтения данных из ФН и ККТ"""
from fastapi import status
from api.DTO.factories.router_factory import RouteDTO
from modules.fiscal.DTO.base_response_dto import BaseResponseDTO
from modules.fiscal.endpoints.read_endpoints import (
    read_fn_document,
    read_licenses,
    read_registration_document,
    parse_complex_attribute,
    read_kkt_settings,
    read_last_document_journal
)


READ_ROUTES = [
    RouteDTO(
        path="/fn-document",
        endpoint=read_fn_document,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Чтение документа из ФН",
        description="Чтение документа из фискального накопителя (ФН) в виде TLV-структур по номеру документа. "
                    "Возвращает тип документа, размер и список всех TLV-реквизитов документа.",
        responses={
            status.HTTP_200_OK: {
                "description": "Документ успешно прочитан из ФН",
            },
        },
    ),
    RouteDTO(
        path="/licenses",
        endpoint=read_licenses,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Чтение списка лицензий",
        description="Чтение списка всех введенных лицензий / кодов защиты ККТ. "
                    "Для каждой лицензии возвращается номер, название и срок действия.",
        responses={
            status.HTTP_200_OK: {
                "description": "Список лицензий успешно получен",
            },
        },
    ),
    RouteDTO(
        path="/registration-document",
        endpoint=read_registration_document,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Чтение документа регистрации",
        description="Чтение документа регистрации из ФН в виде TLV-структур по порядковому номеру регистрации. "
                    "Возвращает все реквизиты документа регистрации.",
        responses={
            status.HTTP_200_OK: {
                "description": "Документ регистрации успешно прочитан",
            },
        },
    ),
    RouteDTO(
        path="/parse-complex-attribute",
        endpoint=parse_complex_attribute,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Разбор составного реквизита",
        description="Разбор массива байтов со значением составного реквизита (STLV). "
                    "Возвращает список всех вложенных реквизитов с их типами и значениями.",
        responses={
            status.HTTP_200_OK: {
                "description": "Составной реквизит успешно разобран",
            },
        },
    ),
    RouteDTO(
        path="/kkt-settings",
        endpoint=read_kkt_settings,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Чтение настроек ККТ",
        description="Чтение всех настроек ККТ (числовых, логических, строковых). "
                    "Для каждой настройки возвращается ID, тип, название и текущее значение.",
        responses={
            status.HTTP_200_OK: {
                "description": "Настройки ККТ успешно прочитаны",
            },
        },
    ),
    RouteDTO(
        path="/last-document-journal",
        endpoint=read_last_document_journal,
        response_model=BaseResponseDTO,
        methods=["POST"],
        status_code=status.HTTP_200_OK,
        summary="Чтение последнего документа из журнала",
        description="Чтение последнего закрытого документа из электронного журнала в формате TLV. "
                    "Возвращает массив TLV-структур (tag, length, value) и сырой массив байтов.",
        responses={
            status.HTTP_200_OK: {
                "description": "Последний документ из журнала успешно прочитан",
            },
        },
    ),
]
