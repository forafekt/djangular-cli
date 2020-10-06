#!/usr/bin/python3
"""""
DJANGULAR CLI args
IN DEVELOPMENT
"""""
import argparse
import os

from djangular_cli.generate.create import cmd_env, cmd_angular, cmd_django
from djangular_cli.git.git import djangular_boilerplate
from djangular_cli.management.commands import activate_env
from djangular_cli.management.exceptions import ArgDoesNotExist
from djangular_cli.management.find import check_modules
from djangular_cli.terminal import cli


def main():
    """""
    DJANGULAR CLI args
    """""
    parser = argparse.ArgumentParser(
        prog='djangular',
        description='Automate your Django / Angular projects'
                    ' with DJANGULAR-CLI.'
    )

    parser.add_argument(
        '-g',
        '--generate',
        type=str,
        help='Run generate argument, eg. djangular -g start'
    )

    parser.add_argument(
        '-gc',
        '--git_clone',
        type=str,
        help='Run Git Clone'
    )
    parser.add_argument(
        '-env',
        '--virtualenv',
        type=str,
        help='Activate Virtualenv'
    )

    parser.add_argument(
        '-s',
        '--serve',
        type=str,
        help='Build Angular to Django static'
    )
    args = parser.parse_args()

    """""
    Serve
    """""
    serve = args.serve

    """""
    Virtualenv
    """""
    activate = args.virtualenv
    new_env = args.virtualenv

    """""
    Git
    """""
    clone = args.git_clone

    """""
    Generate
    """""
    django = args.generate
    angular = args.generate
    start = args.generate

    #    if not os.path.isfile(p):
    #        print('The specified source file does not exist')
    #        sys.exit()

    arg_is_none = ArgDoesNotExist("Argument does not exist. Did you mean...\n"
                                  "djangular -g start\n"
                                  "djangular -g django\n"
                                  "djangular -g angular\n"
                                  "djangular -env activate\n"
                                  "djangular -env new\n"
                                  "djangular -gc https://github.com/user/package\n"
                                  "djangular -s serve")
    if not args:
        raise arg_is_none

    try:
        """""
        Open client
        """""
        if start:
            if start == "start":
                cli.client()
            else:
                pass
        else:
            pass

        """""
        Create Django project & check virtualenv / required modules
        """""
        if django:
            if django == "django":
                check_modules()
                cmd_django()
            else:
                pass
        else:
            pass

        """""
        Create Angular project
        """""
        if angular:
            if angular == "angular":
                cmd_angular()
            else:
                pass
        else:
            pass

        """""
        New env
        """""
        if new_env:
            if new_env == "new":
                cmd_env()
            else:
                pass
        else:
            pass

        """""
        Activate env
        """""
        if activate:
            if activate == "activate":
                activate_env()
            else:
                pass
        else:
            pass

        """""
        Git clone # TEMP
        """""
        if clone:
            if clone == "clone":
                # cmd("git " + "clone " + clone)
                djangular_boilerplate()
            else:
                pass
        else:
            pass

        """""
        Build Angular to Django static
        """""
        if serve:
            if serve == "serve":
                try:
                    os.system("serve -s ng")
                except:
                    print("\nPlease run:  'serve -s ng' to build Angular to Django.\n\n"
                          "See https://github.com/forafekt/djangular-serve for more information.")
            else:
                pass
        else:
            pass

    except KeyboardInterrupt:
        exit("\n => You have force cancelled the session.\n"
             "Thank You for using Djangular-CLI.  Please visit https://djangular.com")


if __name__ == '__main__':
    main()
