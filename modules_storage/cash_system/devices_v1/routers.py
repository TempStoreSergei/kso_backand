from api.router_factory import RouterFactory
from modules.cash_system.routes.bill_acceptor_routes import BILL_ACCEPTOR_ROUTES
from modules.cash_system.routes.bill_dispenser_routes import BILL_DISPENSER_ROUTES
from modules.cash_system.routes.cash_system_routes import CASH_SYSTEM_ROUTES
from modules.cash_system.routes.coin_system_routes import COIN_SYSTEM_ROUTES


routers = list()

routers.append(RouterFactory(
    prefix='/api/v1/cash_system',
    tags=['Наличная система оплаты'],
    routes=CASH_SYSTEM_ROUTES,
))
routers.append(RouterFactory(
    prefix='/api/v1/cash_system/bill_acceptor',
    tags=['Прием купюр'],
    routes=BILL_ACCEPTOR_ROUTES,
))
routers.append(RouterFactory(
    prefix='/api/v1/cash_system/bill_dispenser',
    tags=['Выдача купюр'],
    routes=BILL_DISPENSER_ROUTES,
))
routers.append(RouterFactory(
    prefix='/api/v1/cash_system/coin_system',
    tags=['Прием и выдача монет'],
    routes=COIN_SYSTEM_ROUTES,
))
