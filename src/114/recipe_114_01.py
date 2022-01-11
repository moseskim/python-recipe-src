# 다음 명령어로 실행합니다
# python -m unittest test_recipe_114_01.py 

import unittest


class TestSample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('전체 전처리')

    @classmethod
    def tearDownClass(cls):
        print('전체 후처리')

    def setUp(self):
        print('테스트 전처리')

    def tearDown(self):
        print('테스트 후처리')

    def test_sample1(self):
        print("단위 테스트 1 실행")

    def test_sample2(self):
        print("단위 테스트 2 실행")
