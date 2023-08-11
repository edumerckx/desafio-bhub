import rules
from actions import get_action
from logger import get_logger


def payment_process(data: dict):
    """
    Processa lista de ações para o pagamento

    Parameters:
        data - payload do pagamento

    Returns:
        None
    """
    logger = get_logger()

    list_actions = rules.evaluate(data)
    for action in list_actions:
        logger.info(f'Processando action "{action}"')
        get_action(action)(data)
