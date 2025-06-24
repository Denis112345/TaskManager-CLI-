"""Модуль с декораторами для функций пакета задач"""
from functools import wraps
from typing import Callable


def input_notice(message: str = '') -> Callable:
    def decorator(func):
        wraps(func)

        def wrapper(*args, **kwargs):
            print("\n" + message)
            return func(*args, **kwargs)

        return wrapper

    return decorator
