from openpyxl import load_workbook

from modules.hotel.DTO.transactions.get_rooms_dto import GetRoomsResponseDTO


async def get_rooms():
    # Путь к файлу
    file_path = "modules/hotel/rooms.xlsx"  # замените на свой путь

    # Загружаем книгу
    wb = load_workbook(filename=file_path, data_only=True)

    # Функция для получения значений столбца C, кроме первой строки
    def get_column_c_values(sheet):
        return [cell.value for cell in sheet['C'][1:] if cell.value is not None]

    sheet1 = wb.worksheets[0]  # первая страница
    rooms1 = get_column_c_values(sheet1)

    sheet2 = wb.worksheets[1]
    rooms2 = get_column_c_values(sheet2)

    sheet3 = wb.worksheets[2]
    rooms3 = get_column_c_values(sheet3)

    return GetRoomsResponseDTO(
        rooms1=rooms1,
        rooms2=rooms2,
        rooms3=rooms3,
    )
