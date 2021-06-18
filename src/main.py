import os
from pathlib import Path
from datetime import date
from .converter import Converter
from .color import Colors

CONFIG_FILENAME = os.path.realpath('converter.conf')
 
class ConsoleHelper:
    def __init__(self, settings):
        self.converter = Converter()
        

        self.recursive = False
        self.overwrite = settings["overwrite"] or False
        self.extensions = settings["extensions"] or "php,html"
        self.components = settings["components"] or False
        self.__folderConvert = settings["folderConvert"] or False

    def folderConvert(self, folderPath: str):

        (
            frameworkVersion,
            TailwindVersion
        ) = self.converter.framework.supportedVersion()

        print(
            f"{Colors.OKBLUE}Converting Folder"
            + (" (extracted to tailwindo-components.css)" if self.components else "")
            + f":{Colors.ENDC} "
            + os.path.realpath(folderPath)
        )
        print(
            f"{Colors.OKGREEN}Converting from{Colors.ENDC} "
            + self.converter.framework.frameworkName()
            + " "
            + frameworkVersion
            + f" {Colors.OKGREEN}to{Colors.ENDC} Tailwind "
            + TailwindVersion
        )

        # TODO
        if self.recursive:
            iterator = os.walk(folderPath)
            # iterator = new \RecursiveIteratorIterator(
            #     new \RecursiveDirectoryIterator(
            #         folderPath,
            #         \RecursiveDirectoryIterator::SKIP_DOTS
            #     ),
            #     \RecursiveIteratorIterator::SELF_FIRST,
            #     \RecursiveIteratorIterator::CATCH_GET_CHILD
            # );
        else:
            iterator = [f for f in os.listdir(folderPath) if os.path.isfile(f)]

        # TODO
        if self.__folderConvert and self.components:
            self._newComponentsFile(os.path.realpath(folderPath))

        for directory in iterator:
            extension = directory.split(".")[-1]
            if os.path.isfile(directory) and self._isConvertibleFile(extension):
                self.fileConvert(os.path.realpath(directory))

    @staticmethod
    def rreplace(s, old, new, offset):
        lst = s.rsplit(old, offset)
        return new.join(lst)

    def fileConvert(self, filePath):
        # //just in case
        # realpath>
        filePath = os.path.realpath(filePath)
        # filePath = Path(filePath)

        if not self.__folderConvert:
            print(
                f"{Colors.OKBLUE}Converting File: "
                + ("(extracted to tailwindo-components.css)" if self.components else "")
                + f"{Colors.ENDC} "
                + filePath
            )

            (
                frameworkVersion,
                TailwindVersion,
            ) = self.converter.framework.supportedVersion()
            print(
                f"{Colors.OKGREEN}Converting from{Colors.ENDC} "
                + self.converter.framework.frameworkName()
                + " "
                + frameworkVersion
                + f" {Colors.OKGREEN}to{Colors.ENDC} Tailwind "
                + TailwindVersion
                + "\n"
            )

        if not os.path.isfile(filePath):
            print(f"{Colors.WARNING}Couldn't convert: {Colors.ENDC}" + os.path.basename(filePath))

            return

        with open(filePath, 'r') as f:
            content = f.read()

        lastDotPosition = filePath.rfind(".")
        # 'html' or ...
        ext = filePath.rsplit('.')[-1]

        if lastDotPosition != -1 and not self.overwrite:
            newFilePath = self.rreplace(filePath, ext, "tw", lastDotPosition)
        elif not self.overwrite:
            newFilePath = filePath + "tw"
        else:
            # // Set the new path to the old path to make sure we overwrite it
            newFilePath = filePath

        _newContent = self.converter.setContent(content).convert().get(self.components)

        if content != _newContent:
            print(f"{Colors.OKCYAN}processed: {Colors.ENDC}" + os.path.basename(newFilePath))

            if self.components:
                if not self.__folderConvert:
                    self._newComponentsFile(os.path.dirname(filePath))

                self._writeComponentsToFile(_newContent, os.path.dirname(filePath))
            else:
                with open(newFilePath, 'a') as f:
                    f.write(_newContent)
        else:
            print(f"{Colors.WARNING}Nothing to convert: {Colors.ENDC}"\
                  + os.path.basename(filePath))

    def codeConvert(self, code: str):
        convertedCode = (
            self.converter.setContent(code)
            .classesOnly("<" not in code and ">" not in code)
            .convert()
            .get(self.components)
        )

        if convertedCode != code:
            print(f"{Colors.OKCYAN}Converted Code: {Colors.ENDC}{convertedCode}")
        else:
            print(
                f"{Colors.WARNING}Nothing generated! It means that TailwindCSS has no equivalent for that classes,"
                f"or it has exactly classes with the same name.{Colors.ENDC}"
            )

    # *
    # * Check whether a file is convertible or not based on its extension.
    # */
    # protected
    def _isConvertibleFile(self, extension: str) -> bool:
        """ checks extension is in the list of convertible extensions """
        return extension in self.extensions

    # protected
    def _writeComponentsToFile(self, code, path):
        cssFilePath = f"{path}/tailwindo-components.css"
        # file_put_contents(cssFilePath, code.PHP_EOL, FILE_APPEND)
        with open(cssFilePath, "a") as f:
            f.write("\n")

    # protected
    def _newComponentsFile(self, path):
        cssFilePath = f"{path}/tailwindo-components.css"
        path = cssFilePath  # Path(cssFilePath)

        file_exists = os.path.exists(path)
        if file_exists:
            os.unlink(path)

        with open(cssFilePath, "a") as f:
            f.write(
                f"/** Auto-generated by Tailwindo: {date.today().strftime('%Y-%m-%d')} */\n\n"
            )

