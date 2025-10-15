from api.router_factory import RouterFactory
from modules.hotel.routes.fines_routes import FINES_ROUTES
from modules.hotel.routes.services_routes import SERVICES_ROUTES
from modules.hotel.routes.transactions_routes import TRANSACTIONS_ROUTES


routers = list()

routers.append(RouterFactory(
    prefix='/api/v1/transactions',
    tags=['Транзакции'],
    routes=TRANSACTIONS_ROUTES,
))
routers.append(RouterFactory(
    prefix='/api/v1/services',
    tags=['Услуги'],
    routes=SERVICES_ROUTES,
))
routers.append(RouterFactory(
    prefix='/api/v1/fines',
    tags=['Штрафы'],
    routes=FINES_ROUTES,
))
