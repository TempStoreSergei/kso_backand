from api.db.base_database_repository import BaseDatabaseRepository
from modules.hotel.models.models import Service


class ServiceDatabaseRepository(BaseDatabaseRepository):
    model_class = Service
