import unittest
from main import containsDuplicate

class TestContainsDuplicate(unittest.TestCase):
    def test_basic_case(self):
        self.assertTrue(containsDuplicate([1, 2, 3, 1]))

    def test_all_distinct(self):
        self.assertFalse(containsDuplicate([1, 2, 3, 4]))

    def test_multiple_duplicates(self):
        self.assertTrue(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))

    def test_single_element(self):
        self.assertFalse(containsDuplicate([1]))

    def test_empty_array(self):
        self.assertFalse(containsDuplicate([]))

    def test_two_identical(self):
        self.assertTrue(containsDuplicate([2, 2]))

    def test_large_size(self):
        self.assertTrue(containsDuplicate([i for i in range(10000)] + [0]))

    def test_negative_and_positive(self):
        self.assertTrue(containsDuplicate([-1, -2, -3, -1]))

    def test_all_duplicates(self):
        self.assertTrue(containsDuplicate([5, 5, 5, 5]))

    def test_non_consecutive_duplicates(self):
        self.assertTrue(containsDuplicate([10, 20, 30, 40, 10]))

    def test_max_integers(self):
        self.assertTrue(containsDuplicate([2147483647, -2147483648, 2147483647]))

    def test_alternating_duplicates(self):
        self.assertTrue(containsDuplicate([1, 2, 1, 2, 1, 2]))

if __name__ == "__main__":
    unittest.main()
