from ninja import Schema
from decimal import Decimal
from datetime import datetime
from uuid import UUID

class ProdutoSchema(Schema):
    id:int
    nome:str
    descricao:str
    preco:Decimal
   
    
class ProdutoCriadoSchema(Schema):
    nome:str
    descricao:str
    preco:Decimal
    
class OrdemItemScehma(Schema):
    produyto_id: int
    quantidade:int

class OrdemCriacaoScehma(Schema):
    items:list[OrdemItemScehma]
    
class OrdemScehma(Schema):
    id: int
    usuario_id: UUID
    total: Decimal
    status: str
    criado_em: datetime