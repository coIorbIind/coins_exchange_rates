import logging
import sys

from config.settings import settings


def init_logger(name: str):
    """
    Инициализация логгера
    :param name: название файла, из которого пишем логи
    :return: инстанс логгера
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(settings.LOG_FILE_PATH, mode='a')
    std_handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

    file_handler.setFormatter(formatter)
    std_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(std_handler)

    return logger
