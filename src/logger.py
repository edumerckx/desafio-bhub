import logging
import os


def get_logger():
    FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger(__name__)
    LOG_LEVEL = os.getenv('LOG_LEVEL')
    logger.setLevel(LOG_LEVEL)

    return logger
