#!/usr/bin/python3
"""""
DJANGULAR CLI args
Code readability: 'cmd' reused from DJANGUALR settings
"""""
import argparse

from djangular_cli.generate.g_django import cmd_django

from djangular_cli import cli
from djangular_cli.config.app_settings import cmd
from djangular_cli.serve.serve import build_angular
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
    clone = args.git_clone
    django = args.django

    """""
    Open client
    """""
    if start == str("start"):
        cli.client()
    else:
        raise ArgDoesNotExist("Did you mean 'djangular -b start'?")

    """""
    Git clone
    """""
    if clone:
        cmd("git " + "clone " + clone)

    """""
    Build Angular to Django static
    """""
    if serve:
        build_angular()

    """""
    Create Django project
    """""
    if django:
        cmd_django()
    else:
        raise ArgDoesNotExist("Error with Django loader")


if __name__ == '__main__':
    main()
