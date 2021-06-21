import unittest
from src.framework.bootstrap_framework import BootstrapFramework
from src.converter import Converter


class TestBootstrapFramework(unittest.TestCase):
    def setUp(self):
        self.bootstrap = BootstrapFramework().get()
        self.converter = Converter(framework="bootstrap")

    def test_ignore_class_with_double_dash(self):
        match_array = []

        for item in self.bootstrap:
            for search, replace in item.items():
                if "--" in search:
                    match_array.append(search)
        return self.assertEqual(match_array, [])


if __name__ == "__main__":
    unittest.main()
