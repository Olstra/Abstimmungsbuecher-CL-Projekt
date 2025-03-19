import unittest

from src.nlp.text_cleaner import clean_up_line_breaks


class CleanUpLineBreaksTest(unittest.TestCase):
    def test_clean_up_line_breaks(self):

        test_input =["L’initiative d’allègement des primes plafonnera ces der-",
                     "nières à 10 % du revenu disponible. Le comité estime qu’elle",
                     "pourquoi ils lui opposent un contre-projet indirect qui a égale-",
                     "ment pour objectif de réduire davantage les primes, mais tout"]

        expected_output = ["L’initiative d’allègement des primes plafonnera ces dernières à 10 % du revenu disponible. Le comité estime qu’elle",
                           "pourquoi ils lui opposent un contre-projet indirect qui a également pour objectif de réduire davantage les primes, mais tout"]

        self.assertEqual(expected_output, clean_up_line_breaks(test_input))

    def test_clean_up_multiple_consecutive_line_breaks(self):
        test_input =["a-", "b-", "c-", "d"]
        expected_output = ["abcd"]

        self.assertEqual(expected_output, clean_up_line_breaks(test_input))


if __name__ == '__main__':
    unittest.main()
