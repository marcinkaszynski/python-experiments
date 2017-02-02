import background as bg
import requests
import unittest
import time


class TestBackgroundProcesses(unittest.TestCase):
    def test_basic(self):
        def server_online_at(port):
            try:
                resp = requests.get('http://localhost:%s' % port)
                return resp.status_code == 200
            except requests.ConnectionError:
                return False

        self.assertFalse(server_online_at(30001))
        self.assertFalse(server_online_at(30002))

        with bg.shell_cmds(['python3 -m http.server 30001',
                            'python3 -m http.server 30002']):
            # TODO: wait by checking availability, not a blind delay
            time.sleep(1)
            self.assertTrue(server_online_at(30001))
            self.assertTrue(server_online_at(30002))

        self.assertFalse(server_online_at(30001))
        self.assertFalse(server_online_at(30002))


if __name__ == '__main__':
    unittest.main()
