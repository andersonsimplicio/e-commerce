import json
from decimal import Decimal
from django.test import TestCase, Client
from apps.store.models import Produto

class ProdutoAPITestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = "/api/produtos/"
        self.produto = Produto.objects.create(
            nome="Mouse Gamer",
            descricao="Mouse óptico 16000 DPI",
            preco=Decimal("150.00")
        )

        return super().setUp()

    def test_listar_produtos_sucesso(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code,200)
        dados = response.json()
        self.assertEqual(len(dados), 1)
        self.assertEqual(dados[0]["nome"], "Mouse Gamer")
        self.assertEqual(Decimal(dados[0]["preco"]), Decimal("150.00"))

    def test_cria_produto(self):
        produto = {
            "nome": "Headset Gamer",
            "descricao": "Vou te ouvir no COD",
            "preco": "320.50"
        }

        response = self.client.post(
            self.url,
            data=json.dumps(produto),
            content_type="application/json"
        )
        dados = response.json()
        self.assertIn('id', dados)
        self.assertEqual(dados["nome"], "Headset Gamer")
        self.assertEqual(Decimal(dados["preco"]), Decimal("320.50"))
        self.assertTrue(Produto.objects.filter(nome="Headset Gamer").exists())

    def test_obter_produto_id(self):
        url_detalhe = f"{self.url}{self.produto.id}/"
        response = self.client.get(url_detalhe)
        self.assertEqual(response.status_code, 200)

        dados = response.json()
        self.assertEqual(dados["id"], self.produto.id)
        self.assertEqual(dados["nome"], "Mouse Gamer")
        self.assertEqual(Decimal(dados["preco"]), Decimal("150.00"))

    def test_obter_produto_inexistente(self):
        url_inexistente = f"{self.url}99999/"
        response = self.client.get(url_inexistente)
        self.assertEqual(response.status_code, 404)

    def test_update_produto_sucesso(self):
        url_detalhe = f"{self.url}{self.produto.id}/"
        payload_atualizado = {
            "nome": "Mouse Gamer RGB",
            "descricao": "Mouse óptico atualizado para 20000 DPI",
            "preco": "189.90"
        }

        response = self.client.put(
            url_detalhe,
            data=json.dumps(payload_atualizado),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)
        dados = response.json()
        self.assertEqual(dados["id"], self.produto.id)
        self.assertEqual(dados["nome"], "Mouse Gamer RGB")
        self.assertEqual(Decimal(dados["preco"]), Decimal("189.90"))
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, "Mouse Gamer RGB")
        self.assertEqual(self.produto.preco, Decimal("189.90"))

    def test_update_produto_not_found(self):
        url_inexistente = f"{self.url}99999/"
        payload = {
            "nome": "Inexistente",
            "descricao": "Sem descricao",
            "preco": "50.00"
        }

        response = self.client.put(
            url_inexistente,
            data=json.dumps(payload),
            content_type="application/json"
        )

        self.assertEqual(response.status_code, 404)

    def test_delete_produto(self):
        url_detalhe = f"{self.url}{self.produto.id}/"  
        response = self.client.delete(url_detalhe)
        self.assertEqual(response.status_code, 200)
        dados = response.json()
        self.assertEqual(dados, {"sucesso": True})
        self.assertFalse(Produto.objects.filter(id=self.produto.id).exists())

    def test_deletar_produto_inexistente(self):
        url_inexistente = f"{self.url}99999/"
        response = self.client.delete(url_inexistente)
        self.assertEqual(response.status_code, 404)
