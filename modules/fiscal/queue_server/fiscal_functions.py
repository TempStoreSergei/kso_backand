from fiscal_driver import driver, fn
from configs import error_codes
from utils import parse_kkt_report, print_km_status


def connect():
    """Проверка подключения/подключение к ККТ."""
    if driver.check_connection():
        return {
            "success": True,
            "message": 'Подключение к ККТ уже установлено',
        }
    else:
        driver.connect()
        if not driver.check_connection():
            return {
                "success": False,
                "message": 'Ошибка подключения к ККТ',
            }
        return {
            "success": True,
            "message": 'Успешное подключение к ККТ',
        }


def open_shift():
    """Открытие смены."""
    fn.connect()
    fn.get_fn_status()
    if fn.read_fn_status().get('FNSessionState') == 1:
        return {
            "success": True,
            "message": 'Смена уже открыта',
        }
    response = fn.open_shift()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при открытии смены: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Смена открыта успешно',
    }


def close_shift():
    """Закрытие смены."""
    fn.connect()
    fn.get_fn_status()
    if fn.read_fn_status().get('FNSessionState') == 0:
        return {
            "success": True,
            "message": 'Смена уже закрыта',
        }
    response = fn.close_shift()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при закрытии смены: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Смена закрыта успешно',
    }


def get_fiscal_document(document_number: int):
    """Получение фискального документа."""
    fn.connect()
    response = fn.get_fiscal_document(document_number)
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при получении документа: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    document_str = fn.read_current_fiscal_document()
    return {
        "success": True,
        "message": 'Документ получен успешно',
        "data": parse_kkt_report(document_str),
    }


def reset_ecr():
    """Сброс состояния ККТ."""
    driver.connect()
    response = driver.reset_ecr()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при сбросе состояния ККМ: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Состояние ККМ сброшено успешно',
    }


def cancel_check():
    """Отмена чека."""
    fn.connect()
    response = fn.cancel_check()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при отмене чека: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Чек успешно отменен',
    }


def get_fn_status():
    """Получение статуса ФН."""
    fn.connect()
    response = fn.get_fn_status()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при получении статуса ФН: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Статус ФН получен успешно',
        "data": fn.read_fn_status()
    }


def get_ecr_status():
    """Получение статуса ККТ."""
    driver.connect()
    response = driver.get_ecr_status()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при получении статуса ККТ: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Статус ККТ получен успешно',
        "data": driver.read_ecr_status()
    }


def create_check_after_payment(
    items: list[dict],
    is_printing: bool,
    payment_method: int,
    summ_total: int,
    advance_payment: int,
):
    """Создание фискального чека после оплаты товаров."""
    fn.connect()
    driver.connect()

    # открываем чек
    response = fn.open_check(0)
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при открытии чека: {error_codes.get(response, "Неизвестная ошибка")}',
        }

    # регистрируем позиции
    sum_tax_value1 = 0
    sum_tax_value2 = 0
    TAX_MAP = {
        1: 0.2,
        2: 0.1,
    }
    for item in items:
        tax_value = 0
        if TAX_MAP.get(item.get('tax')) == 0.2:
            tax_value = int(item.get('price') * item.get('quantity') * 0.2)
            sum_tax_value1 += tax_value
        elif TAX_MAP.get(item.get('tax')) == 0.1:
            tax_value = int(item.get('price') * item.get('quantity') * 0.1)
            sum_tax_value2 += tax_value

        item_for_register = item.copy()
        item_for_register.pop('req_id', None)
        item_for_register.pop('req_timestamp', None)
        response = fn.register_item(**item_for_register, check_type=1, tax_value=tax_value)

        # if payment_method == 1:
        #     fn.set_new_tags(summ_total)

        if fair_mark := item.get('fair_mark'):
            check_fair_mark = fn.set_fair_mark(fair_mark)
            print_km_status(driver)

            if check_fair_mark != 0:
                fn.cancel_check()
                return {
                    "success": False,
                    "message": f'Ошибка при проверке честного знака: {error_codes.get(check_fair_mark, "Неизвестная ошибка")}',
                }
            elif driver.driver.KMServerCheckingStatus != 15:
                fn.cancel_check()
                return {
                    "success": False,
                    "message": f'Честный знак не прошел проверку',
                }

            # Устанавливаем теги после проверки ЧЗ
            fn.set_tags_for_mark(item.get('req_id'), item.get('req_timestamp'))

        if response != 0:
            fn.cancel_check()
            return {
                "success": False,
                "message": f'Ошибка при регистрации позиции: {error_codes.get(response, "Неизвестная ошибка")}',
            }

    driver.change_is_printing(is_printing)

    # закрываем чек
    response = fn.close_check(
        payment_method,
        summ_total,
        sum_tax_value1,
        sum_tax_value2,
        advance_payment,
    )
    if response != 0:
        fn.cancel_check()
        return {
            "success": False,
            "message": f'Ошибка при закрытии чека: {response} - {error_codes.get(response, "Неизвестная ошибка")}',
        }

    return {
        "success": True,
        "message": 'Чек создан успешно',
    }


