from functools import lru_cache
from typing import Literal, Any, Dict, Optional

from pydantic.v1 import BaseSettings
from pydantic.v1.env_settings import DotenvType
from pydantic.v1.typing import StrPath


class Settings(BaseSettings):

    # Environment
    APPS_ENV: Literal['local', 'dev', 'qa', 'prod'] = 'dev'

    APP_NAME: str = 'FastAPI'
    APP_BASE_DOMAIN: str

    DEBUG: bool

    def _build_values(
            self,
            init_kwargs: Dict[str, Any],
            _env_file: Optional[DotenvType] = None,
            _env_file_encoding: Optional[str] = None,
            _env_nested_delimiter: Optional[str] = None,
            _secrets_dir: Optional[StrPath] = None,
    ) -> Dict[str, Any]:
        values = super()._build_values(
            init_kwargs,
            _env_file=_env_file,
            _env_file_encoding=_env_file_encoding,
            _env_nested_delimiter=_env_nested_delimiter,
            _secrets_dir=_secrets_dir,
        )
        """
        Convert string boolean to boolean
        """
        for field, value in values.items():
            if value is None:
                raise ValueError(f'Field {field} is not set')
            if isinstance(value, str):
                if value.lower() in ['1', 'true', 'yes']:
                    values[field] = True
                elif value.lower() in ['0', 'false', 'no']:
                    values[field] = False
        return values


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
