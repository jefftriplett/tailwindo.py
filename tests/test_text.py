import unittest
from src.converter import Converter

class TestText(unittest.TestCase):

    def setUp(self):
        self.converter = Converter(classesOnly=True).setFramework('bootstrap')

    def test_converts_text_with_breakpoint(self):
        self.assertEqual(
            'sm:text-left',
            self.converter
            .setContent('text-xs-left')
            .convert()
            .get()
            )
        self.assertEqual(
            'lg:text-justify',
             self.converter
            .setContent('text-lg-justify')
            .convert()
            .get()
            )

if __name__ == '__main__':
    unittest.main()
