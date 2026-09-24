from datetime import datetime,timedelta,timezone
import jwt
from django.conf import settings
from ninja.security import HttpBearer
from django.contrib.auth import get_user_model


User = get_user_model()

def create_jwt_token(user:User):
    """Gera um token JWT com tempo de expiração em UTC."""
    expiracao = datetime.now(timezone.utc) + timedelta(
        seconds=settings.JWT_EXPIRATION_SECONDS
    )
    payload = {
        "user_id": str(user.id),
        "username": user.username,
        "exp": expiracao,
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)

def decode_jwt_token(token:str):
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

class AuthBearer(HttpBearer):
    """Intercepta o header Authorization: Bearer <token> e recupera o usuário autenticado."""
    
    def authenticate(self, request, token):
        payload = decode_jwt_token(token)
        if not payload:
            return None

        user_id = payload.get("user_id")
        return User.objects.filter(id=user_id).first()