from ninja import Router
from apps.store.models import Produto
from apps.store.schemas import ProdutoSchema,ProdutoCriadoSchema
from typing import List
from django.shortcuts import get_object_or_404


produtos_router = Router(tags=["Produtos"])


@produtos_router.get("/", response=List[ProdutoSchema])
def lista_produto(request):
    return Produto.objects.all()

@produtos_router.post("/", response=ProdutoSchema)
def cria_produto(request, payload: ProdutoCriadoSchema):
    produto = Produto.objects.create(**payload.dict())
    return produto


@produtos_router.get("/{produto_id}/",response=ProdutoSchema)
def obter_produto(request,produto_id):
    produto = get_object_or_404(Produto,id=produto_id)
    return produto

@produtos_router.put("/{produto_id}/", response=ProdutoSchema)
def atualizar_produto(request, produto_id: int, payload: ProdutoCriadoSchema):
    produto = get_object_or_404(Produto, id=produto_id)
    
    for attr, value in payload.dict().items():
        setattr(produto, attr, value)   
    produto.save()

    return produto

@produtos_router.delete("/{produto_id}/")
def deletar_produto(request,produto_id:int):
    produto = get_object_or_404(Produto,id=produto_id)
    produto.delete()
    return {"sucesso": True}