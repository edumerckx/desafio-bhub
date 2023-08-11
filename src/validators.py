import os

required_varenvs = [
    'GORULES_TOKEN',
    'GORULES_URL',
    'HTTP_PORT',
    'LOG_LEVEL',
]


def validate_varenvs() -> bool:
    """
    Verifica se as variáveis de ambiente listadas em **required_varenvs** foram configuradas no ambiente

    Parameters:

    Returns:
        Todas as variáveis de ambiente foram configuradas?

    Examples:
        >>> validate_varenvs()
        True
    """
    valid_varenvs = True
    for env in required_varenvs:
        if os.getenv(env) == None:
            print(f'{env} não configurada')
            valid_varenvs = False
    return valid_varenvs
