import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


class ConfigError(RuntimeError):
    pass


def _get_env(name: str, *, default: str | None = None, required: bool = False) -> str:
    value = os.getenv(name, default)
    if required and (value is None or value == ""):
        raise ConfigError(f"Missing required environment variable: {name}")
    return value


@dataclass(frozen=True)
class Settings:
    perplexity_api_key: str


def load_settings() -> Settings:
    return Settings(
        perplexity_api_key=_get_env("PERPLEXITY_API_KEY", required=True),
    )


settings = load_settings()
