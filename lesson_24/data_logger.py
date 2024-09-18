import logging
import os
from logging.handlers import RotatingFileHandler

log_size = 3000 * 1024
log_backup_count = 2
logs_dir = os.path.dirname('logs/')
if not os.path.exists(logs_dir):
    os.makedirs(logs_dir)


def setup_logger(filename):
    logger = logging.getLogger(filename)
    logger.setLevel(logging.INFO)
    file_handler = RotatingFileHandler(filename, maxBytes=log_size, backupCount=log_backup_count, encoding='utf-8')
    file_handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


log = setup_logger('logs/test_search.log')
