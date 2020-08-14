#!/usr/bin/python3
"""""
DJANGULAR CLI args
Code readability: 'cmd' reused from DJANGUALR settings
IN DEVELOPMENT
"""""
import argparse
import subprocess
import sys

from djangular_cli import cli
from djangular_cli.config.app_settings import cmd, OSget, join
from djangular_cli.generate.g_venv import cmd_env
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

    parser.add_argument(
        '-dj',
        '--django',
        type=str,
        help='New Django project'
    )

    args = parser.parse_args()
    serve = args.serve
    start = args.generate
    activate = args.virtualenv
    new_env = args.virtualenv
    clone = args.git_clone
    django = args.django

    #    if not os.path.isfile(p):
    #        print('The specified source file does not exist')
    #        sys.exit()

    if not args:
        raise ArgDoesNotExist("Did you mean...\n"
                              "-g start\n"
                              "-env activate\n"
                              "-env new\n"
                              "-gc https://github.com/user/package")
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
        if activate:
            if activate == "activate":
                venv_path = input("▸ Env path [Leave empty for current directory]: ")
                venv_name = input("▸ Env name [testenv]: ")
                if venv_path:
                    if venv_path[-1] != '/':
                        venv_path = venv_path + '/'
                else:
                    venv_path = ''
                env = f"{venv_path}{venv_name}/bin/activate_this.py"
                with open(env) as f:
                    code = compile(f.read(), env, "exec")
                    e = (code, dict(__file__=env))
                command = e
                process = subprocess.Popen(
                    command,
                    env={'PATH': OSget('PATH')},
                )
                process.wait()
        else:
            pass

        """""
        Open client
        """""
        if start == "start":
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
        # TODO: Make build script args
        """""
        Create Django project
        """""
        # TODO: Make gen django args

        """""
        Create Django project
        """""
        # TODO: Make gen angular args
    except KeyboardInterrupt:
        print("\n => You have force cancelled the session.\n")


if __name__ == '__main__':
    main()
