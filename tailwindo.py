#!/usr/bin/env python3

import argparse
import configparser
from pathlib import Path
from src.color import Colors
from src.main import ConsoleHelper


def get_parser():

    parser = argparse.ArgumentParser(description="totailwind")
    # positional arg
    parser.add_argument("arg", help="a file path/a folder path/Bootstrap CSS classes")
    parser.add_argument(
        "--replace",
        dest="replace",
        help="This will overwrite the original file.",
        action="store_true",
    )
    parser.add_argument(
        "--components",
        dest="components",
        help="Extract changes as components to a separate css file in the current directory.",
        action="store_true",
    )
    parser.add_argument(
        "-r",
        "--recursive",
        dest="recursive",
        help="This will recurs through all directories under the main directory",
        action="store_true",
    )
    parser.add_argument(
        "-e",
        "--extensions",
        dest="extensions",
        help="This allows for custom extensions ex: '.jsx' ",
        type=str,
        default=".php,.html",
    )
    parser.add_argument(
        "-t",
        "--framework",
        dest="framework",
        help="CSS Framework type to convert",
        type=str,
        default="bootstrap",
    )
    parser.add_argument(
        "-p",
        "--prefix",
        dest="prefix",
        help="This allows you to add a custom prefix to all of Tailwind's generated utility classes",
        type=str,
        default="",
    )
    return parser


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    arg = args['arg']
    if not args:
        print(f"{Colors.WARNING}Oops! nothing to convert.{Colors.ENDC}")
        return -1

    acceptedExtensions = args['extensions'].split(",")

    framework = args['framework'].lower()

    # # if (! class_exists('Awssat\\Tailwindo\\Framework\\' . ucfirst(framework).'Framework')):
    # if f'{framework.capitalize()}Framework' not in dir():
    #     print(f"{Colors.WARNING}Oops! {framework} is not supported!{Colors.ENDC}")
    #     return -1

    consoleHelper = ConsoleHelper(
        {
            "recursive": args['recursive'],
            "overwrite": args['replace'],
            "extensions": acceptedExtensions,
            "framework": framework,
            "components": args['components'],
            "prefix": args['prefix'],
            "folderConvert": Path(arg).is_dir(),
        }
    )

    # file?
    if Path(arg).is_file():
        return consoleHelper.fileConvert(arg)

    # folder ?
    if Path(arg).is_dir():
        return consoleHelper.folderConvert(arg)

    # any html/css classes
    return consoleHelper.codeConvert(arg)


if __name__ == "__main__":
    main()
