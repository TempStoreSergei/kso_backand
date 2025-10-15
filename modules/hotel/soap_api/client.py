import httpx
from uuid import uuid4
from typing import Dict, Optional, List, Any
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
import xml.etree.ElementTree as ET


class OrderItem(BaseModel):
    """Схема для представления товара/услуги в заказе"""
    service: str
    item_name: str
    item_id: str
    quantity: int
    price: float
    sum: float


class Client(BaseModel):
    """Схема для представления клиента"""
    room: Optional[str] = None
    card: Optional[str] = None

    @field_validator('room', 'card', mode='before')
    @classmethod
    def validate_client_field(cls, v):
        if v is not None:
            return str(v)
        return v


class Order(BaseModel):
    """Схема для представления заказа"""
    order_id: str
    order_date: datetime
    sum: float
    quantity: int
    currency: str
    items: List[OrderItem]


class SOAPFault(BaseModel):
    """Схема для SOAP ошибки"""
    fault_code: Optional[str] = None
    fault_string: Optional[str] = None
    detail: Optional[str] = None


class SOAPResponse(BaseModel):
    """Схема для ответа от SOAP сервера"""
    success: bool
    status_code: int
    raw_content: str
    data: Optional[Dict[str, Any]] = None
    error: Optional[Dict[str, str] | str] = None
    response_body: Optional[str] = None


