def parse_kkt_report(text: str) -> dict:
    result = {}
    lines = text.strip().splitlines()
    current_product = {}
    section_stack = []
    products = []
    in_product_section = False

    def set_nested_field(container: dict, path: list[str], key: str, value: str):
        """Устанавливает значение по вложенному пути."""
        for section in path:
            container = container.setdefault(section, {})
        container[key] = value

    for line in lines:
        line = line.rstrip()
        stripped = line.lstrip()
        indent = len(line) - len(stripped)

        if not stripped:
            continue

        # Начало секции товаров
        if stripped == "ПРЕДМ. РАСЧЕТА":
            if current_product:
                products.append(current_product)
                current_product = {}
            in_product_section = True
            section_stack = []
            continue

        # Выход из товарной секции
        if in_product_section and indent == 0 and not stripped.startswith(("НАИМЕН. ПРЕДМ. РАСЧЕТА", "ЦЕНА ЗА ЕД. ПРЕДМ. РАСЧ.", "КОЛ-ВО ПРЕДМ. РАСЧЕТА", "МЕРА КОЛ-ВА ПРЕДМ. РАСЧ.", "СТОИМ. ПРЕДМ. РАСЧЕТА", "СТАВКА НДС", "ПРИЗН. СПОСОБА РАСЧ.", "ПРИЗН. ПРЕДМЕТА РАСЧ.")):
            if current_product:
                products.append(current_product)
                current_product = {}
            in_product_section = False
            section_stack = []

        # Вложенная секция (например, "КТ" или "ОТРАСЛ. РЕКВ. ПРЕДМ. РАСЧ.")
        if in_product_section and indent > 0 and ":" not in stripped:
            section_stack.append(stripped)
            continue

        # Вложенное значение
        if in_product_section and indent > 0 and ":" in stripped:
            key, value = stripped.split(":", 1)
            set_nested_field(current_product, section_stack, key.strip(), value.strip())
            continue

        # Основные поля товара
        if in_product_section and indent == 0 and ":" in stripped:
            key, value = stripped.split(":", 1)
            current_product[key.strip()] = value.strip()
            section_stack = []
            continue

        # Общие поля (вне товарной секции)
        if not in_product_section and ":" in stripped:
            key, value = stripped.split(":", 1)
            result[key.strip()] = value.strip()
        else:
            result["ЗАГОЛОВОК"] = result.get("ЗАГОЛОВОК", "") + " " + stripped

    # Последний товар
    if current_product:
        products.append(current_product)

    if products:
        result["ПРЕДМЕТЫ РАСЧЕТА"] = products

    return result


def decode_km_server_checking_status(status_value):
    """
    Расшифровывает значение KMServerCheckingStatus (тег 2106)

    Args:
        status_value: значение статуса (int или -1 если ошибка)

    Returns:
        str: расшифрованное значение статуса
    """

    if status_value == -1:
        return "❌ Сервер ответил с ошибкой - проверка не выполнена"

    # Словарь для расшифровки статусов
    status_map = {
        0b00000000: "🔍 Проверка КП КМ не выполнена, статус товара ОИСМ не проверен",
        0b00000001: "❌ Проверка КП КМ выполнена в ФН с отрицательным результатом, статус товара ОИСМ не проверен",
        0b00000011: "✅ Проверка КП КМ выполнена с положительным результатом, статус товара ОИСМ не проверен",
        0b00010000: "🔍 Проверка КП КМ не выполнена, статус товара ОИСМ не проверен (ККТ в автономном режиме)",
        0b00010001: "❌ Проверка КП КМ выполнена в ФН с отрицательным результатом, статус товара ОИСМ не проверен (ККТ в автономном режиме)",
        0b00010011: "✅ Проверка КП КМ выполнена с положительным результатом, статус товара ОИСМ не проверен (ККТ в автономном режиме)",
        0b00000101: "❌ Проверка КП КМ выполнена с отрицательным результатом, статус товара у ОИСМ корректен",
        0b00000111: "✅ Проверка КП КМ выполнена с положительным результатом, статус товара у ОИСМ корректен"
    }

    # Проверяем точное соответствие
    if status_value in status_map:
        return status_map[status_value]

    # Если точного соответствия нет, анализируем биты
    result = f"Неизвестный статус: {status_value} (0b{status_value:08b})\n"

    # Анализируем отдельные биты
    km_check_bits = status_value & 0b00000011  # биты 0-1
    autonomous_bit = status_value & 0b00010000  # бит 4
    oism_status_bit = status_value & 0b00000100  # бит 2

    # Проверка КП КМ
    if km_check_bits == 0b00:
        result += "- Проверка КП КМ не выполнена\n"
    elif km_check_bits == 0b01:
        result += "- Проверка КП КМ выполнена с отрицательным результатом\n"
    elif km_check_bits == 0b11:
        result += "- Проверка КП КМ выполнена с положительным результатом\n"

    # Автономный режим
    if autonomous_bit:
        result += "- ККТ функционирует в автономном режиме\n"

    # Статус ОИСМ
    if oism_status_bit:
        result += "- Статус товара у ОИСМ корректен\n"
    else:
        result += "- Статус товара ОИСМ не проверен\n"

    return result.strip()


def print_km_status(driver):
    """
    Выводит расшифрованный статус KMServerCheckingStatus

    Args:
        driver: объект драйвера с атрибутом KMServerCheckingStatus
    """
    status = driver.driver.KMServerCheckingStatus
    decoded_status = decode_km_server_checking_status(status)

    print(f"KMServerCheckingStatus: {status}")
    print(f"Расшифровка: {decoded_status}")
    print("-" * 50)
