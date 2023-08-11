import json

from flask import Flask, request

import controller

app = Flask(__name__)


def create_app():
    """
    Configuração das rotas da aplicação
    """

    @app.post('/payments')
    def payment_process():
        """
        Rota responsável por receber requisições de processamento de pagamento
        """
        controller.payment_process(json.loads(request.data))
        return {'message': 'Payment processed'}, 201

    return app
