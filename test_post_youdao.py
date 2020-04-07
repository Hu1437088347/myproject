import unittest
from unittest import mock

from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.addertEqual(True,True)

    def test_get_ts(self):
        # import time
        # ts=time.time()
        # ts=str(int(round(ts*1000)))
        # print(ts)
        get_ts=mock.Mock(return_value='1585378348869')
        self.assertEqual('1585378348869',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15853783488690')
        self.assertEqual('15853783488690',get_salt())

    def test_get_sign(self):
        self.assertEqual('6b9a6ce3ff157252d9a388c507e70474',get_sign())


if __name__ == "__main__":
    unittest.main()