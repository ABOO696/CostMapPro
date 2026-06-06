from fastapi import FastAPI

from app.api.routers.stocks import (
    router as stock_router
)

from app.api.routers.radar import (
    router as radar_router
)

from app.api.routers.dashboard import (
    router as dashboard_router
)

from app.api.routers.costmap import (
    router as costmap_router
)

app = FastAPI(
    title="CostMap API"
)

app.include_router(
    stock_router
)

app.include_router(
    radar_router
)

app.include_router(
    dashboard_router
)

app.include_router(
    costmap_router
)