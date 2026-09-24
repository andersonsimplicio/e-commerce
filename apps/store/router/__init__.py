from ninja import Router
from apps.store.router.produtos_router import produtos_router
from apps.store.router.ordem_router import ordem_router

__all__ = ["ordem_router", "produtos_router"]