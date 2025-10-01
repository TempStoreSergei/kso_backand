from fucns import read_and_save_check, extract_rrn
from loggers import logger
from parser_res_check import parser
from send_to_ws import send_to_ws


class SBPilotAction():
    def __init__(self, command_id):
        self.command_id = command_id
        self.response = {
        "command_id": self.command_id,
        "success": False,
        "message": "",
        "data": None
    }

    def start_pay(self, stdout):
        if "return:0" in stdout:
            content = read_and_save_check('sc552_p12/p', 'logs/pay_checks.txt')
            rrn = extract_rrn(content)
            logger.info('Чек сохранен в файл pay_checks.txt')
            logger.info('Платеж завершен успешно')
            send_to_ws(event='successPayment', data={'rrn': rrn})
        else:
            error_msg = 'Ошибка при совершении платежа'
            logger.info(error_msg)
            send_to_ws(event='errorPayment', data={'error': error_msg})

        self.response.update({'success': True, 'message': 'Запрос отправлен успешно'})
        return self.response

    def refund_pay(self, stdout):
        if "return:0" in stdout:
            content = read_and_save_check('sc552_p12/p', 'logs/return_checks.txt')
            logger.info('Чек сохранен в файл return_checks.txt')
            self.response.update({
                "success": True,
                "message": "Возврат выполнен успешно",
                "data": {"check_content": ''.join(content), "type": "return"}
            })
        else:
            error_msg = 'Ошибка при возврате платежа'
            logger.info(error_msg)
            self.response.update({
                "success": False,
                "message": error_msg,
            })
        return self.response

    def receipt_report(self, stdout):
        if "return:0" in stdout:
            content = read_and_save_check('sc552_p12/p', 'logs/res_checks.txt')
            logger.info('Чек сохранен в файл res_checks.txt')

            # Собираем словарь с данными отчета
            receipt = parser.parse(''.join(content))
            receipt_dict = parser.to_dict(receipt)
            logger.info(receipt_dict)
            self.response.update({
                "success": True,
                "message": "Сверка итогов выполнена успешно",
                "data": {'receipt_dict': receipt_dict, 'receipt_lst_str': content}
            })
        else:
            error_msg = 'Ошибка при выполнении сверки итогов'
            logger.info(error_msg)
            self.response.update({
                "success": False,
                "message": error_msg,
            })
        return self.response

    def cancel_pay(self, stdout):
        if "return:0" in stdout:
            content = read_and_save_check('sc552_p12/p', 'logs/cancel_checks.txt')
            logger.info('Чек сохранен в файл cancel_checks.txt')
            self.response.update({
                "success": True,
                "message": "Отмена платежа выполнена успешно",
                "data": {"check_content": ''.join(content), "type": "cancel"}
            })
        else:
            error_msg = 'Ошибка при отмене платежа'
            logger.info(error_msg)

            self.response.update({
                "success": False,
                "message": error_msg,
            })
        return self.response

    def open_menu(self):
        return self.response.update({
            "success": True,
            "message": "Технологическое меню открыто успешно",
        })

    def check_connect(self, stdout):
        if "return:0" in stdout:
            self.response.update({
                "success": True,
                "message": "Устройство доступно",
            })
        else:
            self.response.update({
                "success": False,
                "message": "Устройство недоступно",
            })
        return self.response
