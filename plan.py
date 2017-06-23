import os
import typing

import requests
from flask import Flask
from aiohttp import web, request


RequestDataType = typing.Dict[str, str]


BOT_API_TOKEN = os.environ.get('PLAN_BOT_API_TOKEN', '_plan_bot_token_not_found')
API_URL = 'https://api.telegram.org/bot'+ BOT_API_TOKEN + '/{}'
WEBHOOK_URL = '/bot/{}/'.format(BOT_API_TOKEN)


def make_api_request(verb, method, data):
    resp = requests.request(verb.capitalize(), API_URL.format(method), json=data)
    if resp:
        return resp.json
    else:
        return None


def is_webhook_set():
    resp = make_api_request('get', 'getWebhookInfo')
    if resp:
        info = resp.json()
        return (info or {}).get('url')
    else:
        return False


def set_webhook():
    pass


def process_request():
    pass


app = Flask(__name__)

@app.route(WEBHOOK_URL)
def bot_hook(request):
    return 'gigla'


if __name__ == '__main__':
    pass
