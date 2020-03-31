import unittest
from post_youdao import *

class PostYoudaoTest(unittest.TestCase):
    def test_something(self):
        self.addertEqual(True,True)

    def test_get_ts(self):
        # import time
        # ts=time.time()
        # ts=str(int(round(ts*1000)))
        # print(ts)
        get.ts=mock.Mock(return_value='1585378348869')
        self.assertEqual('1585378348869',get_ts())

if __name__ == "__main__":
    unittest.main()