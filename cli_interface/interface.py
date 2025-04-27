"""Модуль описывает CLI класс с методами и свойствами для взаимодействия с пользователем"""

from typing import Callable


class CLIInterface:
    def __init__(self, options: dict[str, Callable]):
        self.options: dict[str, Callable] = options
        self.welcome_message: str = '\nДобро пожаловать, в систему контроля задач!'
    
    def _show_options(self) -> None:
        """
        Отображает список опций для пользователя.
        """
        print('\n')
        for index, option in enumerate(self.options):
            print(f"{index}. {option}")

    def _type_validate_option(self, option: str) -> bool:
        """
        Проверяет ввел ли пользователь число
        """
        if option.isdigit():
            return True
        return False
    
    def _in_options_range_validate_option(self, option: str) -> bool:
        """
        Проверяет входит ли в диапазон существующих опций,
        введенная опция
        """
        if int(option) in range(0, len(self.options)):
            return True
        return False
    
    def _validate_option(self, option: str) -> bool:
        if not self._type_validate_option(option):
            raise ValueError('Введено не натуральное число/цифра')
        if not self._in_options_range_validate_option(option):
            raise ValueError('Номер опции находится вне диапазона опций')
        
        return True
    
    def _validate_option_with_error_handling(self, option) -> bool:
        try:
            self._validate_option(option)
            return True
        except ValueError as e:
            print(f'Ошибка: {str(e)}')
            return False

    def _get_function_for_option(self, option_number: int) -> Callable:
        options_functions: list[Callable] = list(self.options.values())
        target_function: Callable = options_functions[option_number]
        return target_function

    def _run_selected_option(self, option_number: int) -> None:
        target_function = self._get_function_for_option(option_number)
        target_function()

    def _input_user_select(self) -> str:
        selected_option: str = input("\nВыберите опцию: ")
        return selected_option

    def _get_valid_user_select(self) -> str:
        while True:
            selected_option: str = self._input_user_select()
            if self._validate_option_with_error_handling(selected_option):
                return selected_option

    def start(self) -> None:
        """
        Метод даёт выбор опций пользователю и вызывает выбранную
        """
        print(self.welcome_message)
        self._show_options()

        selected_option: str = self._get_valid_user_select()

        self._run_selected_option(int(selected_option))
