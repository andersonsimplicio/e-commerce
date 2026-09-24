from django.contrib.auth import get_user_model
from datetime import datetime, timedelta, timezone
from django.test import TestCase
import jwt
from core.security import create_jwt_token, decode_jwt_token,AuthBearer
from django.conf import settings



User = get_user_model()

class TestCaseJWT(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="anderson",
            email="anderson@example.com",
            password="senha_segura_123"
        )
        return super().setUp()

    def test_gerar_e_decodificar_token_com_sucesso(self):
        token = create_jwt_token(self.user)
        self.assertIsInstance(token,str)
        payload = decode_jwt_token(token)
        self.assertIsNotNone(payload)
        self.assertEqual(payload["user_id"], str(self.user.id))
        self.assertEqual(payload["username"], self.user.username)
        self.assertIn("exp", payload)
    
    def test_decodificar_token_invalido_retorna_none(self):
        token_forjado = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.invalido.assinatura"
        payload = decode_jwt_token(token_forjado)
        self.assertIsNone(payload)
    
    def test_decodificar_token_expirado_retorna_none(self):
        # Simula um token criado já no passado (expirado há 10 segundos)
        data_passada = datetime.now(timezone.utc) - timedelta(seconds=10)
        payload_expirado = {
            "user_id": str(self.user.id),
            "username": self.user.username,
            "exp": data_passada,
        }
        token_vencido = jwt.encode(
            payload_expirado,
            settings.JWT_SECRET,
            algorithm=settings.JWT_ALGORITHM
        )
        # A função deve retornar None
        resultado = decode_jwt_token(token_vencido)
        self.assertIsNone(resultado)
        
    def test_auth_bearer_com_token_valido_retorna_usuario(self):
        bearer = AuthBearer()
        token = create_jwt_token(self.user)

        # O Django Ninja passa o request e a string do token para authenticate
        usuario_autenticado = bearer.authenticate(request=None, token=token)

        self.assertIsNotNone(usuario_autenticado)
        self.assertEqual(usuario_autenticado.id, self.user.id)
        self.assertEqual(usuario_autenticado.username, self.user.username)