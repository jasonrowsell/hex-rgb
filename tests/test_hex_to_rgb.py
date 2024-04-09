import os
import unittest
import re
from lib import hex_to_dec


def hex_to_rgb(r: re.Match):
    hex = r.group(1).lower()
    return hex_to_dec.hex_to_dec(hex)


def convert_css(file: str):
    file_path = os.path.join(os.path.dirname(__file__), file)

    with open(file_path) as f:
        content = f.read()

    res = re.sub(r"\#([0-9a-fA-F]+)", hex_to_rgb, content)
    return res


def read(file: str):
    file_path = os.path.join(os.path.dirname(__file__), file)

    with open(file_path) as f:
        content = f.read()

    return content


class TestHexToRGB(unittest.TestCase):
    def test_simple_css(self):
        self.assertEqual(convert_css("simple.css"), read("simple_expected.css"))

    def test_advanced_css(self):
        self.assertEqual(convert_css("advanced.css"), read("advanced_expected.css"))


if __name__ == "__main__":
    unittest.main()
