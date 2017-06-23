import os

import flask
import telepot
import telepot.loop as pot_loop
import telepot.delegate as pot_delegate


BOT_API_TOKEN = os.environ.get('BOT_TOKEN', '')
BOT_HOOK_URL = os.environ.get('BOT_HOOK_URL', '/bot/hook')
BOT_HOST = os.environ.get('BOT_HOST', '')

# bot related
class Planner(telepot.helper.ChatHandler):
    def __init__(self, *args, **kwargs):
        super(Planner, self).__init__(*args, **kwargs)

    def on_chat_message(self, msg):
        self.sender.sendMessage('gigla')


bot = telepot.DelegatorBot(BOT_API_TOKEN, [
    pot_delegate.pave_event_space()(
        pot_delegate.per_chat_id(),
        pot_delegate.create_open,
        Planner,
        timeout=15
    )
])

webhook = pot_loop.OrderedWebhook(bot)

# server related
app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'planner bot'

@app.route(BOT_HOOK_URL, methods=['GET', 'POST'])
def on_event():
    webhook.feed(flask.request.data)
    return 'OK'


if __name__ == '__main__':
    try:
        bot.setWebhook(BOT_HOST+BOT_HOOK_URL)
    except telepot.exception.TooManyRequestsError:
        pass

    webhook.run_as_thread()
    app.run()
