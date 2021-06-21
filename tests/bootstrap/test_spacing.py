import unittest

from src.converter import Converter


class TestSpacing(unittest.TestCase):
    def setUp(self):
        self.converter = Converter(classes_only=True)

    def test_padding_it_converts_on_all_sides(self):
        self.assertEqual("p-1", self.converter.set_content("p-1").convert())

        self.assertEqual(
            "sm:p-1", self.converter.set_content("p-sm-1").convert(),
        )

        self.assertEqual(
            "md:p-2", self.converter.set_content("p-md-2").convert(),
        )

        self.assertEqual(
            "lg:p-4", self.converter.set_content("p-lg-3").convert(),
        )

        self.assertEqual(
            "xl:p-6", self.converter.set_content("p-xl-4").convert(),
        )

        self.assertEqual(
            "xl:p-12", self.converter.set_content("p-xl-5").convert(),
        )

    #  @test */
    def test_padding_it_converts_on_y(self):

        self.assertEqual("py-1", self.converter.set_content("py-1").convert())

        self.assertEqual(
            "sm:py-1", self.converter.set_content("py-sm-1").convert(),
        )

        self.assertEqual(
            "md:py-2", self.converter.set_content("py-md-2").convert(),
        )

        self.assertEqual(
            "lg:py-4", self.converter.set_content("py-lg-3").convert(),
        )

        self.assertEqual(
            "xl:py-6", self.converter.set_content("py-xl-4").convert(),
        )

        self.assertEqual(
            "xl:py-12", self.converter.set_content("py-xl-5").convert(),
        )

    #  @test */
    def test_padding_it_converts_on_x(self):

        self.assertEqual("px-1", self.converter.set_content("px-1").convert())

        self.assertEqual(
            "sm:px-1", self.converter.set_content("px-sm-1").convert(),
        )

        self.assertEqual(
            "md:px-2", self.converter.set_content("px-md-2").convert(),
        )

        self.assertEqual(
            "lg:px-4", self.converter.set_content("px-lg-3").convert(),
        )

        self.assertEqual(
            "xl:px-6", self.converter.set_content("px-xl-4").convert(),
        )

        self.assertEqual(
            "xl:px-12", self.converter.set_content("px-xl-5").convert(),
        )

    #  @test */
    def test_padding_it_converts_0_on_all_sides(self):

        self.assertEqual("p-0", self.converter.set_content("p-0").convert())

        self.assertEqual(
            "lg:py-0", self.converter.set_content("py-lg-0").convert(),
        )

    #
    # * @group Margin
    # */

    #  @test */
    def test_margin_it_converts_on_all_sides(self):

        self.assertEqual("m-1", self.converter.set_content("m-1").convert())

        self.assertEqual(
            "sm:m-1", self.converter.set_content("m-sm-1").convert(),
        )

        self.assertEqual(
            "md:m-2", self.converter.set_content("m-md-2").convert(),
        )

        self.assertEqual(
            "lg:m-4", self.converter.set_content("m-lg-3").convert(),
        )

        self.assertEqual(
            "xl:m-6", self.converter.set_content("m-xl-4").convert(),
        )

        self.assertEqual(
            "xl:m-12", self.converter.set_content("m-xl-5").convert(),
        )

    #  @test */
    def test_margin_it_converts_on_y(self):

        self.assertEqual("my-1", self.converter.set_content("my-1").convert())

        self.assertEqual(
            "sm:my-1", self.converter.set_content("my-sm-1").convert(),
        )

        self.assertEqual(
            "md:my-2", self.converter.set_content("my-md-2").convert(),
        )

        self.assertEqual(
            "lg:my-4", self.converter.set_content("my-lg-3").convert(),
        )

        self.assertEqual(
            "xl:my-6", self.converter.set_content("my-xl-4").convert(),
        )

        self.assertEqual(
            "xl:my-12", self.converter.set_content("my-xl-5").convert(),
        )

    #  @test */
    def test_margin_it_converts_on_x(self):
        self.assertEqual("mx-1", self.converter.set_content("mx-1").convert())

        self.assertEqual(
            "sm:mx-1", self.converter.set_content("mx-sm-1").convert(),
        )

        self.assertEqual(
            "md:mx-2", self.converter.set_content("mx-md-2").convert(),
        )

        self.assertEqual(
            "lg:mx-4", self.converter.set_content("mx-lg-3").convert(),
        )

        self.assertEqual(
            "xl:mx-6", self.converter.set_content("mx-xl-4").convert(),
        )

        self.assertEqual(
            "xl:mx-12", self.converter.set_content("mx-xl-5").convert(),
        )

    #  @test */
    def test_margin_it_converts_0_on_all_sides(self):
        self.assertEqual("m-0", self.converter.set_content("m-0").convert())

        self.assertEqual(
            "lg:my-0", self.converter.set_content("my-lg-0").convert(),
        )
