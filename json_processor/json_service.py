"""Модуль для взаимодействия с JSON-хранилищем данных"""
import json
from pathlib import Path
from logger.logger_service import logger
from tasks.task_structures import Task
from utils.utils import get_storage_path


def add_task_to_storage(task: Task) -> bool:
    path_to_storage: Path = get_storage_path()

    if not check_exists_storage(path_to_storage):
        path_to_storage: Path = get_storage_path()
        create_storage(path_to_storage)

    with open(path_to_storage, 'r', encoding='utf-8') as file:
        data: dict = json.load(file)

    if data:
        last_task_id: int = get_last_task_id(data)
        task.id = last_task_id + 1
        tasks: list[dict[str, str]] = data['tasks']
        tasks.append(task.model_dump())
    else:
        task.id = 0
        data['tasks'] = [task.model_dump()]

    with open(path_to_storage, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    return True


def create_storage(path: Path) -> None:
    with open(path, 'w', encoding='utf-8') as file:
        json.dump({}, file, ensure_ascii=False, indent=4)


def get_last_task_id(data: dict) -> int:
    tasks: list[dict[str, str]] = data.get('tasks', [])
    if tasks:
        last_task: dict[str, str] = tasks[-1]
        return int(last_task['id'])
    return 0


def check_exists_storage(path: Path) -> bool:
    if path.is_file():
        return True
    else:
        logger.error(f'Файл хранилища по пути {path} не найден')
