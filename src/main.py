import os
import argparse
from pathlib import Path
from datetime import date
from converter import Converter


class ConsoleHelper:
    def __init__(self, settings: dict):
        self.converter = (
            Converter()
            .setFramework("bootstrap")
            .setGenerateComponents(False)
            .setPrefix("")
        )

        self.recursive = False
        self.overwrite = False # settings["overwrite"] or False
        self.extensions = 'php,html' # settings["extensions"] or "php,html"
        self.components = False # settings["components"] or False
        self.__folderConvert = False # settings["folderConvert"] or False

    def folderConvert(self, folderPath: str):

        (
            frameworkVersion,
            TailwindVersion
        ) = self.converter.getFramework().supportedVersion()

        print(
            "<fg=black;bg=blue>Converting Folder"
            + (" (extracted to tailwindo-components.css)" if self.components else "")
            + ":</> "
            + os.path.realpath(folderPath)
        )
        print(
            "<fg=black;bg=green>Converting from</> "
            + self.converter.getFramework().frameworkName()
            + " "
            + frameworkVersion
            + " <fg=black;bg=green> to </> Tailwind "
            + TailwindVersion
        )

        # if (self.recursive):
        #     iterator = new \RecursiveIteratorIterator(
        #         new \RecursiveDirectoryIterator(
        #             folderPath,
        #             \RecursiveDirectoryIterator::SKIP_DOTS
        #         ),
        #         \RecursiveIteratorIterator::SELF_FIRST,
        #         \RecursiveIteratorIterator::CATCH_GET_CHILD
        #     );
        # } else {
        #     iterator = new \DirectoryIterator(folderPath);
        # }

        iterator = folderPath
        if self.__folderConvert and self.components:
            self.newComponentsFile(os.path.realpath(folderPath))

        for directory in iterator:
            extension = directory.split(".")[-1]
            if os.path.isfile(directory) and self.isConvertibleFile(extension):
                self.fileConvert(os.path.realpath(directory))

    def fileConvert(self, filePath):
        # //just in case
        # realpath>
        filePath = os.path.realpath(filePath)
        # filePath = Path(filePath)

        if not self.__folderConvert:
            print(
                "<fg=black;bg=blue>Converting File: "
                + ("(extracted to tailwindo-components.css)" if self.components else "")
                + "</> "
                + filePath
            )

            (
                frameworkVersion,
                TailwindVersion,
            ) = self.converter.getFramework().supportedVersion()
            print(
                "<fg=black;bg=green>Converting from</> "
                + self.converter.getFramework().frameworkName()
                + " "
                + frameworkVersion
                + " <fg=black;bg=green> to </> Tailwind "
                + TailwindVersion
                + "\n"
            )

        if not os.path.isfile(filePath):
            print("<comment>Couldn't convert: </comment>" + os.path.basename(filePath))

            return

        content = file_get_contents(filePath)

        lastDotPosition = filePath.rfind(".")

        if lastDotPosition != -1 and not self.overwrite:
            newFilePath = substr_replace(filePath, ".tw", lastDotPosition, 0)
        elif not self.overwrite:
            newFilePath = filePath + ".tw"
        else:
            # // Set the new path to the old path to make sure we overwrite it
            newFilePath = filePath

        newContent = self.converter.setContent(content).convert().get(self.components)

        if content != newContent:
            print("<info>processed: </info>" + os.path.basename(newFilePath))

            if self.components:
                if not self.__folderConvert:
                    self.newComponentsFile(dirname(filePath))

                self.writeComponentsToFile(newContent, os.path.dirname(filePath))
            else:
                with open(newFilePath, 'a') as f:
                    f.write(newContent)
        else:
            print("<comment>Nothing to convert: </comment>"\
                  + os.path.basename(filePath))

    def codeConvert(self, code: str):
        convertedCode = (
            self.converter.setContent(code)
            .classesOnly("<" not in code and ">" not in code)
            .convert()
            .get(self.components)
        )

        if convertedCode:
            print(f"<info>Converted Code: </info>{convertedCode}")
        else:
            print(
                "<comment>Nothing generated! It means that TailwindCSS has no equivalent for that classes,"
                "or it has exactly classes with the same name.</comment>"
            )

    # *
    # * Check whether a file is convertible or not based on its extension.
    # */
    # protected
    def isConvertibleFile(self, extension: str) -> bool:
        return extension in self.extensions

    # protected
    def writeComponentsToFile(self, code, path):
        cssFilePath = f"{path}/tailwindo-components.css"
        # file_put_contents(cssFilePath, code.PHP_EOL, FILE_APPEND)
        with open(cssFilePath, "a") as f:
            f.write("\n")

    # protected
    def newComponentsFile(self, path):
        cssFilePath = f"{path}/tailwindo-components.css"
        path = cssFilePath  # Path(cssFilePath)

        file_exists = os.path.exists(path)
        if file_exists:
            os.unlink()

        with open(cssFilePath, "a") as f:
            f.write(
                f"/** Auto-generated by Tailwindo: {date.today.strftime('%Y-%m-%d')} */\n\n"
            )


# def main():
#     parser = argparse.ArgumentParser(description = 'argparse recipe book')
#     fn(parser)
#
# if __name__ == '__main__':
#     main()
