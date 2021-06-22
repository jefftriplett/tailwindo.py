import unittest

from src.converter import Converter
from src.framework.bootstrap_framework import BootstrapFramework


class TestBootstrapFramework(unittest.TestCase):
    def setUp(self):
        self.bootstrap = BootstrapFramework()
        self.converter = Converter(framework="bootstrap")

    def test_ignore_class_with_double_dash(self):
        match_array = []

        for item in self.bootstrap.get():
            for search, replace in item.items():
                if "--" in search:
                    match_array.append(search)
        return self.assertEqual(match_array, [])

    def test_supported_version(self):
        return self.assertEqual(
                self.bootstrap.supported_version,
                ("4.4.1",  "1.4.0")
        )

    def test_framework_name(self):
        return self.assertEqual(
                self.bootstrap.name,
                "Bootstrap"
        )
