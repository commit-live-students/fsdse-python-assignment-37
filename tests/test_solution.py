from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        a_list = [1, 2, -8, -2, 0]
        result = solution(a_list)

        self.assertEqual(result, -2)
