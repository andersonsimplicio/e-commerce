from datetime import datetime,timedelta,timezone
import jwt
from django.conf import settings
from django.contrib.auth.models import User


def create_jwt_token(user:User):
    """Gera um token JWT com tempo de expiração em UTC."""
    expiracao = datetime.now(timezone.utc) + timedelta(
       seconds=settings.JWT_EXPIRATION_SECONDS
    )
     
    payload = {
        "user_id": user.id,
        "username": user.username,
        "exp": expiracao,
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def decode_jwt_token(token: str) -> dict | None:
    """Valida a assinatura e expiração do token, retornando o payload ou None."""
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM]
        )
        return payload
    except jwt.PyJWTError:
        return None
    
def test_auth_bearer_com_token_invalido_retorna_none(self):
        bearer = AuthBearer()
        usuario = bearer.authenticate(request=None, token="token_invalido")

        self.assertIsNone(usuario)
    

    