#!/usr/bin/python3
"""""
DJANGULAR CLI args
Code readability: 'cmd' reused from DJANGUALR settings
IN DEVELOPMENT
"""""
import argparse
from djangular_cli.terminal import cli
from djangular_cli.config.app_settings import cmd
from djangular_cli.generate.create import cmd_env, cmd_angular, cmd_django
from djangular_cli.management.commands import activate_env
from djangular_cli.management.exceptions import ArgDoesNotExist
from djangular_cli.management.find import check_modules


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
        '-srv',
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
                                  "djangular -gc https://github.com/user/package")
    if args == str is None:
        raise arg_is_none

    try:

        """""
        New env
        """""
        if new_env:
            if new_env == "new":
                cmd_env()
        else:
            pass

        """""
        Activate env
        """""
        if activate and activate == "activate":
            activate_env()
        else:
            pass

        """""
        Open client
        """""
        if start and start == "start":
            cli.client()
        else:
            pass

        """""
        Git clone # TEMP
        """""
        if clone:
            cmd("git " + "clone " + clone)

        """""
        Build Angular to Django static
        """""
        if serve:
            "Do something"  # TODO: Sister package djangular-serve

        """""
        Create Django project & check virtualenv / required modules
        """""
        if django and django == "django":
            check_modules()
            cmd_django()
        else:
            pass

        """""
        Create Angular project
        """""
        if angular and angular == "angular":
            cmd_angular()
        else:
            pass

    except KeyboardInterrupt:
        print("\n => You have force cancelled the session.\n")


if __name__ == '__main__':
    main()
