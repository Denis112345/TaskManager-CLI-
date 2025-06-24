"""Модуль для дополнительных функций-утилит"""
import os
from pathlib import Path
from dotenv import load_dotenv, find_dotenv
from tasks.task_structures import Task
from logger.logger_service import logger


def task_is_valid(task: Task):
    pass


def get_storage_path(path_to_env: Path = Path('.env')) -> Path:
    if not find_dotenv(path_to_env):
        logger.error(f'Файл .env по пути {path_to_env} не найден')
        raise FileNotFoundError

    # TODO Сделать проверку на наличие JSON_STORAGE_PATH
    load_dotenv(path_to_env)
    path_to_storage: Path = Path(os.getenv('JSON_STORAGE_PATH'))
    return path_to_storage
