import os
import logging
from db import talker

pemfilepath = os.path.join(os.getcwd(), 'apps/common/ca.pem')
logging.basicConfig(level=logging.INFO)
console = logging.StreamHandler()
logger = logging.getLogger(__name__)
logger.addHandler(console)


def create_pem_file():
    f = open(pemfilepath, "w")
    ar_pem = os.environ.get("CA_PEM").split(' ')
    pembegin = f'{ar_pem.pop(0)} {ar_pem.pop(0)}'
    pemend = f'{ar_pem.pop(-2)} {ar_pem.pop()}'
    pembody = f'\n'.join(ar_pem)
    pem = f'\n'.join((pembegin, pembody, pemend))
    f.write(pem)
    f.close()


def delete_pem_at_exit():
    open(pemfilepath, 'w').close()


def get_logger():
    return logger


def start_db():
    talker.connect_db()


def stop_db():
    talker.terminate_db()
