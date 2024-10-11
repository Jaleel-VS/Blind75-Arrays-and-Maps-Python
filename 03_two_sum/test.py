from main import twoSum
import unittest

class TestTwoSum(unittest.TestCase):

    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = twoSum(nums, target)
        self.assertCountEqual(result, [0, 1])  # Order does not matter

    def test_no_solution(self):
        nums = [1, 2, 3, 4]
        target = 10
        result = twoSum(nums, target)
        self.assertEqual(result, [])

    def test_negative_numbers(self):
        nums = [-3, 4, 3, 90]
        target = 0
        result = twoSum(nums, target)
        self.assertCountEqual(result, [0, 2])  # Order does not matter

    def test_single_element(self):
        nums = [1]
        target = 1
        result = twoSum(nums, target)
        self.assertEqual(result, [])

    def test_duplicates(self):
        nums = [3, 3]
        target = 6
        result = twoSum(nums, target)
        self.assertCountEqual(result, [0, 1])  # Order does not matter

    def test_large_input(self):
        nums = [i for i in range(100000)]
        target = 199998
        result = twoSum(nums, target)
        self.assertCountEqual(result, [99998, 99999])  # Order does not matter

    def test_multiple_valid_pairs(self):
        nums = [1, 2, 3, 4, 4]
        target = 8
        result = twoSum(nums, target)
        self.assertCountEqual(result, [3, 4])  # Order does not matter

if __name__ == "__main__":
    unittest.main()