#!/usr/bin/env python3

import unittest
from io import StringIO
from unittest.mock import patch
from src.console_helper import ConsoleHelper
from src.color import Colors


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
        expected_output = f'{Colors.OKCYAN}Converted Code: {Colors.ENDC}<div class="relative px-3 py-3 mb-4 border rounded bg-teal-200 border-teal-300 text-teal-800 mb-2 mt-3">hi</div>\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console_helper.code_convert(
                    '<div class="alert alert-info mb-2 mt-3">hi</div>'
                    )
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_no_coversion_change(self):
        expected_output = f'{Colors.WARNING}Nothing generated! It means that TailwindCSS has no equivalent for that classes,or it has exactly classes with the same name.{Colors.ENDC}\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.console_helper.code_convert('<div class="box"> </div>')
            self.assertEqual(fake_out.getvalue(), expected_output)

    def test_convert_file(self):
        # Fake file
        pass

    def test_convert_folder(self):
        pass

    def test_convert_recursive_folder(self):
        pass
