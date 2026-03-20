from enum import Enum
from typing import Self
from pathlib import Path  # ← ОБЯЗАТЕЛЬНО ДОБАВИТЬ

from pydantic import EmailStr, FilePath, HttpUrl, DirectoryPath, BaseModel, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

# ← ДОБАВИТЬ: корень проекта = папка, где лежит config.py
_PROJECT_ROOT = Path(__file__).parent


class Browser(str, Enum):
    WEBKIT = "webkit"
    FIREFOX = "firefox"
    CHROMIUM = "chromium"


class TestUser(BaseModel):
    email: EmailStr
    username: str
    password: str


class TestData(BaseModel):
    image_png_file: FilePath

    # ← ДОБАВИТЬ: валидатор для относительных путей
    @field_validator('image_png_file', mode='before')
    @classmethod
    def resolve_relative_path(cls, v):
        """Преобразует относительные пути в абсолютные относительно проекта"""
        if isinstance(v, str) and (v.startswith('./') or v.startswith('../')):
            return _PROJECT_ROOT / v
        return Path(v) if isinstance(v, str) else v


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # ← ИСПРАВЛЕНО: ищем .env относительно config.py, а не рабочей директории
        env_file=_PROJECT_ROOT / ".env",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    def get_base_url(self) -> str:
        return f"{self.app_url}/"

    app_url: HttpUrl
    headless: bool
    browsers: list[Browser]
    test_user: TestUser
    test_data: TestData
    videos_dir: DirectoryPath
    tracing_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    browser_state_file: FilePath

    @classmethod
    def initialize(cls) -> Self:
        # ← ИСПРАВЛЕНО: строим пути относительно _PROJECT_ROOT
        videos_dir = _PROJECT_ROOT / "videos"
        tracing_dir = _PROJECT_ROOT / "tracing"
        allure_results_dir = _PROJECT_ROOT / "allure-results"
        browser_state_file = _PROJECT_ROOT / "browser-state.json"

        videos_dir.mkdir(exist_ok=True)
        tracing_dir.mkdir(exist_ok=True)
        allure_results_dir.mkdir(exist_ok=True)
        browser_state_file.touch(exist_ok=True)

        return Settings(
            videos_dir=videos_dir,
            tracing_dir=tracing_dir,
            allure_results_dir=allure_results_dir,
            browser_state_file=browser_state_file
        )


# Инициализируем настройки
settings = Settings.initialize()