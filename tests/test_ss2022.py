import unittest

from special_lecture.ss2022 import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read(self):
        printer = CSVPrinter("tests/sample.csv")
        results = printer.read()
        self.assertEqual(9, len(results))
        for result in results:
            self.assertEqual(int, type(result))