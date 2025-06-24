"""Модуль описывает структуры данных для задач"""

from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    desscription: str
