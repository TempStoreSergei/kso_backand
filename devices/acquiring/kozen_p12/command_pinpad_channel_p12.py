import subprocess

from loggers import logger
from sb_pilot_action import SBPilotAction


OPERATION_TYPE_MAP = {
    'start_pay': '1',
    'refund_pay': '3',
    'receipt_report': '7',
    'cancel_pay': '8',
    'open_menu': '11',
    'check_connect_old': '26',
    'check_connect': '36',
}
PATH_TO_SB_PILOT = './sc552_p12/sb_pilot'


async def command_pinpad_channel_p12(command):
    """Выполнение команды на основе полученной из pubsub"""
    command_id = command.get('command_id')
    response = {
        "command_id": command_id,
        "success": False,
        "message": "",
        "data": None
    }
    sb_pilot_action = SBPilotAction(command_id)

    try:
        # Получаем параметры процесса из команды
        command_name = command.get('command')
        command_num = OPERATION_TYPE_MAP.get(command_name)
        amount = command.get('data', {}).get('amount', None)
        # Запуск процесса
        if amount:
            result = subprocess.run([PATH_TO_SB_PILOT, command_num, amount], capture_output=True, text=True)
        else:
            result = subprocess.run([PATH_TO_SB_PILOT, command_num], capture_output=True, text=True)
        # Получаем стандартный вывод
        stdout = result.stdout
        logger.info(f"Output: {stdout}")

        if command_name == 'start_pay':  # Оплата
            response = sb_pilot_action.start_pay(stdout)

        elif command_name == "refund_pay":  # Возврат
            response = sb_pilot_action.refund_pay(stdout)

        elif command_name == "receipt_report":  # Сверка итогов
            response = sb_pilot_action.receipt_report(stdout)

        elif command_name == "cancel_pay":  # Отмена платежа
            response = sb_pilot_action.cancel_pay(stdout)

        elif command_name == "open_menu": # Открыть технологическое меню
            response = sb_pilot_action.open_menu()

        elif command_name in {"check_connect", "check_connect_old"}:  # Проверка подключения
            response = sb_pilot_action.check_connect(stdout)

        else:
            # Неизвестный тип операции
            response.update({
                "success": False,
                "message": "Неизвестный тип операции",
                "data": {"stdout": stdout, "type": "unknown"}
            })

    except Exception as e:
        error_msg = f"Ошибка при выполнении команды: {str(e)}"
        logger.info(error_msg)
        response.update({
            "success": False,
            "message": error_msg,
            "data": {"error": str(e)}
        })

    return response
