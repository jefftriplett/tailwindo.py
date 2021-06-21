import unittest
from src.converter import Converter


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.class_only = Converter(classes_only=True)
        self.converter = Converter()

    def test_it_returns_output(self):

        self.assertEqual(
            "sm:flex", self.class_only.set_content("d-sm-flex").convert(),
        )
        self.assertEqual(
            '<a class="text-gray-700">love</a>',
            self.converter.set_content('<a class="text-muted">love</a>').convert(),
        )

    #  @test */
    def test_it_output_with_prefix(self):

        self.converter.set_prefix("tw-")
        self.class_only.set_prefix("tw-")
        self.assertEqual(
            "sm:tw-flex", self.class_only.set_content("d-sm-flex").convert(),
        )
        self.assertEqual(
            '<a class="tw-text-gray-700">love</a>',
            self.converter.set_content('<a class="text-muted">love</a>').convert(),
        )

    #  @test */
    def test_it_handles_jsx_class_name(self):

        self.assertEqual(
            '<a className="sm:flex text-gray-700">love</a>',
            self.converter.set_content(
                '<a className="d-sm-flex text-muted">love</a>'
            ).convert(),
        )


# if __name__ == '__main__':
#    unittest.main()
