import utils
import const
import unittest


class TestIPChange(unittest.TestCase):

    def test_useproxies(self):
        utils.tor_restart()  # torの起動
        ip_address__local = utils.get_ipinfo(None)['ip']
        ip_address__proxies = utils.get_ipinfo(const.PROXIES)['ip']
        self.assertNotEqual(ip_address__local, ip_address__proxies)

    def test_ipchange(self):
        utils.tor_restart()  # torの起動
        ip_address__before_restart = utils.get_ipinfo(const.PROXIES)['ip']
        utils.tor_restart()  # torの再起動
        ip_address__after_restart = utils.get_ipinfo(const.PROXIES)['ip']
        self.assertNotEqual(ip_address__before_restart,
                            ip_address__after_restart)
