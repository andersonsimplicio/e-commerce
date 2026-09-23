from ninja import Router
from .produtos_router import produtos_router
from .ordem_router import ordem_router

__all__ = ["ordem_router", "produtos_router"]