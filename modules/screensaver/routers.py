from api.router_factory import RouterFactory
from modules.screensaver.routes.screensaver_routes import SCREENSAVER_ROUTES

routers = list()

routers.append(RouterFactory(
    prefix='/api/v1/screensaver',
    tags=['Заставка'],
    routes=SCREENSAVER_ROUTES,
))
