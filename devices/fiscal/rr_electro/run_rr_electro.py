import json

import redis

from configs import REDIS_HOST, REDIS_PORT
from fiscal_functions import *
from loggers import logger


def process_command(command_data):
    """Выполнение команды на основе полученной из pubsub"""
    response = {
        "command_id": command_data.get('command_id'),
        "success": False,
        "message": None,
        "data": None,
    }

    try:
        command = command_data.get('command')
        kwargs = command_data.get('kwargs')
        if command == 'connect':
            response.update(connect())
        elif command == 'open_shift':
            response.update(open_shift())
        elif command == 'close_shift':
            response.update(close_shift())
        elif command == 'get_fiscal_document':
            if not kwargs:
                response['success'] = False
                response['message'] = 'Ошибка. Не переданы аргументы для функции'
                return response
            response.update(get_fiscal_document(**kwargs))
        elif command == 'reset_ecr':
            response.update(reset_ecr())
        elif command == 'cancel_check':
            response.update(cancel_check())
        elif command == 'get_fn_status':
            response.update(get_fn_status())
        elif command == 'get_ecr_status':
            response.update(get_ecr_status())
        elif command == 'create_check_after_payment':
            if not kwargs:
                response['success'] = False
                response['message'] = 'Ошибка. Не переданы аргументы для функции'
                return response
            response.update(create_check_after_payment(**kwargs))
        elif command == 'refund_check_by_fd':
            if not kwargs:
                response['success'] = False
                response['message'] = 'Ошибка. Не переданы аргументы для функции'
                return response
            response.update(refund_check_by_fd(**kwargs))
        elif command == 'repeat_document':
            response.update(repeat_document())
        elif command == 'get_last_document':
            response.update(get_last_document())
        elif command == 'print_list_str':
            if not kwargs:
                response['success'] = False
                response['message'] = 'Ошибка. Не переданы аргументы для функции'
                return response
            response.update(print_list_str(**kwargs))
        elif command == 'print_x_report':
            response.update(print_x_report())

    except Exception as e:
        error_msg = f"Ошибка при выполнении команды: {str(e)}"
        logger.error(error_msg)
        response["message"] = error_msg

    return response


def listen_to_redis():
    """Подключение к Redis и обработка команд"""
    # Подключение к Redis
    r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
    pubsub = r.pubsub()

    channel = 'command_fr_channel'
    response_channel = f'{channel}_response'
    pubsub.subscribe(channel)
    logger.info("Ожидание команд...")

    # Слушаем канал и выполняем команды
    for message in pubsub.listen():
        if message.get('type') == 'message':
            # обработка пинга при проверке доступности канала
            if message.get('data') == 'ping':
                continue
            try:
                command_data = json.loads(message.get('data'))
                logger.info(f"Получена команда: {command_data}")

                response = process_command(command_data)

                r.publish(response_channel, json.dumps(response))
                logger.info(f"Ответ отправлен в канал {response_channel}: {response}")
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка парсинга команды: {e}")
            except Exception as e:
                logger.error(f"Неожиданная ошибка: {e}")


if __name__ == "__main__":
    listen_to_redis()
