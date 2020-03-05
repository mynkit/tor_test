import const
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
import time


def get_soup_with_requests(url, proxies=None):
    '''requestsを用いてsoupを返す
    '''
    if proxies:
        r = requests.get(url, proxies=proxies, headers = {"User-Agent": const.USERAGENT})
    else:
        r = requests.get(url, headers = {"User-Agent": const.USERAGENT})
    soup = BeautifulSoup(r.content, 'lxml')
    return soup


def get_soup_with_selenium(url, proxies=None):
    '''seleniumを用いてsoupを返す
    '''
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,1024')
    options.add_argument(f'--user-agent={const.USERAGENT}')
    if proxies:
        options.add_argument(f'--proxy-server={proxies["http"]}')
    driver = webdriver.Chrome(
            options=options, executable_path=const.DRIVER_PATH)
    driver.get(url)
    time.sleep(1)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    driver.close()
    return soup


def get_ipinfo(proxies=None) -> dict:
    '''ipアドレス周りの情報を取得する
    '''
    return requests.get('https://ipinfo.io', proxies=proxies).json()


def tor_restart():
    '''torを再起動してipアドレスを変更する
    '''
    subprocess.call(['killall', 'tor'])
    subprocess.call(['service', 'tor', 'start'])