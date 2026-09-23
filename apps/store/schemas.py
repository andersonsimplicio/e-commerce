from ninja import Schema
from decimal import Decimal
from datetime import datetime

class ProdutoSchema(Schema):
    id:int
    nome:str
    descicao:str
    preco:Decimal
    quantidade:int 
   
    
class ProdutoCriadoSchema(Schema):
    id: int
    nome:str
    descicao:str
    preco:Decimal
    quantidade:int 
    
class OrdemItemScehma(Schema):
    produyto_id: int
    quantidade:int

class OrdemCriacaoScehma(Schema):
    items:list[OrdemItemScehma]
    
class OrdemScehma(Schema):
    id: int
    usuario_id: int
    total: Decimal
    status: str
    criado_em: datetime