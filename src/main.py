from pathlib import Path
from datetime import date
from .converter import Converter
from .color import Colors


class ConsoleHelper:
    def __init__(self, settings):
        self.converter = Converter()

        self.recursive = settings["recursive"] or False
        self.overwrite = settings["overwrite"] or False
        self.extensions = settings["extensions"] or {".php",".html"}
        self.components = settings["components"] or False
        self._folderConvert = settings["folderConvert"] or False

    def folderConvert(self, folderPath: str):
        frameworkVersion, TailwindVersion = self.converter.framework.supportedVersion()
        folderPath = Path(folderPath)

        print(
            f"{Colors.OKBLUE}Converting Folder"
            + (" (extracted to tailwindo-components.css)" if self.components else "")
            + f":{Colors.ENDC} "
            + folderPath.resolve().name
        )
        print(
            f"{Colors.OKGREEN}Converting from{Colors.ENDC} "
            + self.converter.framework.frameworkName()
            + " "
            + frameworkVersion
            + f" {Colors.OKGREEN}to{Colors.ENDC} Tailwind "
            + TailwindVersion
        )

        if self.recursive:
            iterator = (f for f in folderPath.rglob("*") if f.is_file())
        else:
            iterator = (f for f in folderPath.iterdir() if f.is_file())

        if self._folderConvert and self.components:
            self._newComponentsFile(folderPath.resolve())

        for child in iterator:
            extension = child.suffix
            if self._isConvertibleFile(extension):
                self.fileConvert(child.resolve())

    @staticmethod
    def rreplace(s, old, new, offset):
        lst = s.rsplit(old, offset)
        return new.join(lst)

    def fileConvert(self, filePath):
        filePath = Path(filePath).resolve()

        if not self._folderConvert:
            print(
                f"{Colors.OKBLUE}Converting File: "
                + ("(extracted to tailwindo-components.css)" if self.components else "")
                + f"{Colors.ENDC} "
                + str(filePath)
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

        if not filePath.is_file():
            print(f"{Colors.WARNING}Couldn't convert: {Colors.ENDC}" + str(filePath.name))

            return

        with open(filePath, 'r') as f:
            content = f.read()

        if not self.overwrite:
            newFilePath = filePath.with_suffix(".tw")
        else:
            # // Set the new path to the old path to make sure we overwrite it
            newFilePath = filePath

        _newContent = self.converter.setContent(content).convert().get(self.components)

        if content != _newContent:
            print(f"{Colors.OKCYAN}processed: {Colors.ENDC}" + str(newFilePath.name))

            if self.components:
                if not self._folderConvert:
                    self._newComponentsFile(str(filePath.parent))

                self._writeComponentsToFile(_newContent, str(filePath.parent))
            else:
                with open(newFilePath, 'a') as f:
                    f.write(_newContent)
        else:
            print(f"{Colors.WARNING}Nothing to convert: {Colors.ENDC}"\
                  + str(filePath.name))

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
        with open(cssFilePath, "a") as f:
            f.write("\n")

    # protected
    def _newComponentsFile(self, path):
        cssFilePath = f"{path}/tailwindo-components.css"
        path = Path(cssFilePath)

        file_exists = path.exists()
        if file_exists:
            path.unlink()

        with open(cssFilePath, "a") as f:
            f.write(
                f"/** Auto-generated by Tailwindo: {date.today().strftime('%Y-%m-%d')} */\n\n"
            )