class HotelSOAPClient:
    """Асинхронный SOAP клиент для работы с API 1C:Отель"""

    NAMESPACES = {
        'soap': 'http://schemas.xmlsoap.org/soap/envelope/',
        'res': 'http://www.1chotel.ru/ws/interfaces/restaurant/',
        'int': 'http://www.1chotel.ru/interfaces/restaurant/'
    }

    # Тестовые данные
    TEST_ENVIRONMENT = {
        'url': 'https://demo.1c-hotel.cloud/link/ws/RestaurantInterfaces',
        'token': 'de83353e-2bea-4651-8707-2e2e2be18caf',
        'test_cards': {
            'active': '114477',
            'discount_10': 'FR114320D90',
            'blocked': '444555',
            'non_existent': '220055'
        },
        'test_rooms': {
            'single_guest': '21',
            'two_guests': '55',
            'banquet': '642'
        }
    }

    def __init__(
            self,
            base_url: str,
            token: str,
            timeout: float = 30.0
    ):
        """
        Инициализация асинхронного SOAP клиента для 1C:Отель

        Args:
            base_url: Базовый URL для SOAP запросов
            token: Токен авторизации (ExternalSystemCode)
            timeout: Таймаут для запросов в секундах
        """
        self.base_url = base_url
        self.token = token
        self.timeout = timeout
        self.client: Optional[httpx.AsyncClient] = None

    @classmethod
    def test_environment(cls):
        """Создать клиент для тестовой среды"""
        return cls(
            base_url=cls.TEST_ENVIRONMENT['url'],
            token=cls.TEST_ENVIRONMENT['token']
        )

    async def __aenter__(self):
        """Вход в контекстный менеджер"""
        self.client = httpx.AsyncClient(timeout=self.timeout, verify=False)
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Выход из контекстного менеджера"""
        if self.client:
            await self.client.aclose()

    def _format_number(self, value: float) -> str:
        """Форматирование числа без дробной части, если это целое число"""
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)

    def _build_order_item_xml(self, item: OrderItem) -> str:
        """Построение XML для товара/услуги"""
        return f"""          <int:OrderItem>
            <int:Service>{item.service}</int:Service>
            <int:ItemName>{item.item_name}</int:ItemName>
            <int:ItemId>{item.item_id}</int:ItemId>
            <int:Quantity>{item.quantity}</int:Quantity>
            <int:Price>{self._format_number(item.price)}</int:Price>
            <int:Sum>{self._format_number(item.sum)}</int:Sum>
          </int:OrderItem>"""

    def _build_client_xml(self, client: Client) -> str:
        """Построение XML для клиента"""
        client_xml = "      <res:Client>\n"
        if client.room:
            client_xml += f"        <int:Room>{client.room}</int:Room>\n"
        if client.card:
            client_xml += f"        <int:Card>{client.card}</int:Card>\n"
        client_xml += "      </res:Client>"
        return client_xml

    def _build_soap_envelope(
            self,
            client: Client,
            order: Order,
            pos: str
    ) -> str:
        """Построение SOAP конверта для запроса"""
        items_xml = '\n'.join(
            self._build_order_item_xml(item) for item in order.items
        )

        order_date_str = order.order_date.isoformat()
        client_xml = self._build_client_xml(client)

        soap_body = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
  <soap:Body>
    <res:WritePOSOrder
        xmlns:res="http://www.1chotel.ru/ws/interfaces/restaurant/"
        xmlns:int="http://www.1chotel.ru/interfaces/restaurant/">
{client_xml}

      <res:Order>
        <int:OrderID>{order.order_id}</int:OrderID>
        <int:OrderDate>{order_date_str}</int:OrderDate>
        <int:Sum>{self._format_number(order.sum)}</int:Sum>
        <int:Quantity>{order.quantity}</int:Quantity>
        <int:Currency>{order.currency}</int:Currency>

        <int:OrderItems>
{items_xml}
        </int:OrderItems>

      </res:Order>

      <res:Source>
        <int:ExternalSystemCode>{self.token}</int:ExternalSystemCode>
        <int:POS>{pos}</int:POS>
      </res:Source>

    </res:WritePOSOrder>
  </soap:Body>
</soap:Envelope>"""

        return soap_body

    async def send_order(
            self,
            client: Client,
            order: Order,
            pos: str,
            debug: bool = False
    ) -> SOAPResponse:
        """
        Асинхронная отправка заказа через SOAP

        Args:
            client: Объект клиента (комната или карта)
            order: Объект заказа
            pos: Идентификатор POS терминала
            debug: Выводить ли отладочную информацию

        Returns:
            SOAPResponse с результатом запроса
        """
        if not client.room and not client.card:
            return SOAPResponse(
                success=False,
                status_code=400,
                raw_content='',
                error='Client must have either room or card'
            )

        if not self.client:
            raise RuntimeError('Client not initialized. Use async with HotelSOAPClient(...)')

        try:
            soap_envelope = self._build_soap_envelope(client, order, pos)

            if debug:
                print("=== SOAP ENVELOPE ===")
                print(soap_envelope)
                print("=== END ENVELOPE ===\n")

            headers = {
                'Content-Type': 'text/xml; charset=utf-8',
                'SOAPAction': 'http://www.1chotel.ru/ws/interfaces/restaurant/WritePOSOrder'
            }

            response = await self.client.post(
                self.base_url,
                content=soap_envelope,
                headers=headers
            )

            return await self._parse_response(response)

        except httpx.RequestError as e:
            return SOAPResponse(
                success=False,
                status_code=0,
                raw_content='',
                error=f'Request failed: {str(e)}'
            )

    async def _parse_response(self, response: httpx.Response) -> SOAPResponse:
        """
        Асинхронный парсинг ответа от сервера

        Args:
            response: Response объект от httpx

        Returns:
            SOAPResponse с результатом
        """
        raw_content = response.text
        result_data = {
            'success': False,
            'status_code': response.status_code,
            'raw_content': raw_content
        }

        # Если статус код не 200, обычно это ошибка
        if response.status_code != 200:
            result_data['error'] = f'HTTP {response.status_code}: {raw_content[:1000]}'
            return SOAPResponse(**result_data)

        try:
            # Регистрируем namespace для правильного парсинга
            for prefix, uri in self.NAMESPACES.items():
                ET.register_namespace(prefix, uri)

            root = ET.fromstring(response.content)

            # Проверяем наличие ошибок в SOAP ответе
            fault = root.find('.//soap:Fault', self.NAMESPACES)
            if fault is not None:
                result_data['error'] = self._parse_fault(fault)
                return SOAPResponse(**result_data)

            # Ищем элемент ответа
            body = root.find('.//soap:Body', self.NAMESPACES)
            if body is not None:
                result_data['success'] = True
                result_data['response_body'] = ET.tostring(body, encoding='unicode')
                result_data['data'] = self._extract_response_data(body)

        except ET.ParseError as e:
            result_data['error'] = f'XML parse error: {str(e)}\nResponse: {raw_content[:1000]}'

        return SOAPResponse(**result_data)

    def _parse_fault(self, fault: ET.Element) -> Dict[str, str]:
        """Парсинг SOAP ошибки"""
        fault_dict = {}
        for child in fault:
            tag = child.tag.split('}')[-1]
            fault_dict[tag] = child.text if child.text else ''
        return fault_dict

    def _extract_response_data(self, body: ET.Element) -> Optional[Dict[str, Any]]:
        """Попытка извлечения данных из ответа"""
        try:
            data = {}
            for elem in body.iter():
                tag = elem.tag.split('}')[-1]
                if elem.text and elem.text.strip():
                    text = elem.text.strip()
                    # Обработка даты 0001-01-01 (пустое значение в 1C)
                    if tag == 'Date' and text == '0001-01-01T00:00:00':
                        text = None
                    data[tag] = text
            return data if data else None
        except Exception:
            return None

    def _build_guest_payment_xml(
            self,
            room: Optional[str] = None,
            card: Optional[str] = None,
            folio_number: Optional[str] = None,
            payer_name: Optional[str] = None,
            payment_method: str = 'Наличные',
            currency: str = '643',
            sum_: float = 0.0,
            remarks: Optional[str] = None,
            hotel: str = 'Отель ОБЛАКО',
            pos_code: str = 'RESTR',
    ) -> str:
        """Построение SOAP конверта для WriteGuestPaymentExt"""
        sum_str = self._format_number(sum_)
        room_xml = f"<res:Room>{room}</res:Room>" if room else '<res:Room xsi:nil="true"/>'
        card_xml = f"<res:Card>{card}</res:Card>" if card else '<res:Card xsi:nil="true"/>'
        folio_xml = f"<res:FolioNumber>{folio_number}</res:FolioNumber>" if folio_number else '<res:FolioNumber xsi:nil="true"/>'
        payer_xml = f"<res:PayerName>{payer_name}</res:PayerName>" if payer_name else '<res:PayerName/>'
        remarks_xml = f"<res:Remarks>{remarks}</res:Remarks>" if remarks else '<res:Remarks/>'

        soap_envelope = f"""<?xml version="1.0" encoding="utf-8"?>
<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope"
               xmlns:res="http://www.1chotel.ru/ws/interfaces/restaurant/"
               xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <soap:Header/>
  <soap:Body>
    <res:WriteGuestPaymentExt>
      {payer_xml}
      {card_xml}
      {folio_xml}
      {room_xml}
      <res:PaymentMethod>{payment_method}</res:PaymentMethod>
      <res:Currency>{currency}</res:Currency>
      <res:Sum>{sum_str}</res:Sum>
      <res:ExternalSystemCode>{self.token}</res:ExternalSystemCode>
      <res:PaymentExternalCode xsi:nil="true"/>
      {remarks_xml}
      <res:Hotel>{hotel}</res:Hotel>
      <res:POSCode>{pos_code}</res:POSCode>
      <res:PaymentSection xsi:nil="true"/>
      <res:ReferenceNumber xsi:nil="true"/>
      <res:AuthorizationCode xsi:nil="true"/>
      <res:ExternalPaymentData xsi:nil="true"/>
    </res:WriteGuestPaymentExt>
  </soap:Body>
</soap:Envelope>"""
        return soap_envelope

    async def send_guest_payment(
            self,
            room: Optional[str] = None,
            card: Optional[str] = None,
            folio_number: Optional[str] = None,
            payer_name: Optional[str] = None,
            payment_method: str = 'Наличные',
            currency: str = '643',
            sum_: float = 0.0,
            remarks: Optional[str] = None,
            hotel: str = 'Отель ОБЛАКО',
            pos_code: str = 'RESTR',
            debug: bool = False
    ) -> SOAPResponse:
        """Отправка платежа гостя через WriteGuestPaymentExt"""
        if not room and not card and not folio_number:
            return SOAPResponse(
                success=False,
                status_code=400,
                raw_content='',
                error='At least one of room, card or folio_number must be provided'
            )

        if not self.client:
            raise RuntimeError('Client not initialized. Use async with HotelSOAPClient(...)')

        try:
            soap_envelope = self._build_guest_payment_xml(
                room=room,
                card=card,
                folio_number=folio_number,
                payer_name=payer_name,
                payment_method=payment_method,
                currency=currency,
                sum_=sum_,
                remarks=remarks,
                hotel=hotel,
                pos_code=pos_code
            )

            if debug:
                print("=== SOAP GUEST PAYMENT ENVELOPE ===")
                print(soap_envelope)
                print("=== END ENVELOPE ===\n")

            headers = {
                'Content-Type': 'application/soap+xml; charset=utf-8',
                'SOAPAction': 'http://www.1chotel.ru/ws/interfaces/restaurant/WriteGuestPaymentExt'
            }

            response = await self.client.post(
                self.base_url,
                content=soap_envelope,
                headers=headers
            )

            return await self._parse_response(response)

        except httpx.RequestError as e:
            return SOAPResponse(
                success=False,
                status_code=0,
                raw_content='',
                error=f'Request failed: {str(e)}'
            )


