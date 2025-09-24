import re
from dataclasses import dataclass
from datetime import datetime
from typing import Optional, Dict, Any
from decimal import Decimal


@dataclass
class ReceiptData:
    """Класс для хранения данных чека"""
    # Информация о продавце
    merchant_name: Optional[str] = None
    merchant_address: Optional[str] = None
    merchant_phone: Optional[str] = None

    # Информация о дате и времени
    date: Optional[str] = None
    time: Optional[str] = None
    datetime_obj: Optional[datetime] = None

    # Банковская информация
    bank_name: Optional[str] = None
    terminal_id: Optional[str] = None
    merchant_id: Optional[str] = None

    # Статус операции
    status: Optional[str] = None
    currency: Optional[str] = None

    # Итоги операций
    total_operations: int = 0
    total_amount: Decimal = Decimal('0')

    # Детали операций
    payments_count: int = 0
    payments_amount: Decimal = Decimal('0')

    cancellations_count: int = 0
    cancellations_amount: Decimal = Decimal('0')

    refunds_count: int = 0
    refunds_amount: Decimal = Decimal('0')

    # Дополнительная информация
    support_info: Optional[str] = None
    raw_text: Optional[str] = None


class ReceiptParser:
    """Парсер для банковских чеков"""

    def __init__(self):
        # Регулярные выражения для извлечения данных
        self.patterns = {
            'merchant_name': r'^([А-ЯЁа-яё\s\.]+)\s*$',
            'address': r'г\.\s*([^,]+),\s*([^,\n]+)',
            'street': r'ул\.\s*([^,\n]+)',
            'phone': r'т\.\s*(\d+)',
            'datetime': r'(\d{2}\.\d{2}\.\d{2})\s+(\d{2}:\d{2})',
            'bank': r'(ПАО\s+[А-ЯЁа-яё]+|[А-ЯЁа-яё]+\s+БАНК)',
            'terminal': r'Т:\s*(\d+)',
            'merchant_id': r'М:\s*(\d+)',
            'status': r'(Итоги совпали|Итоги не совпали)',
            'currency': r'Валюта\s*:\s*([А-ЯЁа-яё]+)',
            'total_ops': r'Всего операций:\s*(\d+)',
            'total_sum': r'На сумму:\s*([\d,\.]+)',
            'payments': r'Количество оплат:\s*(\d+)',
            'payments_sum': r'Количество оплат:\s*\d+\s*На сумму:\s*([\d,\.]+)',
            'cancellations': r'Количество отмен:\s*(\d+)',
            'cancellations_sum': r'Количество отмен:\s*\d+\s*На сумму:\s*([\d,\.]+)',
            'refunds': r'Количество возвратов:\s*(\d+)',
            'refunds_sum': r'Количество возвратов:\s*\d+\s*На сумму:\s*([\d,\.]+)',
            'support': r'(Оплата-картой\.рф|База знаний кассира)'
        }

    def parse(self, raw_text: str) -> ReceiptData:
        """
        Парсит текст чека и возвращает объект ReceiptData

        Args:
            raw_text (str): Сырой текст чека

        Returns:
            ReceiptData: Распарсенные данные чека
        """
        receipt = ReceiptData(raw_text=raw_text.strip())

        # Очищаем текст от лишних пробелов и разделителей
        cleaned_text = self._clean_text(raw_text)

        # Извлекаем данные
        self._extract_merchant_info(cleaned_text, receipt)
        self._extract_datetime_info(cleaned_text, receipt)
        self._extract_bank_info(cleaned_text, receipt)
        self._extract_transaction_info(cleaned_text, receipt)
        self._extract_additional_info(cleaned_text, receipt)

        return receipt

    def _clean_text(self, text: str) -> str:
        """Очищает текст от лишних символов"""
        # Убираем строки с разделителями
        lines = text.split('\n')
        cleaned_lines = []

        for line in lines:
            # Пропускаем строки только с разделителями
            if re.match(r'^[-*~Q=\s]*$', line):
                continue
            cleaned_lines.append(line.strip())

        return '\n'.join(cleaned_lines)

    def _extract_merchant_info(self, text: str, receipt: ReceiptData):
        """Извлекает информацию о продавце"""
        lines = text.split('\n')

        # Первая строка обычно содержит название
        if lines:
            first_line = lines[0].strip()
            if first_line and not re.match(r'^\d', first_line):
                receipt.merchant_name = first_line

        # Ищем адрес
        address_match = re.search(self.patterns['address'], text)
        if address_match:
            receipt.merchant_address = f"г. {address_match.group(1)}, {address_match.group(2)}"

        # Ищем улицу
        street_match = re.search(self.patterns['street'], text)
        if street_match:
            street = street_match.group(1).strip()
            if receipt.merchant_address:
                receipt.merchant_address += f", ул. {street}"
            else:
                receipt.merchant_address = f"ул. {street}"

        # Ищем телефон
        phone_match = re.search(self.patterns['phone'], text)
        if phone_match:
            receipt.merchant_phone = phone_match.group(1)

    def _extract_datetime_info(self, text: str, receipt: ReceiptData):
        """Извлекает информацию о дате и времени"""
        datetime_match = re.search(self.patterns['datetime'], text)
        if datetime_match:
            receipt.date = datetime_match.group(1)
            receipt.time = datetime_match.group(2)

            # Преобразуем в объект datetime
            try:
                # Предполагаем, что год в формате YY (последние две цифры)
                date_parts = receipt.date.split('.')
                if len(date_parts) == 3:
                    day, month, year = date_parts
                    # Если год двузначный, добавляем 20
                    if len(year) == 2:
                        year = '20' + year

                    datetime_str = f"{day}.{month}.{year} {receipt.time}"
                    receipt.datetime_obj = datetime.strptime(datetime_str, "%d.%m.%Y %H:%M")
            except ValueError:
                pass  # Оставляем datetime_obj как None если не удалось распарсить

    def _extract_bank_info(self, text: str, receipt: ReceiptData):
        """Извлекает банковскую информацию"""
        # Банк
        bank_match = re.search(self.patterns['bank'], text)
        if bank_match:
            receipt.bank_name = bank_match.group(1)

        # Терминал
        terminal_match = re.search(self.patterns['terminal'], text)
        if terminal_match:
            receipt.terminal_id = terminal_match.group(1)

        # ID мерчанта
        merchant_id_match = re.search(self.patterns['merchant_id'], text)
        if merchant_id_match:
            receipt.merchant_id = merchant_id_match.group(1)

        # Статус
        status_match = re.search(self.patterns['status'], text)
        if status_match:
            receipt.status = status_match.group(1)

        # Валюта
        currency_match = re.search(self.patterns['currency'], text)
        if currency_match:
            receipt.currency = currency_match.group(1)

    def _extract_transaction_info(self, text: str, receipt: ReceiptData):
        """Извлекает информацию о транзакциях"""
        # Общее количество операций
        total_ops_match = re.search(self.patterns['total_ops'], text)
        if total_ops_match:
            receipt.total_operations = int(total_ops_match.group(1))

        # Общая сумма (ищем первое вхождение "На сумму")
        total_sum_matches = re.findall(self.patterns['total_sum'], text)
        if total_sum_matches:
            receipt.total_amount = self._parse_amount(total_sum_matches[0])

        # Количество оплат
        payments_match = re.search(self.patterns['payments'], text)
        if payments_match:
            receipt.payments_count = int(payments_match.group(1))

        payments_sum_match = re.search(self.patterns['payments_sum'], text)
        if payments_sum_match:
            receipt.payments_amount = self._parse_amount(payments_sum_match.group(1))

        # Количество отмен
        cancellations_match = re.search(self.patterns['cancellations'], text)
        if cancellations_match:
            receipt.cancellations_count = int(cancellations_match.group(1))

        cancellations_sum_match = re.search(self.patterns['cancellations_sum'], text)
        if cancellations_sum_match:
            receipt.cancellations_amount = self._parse_amount(cancellations_sum_match.group(1))

        # Количество возвратов
        refunds_match = re.search(self.patterns['refunds'], text)
        if refunds_match:
            receipt.refunds_count = int(refunds_match.group(1))

        refunds_sum_match = re.search(self.patterns['refunds_sum'], text)
        if refunds_sum_match:
            receipt.refunds_amount = self._parse_amount(refunds_sum_match.group(1))

    def _extract_additional_info(self, text: str, receipt: ReceiptData):
        """Извлекает дополнительную информацию"""
        support_match = re.search(self.patterns['support'], text)
        if support_match:
            receipt.support_info = support_match.group(1)

    def _parse_amount(self, amount_str: str) -> Decimal:
        """Преобразует строку суммы в Decimal"""
        # Убираем пробелы и заменяем запятую на точку
        clean_amount = amount_str.replace(' ', '').replace(',', '.')
        try:
            return Decimal(clean_amount)
        except:
            return Decimal('0')

    def to_dict(self, receipt: ReceiptData) -> Dict[str, Any]:
        """Преобразует объект ReceiptData в словарь (без raw_text)"""
        result = {}
        for field in receipt.__dataclass_fields__:
            # Пропускаем raw_text
            if field == 'raw_text':
                continue

            value = getattr(receipt, field)
            if isinstance(value, Decimal):
                result[field] = float(value)
            elif isinstance(value, datetime):
                result[field] = value.isoformat()
            else:
                result[field] = value
        return result


parser = ReceiptParser()
