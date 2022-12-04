import unittest

from special_lecture.ss2022 import CSVPrinter


class TestCSVPrinter(unittest.TestCase):

    def test_read1(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        self.assertEqual(3, len(l))

    def test_read2(self):
        printer = CSVPrinter("tests/sample.csv")
        l = printer.read()
        self.assertEqual("value2B", l[1][1])

    def test_read3(self):
        with self.assertRaises(FileNotFoundError):
            printer = CSVPrinter("no_exist.csv")
            l = printer.read()

    def test_read4(self):
        printer = CSVPrinter("tests/sample.csv")
        lines = printer.read()
        self.assertEqual(3, len(lines))
        for line in lines:
            self.assertEqual(3, len(line))