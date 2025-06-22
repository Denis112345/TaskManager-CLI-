"""Модуль для взаимодействия с JSON-хранилищем данных"""
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from logger.logger_service import logger


def add_task_to_storage(task: dict[str, str]) -> bool:
    path_to_storage: Path = get_path_to_storage_from_env()
    if check_exists_storage(path_to_storage):
        pass


def get_path_to_storage_from_env() -> Path:
    path_to_env: str = '../.env'

    if not find_dotenv(path_to_env):
        logger.error(f'Файл .env по пути {path_to_env} не найден')
        raise FileNotFoundError

    # TODO Сделать проверку на наличие JSON_STORAGE_PATH
    load_dotenv(path_to_env)
    path_to_storage: Path = Path(os.getenv('JSON_STORAGE_PATH'))
    return path_to_storage


def check_exists_storage(path: Path) -> bool:
    if path.is_file():
        return True
    else:
        logger.error(f'Файл хранилища по пути {path} не найден')
