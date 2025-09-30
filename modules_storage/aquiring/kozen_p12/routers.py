from api.router_factory import RouterFactory
from modules.acquiring.routes.acquiring_routes import ACQUIRING


routers = list()

routers.append(RouterFactory(
    prefix='/api/v1/acquiring',
    tags=['Эквайринг'],
    routes=ACQUIRING,
))
