import unittest
from spider_demo import douban_spider


class YouDemoTests(unittest.TestCase):
    def test_spider(self):
        a = douban_spider.get_total_page()
        print(a)

    def test_fun(self):
        self.seq = range(10)
        print("call set up")


if __name__ == '__main__':
    unittest.main()
