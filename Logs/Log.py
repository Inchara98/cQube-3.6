import logging
import os

from log_path import log_file_path


class log_Details():



    @staticmethod
    def logen():
        file = log_file_path()
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler(file.get_log_file_dir()+'/status.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger
