from src.logger import get_logger


def test_should_return_logger_object():
    logger = get_logger()
    assert (type(logger)).__name__ == 'Logger'