# Пример использования
async def main():
    # Создаем товар/услугу
    order_item = OrderItem(
        service='901',
        item_name='Уборка',
        item_id=str(uuid4()),
        quantity=1,
        price=100.0,
        sum=100
    )

    # Создаем заказ
    order = Order(
        order_id=str(uuid4()),
        order_date=datetime(2025, 9, 9, 10, 0, 0),
        sum=100,
        quantity=1,
        currency='643',
        items=[order_item]
    )

    # Создаем клиента (указываем комнату)
    client = Client(room='21')

    # Используем асинхронный клиент для тестовой среды
    async with HotelSOAPClient.test_environment() as hotel_client:
        # Отправляем заказ
        result = await hotel_client.send_order(
            client=client,
            order=order,
            pos='BAR-1',
            debug=True
        )

        # Выводим результат
        print(f'Success: {result.success}')
        print(f'Status Code: {result.status_code}')
        if result.error:
            print(f'Error: {result.error}')
        if result.data:
            print(f'Data: {result.data}')
        if result.response_body:
            print(f'Response Body: {result.response_body[:500]}')

    async with HotelSOAPClient.test_environment() as client:
        result = await client.send_guest_payment(
            room='25',
            sum_=100,
            remarks='Платеж для погашения кредита',
            debug=True
        )
        print(result.success, result.status_code, result.error)


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())