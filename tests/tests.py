import unittest
import src.pitchup


__author__ = 'josebermudez'


class TestsPitchup(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestsPitchup, self).__init__(*args, **kwargs)
        self.pitchup = src.pitchup

    def test_calculate_divisors(self):
        num = 3
        expected_divisors = set([1, 3])
        self.assertEqual(self.pitchup.calculate_divisors(num=num), expected_divisors)

    def test_calculate_sum(self):
        nums = [0, 1, 2, 3]
        expected_sum = 6
        self.assertEqual(self.pitchup.calculate_sum(nums=nums), expected_sum)

    def test_calculate_sum_zero(self):
        nums = [0]
        expected_sum = 0
        self.assertEqual(self.pitchup.calculate_sum(nums=nums), expected_sum)

    def test_check_subsets_true(self):
        num = 1
        divisors = self.pitchup.calculate_divisors(num=num)
        self.assertTrue(self.pitchup.check_subsets(divisors=divisors, num=num))

    def test_check_subsets_false(self):
        num = 12
        divisors = self.pitchup.calculate_divisors(num=num)
        self.assertFalse(self.pitchup.check_subsets(divisors=divisors, num=num))
