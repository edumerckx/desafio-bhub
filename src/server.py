import os

from dotenv import load_dotenv

import validators
from app import create_app
from logger import get_logger

load_dotenv()


if __name__ == '__main__' and validators.validate_varenvs():
    app = create_app()
    logger = get_logger()

    HTTP_PORT = os.getenv('HTTP_PORT')
    DEBUG = False if str(os.getenv('ENVIRONMENT')).lower() == 'prod' else True

    logger.info('Server running...')
    app.run(port=HTTP_PORT, debug=DEBUG)
