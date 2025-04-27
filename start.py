"""Модуль для запуска сервиса"""
from typing import Callable
from cli_interface.interface import CLIInterface


def foo():
    print('Hello, world!')

options: dict[str, Callable] = {
    'Добавить задачу': foo
}

cli_interface = CLIInterface(options=options)
cli_interface.start()