import os
import typing

from aiohttp import web, request


RequestDataType = typing.Dict[str, str]


BOT_API_TOKEN = os.environ.get('BOT_API_TOKEN')
API_URL = 'https://api.telegram.org/bot'+ BOT_API_TOKEN + '/{}'


async def make_api_request(http_verb:str, api_method:str, data: RequestDataType=None) -> typing.Awaitable:
    async with request(method=http_verb.capitalize(), url=API_URL.format(api_method), json=data) as resp:
        return await resp.json()


async def check_webhook() -> bool:
    async with make_api_request('get', 'getWebhookInfo') as resp:
        hook_info = await resp.json()
        return (hook_info or {}).get('url')


async def set_webhook() -> bool:
    pass


async def handle_request(request: web.Request) -> web.Response:
    return web.Response(text='response')


app = web.Application()
app.router.add_get('/', handle_request)


web.run_app(app, port=8666)