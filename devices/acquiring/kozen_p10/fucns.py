import re


def read_and_save_check(source_file, dest_file):
    """Чтение файла чека и сохранение в целевой файл"""
    try:
        with open(source_file, 'r', encoding='KOI8-R') as f:
            content = f.readlines()
        with open(dest_file, 'a', encoding='utf-8') as f:
            f.writelines(content)
        return content
    except Exception as e:
        print(f"Ошибка при работе с файлами: {e}")
        return []


def extract_rrn(lines: list[str]) -> str | None:
    for line in lines:
        match = re.search(r'RRN:\s*(\d+)', line)
        if match:
            return match.group(1)
    return None
