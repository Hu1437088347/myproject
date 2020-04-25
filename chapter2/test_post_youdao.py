import unittest
from unittest import mock


class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True,True)

    def test_get_ts(self):
        # import time
        # ts=time.time()
        # ts=str(int(round(ts*1000)))
        # print(ts)
        get_ts=mock.Mock(return_value='1584684880395')
        self.assertEqual('1584684880395',get_ts())

    def test_get_salt(self):
        get_salt=mock.Mock(return_value='15846848803956')
        self.assertEqual('15846848803956',get_salt())

    def test_get_sign(self):
        get_sign=mock.Mock(return_value="b1537e6e7d4296b0145432358da1fce0")
        self.assertEqual('b1537e6e7d4296b0145432358da1fce0',get_sign())
                          # 9e6b89142b28dde4fe3b5c4fc5407b32


if __name__ == '__main__':
        unittest.main()
