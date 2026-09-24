from django.db import models
from django.conf import settings


class Produto(models.Model):
    nome =  models.CharField(max_length=100)
    descricao = models.TextField()
    preco =  models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)
    class Meta:
        app_label = 'store'
    
    def __str__(self):
        return f"Nome: {self.nome} "
    
class Ordem(models.Model):
    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="ordens",
    )
    produto = models.ManyToManyField(Produto, through="OrdemItem")
    total = models.DecimalField(max_digits=10,decimal_places=2)
    status = models.CharField(max_length=20, default='pendencia')
    criado_em = models.DateTimeField(auto_now_add=True)
    class Meta:
            app_label = 'store'
    def __str__(self):
        return f"Ordem #{self.id} - {self.usuario.username}"
    

class OrdemItem(models.Model):
    ordem = models.ForeignKey(Ordem, on_delete=models.CASCADE)
    produto =  models.ForeignKey(Produto,on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1)
    preco = models.DecimalField(max_digits=10,decimal_places=2)
    class Meta:
            app_label = 'store'
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome} (Ordem #{self.ordem.id})"