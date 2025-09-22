from fastapi import APIRouter

from api.DTO.factories.router_factory import RouteDTO


class RouterFactory:
    def __init__(self, prefix: str, tags: list[str], routes: list[RouteDTO] | None = None):
        self.router = APIRouter(prefix=prefix, tags=tags)
        self.routes = routes
        if routes:
            self._setup_router()

    def _setup_router(self):
        for route in self.routes:
            self.router.add_api_route(
                path=route.path,
                endpoint=route.endpoint,
                response_model=route.response_model,
                status_code=route.status_code,
                methods=route.methods,
                summary=route.summary,
                description=route.description,
                responses=route.responses,
            )

    def __call__(self):
        return self.router