import requests
import subprocess
import logging

logging.basicConfig(
    format='%(asctime)s PID:%(process)d [%(levelname)s] %(message)s',
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)


proxies = {
    'http': 'socks5://127.0.0.1:9050',
    'https': 'socks5://127.0.0.1:9050'
}

if __name__ == '__main__':
    subprocess.call(['service', 'tor', 'restart'])

    LOGGER.info(f'proxies: {proxies}')

    LOGGER.info('proxiesの設定なし')
    res = requests.get('https://ipinfo.io').json()
    LOGGER.info(f'res: {res}')

    LOGGER.info('proxiesの設定あり')
    res = requests.get('https://ipinfo.io', proxies=proxies).json()
    LOGGER.info(f'res: {res}')
