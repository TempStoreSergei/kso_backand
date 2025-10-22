from typing import Optional, List

from pydantic import BaseModel, Field


class OpenReceiptRequest(BaseModel):
    """Запрос на открытие чека"""
    receipt_type: int = Field(..., description="Тип чека (0-7, см. константы RECEIPT_TYPE_*)")
    electronically: bool = Field(False, description="Электронный чек (не печатать)")
    customer_contact: Optional[str] = Field(None, description="Email или телефон покупателя (тег 1008)")
    customer_name: Optional[str] = Field(None, description="Покупатель (клиент) (тег 1227, ФФД < 1.2)")
    customer_inn: Optional[str] = Field(None, description="ИНН покупателя (тег 1228)")
    email_sender: Optional[str] = Field(None, description="Email отправителя чека (тег 1117)")
    tax_system: Optional[int] = Field(None, description="Применяемая СНО (тег 1055, 0-4)")
    settlement_place: Optional[str] = Field(None, description="Место расчетов (тег 1187)")
    settlement_address: Optional[str] = Field(None, description="Адрес расчетов (тег 1009, ФФД ≥ 1.2)")
    fns_site: Optional[str] = Field(None, description="Адрес сайта ФНС (тег 1060)")
    agent_type: Optional[int] = Field(None, description="Признак агента (тег 1057, ФФД < 1.2, 0-6)")
    supplier_phone: Optional[str] = Field(None, description="Телефон поставщика (тег 1171, ФФД < 1.2)")
    bank_agent_operation: Optional[str] = Field(None, description="Операция банковского платежного агента (тег 1044)")
    payment_agent_phones: Optional[List[str]] = Field(None, description="Телефоны платежного агента (тег 1073)")
    transfer_operator_address: Optional[str] = Field(None, description="Адрес оператора перевода (тег 1005)")
    transfer_operator_inn: Optional[str] = Field(None, description="ИНН оператора перевода (тег 1016)")
    transfer_operator_name: Optional[str] = Field(None, description="Наименование оператора перевода (тег 1026)")
    transfer_operator_phones: Optional[List[str]] = Field(None, description="Телефоны оператора перевода (тег 1075)")
    payment_receiver_operator_phones: Optional[List[str]] = Field(None, description="Телефоны оператора по приему платежей (тег 1074)")
    user_attribute: Optional[bytes] = Field(None, description="Дополнительный реквизит пользователя (тег 1084)")
    receipt_additional_attribute: Optional[str] = Field(None, description="Дополнительный реквизит чека (БСО) (тег 1192)")
    client_info: Optional[bytes] = Field(None, description="Сведения о покупателе (тег 1256, ФФД ≥ 1.2)")
    industry_attribute: Optional[bytes] = Field(None, description="Отраслевой реквизит чека (тег 1261, ФФД ≥ 1.2)")
    operational_attribute: Optional[bytes] = Field(None, description="Операционный реквизит чека (тег 1270, ФФД ≥ 1.2)")
    internet_sign: bool = Field(False, description="Признак расчета в Интернет (тег 1125)")
    # Для чеков коррекции
    correction_type: Optional[int] = Field(None, description="Тип коррекции (тег 1173): 0=самостоятельно, 1=по предписанию")
    correction_base_date: Optional[str] = Field(None, description="Дата корректируемого расчета (тег 1178, формат YYYY-MM-DD)")
    correction_base_number: Optional[str] = Field(None, description="Номер предписания налогового органа (тег 1179)")
