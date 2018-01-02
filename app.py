import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = "500949998:AAGTNZ_AZHHRCSS0JDKVYbtZv5gCTI_ZFzI"
WEBHOOK_URL = 'https://b022b5be.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'basic',
        'crouched',
        'set_up',
        'spike',
        'advanced',
        'defence',
        'attack',
        'record',
        'year102',
        'year103',
        'year104',
        'year105'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'basic',
            'conditions': 'is_going_to_basic'
        },
        {
            'trigger': 'advance',
            'source': 'basic',
            'dest': 'crouched',
            'conditions': 'is_going_to_crouched'
        },
        {
            'trigger': 'advance',
            'source': 'basic',
            'dest': 'set_up',
            'conditions': 'is_going_to_set_up'
        },
        {
            'trigger': 'advance',
            'source': 'basic',
            'dest': 'spike',
            'conditions': 'is_going_to_spike'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'advanced',
            'conditions': 'is_going_to_advanced'
        },
        {
            'trigger': 'advance',
            'source': 'advanced',
            'dest': 'defence',
            'conditions': 'is_going_to_defence'
        },
        {
            'trigger': 'advance',
            'source': 'advanced',
            'dest': 'attack',
            'conditions': 'is_going_to_attack'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'record',
            'conditions': 'is_going_to_record'
        },
        {
            'trigger': 'advance',
            'source': 'record',
            'dest': 'year102',
            'conditions': 'is_going_to_year102'
        },
        {
            'trigger': 'advance',
            'source': 'record',
            'dest': 'year103',
            'conditions': 'is_going_to_year103'
        },
        {
            'trigger': 'advance',
            'source': 'record',
            'dest': 'year104',
            'conditions': 'is_going_to_year104'
        },
        {
            'trigger': 'advance',
            'source': 'record',
            'dest': 'year105',
            'conditions': 'is_going_to_year105'
        },
        {
            'trigger': 'go_back',
            'source': [
                'crouched',
                'set_up',
                'spike',
                'defence',
                'attack',
                'year102',
                'year103',
                'year104',
                'year105'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
