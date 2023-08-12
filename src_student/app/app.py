import logging
import random
import logstash

from flask import Flask, request
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(integrations=[FlaskIntegration()])

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
app.logger = logging.getLogger(__name__)


logstash_handler = logstash.LogstashHandler('logstash', 5044, version=1)


class RequestIdFilter(logging.Filter):
    def filter(self, record):
        record.request_id = request.headers.get('X-Request-Id')
        return True


app.logger.addFilter(RequestIdFilter())
app.logger.setLevel(logging.INFO)
app.logger.addHandler(logstash_handler)
# Handler отвечают за вывод и отправку сообщений. В модуль logging доступно несколько классов-обработчиков
# Например, SteamHandler для записи в поток stdin/stdout, DatagramHandler для UDP, FileHandler для syslog
# LogstashHandler не только отправляет данные по TCP/UDP, но и форматирует логи в json-формат.


@app.before_request
def before_request():
    request_id = request.headers.get('X-Request-Id')
    if not request_id:
        app.logger.error(f'request id is requred')
        raise RuntimeError('request id is requred')


@app.route('/')
def index():
    result = random.randint(1, 50)
    app.logger.info(f'Пользователю досталось число {result}')
    return f"Ваше число {result}!"
