from ninja import Router

ordem_router = Router(tags=["Ordens"])

@ordem_router.get("/")
def listar_ordens(request):
    return {"mensagem": "Lista de ordens"}