import asyncio
from pathlib import Path

from api.configs.loggers import logger


async def set_and_run_modules_services():
    """
    Функция собирает systemd сервисы из папок модулей и устанавливает их
    в /etc/systemd/system/ с последующим запуском через sudo.
    """
    services_dir = Path('/etc/systemd/system/')
    modules_path = Path('modules')

    if not modules_path.exists():
        logger.error(f"Ошибка: папка {modules_path} не существует")
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
        destination = services_dir / service_name

        # Копируем через sudo, если файла ещё нет
        if destination.exists():
            logger.info(f"Файл {destination} уже существует, копирование пропущено")
        else:
            logger.info(f"Копируем файл сервиса {service_name} в {destination}")
            proc = await asyncio.create_subprocess_exec(
                "sudo", "cp", str(service_file), str(destination),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc.communicate()
            if proc.returncode != 0:
                raise RuntimeError(f"Ошибка копирования: {stderr.decode()}")

            # Перезагрузка daemon systemd
            proc_reload = await asyncio.create_subprocess_exec(
                "sudo", "systemctl", "daemon-reload",
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc_reload.communicate()
            if proc_reload.returncode != 0:
                raise RuntimeError(f"Ошибка daemon-reload: {stderr.decode()}")

        # Проверяем, запущен ли сервис
        proc_status = await asyncio.create_subprocess_exec(
            "sudo", "systemctl", "is-active", service_name,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        status_out, _ = await proc_status.communicate()
        status = status_out.decode().strip()

        if status == "active":
            logger.info(f"Сервис {service_name} уже работает")
        else:
            # Запускаем только если он не активен
            logger.info(f"Запускаем сервис {service_name}")
            proc_start = await asyncio.create_subprocess_exec(
                "sudo", "systemctl", "start", service_name,
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE
            )
            stdout, stderr = await proc_start.communicate()
            if proc_start.returncode != 0:
                raise RuntimeError(f"Ошибка запуска сервиса {service_name}: {stderr.decode()}")

            logger.info(f"Сервис {service_name} успешно запущен")
