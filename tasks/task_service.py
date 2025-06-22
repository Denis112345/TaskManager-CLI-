"""Модуля с функцияи для взаимодейтсвия с задачами"""
from json_processor.json_service import add_task_to_storage


def add_task(task: dict[str, str]) -> bool:
    add_task_to_storage(task)
