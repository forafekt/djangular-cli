#!/usr/bin/python3
"""""
DJANGULAR CLI args
Code readability: 'cmd' reused from DJANGUALR settings
IN DEVELOPMENT
"""""
import argparse

from djangular_cli import cli
from djangular_cli.config.app_settings import cmd
from djangular_cli.management.exceptions import ArgDoesNotExist


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
        '-b',
        '--begin',
        type=str,
        help='Run begin argument, eg. djangular -b start'
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

    parser.add_argument(
        '-dj',
        '--django',
        type=str,
        help='New Django project'
    )

    args = parser.parse_args()
    serve = args.serve
    start = args.begin
    activate = args.virtualenv
    clone = args.git_clone
    django = args.django

    """""
    Activate env
    """""

    # TODO: Make venv args

    """""
    Open client
    """""
    # TODO: TEMP
    if start == str("start"):
        cli.client()
    else:
        assert ArgDoesNotExist("'djangular -b start'?")

    """""
    Git clone # TEMP
    """""
    if clone:
        cmd("git " + "clone " + clone)

    """""
    Build Angular to Django static
    """""
    # TODO: Make build script args
    """""
    Create Django project
    """""
    # TODO: Make gen django args

    """""
    Create Django project
    """""
    # TODO: Make gen angular args


if __name__ == '__main__':
    main()
