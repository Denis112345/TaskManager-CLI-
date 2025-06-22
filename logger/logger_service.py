"""Модуль для логирования сервиса"""
import logging
from pathlib import Path


class Logger:
    def __init__(
            self,
            logger_name: str = 'task_manager_logger',
            level: int = logging.INFO,
            log_folder: Path = Path('../logs/logs.log')
    ) -> None:
        self.logger: logging.Logger = logging.getLogger(name=logger_name)
        self.logger.level = level

        self.log_folder: Path = log_folder

        self.formatter: logging.Formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(name)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        self._init_logger_handlers()

    def _init_logger_handlers(self) -> None:
        console_handler: logging.StreamHandler = logging.StreamHandler()
        console_handler.setFormatter(self.formatter)

        file_handler: logging.FileHandler = logging.FileHandler(
                                                filename=self.log_folder
                                            )
        file_handler.setFormatter(self.formatter)

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

    def get_logger(self) -> logging.Logger:
        return self.logger


logger: logging.Logger = Logger().get_logger()
