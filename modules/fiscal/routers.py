from api.router_factory import RouterFactory

from modules.fiscal.routes.cash_routes import CASH_ROUTES
from modules.fiscal.routes.shift_routes import SHIFT_ROUTES
from modules.fiscal.routes.receipt_routes import RECEIPT_ROUTES
from modules.fiscal.routes.query_routes import QUERY_ROUTES
from modules.fiscal.routes.print_routes import PRINT_ROUTES
from modules.fiscal.routes.operator_routes import OPERATOR_ROUTES
from modules.fiscal.routes.connection_routes import CONNECTION_ROUTES
from modules.fiscal.routes.config_routes import CONFIG_ROUTES
from modules.fiscal.routes.read_routes import READ_ROUTES
from modules.fiscal.routes.cashier_routes import CASHIER_ROUTES


routers = list()

routers.append(RouterFactory(
    prefix='/cash',
    tags=['Cash Operations'],
    routes=CASH_ROUTES,
))
routers.append(RouterFactory(
    prefix='/shift',
    tags=['Shift'],
    routes=SHIFT_ROUTES,
))
routers.append(RouterFactory(
    prefix='/receipt',
    tags=['Receipt'],
    routes=RECEIPT_ROUTES,
))
routers.append(RouterFactory(
    prefix='/query',
    tags=['Device Information Query'],
    routes=QUERY_ROUTES,
))
routers.append(RouterFactory(
    prefix='/print',
    tags=['Non-Fiscal Printing'],
    routes=PRINT_ROUTES,
))
routers.append(RouterFactory(
    prefix='/operator',
    tags=['Operator & Document Operations'],
    routes=OPERATOR_ROUTES,
))
routers.append(RouterFactory(
    prefix='/connection',
    tags=['Connection'],
    routes=CONNECTION_ROUTES,
))
routers.append(RouterFactory(
    prefix='/config',
    tags=['Configuration & Logging'],
    routes=CONFIG_ROUTES,
))
routers.append(RouterFactory(
    prefix='/read',
    tags=['Read Records (FN & KKT Data)'],
    routes=READ_ROUTES,
))
routers.append(RouterFactory(
    prefix='/cashier',
    tags=['Cashier Management'],
    routes=CASHIER_ROUTES,
))
