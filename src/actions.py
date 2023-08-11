"""
Nesse módulo são configuradas as _actions_ relacionadas às regras
"""
from collections.abc import Callable

_actions = {}
_actions['emitirRemessaEntrega'] = lambda payload: print(
    'Executando "emitirRemessaEntrega"', payload
)
_actions['atualizaAssociacao'] = lambda payload: print(
    'Executando "atualizaAssociacao"', payload
)
_actions['ativaAssociacao'] = lambda payload: print(
    'Executando "ativaAssociacao"', payload
)
_actions['notificaAssociacao'] = lambda payload: print(
    'Executando "notificaAssociacao"', payload
)


def get_action(action: str) -> Callable:
    """
    Dada uma 'action' retorna a função associada.

    Parameters:
        action: Nome da action

    Returns:
        Função associada à action
    """
    if action in _actions:
        return _actions[action]

    return lambda _: print(f'Action "{action}" não encontrada')
