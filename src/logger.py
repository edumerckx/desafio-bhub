import logging
import os


def get_logger():
    FORMAT = '%(asctime)s %(message)s'
    logging.basicConfig(format=FORMAT)
    logger = logging.getLogger(__name__)
    LOG_LEVEL = (
        os.getenv('LOG_LEVEL') if 'LOG_LEVEL' in os.environ else 'DEBUG'
    )
    logger.setLevel(LOG_LEVEL)

    return logger
