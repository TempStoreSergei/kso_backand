import base64
import uuid
from io import BytesIO
from urllib.parse import urlparse

from minio import InvalidResponseError, Minio, S3Error
from minio.error import MinioException

from modules.screensaver.configs.settings import settings
from api.configs.loggers import logger


minio_client = Minio(
    endpoint=settings.MINIO_URL, access_key="minio", secret_key="minio123", secure=False
)


async def delete_file_from_minio(file_url: str):
    """Функция удаляет файл из файлового хранилища minio.

    Args:
        file_url(str): путь к файлу в minio
    """
    parsed_url = urlparse(file_url)

    # Извлекаем имя бакета и название файла (из пути URL)
    path_parts = parsed_url.path.lstrip("/").split("/", 1)
    if len(path_parts) < 2:
        logger.error("Некорректный URL: не удалось извлечь имя бакета и файла")
        return

    bucket_name, file_name = path_parts

    # Удаляем файл
    try:
        minio_client.remove_object(bucket_name, file_name)
        logger.info(f"Файл {file_name} удален из бакета {bucket_name}")
    except S3Error as e:
        logger.error(f"Объект не найден или проблема с доступом: {e}")
    except InvalidResponseError as e:
        logger.error(f"Сервер MinIO вернул неожиданный ответ: {e}")
    except MinioException as e:
        logger.error(f"Неизвестная базовая ошибка MinIO: {e}")
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")


async def upload_file_in_minio(file_base64: str, bucket_name: str):
    """Функция загружает файл в файловое хранилище minio.

    Args:
        file_base64(str): файл в формате base64 в виде строки
        bucket_name(str): название бакета в minio

    Return:
        ссылка на файл, тип файла
    """

    def get_file_type(base64_string: str):
        if "," in base64_string:  # Проверяем, есть ли заголовок
            header, _ = base64_string.split(",", 1)
            if ":" in header and ";" in header:
                return header.split(":")[1].split(";")[0]

    file_type = get_file_type(file_base64)
    if file_type:
        filename = f"{uuid.uuid4()}.{file_type.split('/')[1]}"

        # Декодируем Base64 строку обратно в бинарные данные
        decoded_file = base64.b64decode(file_base64.split(",")[1])

        # Преобразуем содержимое в BytesIO объект для передачи в MinIO
        data = BytesIO(decoded_file)

        # Проверяем, существует ли бакет, если нет - создаем
        if not minio_client.bucket_exists(bucket_name):
            minio_client.make_bucket(bucket_name)

        # Загружаем файл в MinIO
        minio_client.put_object(
            bucket_name, filename, data, len(decoded_file), content_type=file_type
        )
        return minio_client.presigned_get_object(bucket_name, filename), file_type.split("/")[0]
