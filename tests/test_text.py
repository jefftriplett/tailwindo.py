import unittest
from src.converter import Converter

class TestText(unittest.TestCase):

    def setUp(self):
        self.converter = Converter().setFramework('bootstrap')

    def test_converts_text_with_breakpoint(self):
        self.assertEquals(
            'sm:text-left',
            self.converter
            .classesOnly(True)
            .setContent('text-xs-left')
            .convert()
            .get()
            )
        self.assertEquals(
            'lg:text-justify',
             self.converter
            .classesOnly(True)
            .setContent('text-lg-justify')
            .convert()
            .get()
            )

if __name__ == '__main__':
    unittest.main()
