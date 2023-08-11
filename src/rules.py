import json
import os

import requests


def evaluate(payload: dict):
    GORULES_TOKEN = os.getenv('GORULES_TOKEN')
    GORULES_URL = os.getenv('GORULES_URL')

    headers = {
        'X-Access-Token': GORULES_TOKEN,
        'Content-Type': 'application/json',
    }

    data = {}
    data['context'] = payload

    response = requests.post(
        url=GORULES_URL, data=json.dumps(data), headers=headers
    )
    data = response.json()

    return data['result']['actions']
