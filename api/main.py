from pathlib import Path
import importlib.util

from api.configs.app import app
from api.router_factory import RouterFactory
from api.routes.auth_routes import AUTH_ROUTES
from api.routes.notifications_routes import NOTIFICATIONS_ROUTES
from api.routes.system_routes import SYSTEM_ROUTES


routers = list()

routers.append(RouterFactory(prefix='/api/v1/auth', tags=['Аутентификация'], routes=AUTH_ROUTES))
routers.append(RouterFactory(prefix='/api/v1/notifications', tags=['Уведомления'], routes=NOTIFICATIONS_ROUTES))
routers.append(RouterFactory(prefix='/api/v1/system', tags=['Система'], routes=SYSTEM_ROUTES))

# Ищем все routers.py внутри подпапок modules
for router_file in Path("modules").glob("*/routers.py"):
    module_name = f"modules.{router_file.parent.name}.routers"
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "routers"):
            module_routers = getattr(module, "routers")
            routers += module_routers
            print(f"✓ Добавлены роутеры из модуля {module_name}")
    except Exception as e:
        print(f"✗ Ошибка при загрузке {module_name}: {e}")
        continue

for router in routers:
    app.include_router(router())
