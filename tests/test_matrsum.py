"""Модульные тесты для МатрСум-11 (по плану тестирования из ЛР №1)."""
import os
import sys
import unittest
from unittest import mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import matrsum  # noqa: E402


class FindZeroColumnsSumTest(unittest.TestCase):
    def test_one_column(self):
        m = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
        self.assertEqual(matrsum.find_zero_columns_sum(m), ([2], 10))

    def test_several_columns(self):
        m = [[0, 2, 3], [4, 5, 0], [7, 8, 9]]
        self.assertEqual(matrsum.find_zero_columns_sum(m), ([1, 3], 23))

    def test_no_zeros(self):
        self.assertEqual(
            matrsum.find_zero_columns_sum([[1, 2], [3, 4]]), ([], 0))

    def test_all_zeros(self):
        self.assertEqual(
            matrsum.find_zero_columns_sum([[0, 0], [0, 0]]), ([1, 2], 0))

    def test_single_column(self):
        self.assertEqual(
            matrsum.find_zero_columns_sum([[5], [0], [3]]), ([1], 8))

    def test_single_row(self):
        self.assertEqual(
            matrsum.find_zero_columns_sum([[1, 0, 3, 4]]), ([2], 0))

    def test_negative_numbers(self):
        m = [[-1, 0, 5], [2, 3, -4]]
        self.assertEqual(matrsum.find_zero_columns_sum(m), ([2], 3))

    def test_large_numbers(self):
        m = [[1e10, 0, -1e10], [2.5, 3.5, 4.5]]
        self.assertEqual(matrsum.find_zero_columns_sum(m), ([2], 3.5))


class InputTest(unittest.TestCase):
    def test_invalid_row_then_valid(self):
        answers = ["1", "2", "abc", "1 2", ]
        with mock.patch("builtins.input", side_effect=answers):
            with mock.patch("builtins.print"):
                self.assertEqual(matrsum.input_matrix(), [[1.0, 2.0]])

    def test_invalid_size_then_valid(self):
        answers = ["0", "-2", "x", "2"]
        with mock.patch("builtins.input", side_effect=answers):
            with mock.patch("builtins.print"):
                self.assertEqual(matrsum.read_positive_int("n: "), 2)


if __name__ == "__main__":
    unittest.main()
