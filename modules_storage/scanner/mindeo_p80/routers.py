from api.router_factory import RouterFactory
from modules.scanner.scanner_routes import SCANNER


routers = list()

routers.append(RouterFactory(
    prefix='/api/v1/scanner',
    tags=['Сканер'],
    routes=SCANNER,
))
