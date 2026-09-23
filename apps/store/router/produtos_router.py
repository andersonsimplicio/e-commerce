from ninja import Router
from apps.store.models import Produto
from apps.store.schemas import ProdutoSchema,ProdutoCriadoSchema
from typing import List

produtos_router = Router(tags=["Produtos"])


@produtos_router.get("/produtos", response=List[ProdutoSchema])
def lista_produto(request):
    return Produto.objects.all()

@produtos_router.post("/produtos", response=ProdutoSchema)
def cria_produto(request, payload: ProdutoCriadoSchema):
    produto = Produto.objects.create(**payload.dict())
    return produto