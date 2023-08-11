from src.actions import get_action


def test_should_return_function_when_exists_action():
    res = get_action('emitirRemessaEntrega')
    assert type(res).__name__ == 'function'

    res = get_action('ativaAssociacao')
    assert type(res).__name__ == 'function'


def test_should_return_function_when_not_exists_action():
    res = get_action('not_found')
    assert type(res).__name__ == 'function'
