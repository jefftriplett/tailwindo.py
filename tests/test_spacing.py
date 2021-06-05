import unittest

from src.converter import Converter


class TestSpacing(unittest.TestCase):
    def setUp(self):
        self.converter = Converter().setFramework("bootstrap")

    def test_padding_it_converts_on_all_sides(self):
        self.assertEquals(
            "p-1", self.converter.classesOnly(True).setContent("p-1").convert().get()
        )

        self.assertEquals(
            "sm:p-1",
            self.converter.classesOnly(True).setContent("p-sm-1").convert().get(),
        )

        self.assertEquals(
            "md:p-2",
            self.converter.classesOnly(True).setContent("p-md-2").convert().get(),
        )

        self.assertEquals(
            "lg:p-4",
            self.converter.classesOnly(True).setContent("p-lg-3").convert().get(),
        )

        self.assertEquals(
            "xl:p-6",
            self.converter.classesOnly(True).setContent("p-xl-4").convert().get(),
        )

        self.assertEquals(
            "xl:p-12",
            self.converter.classesOnly(True).setContent("p-xl-5").convert().get(),
        )

    #  @test */
    def test_padding_it_converts_on_y(self):

        self.assertEquals(
            "py-1", self.converter.classesOnly(True).setContent("py-1").convert().get()
        )

        self.assertEquals(
            "sm:py-1",
            self.converter.classesOnly(True).setContent("py-sm-1").convert().get(),
        )

        self.assertEquals(
            "md:py-2",
            self.converter.classesOnly(True).setContent("py-md-2").convert().get(),
        )

        self.assertEquals(
            "lg:py-4",
            self.converter.classesOnly(True).setContent("py-lg-3").convert().get(),
        )

        self.assertEquals(
            "xl:py-6",
            self.converter.classesOnly(True).setContent("py-xl-4").convert().get(),
        )

        self.assertEquals(
            "xl:py-12",
            self.converter.classesOnly(True).setContent("py-xl-5").convert().get(),
        )

    #  @test */
    def test_padding_it_converts_on_x(self):

        self.assertEquals(
            "px-1", self.converter.classesOnly(True).setContent("px-1").convert().get()
        )

        self.assertEquals(
            "sm:px-1",
            self.converter.classesOnly(True).setContent("px-sm-1").convert().get(),
        )

        self.assertEquals(
            "md:px-2",
            self.converter.classesOnly(True).setContent("px-md-2").convert().get(),
        )

        self.assertEquals(
            "lg:px-4",
            self.converter.classesOnly(True).setContent("px-lg-3").convert().get(),
        )

        self.assertEquals(
            "xl:px-6",
            self.converter.classesOnly(True).setContent("px-xl-4").convert().get(),
        )

        self.assertEquals(
            "xl:px-12",
            self.converter.classesOnly(True).setContent("px-xl-5").convert().get(),
        )

    #  @test */
    def test_padding_it_converts_0_on_all_sides(self):

        self.assertEquals(
            "p-0", self.converter.classesOnly(True).setContent("p-0").convert().get()
        )

        self.assertEquals(
            "lg:py-0",
            self.converter.classesOnly(True).setContent("py-lg-0").convert().get(),
        )

    #
    # * @group Margin
    # */

    #  @test */
    def test_margin_it_converts_on_all_sides(self):

        self.assertEquals(
            "m-1", self.converter.classesOnly(True).setContent("m-1").convert().get()
        )

        self.assertEquals(
            "sm:m-1",
            self.converter.classesOnly(True).setContent("m-sm-1").convert().get(),
        )

        self.assertEquals(
            "md:m-2",
            self.converter.classesOnly(True).setContent("m-md-2").convert().get(),
        )

        self.assertEquals(
            "lg:m-4",
            self.converter.classesOnly(True).setContent("m-lg-3").convert().get(),
        )

        self.assertEquals(
            "xl:m-6",
            self.converter.classesOnly(True).setContent("m-xl-4").convert().get(),
        )

        self.assertEquals(
            "xl:m-12",
            self.converter.classesOnly(True).setContent("m-xl-5").convert().get(),
        )

    #  @test */
    def test_margin_it_converts_on_y(self):

        self.assertEquals(
            "my-1", self.converter.classesOnly(True).setContent("my-1").convert().get()
        )

        self.assertEquals(
            "sm:my-1",
            self.converter.classesOnly(True).setContent("my-sm-1").convert().get(),
        )

        self.assertEquals(
            "md:my-2",
            self.converter.classesOnly(True).setContent("my-md-2").convert().get(),
        )

        self.assertEquals(
            "lg:my-4",
            self.converter.classesOnly(True).setContent("my-lg-3").convert().get(),
        )

        self.assertEquals(
            "xl:my-6",
            self.converter.classesOnly(True).setContent("my-xl-4").convert().get(),
        )

        self.assertEquals(
            "xl:my-12",
            self.converter.classesOnly(True).setContent("my-xl-5").convert().get(),
        )

    #  @test */
    def test_margin_it_converts_on_x(self):
        self.assertEquals(
            "mx-1", self.converter.classesOnly(True).setContent("mx-1").convert().get()
        )

        self.assertEquals(
            "sm:mx-1",
            self.converter.classesOnly(True).setContent("mx-sm-1").convert().get(),
        )

        self.assertEquals(
            "md:mx-2",
            self.converter.classesOnly(True).setContent("mx-md-2").convert().get(),
        )

        self.assertEquals(
            "lg:mx-4",
            self.converter.classesOnly(True).setContent("mx-lg-3").convert().get(),
        )

        self.assertEquals(
            "xl:mx-6",
            self.converter.classesOnly(True).setContent("mx-xl-4").convert().get(),
        )

        self.assertEquals(
            "xl:mx-12",
            self.converter.classesOnly(True).setContent("mx-xl-5").convert().get(),
        )

    #  @test */
    def test_margin_it_converts_0_on_all_sides(self):
        self.assertEquals(
            "m-0", self.converter.classesOnly(True).setContent("m-0").convert().get()
        )

        self.assertEquals(
            "lg:my-0",
            self.converter.classesOnly(True).setContent("my-lg-0").convert().get(),
        )


if __name__ == '__main__':
    unittest.main()
