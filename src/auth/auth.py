from fastapi_users.authentication import CookieTransport, JWTStrategy, AuthenticationBackend

from src.config import JWT_SECRET_TOKEN

cookie_transport = CookieTransport(cookie_name='libraries', cookie_max_age=3600)


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=JWT_SECRET_TOKEN, lifetime_seconds=3600)

auth_backend = AuthenticationBackend(
    name = "library_back",
    transport = cookie_transport,
    get_strategy = get_jwt_strategy,
)