def refund_check_by_fd(document_number: int, item_names: list[str] | None = None):
    """Создание чека на возврат по номеру документа или возврат части позиций документа."""
    driver.connect()
    fn.connect()

    # читаем документ
    response = fn.get_fiscal_document(document_number)
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при получении документа: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    document = parse_kkt_report(fn.read_current_fiscal_document())
    items = document.get('ПРЕДМЕТЫ РАСЧЕТА')

    # открываем чек
    response = fn.open_check(2)
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при открытии чека: {error_codes.get(response, "Неизвестная ошибка")}',
        }

    # регистрируем позиции
    TAX_MAP = {
        1: 0.2,
        2: 0.1,
    }
    TAX_TAG_MAP = {
        6: 0,
        5: 3,
        1: 1,
        2: 2,
    }
    sum_tax_value1 = 0
    sum_tax_value2 = 0
    for item in items:
        prepared_item = {
            'quantity': float(item.get('КОЛ-ВО ПРЕДМ. РАСЧЕТА').replace(',', '.')),
            'price': int(float(item.get('ЦЕНА ЗА ЕД. ПРЕДМ. РАСЧ.').replace(',', '.')) * 100),
            'tax': TAX_TAG_MAP.get(int(item.get('СТАВКА НДС'))),
            'name': item.get('НАИМЕН. ПРЕДМ. РАСЧЕТА'),
            # 'fair_mark': f'0104650167230503215ph.SS9k5qW*D' + chr(29) + '91EE10' + chr(29) + '92lX2OSKoVye4XdAPnOKn9AbQpDSTr0r7O2vrGeQP2Rzw='
        }

        tax_mapped = TAX_MAP.get(prepared_item.get('tax'), 0)
        tax_value = int(prepared_item.get('price') * prepared_item.get('quantity') * tax_mapped)
        if tax_mapped == 0.2:
            sum_tax_value1 += tax_value
        elif tax_mapped == 0.1:
            sum_tax_value2 += tax_value

        if item_names:
            if prepared_item.get('name') in item_names:
                response = fn.register_item(**prepared_item, check_type=2, tax_value=tax_value)
            else: continue
        else:
            response = fn.register_item(**prepared_item, check_type=2, tax_value=tax_value)

        # Добавление маркировки
        # fn.set_fair_mark(f'0104650167230503215ph.SS9k5qW*D' + chr(29) + '91EE10' + chr(29) + '92lX2OSKoVye4XdAPnOKn9AbQpDSTr0r7O2vrGeQP2Rzw=')
        # fn.set_tags_for_mark('f516115f-b456-4954-bb0d-e57f2f10c063', '123214352')

        if response != 0:
            fn.cancel_check()
            return {
                "success": False,
                "message": f'Ошибка при регистрации позиции: {error_codes.get(response, "Неизвестная ошибка")}',
            }

    # закрываем чек
    summ_total = None
    payment_method = None
    value = document.get('СУММА ПО ЧЕКУ НАЛ (БСО)').replace(',', '.')
    if value and float(value) > 0:
        summ_total = int(float(value) * 100)
        payment_method = 0
    else:
        value = document.get('СУММА ПО ЧЕКУ ЭЛЕКТРОННЫМИ(БСО)').replace(',', '.')
        if value and float(value) > 0:
            summ_total = int(float(value) * 100)
            payment_method = 1

    if payment_method is None:
        fn.cancel_check()
        return {
            "success": False,
            "message": 'Не удалось определить тип оплаты чека',
        }

    if summ_total is None:
        fn.cancel_check()
        return {
            "success": False,
            "message": 'Не удалось определить полную стоимость товаров',
        }

    driver.change_is_printing(True)
    advance_payment = int(float(document.get('СУММА ПО ЧЕКУ БСО ПРЕДОПЛ.', '0').replace(',', '.')) * 100)
    response = fn.close_check(
        payment_method,
        summ_total,
        sum_tax_value1,
        sum_tax_value2,
        advance_payment,
    )
    if response != 0:
        fn.cancel_check()
        return {
            "success": False,
            "message": f'Ошибка при закрытии чека: {response} - {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Отмена чека прошла успешно',
    }


def repeat_document():
    """Повторить и напечатать последний документ."""
    fn.connect()
    response = fn.repeat_document()
    if response != 0:
        fn.cancel_check()
        return {
            "success": False,
            "message": f'Ошибка при повторе последнего чека: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'Последний чек напечатан успешно',
    }


def get_last_document():
    """Получить последний созданный документ."""
    fn.connect()
    fn.get_fn_status()
    document_number = fn.read_fn_status().get('DocumentNumber')
    response = fn.get_fiscal_document(document_number)
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при чтении последнего документа: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    document = fn.read_current_fiscal_document()
    return {
        "success": True,
        "message": 'Последний документ прочитан успешно',
        "data": parse_kkt_report(document)
    }


def print_list_str(content: list[str]):
    """Печать не фискального чека сверки итогов пинпада."""
    driver.connect()
    for line in content:
        driver.print_string(line)
    for i in range(10):
        driver.print_string(' ')
    driver.cut_check()
    return {
        "success": True,
        "message": 'Сверка итогов распечатана успешно',
    }


def print_x_report():
    fn.connect()
    response = fn.print_x_report()
    if response != 0:
        return {
            "success": False,
            "message": f'Ошибка при печати x-отчета: {error_codes.get(response, "Неизвестная ошибка")}',
        }
    return {
        "success": True,
        "message": 'X-отчет напечатан успешно',
    }
