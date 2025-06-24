"""Модуля с функцияи для взаимодейтсвия с задачами"""
from json_processor.json_service import add_task_to_storage
from tasks.task_structures import Task
from tasks.decorators import input_notice


def add_task() -> None:
    task: Task = get_task_input_data()
    add_task_to_storage(task)


@input_notice('Пожалуйста введите данные для задачи \n')
def get_task_input_data() -> Task:

    title: str = input('\n Заголовок: ')
    description: str = input('\n Описание: ')

    return Task(id=0, title=title, desscription=description)
