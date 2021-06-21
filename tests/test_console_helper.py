#!/usr/bin/env python3

import unittest
from src.console_helper import ConsoleHelper


class CommandLineTests(unittest.TestCase):
    def setUp(self):
        self.settings = {
            "recursive": False,
            "overwrite": False,
            "extensions": ".php,.html,.jsx",
            "framework": "bootstrap",
            "components": False,
            "prefix": "",
            "folder_convert": False,
        }
        self.console_helper = ConsoleHelper(self.settings)

    def test_convert_code_snippet(self):
        actual_output = self.console_helper.code_convert(
            '<div class="alert alert-info mb-2 mt-3">hi</div>'
        )
        expected_output = 'Converted Code: <div class="relative px-3 py-3 mb-4 border rounded bg-teal-200 border-teal-300 text-teal-800 mb-2 mt-3">hi</div>'
        self.assertEqual(actual_output, actual_output)

    def test_convert_file(self):
        pass

    def test_convert_folder(self):
        pass

    def test_convert_recursive_folder(self):
        pass
