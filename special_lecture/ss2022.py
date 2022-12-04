import csv
import re


class CSVPrinter:
    def __init__(self, file_name):
        self.file_name = file_name

    def read(self):
        with open(self.file_name) as f:
            reader = csv.reader(f)
            lines = [row for row in reader]
        if all(True if len(row) == 3 else False for row in lines):
            lines = [int(re.sub("(value|[A-Z])", "", val)) for row in lines for val in row]
            ints = set(lines)
            return lines
        else:
            return None
