import subprocess
import sys
import time

import pip  # noqa

from djangular_cli.config.app_settings import OSEnv, djangular_root_dir


def check_modules():
    """
    Module Check
    """
    venv_dir = OSEnv['VIRTUAL_ENV']
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
