# test_sample.py 테스트를 수행하는 측의 코드
import unittest
import sample


class TestNumberFuncs(unittest.TestCase):

    def test_add_num(self):
        """
        add_num 단위 테스트
        """
        self.assertEqual(7, sample.add_num(3, 4))

    def test_is_positive(self):
        """
        is_num 단위 테스트
        """
        self.assertTrue(sample.is_positive(3))
        self.assertFalse(sample.is_positive(0))
        self.assertFalse(sample.is_positive(-1))
