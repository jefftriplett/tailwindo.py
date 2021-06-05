import unittest

from src.converter import Converter


class TestSpacing(unittest.TestCase):
    def setUp(self):
        self.converter = Converter().setFramework("bootstrap")

    def test_padding_it_converts_on_all_sides(self):
        self.assertEqual(
            "p-1", self.converter.classesOnly(True).setContent("p-1").convert().get()
        )

        self.assertEqual(
            "sm:p-1",
            self.converter.classesOnly(True).setContent("p-sm-1").convert().get(),
        )

        self.assertEqual(
            "md:p-2",
            self.converter.classesOnly(True).setContent("p-md-2").convert().get(),
        )

        self.assertEqual(
            "lg:p-4",
            self.converter.classesOnly(True).setContent("p-lg-3").convert().get(),
        )

        self.assertEqual(
            "xl:p-6",
            self.converter.classesOnly(True).setContent("p-xl-4").convert().get(),
        )

        self.assertEqual(
            "xl:p-12",
            self.converter.classesOnly(True).setContent("p-xl-5").convert().get(),
        )

    #  @test */
    def test_padding_it_converts_on_y(self):

        self.assertEqual(
            "py-1", self.converter.classesOnly(True).setContent("py-1").convert().get()
        )

        self.assertEqual(
            "sm:py-1",
            self.converter.classesOnly(True).setContent("py-sm-1").convert().get(),
        )

        self.assertEqual(
            "md:py-2",
            self.converter.classesOnly(True).setContent("py-md-2").convert().get(),
        )

        self.assertEqual(
            "lg:py-4",
            self.converter.classesOnly(True).setContent("py-lg-3").convert().get(),
        )

        self.assertEqual(
            "xl:py-6",
            self.converter.classesOnly(True).setContent("py-xl-4").convert().get(),
        )

        self.assertEqual(
            "xl:py-12",
            self.converter.classesOnly(True).setContent("py-xl-5").convert().get(),
        )

    #  @test */
    def test_padding_it_converts_on_x(self):

        self.assertEqual(
            "px-1", self.converter.classesOnly(True).setContent("px-1").convert().get()
        )

        self.assertEqual(
            "sm:px-1",
            self.converter.classesOnly(True).setContent("px-sm-1").convert().get(),
        )

        self.assertEqual(
            "md:px-2",
            self.converter.classesOnly(True).setContent("px-md-2").convert().get(),
        )

        self.assertEqual(
            "lg:px-4",
            self.converter.classesOnly(True).setContent("px-lg-3").convert().get(),
        )

        self.assertEqual(
            "xl:px-6",
            self.converter.classesOnly(True).setContent("px-xl-4").convert().get(),
        )

        self.assertEqual(
            "xl:px-12",
            self.converter.classesOnly(True).setContent("px-xl-5").convert().get(),
        )

    #  @test */
    def test_padding_it_converts_0_on_all_sides(self):

        self.assertEqual(
            "p-0", self.converter.classesOnly(True).setContent("p-0").convert().get()
        )

        self.assertEqual(
            "lg:py-0",
            self.converter.classesOnly(True).setContent("py-lg-0").convert().get(),
        )

    #
    # * @group Margin
    # */

    #  @test */
    def test_margin_it_converts_on_all_sides(self):

        self.assertEqual(
            "m-1", self.converter.classesOnly(True).setContent("m-1").convert().get()
        )

        self.assertEqual(
            "sm:m-1",
            self.converter.classesOnly(True).setContent("m-sm-1").convert().get(),
        )

        self.assertEqual(
            "md:m-2",
            self.converter.classesOnly(True).setContent("m-md-2").convert().get(),
        )

        self.assertEqual(
            "lg:m-4",
            self.converter.classesOnly(True).setContent("m-lg-3").convert().get(),
        )

        self.assertEqual(
            "xl:m-6",
            self.converter.classesOnly(True).setContent("m-xl-4").convert().get(),
        )

        self.assertEqual(
            "xl:m-12",
            self.converter.classesOnly(True).setContent("m-xl-5").convert().get(),
        )

    #  @test */
    def test_margin_it_converts_on_y(self):

        self.assertEqual(
            "my-1", self.converter.classesOnly(True).setContent("my-1").convert().get()
        )

        self.assertEqual(
            "sm:my-1",
            self.converter.classesOnly(True).setContent("my-sm-1").convert().get(),
        )

        self.assertEqual(
            "md:my-2",
            self.converter.classesOnly(True).setContent("my-md-2").convert().get(),
        )

        self.assertEqual(
            "lg:my-4",
            self.converter.classesOnly(True).setContent("my-lg-3").convert().get(),
        )

        self.assertEqual(
            "xl:my-6",
            self.converter.classesOnly(True).setContent("my-xl-4").convert().get(),
        )

        self.assertEqual(
            "xl:my-12",
            self.converter.classesOnly(True).setContent("my-xl-5").convert().get(),
        )

    #  @test */
    def test_margin_it_converts_on_x(self):
        self.assertEqual(
            "mx-1", self.converter.classesOnly(True).setContent("mx-1").convert().get()
        )

        self.assertEqual(
            "sm:mx-1",
            self.converter.classesOnly(True).setContent("mx-sm-1").convert().get(),
        )

        self.assertEqual(
            "md:mx-2",
            self.converter.classesOnly(True).setContent("mx-md-2").convert().get(),
        )

        self.assertEqual(
            "lg:mx-4",
            self.converter.classesOnly(True).setContent("mx-lg-3").convert().get(),
        )

        self.assertEqual(
            "xl:mx-6",
            self.converter.classesOnly(True).setContent("mx-xl-4").convert().get(),
        )

        self.assertEqual(
            "xl:mx-12",
            self.converter.classesOnly(True).setContent("mx-xl-5").convert().get(),
        )

    #  @test */
    def test_margin_it_converts_0_on_all_sides(self):
        self.assertEqual(
            "m-0", self.converter.classesOnly(True).setContent("m-0").convert().get()
        )

        self.assertEqual(
            "lg:my-0",
            self.converter.classesOnly(True).setContent("my-lg-0").convert().get(),
        )


if __name__ == '__main__':
    unittest.main()
