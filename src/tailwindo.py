#!/usr/bin/env python3

import argparse
import os
import configparser
from color import Colors
from main import ConsoleHelper

parser = argparse.ArgumentParser(description = 'totailwind')
# positional arg
parser.add_argument('arg', help='a file path/a folder path/Bootstrap CSS classes')

parser.add_argument('--replace', dest='replace', help='This will overwrite the original file.', type=bool, default=False)

parser.add_argument('--components', dest='components', help='Extract changes as components to a separate css file in the current directory.', type=bool, default=False)

parser.add_argument('-r', dest='recursive',  help='This will recurs through all directories under the main directory', type=bool, default=False)

parser.add_argument('-e', dest='extensions', help='This allows for custom extensions', type=str, default='php,html')

parser.add_argument('-t', dest='framework', help='CSS Framework type to convert', type=str, default='bootstrap')

parser.add_argument('-p', dest='prefix', help='This allows you to add a custom prefix to all of Tailwind\'s generated utility classes', type=str, default='')


# (function (InputInterface input, OutputInterface output) {
def main():
        #  output arguments and options
        args = parser.parse_args()
        #args = vars(parser.parse_args())
        arg = args.arg
        if not args:
            print(f'{Colors.WARNING}Oops! nothing to convert.{Colors.ENDC}')
            return -1

        print(args)
        acceptedExtensions = args.extensions.split(',')

        framework = args.framework.lower()

        # # if (! class_exists('Awssat\\Tailwindo\\Framework\\' . ucfirst(framework).'Framework')):
        # if f'{framework.capitalize()}Framework' not in dir():
        #     print(f"{Colors.WARNING}Oops! {framework} is not supported!{Colors.ENDC}")
        #     return -1

        consoleHelper = ConsoleHelper({
                'recursive': args.recursive,
                'overwrite': args.replace,
                'extensions': acceptedExtensions,
                'framework': framework,
                'components': args.components,
                'prefix': args.prefix,
                'folderConvert': os.path.isdir(arg)
                })

        # file?
        if os.path.isfile(arg):
            return consoleHelper.fileConvert(arg)

        # folder ?
        if os.path.isdir(arg):
            return consoleHelper.folderConvert(arg)

        # any html/css classes
        return consoleHelper.codeConvert(arg)

if __name__ == '__main__':
     main()


