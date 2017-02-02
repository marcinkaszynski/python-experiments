import background as bg
import requests
import unittest
import time


class TestBackgroundProcesses(unittest.TestCase):
    def test_basic(self):
        self.assertRaises(requests.ConnectionError,
                          requests.get, 'http://localhost:30001')
        with bg.shell_cmds(['python -m http.server 30001']):
            # TODO: wait by checking availability, not a blind delay
            time.sleep(1)
            resp = requests.get('http://localhost:30001')
            self.assertEqual(200, resp.status_code)

        self.assertRaises(requests.ConnectionError,
                          requests.get, 'http://localhost:30001')


if __name__ == '__main__':
    unittest.main()
