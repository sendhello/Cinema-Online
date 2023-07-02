from async_fastapi_jwt_auth import AuthJWT
from async_fastapi_jwt_auth.exceptions import AuthJWTException
from db.redis_db import get_redis
from fastapi import Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials
from fastapi.security.http import HTTPBearer
from redis.asyncio import Redis
from starlette import status


async def full_protected(
    authorize: AuthJWT = Depends(),
    redis: Redis = Depends(get_redis),
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))
) -> AuthJWT:
    try:
        await authorize.jwt_required()

    except AuthJWTException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

    access_key = await authorize.get_jwt_subject()
    blocked_access_tokens = await redis.smembers(access_key)
    if not blocked_access_tokens:
        return authorize

    current_access_token = credentials.credentials
    if current_access_token not in blocked_access_tokens:
        return authorize

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Signature has blocked')


async def partial_protected(
    authorize: AuthJWT = Depends(),
    redis: Redis = Depends(get_redis),
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> AuthJWT:
    try:
        await authorize.jwt_optional()

    except AuthJWTException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e))

    access_key = await authorize.get_jwt_subject()
    if access_key is None:
        return authorize

    blocked_access_tokens = await redis.smembers(access_key)
    if not blocked_access_tokens:
        return authorize

    current_access_token = credentials.credentials
    if current_access_token not in blocked_access_tokens:
        return authorize

    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Signature has blocked')


async def refresh_protected(
    authorize: AuthJWT = Depends(),
    redis: Redis = Depends(get_redis),
    credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
) -> AuthJWT:
    try:
        await authorize.jwt_refresh_token_required()
    except AuthJWTException as e:
        raise HTTPException(status_code=e.status_code, detail=e.message)

    current_refresh_token = credentials.credentials
    refresh_key = await authorize.get_jwt_subject()
    active_refresh_token = await redis.get(name=refresh_key)
    if current_refresh_token == active_refresh_token:
        return authorize

    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail='Signature has blocked',
    )
