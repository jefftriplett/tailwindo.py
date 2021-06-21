from pathlib import Path
from datetime import date
from .converter import Converter
from .color import Colors


class ConsoleHelper:
    def __init__(self, settings):

        self.recursive = settings["recursive"] or False
        self.overwrite = settings["overwrite"] or False
        self.extensions = settings["extensions"] or {".php", ".html"}
        self.components = settings["components"] or False
        self._folder_convert = settings["folder_convert"] or False

        self.converter = Converter(
                generate_components=settings["components"],
                prefix=settings["prefix"],
                framework=settings["framework"],
                )

    def folder_convert(self, folder_path: str):
        framework_version, tailwind_version = self.converter.framework.supported_version
        folder_path = Path(folder_path)

        print(
            f"{Colors.OKBLUE}Converting Folder"
            + (" (extracted to tailwindo-components.css)" if self.components else "")
            + f":{Colors.ENDC} "
            + folder_path.resolve().name
        )
        print(
            f"{Colors.OKGREEN}Converting from{Colors.ENDC} "
            + self.converter.framework.name
            + " "
            + framework_version
            + f" {Colors.OKGREEN}to{Colors.ENDC} Tailwind "
            + tailwind_version
        )

        if self.recursive:
            iterator = (f for f in folder_path.rglob("*") if f.is_file())
        else:
            iterator = (f for f in folder_path.iterdir() if f.is_file())

        if self._folder_convert and self.components:
            self._new_components_file(folder_path.resolve())

        for child in iterator:
            extension = child.suffix
            if self._is_convertible_file(extension):
                self.file_convert(child.resolve())

    @staticmethod
    def rreplace(s, old, new, offset):
        lst = s.rsplit(old, offset)
        return new.join(lst)

    def file_convert(self, file_path):
        file_path = Path(file_path).resolve()

        if not self._folder_convert:
            print(
                f"{Colors.OKBLUE}Converting File: "
                + ("(extracted to tailwindo-components.css)" if self.components else "")
                + f"{Colors.ENDC} "
                + str(file_path)
            )

            (
                framework_version,
                tailwind_version,
            ) = self.converter.framework.supported_version
            print(
                f"{Colors.OKGREEN}Converting from{Colors.ENDC} "
                + self.converter.framework.name
                + " "
                + framework_version
                + f" {Colors.OKGREEN}to{Colors.ENDC} Tailwind "
                + tailwind_version
                + "\n"
            )

        if not file_path.is_file():
            print(
                f"{Colors.WARNING}Couldn't convert: {Colors.ENDC}" + str(file_path.name)
            )

            return

        with open(file_path, "r") as f:
            content = f.read()

        if not self.overwrite:
            new_file_path = file_path.with_suffix(".tw")
        else:
            # Set the new path to the old path to make sure we overwrite it
            new_file_path = file_path

        _new_content = self.converter.set_content(content).convert(self.components)

        if content != _new_content:
            print(f"{Colors.OKCYAN}processed: {Colors.ENDC}" + str(new_file_path.name))

            if self.components:
                if not self._folder_convert:
                    self._new_components_file(str(file_path.parent))

                self._write_components_to_file(_new_content, str(file_path.parent))
            else:
                with open(new_file_path, "a") as f:
                    f.write(_new_content)
        else:
            print(
                f"{Colors.WARNING}Nothing to convert: {Colors.ENDC}"
                + str(file_path.name)
            )

    def code_convert(self, code: str):
        converted_code = (
            self.converter
            .classes_only(("<" not in code and ">" not in code))
            .set_content(code)
            .convert(self.components)
        )

        if converted_code != code:
            print(f"{Colors.OKCYAN}Converted Code: {Colors.ENDC}{converted_code}")
        else:
            print(
                f"{Colors.WARNING}Nothing generated! It means that TailwindCSS has no equivalent for that classes,"
                f"or it has exactly classes with the same name.{Colors.ENDC}"
            )

    # protected
    def _is_convertible_file(self, extension: str) -> bool:
        """ checks extension is in the list of convertible extensions """
        return extension in self.extensions

    # protected
    def _write_components_to_file(self, code, path):
        css_file_path = f"{path}/tailwindo-components.css"
        with open(css_file_path, "a") as f:
            f.write(code)
            f.write("\n")

    # protected
    def _new_components_file(self, path):
        css_file_path = f"{path}/tailwindo-components.css"
        path = Path(css_file_path)

        file_exists = path.exists()
        if file_exists:
            path.unlink()

        with open(css_file_path, "a") as f:
            f.write(
                f"/** Auto-generated by Tailwindo: {date.today().strftime('%Y-%m-%d')} */\n\n"
            )
