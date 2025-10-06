from enum import Enum
from datetime import datetime

from pydantic import BaseModel, Field


class PaymentType(str, Enum):
    cash = 'cash'
    card = 'card'


class PayOrderDTO(BaseModel):
    order: str = Field(
        examples=['e152b72d-675a-11ee-b5fe-eb21b8c7eb9d'],
        description='GUID документа в 1С(квитанции',
    )
    payment_type: PaymentType = Field(
        examples=['cash'],
        description='Тип оплаты',
    )
    sum: int = Field(
        examples=[300],
        description='Сумма платежа',
    )
    avance: int = Field(
        0,
        examples=[0],
        description='Предоплата',
    )
    paymentId: str = Field(
        examples=['e152b72d-675a-11ee-b5fe-eb21b8c7eb9d'], # генерирует касса
        description='Id платежа',
    )
    datetime_field: datetime = Field(
        examples=['2024-02-18 32:20:43'],
        description='Id платежа',
        alias='datetime',
    )
    fiscal: str # уточнить



# class FiscalDocument(BaseModel):
#     """Поля фискального документа для 1C."""
#     fiscal_drive_number: str = Field(description='НОМЕР ФН')
#     cash_register_reg_number: str = Field(description='РЕГ. НОМЕР ККТ')
#     fiscal_document_number: str = Field(description='НОМЕР ФД')
#     date_time: str = Field(description='ДАТА, ВРЕМЯ')
#     document_signature: str = Field(description='ФП ДОКУМЕНТА')
#     shift_number: str = Field(description='НОМЕР СМЕНЫ')
#     receipt_number_in_shift: str = Field(description='НОМЕР ЧЕКА ЗА СМЕНУ')
#     transaction_type: str = Field(description='ПРИЗН. РАСЧЕТА')
#
#
# class PinpadReportData(BaseModel):
#     """Схема данных сверки итогов пинпада."""
#     merchant_name: str = Field(description='Название продавца')
#     merchant_address: str = Field(description='Адрес продавца')
#     merchant_phone: str = Field(description='Телефон продавца')
#     date: str = Field(description='Дата отчета (формат: ДД.ММ.ГГ)')
#     time: str = Field(description='Время отчета (формат: ЧЧ:ММ)')
#     datetime_obj: str = Field(description='Дата и время операции')
#     bank_name: str = Field(description='Название банка')
#     terminal_id: str = Field(description='ID терминала')
#     merchant_id: str = Field(description='ID продавца')
#     status: str = Field(description='Статус отчета')
#     currency: str | None = Field(default=None, description='Валюта операций')
#     total_operations: int = Field(description='Общее количество операций')
#     total_amount: float = Field(description='Общая сумма операций')
#     payments_count: int = Field(description='Количество оплат')
#     payments_amount: float = Field(description='Сумма оплат')
#     cancellations_count: int = Field(description='Количество отмен')
#     cancellations_amount: float = Field(description='Сумма отмен')
#     refunds_count: int = Field(description='Количество возвратов')
#     refunds_amount: float = Field(description='Сумма возвратов')
#
#
# class ZReportData(BaseModel):
#     ffd_version: str = Field(..., description="ФФД версия (ВЕРСИЯ ФФД)")
#     fn_number: str = Field(..., description="Номер фискального накопителя (НОМЕР ФН)")
#     kkt_registration_number: str = Field(...,
#                                          description="Регистрационный номер ККТ (РЕГ. НОМЕР ККТ)")
#     user_inn: str = Field(..., description="ИНН пользователя (ИНН ПОЛЬЗ.)")
#     fd_number: str = Field(..., description="Номер фискального документа (НОМЕР ФД)")
#     date_time: str = Field(..., description="Дата и время формирования (ДАТА, ВРЕМЯ)")
#     document_fp: str = Field(..., description="Фискальный признак документа (ФП ДОКУМЕНТА)")
#     shift_number: str = Field(..., description="Номер смены (НОМЕР СМЕНЫ)")
#     receipts_count: str = Field(..., description="Количество чеков (БСО) за смену")
#     fds_count: str = Field(..., description="Общее количество ФД за смену")
#     unsent_fds_count: str = Field(..., description="Количество непереданных ФД")
#     first_unsent_fd_datetime: str = Field(...,
#                                                description="Дата и время первого непереданного ФД")
#     operator_message: str = Field(..., description="Сообщение оператора (СООБЩ. ОПЕР.)")
#     fp_keys_resource: str = Field(..., description="Ресурс ключей ФП")
#     receipts_bso_with_signs_count: str = Field(...,
#                                                description="Количество чеков БСО со всеми признаками расчёта")
#     receipts_by_signs_count: str = Field(..., description="Количество чеков по признакам расчёта")
#     total_amount_bso: str = Field(..., description="Общая итоговая сумма в чеках БСО")
#     total_amount_bso_cash: str = Field(..., description="Итоговая сумма в чеках БСО наличными")
#     total_amount_bso_electronic: str = Field(...,
#                                                description="Итоговая сумма в чеках БСО электронными")
#     total_amount_bso_prepayment: str = Field(...,
#                                                description="Итоговая сумма в чеках БСО предоплата")
#     total_amount_bso_postpayment: str = Field(...,
#                                                 description="Итоговая сумма в чеках БСО постоплата")
#     total_amount_bso_counter_provision: str = Field(...,
#                                                       description="Итоговая сумма в чеках БСО встречное предоставление")
#     vat_20: str = Field(..., description="Сумма НДС 20%")
#     vat_10: str = Field(..., description="Сумма НДС 10%")
#     amount_with_vat_0: str = Field(..., description="Сумма расчётов с НДС 0%")
#     amount_without_vat: str = Field(..., description="Сумма расчётов без НДС")
#     vat_20_120: str = Field(..., description="Сумма НДС по расчетной ставке 20/120")
#     vat_10_110: str = Field(..., description="Сумма НДС по расчетной ставке 10/110")
#
#
# class ShiftReportData(BaseModel):
#     z_report: ZReportData | None
#     reconciliation_of_results: PinpadReportData | None
