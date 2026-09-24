from ninja import NinjaAPI
from ninja import NinjaAPI
from apps.store.router import ordem_router, produtos_router


api = NinjaAPI(title="Ecommerce API")

api.add_router("/ordens", ordem_router)
api.add_router("/produtos", produtos_router)
