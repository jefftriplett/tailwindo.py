#!/usr/bin/env python3

import unittest
from io import StringIO
from pathlib import Path
from unittest.mock import patch, mock_open, MagicMock
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

    @patch('builtins.print')
    def test_convert_code_snippet(self, mock_print):
        expected_output = f'{Colors.OKCYAN}Converted Code: {Colors.ENDC}<div class="relative px-3 py-3 mb-4 border rounded bg-teal-200 border-teal-300 text-teal-800 mb-2 mt-3">hi</div>'
        self.console_helper.code_convert(
            '<div class="alert alert-info mb-2 mt-3">hi</div>'
        )
        mock_print.assert_called_with(expected_output)

    @patch('builtins.print')
    def test_no_coversion_change(self, mock_print):
        expected_output = f'{Colors.WARNING}Nothing generated! It means that TailwindCSS has no equivalent for that classes,or it has exactly classes with the same name.{Colors.ENDC}'
        self.console_helper.code_convert('<div class="box"> </div>')
        mock_print.assert_called_with(expected_output)

    @patch('src.console_helper.Path')
    def test_convert_file_message(self, mock_path):
        # file_name = 'file.html'
        # (
        #   framework_version,
        #   tailwind_version
        # ) = self.console_helper.converter.framework.supported_version
        # name = self.console_helper.converter.framework.name
        # expected_output = f"""{Colors.OKBLUE}Converting File: (extracted to tailwindo-components.css){Colors.ENDC} {file_name}\n{Colors.OKGREEN}Converting from{Colors.ENDC} {name} {framework_version} {Colors.OKGREEN}to{Colors.ENDC} Tailwind {tailwind_version}\n{Colors.WARNING}Couldn't convert: {Colors.ENDC} {file_name}\n\n"""
        # with patch('sys.stdout', new=StringIO()) as fake_out:
        #     self.console_helper.file_convert(file_name)
        #     self.assertEqual(expected_output, fake_out.getvalue())
        pass

    def test_convert_file(self):
        # # Fake file
        # file_path = '/some/path/to/file.html'
        # content = "Message to write on file to be written"
        # with patch('src.console_helper.open', mock_open()) as mocked_file:
        #     self.console_helper.file_convert(file_path)
        #     # assert if opened file on write mode 'w'
        #     mocked_file.assert_called_once_with(file_path, 'w')
        #     # assert if write(content) was called from the file opened
        #     # in another words, assert if the specific content was written in file
        #     mocked_file().write.assert_called_once_with(content)

        pass

    def test_convert_folder(self):
        pass

    def test_convert_recursive_folder(self):
        pass

    def test_write_to_file(self):
        file_path = "fake/file/path"
        content = "Message to write on file to be written"
        with patch('src.console_helper.open', mock_open()) as mocked_file:
            self.console_helper._write_components_to_file(content, file_path)
            # assert if opened file on write mode 'w'
            mocked_file.assert_called_once_with(
                    f'{file_path}/tailwindo-components.css', 'a'
            )
            # assert if write(content) was called from the file opened
            # in another words, assert if the specific content was written in
            # file
            mocked_file().write.assert_called_with(content+"\n")

    @patch('src.console_helper.Path')
    def test_new_components_file(self, _path):
        mock_path = MagicMock()
        _path.return_value = mock_path
        mock_path.is_file.return_value = False
        print(mock_path)
        pass
