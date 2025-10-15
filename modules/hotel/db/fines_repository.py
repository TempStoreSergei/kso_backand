from api.db.base_database_repository import BaseDatabaseRepository
from modules.hotel.models.models import Fine


class FineDatabaseRepository(BaseDatabaseRepository):
    model_class = Fine
