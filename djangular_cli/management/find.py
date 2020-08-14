import subprocess
import sys
import time

import pip  # noqa

from djangular_cli.config.app_settings import OSEnv, djangular_root_dir, current_dir, cmd
from djangular_cli.generate.g_venv import cmd_env


def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))


def check_modules():
    """
    Module Check
    """
    if is_venv():
        print('Checking for Virtualenv...')
        time.sleep(2)
        print('Virtualenv exists... Continuing setup.')
    else:
        print('No Virtualenv...\n'
              'Please setup Virtualenv to install modules.')
        time.sleep(2)
        try:
            cmd_env()
        except:
            exit("Finishing setup...")

    venv_dir = OSEnv["VIRTUAL_ENV"]
    requirements = djangular_root_dir("dependencies/django.txt")
    modules = "Django"
    reqs = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze'])
    installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
    print("▸", "Checking if requirements are installed...\n")
    time.sleep(5)
    if modules in installed_packages:
        print(modules, "is installed. Please continue to enter your project name..\n")
    else:
        print("▸", modules, "not installed...\n"
                            f"=> Installing {modules} ...")
        time.sleep(5)
        pip.main(["install", "--prefix", venv_dir, "-r", requirements])
