"""Модуль для запуска сервиса"""
from typing import Callable
from cli_interface.interface import CLIInterface
from tasks.task_service import add_task


options: dict[str, Callable] = {
    'Добавить задачу': add_task
}

cli_interface = CLIInterface(options=options)
cli_interface.start()
