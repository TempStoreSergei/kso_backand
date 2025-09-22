import asyncio
import shutil
from pathlib import Path

from api.configs.loggers import logger


async def set_and_run_modules_services():
    """Функция собирает файлы systemd сервисов из папок модулей и запускает их."""
    user_services_dir = Path.home() / '.config/systemd/user'
    modules_path = Path('modules')

    if not modules_path.exists():
        logger.info(f"Ошибка: папка {modules_path} не существует")
        return

    found_services = []
    # Ищем все файлы *.service в подпапках modules
    for subdir in modules_path.iterdir():
        if subdir.is_dir():
            service_files = list(subdir.glob("*.service"))

            for service_file in service_files:
                found_services.append(service_file)
                logger.info(f"Найден файл сервиса: {service_file}")

    if not found_services:
        logger.info("Сервисные файлы не найдены")
        return

    for service_file in found_services:
        service_name = service_file.name
        destination = user_services_dir / service_name

        if destination.exists():
            logger.info(f"Файл {destination} уже существует, копирование пропущено")
        else:
            logger.info(f"Копируем файл сервиса {service_name}")
            shutil.copy2(service_file, destination)

            proc = await asyncio.create_subprocess_exec(
                "systemctl", "--user", "daemon-reload",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()

            if proc.returncode != 0:
                raise RuntimeError(f"Ошибка daemon-reload: {stderr.decode()}")

        proc = await asyncio.create_subprocess_exec(
            "systemctl", "--user", "start", service_name,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await proc.communicate()

        if proc.returncode != 0:
            raise RuntimeError(f"Ошибка запуска: {stderr.decode()}")

        # Проверяем статус
        check_proc = await asyncio.create_subprocess_exec(
            "systemctl", "--user", "is-active", service_name,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        status_out, _ = await check_proc.communicate()

        status = status_out.decode().strip()
        if status == "active":
            logger.info(
                f'Сервис {service_name} запущен успешно')
        else:
            raise RuntimeError(f"Ошибка запуска, cервис не запущен")
