import unittest

import misc


class TestMisc(unittest.TestCase):

    def test_should_get_missing_integer_correctly(self):
        cases = [
            {"input": [1, 3, 6, 4, 1, 2], "want": 5},
            {"input": [1, 2, 3], "want": 4},
            {"input": [-1, -3], "want": 1}
        ]
        for c in cases:
            self.assertEqual(
                c["want"],
                misc.solution(c["input"], len(c["input"])),
                "Wrong missing integer for {}".format(c["input"])
            )


if __name__ == '__main__':
    unittest.main()
