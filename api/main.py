from pathlib import Path
import importlib.util

from api.configs.app import app
from api.router_factory import RouterFactory
from api.routes.auth_routes import AUTH_ROUTES


routers = list()

routers.append(RouterFactory(prefix='/api/v1/auth', tags=['Аутентификация'], routes=AUTH_ROUTES))

# Ищем все routers.py внутри подпапок modules
for router_file in Path("modules").glob("*/routers.py"):
    module_name = f"modules.{router_file.parent.name}.routers"
    try:
        module = importlib.import_module(module_name)
        if hasattr(module, "routers"):
            module_routers = getattr(module, "routers")
            routers += module_routers
            print(f"✓ Добавлено {len(module_routers)} роутеров из {module_name}")
    except Exception as e:
        print(f"✗ Ошибка при загрузке {module_name}: {e}")
        continue

for router in routers:
    app.include_router(router())
