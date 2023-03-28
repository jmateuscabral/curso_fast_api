from typing import List
from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:@localhost:5432/faculdade'

    DBBaseModel = declarative_base()

    """
    import secrets
    token: str = secrets.token_urlsafe(32)
    """
    JWT_SECRET: str = 'eAIozClf3otBH2Dp05tqWgiIqzGK_4tLTKFkP3Lz6zM  '
    ALGORITHM: str = 'HS256'

    # 50 Minutos * 24 Horas * 7 Dias == 1 Semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:

        case_sensitive = True


settings: Settings = Settings()
