from src.app import create_app


def test_should_return_flask_app():
    app = create_app()
    assert type(app).__name__ == 'Flask'
