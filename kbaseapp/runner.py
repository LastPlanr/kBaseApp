import sys

from autobahn.asyncio.wamp import ApplicationRunner
from prettyconf import config

URL = config('URL', default='ws://crossbar.dronemapp.com:80/ws')
REALM = config('REALM', default='kotoko')


def run(cls):
    runner = ApplicationRunner(URL, REALM)
    try:
        runner.run(cls)
    except OSError as ex:
        print('OSError:', ex)
        sys.exit(100)
