import requests
import subprocess
import logging

logging.basicConfig(
    format='%(asctime)s PID:%(process)d [%(levelname)s] %(message)s',
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


PROXIES = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}


def get_ipinfo(proxies=None) -> dict:
    return requests.get('https://ipinfo.io', proxies=proxies).json()


def tor_restart():
    '''torを再起動してipアドレスを変更する
    '''
    subprocess.call(['killall', 'tor'])
    subprocess.call(['service', 'tor', 'start'])


if __name__ == '__main__':
    tor_restart()
    LOGGER.info(f'proxies: {PROXIES}')

    LOGGER.info('proxiesの設定なし')
    res = get_ipinfo()
    LOGGER.info(f'res: {res}')

    LOGGER.info('proxiesの設定あり')
    res = get_ipinfo(PROXIES)
    LOGGER.info(f'res: {res}')

    LOGGER.info('torの再起動')
    tor_restart()
    res = get_ipinfo(PROXIES)
    LOGGER.info(f'res: {res}')
